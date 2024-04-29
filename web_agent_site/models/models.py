"""
Model implementations. The model interface should be suitable for both
the ``site env'' and the ``text env''.
"""
import json
import random
import requests
from functools import reduce

random.seed(4)


class BasePolicy:
    def __init__(self):
        pass
    
    def forward(observation, available_actions):
        """
        Args:
            observation (`str`):
                HTML string

            available_actions ():
                ...
        Returns:
            action (`str`): 
                Return string of the format ``action_name[action_arg]''.
                Examples:
                    - search[white shoes]
                    - click[button=Reviews]
                    - click[button=Buy Now]
        """
        raise NotImplementedError


class HumanPolicy(BasePolicy):
    def __init__(self):
        super().__init__()

    def forward(self, observation, available_actions):
        action = input('> ')
        return action


class RandomPolicy(BasePolicy):
    def __init__(self):
        super().__init__()
    
    def forward(self, observation, available_actions):
        if available_actions['has_search_bar']:
            action = 'search[shoes]'
        else:
            action_arg = random.choice(available_actions['clickables'])
            action = f'click[{action_arg}]'
        return action


class QwenPolicy(BasePolicy):
    def __init__(self, instruction_text):
        super().__init__()
        self.instruction_text = instruction_text
        self.previous_actions = []
    
    def get_prompt(self, observation, available_actions):
        if (available_actions['has_search_bar']):
            action_choices_string = 'SEARCH'
        else:
            action_choices_string = '\n'.join([f'CLICK {c}' for c in available_actions['clickables']])
        
        previous_steps = ''
        if len(self.previous_actions) > 0:
            previous_steps = 'Here are the previous steps I have completed:\n'
            for idx, prev in enumerate(self.previous_actions):
                previous_steps = previous_steps + f'{idx+1}. {prev}\n'

        print(f'>>> Action options given to LLM: {action_choices_string}')
        print(f'>>> Previous steps string: {previous_steps}')

        return '''My goal is to buy the following on a shopping website: \"{}\".
I will give you a list of choices you must select from.
Your job is to tell me which HTML element I should click on or term I should search to get closer to acheiving this goal.
It is ok if your instruction does not complete the goal in this step because I will follow up asking for more questions after completing this step if your response element does not complete the goal.
Respond with the following JSON format if I should type in the search bar: 
{{\"action\": \"SEARCH\", \"search_text\": \"women faux fur lined winter jacket\"}}
Respond with the following JSON format if I should click on an element: 
{{\"action\": \"CLICK\", \"element\": \"B09PY89B1S\"}}
Respond with the following JSON format to complete the buy action once you are confident with the item selected: 
{{\"action\": \"CLICK\", \"element\": \"Buy Now\"}}
Only respond with one of these two formats.
Here is the full page HTML: {}
{}
Here are the available actions to choose from. You may only choose from these actions.:
{}'''.format(self.instruction_text, observation, previous_steps, action_choices_string)
    
    def forward(self, observation, available_actions):
        prompt = self.get_prompt(observation, available_actions)
        post_response = requests.post(
            'https://q0xgtmmhf9hmeg-4000.proxy.runpod.net/predict',
            json= {
                'token': 'ericsecret',
                'prompt': prompt,
            },
        )

        post_response_json = post_response.json()
        result = json.loads(post_response_json['result'])
        llm_action = result['action']
        debug_str = f'llm_action: {llm_action}\n'
        
        if llm_action == 'SEARCH':
            search_text = result['search_text']
            driver_action = f'search[{search_text}]'
            self.previous_actions.append(f'{llm_action} {search_text}')
            debug_str = debug_str + f'search text: {search_text}\n'
        elif llm_action == 'CLICK':
            element = result['element']
            driver_action = f'click[{element}]'
            self.previous_actions.append(f'{llm_action} {element}')
            debug_str = debug_str + f'Element: {element}\n'
        else:
            raise Exception(f'unknown llm_action: {result}')
        
        print('>>> ' + debug_str)

        return driver_action