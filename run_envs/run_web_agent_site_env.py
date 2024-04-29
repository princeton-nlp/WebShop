"""
Test the site gym environment.

TODO: move to testing dir for more rigorous tests
"""
from rich import print
from rich.markup import escape

from web_agent_site.envs import WebAgentSiteEnv
from web_agent_site.models import (
    QwenPolicy,
)
from web_agent_site.utils import DEBUG_PROD_SIZE

import sys


if __name__ == '__main__':
    #env = gym.make('WebAgentSite-v0')
    #env = WebAgentSiteEnv(render=True, pause=2.0)
    #env = WebAgentSiteEnv(observation_mode='html', render=False)
    env = WebAgentSiteEnv(observation_mode='html', run_id='69', render=False, num_products=DEBUG_PROD_SIZE)
    global_step = 0
    if len(sys.argv) > 1:
        print(f'PID: {sys.argv[1]}')
    else:
        print("No arguments provided.") 
        exit(0)
    try:
        policy = QwenPolicy(env.instruction_text)
    
        observation = env.observation
        while True:
            # print(observation)
            available_actions = env.get_available_actions()
            print('Available actions:', available_actions)
            action = policy.forward(observation, available_actions)
            observation, reward, done, info = env.step(action)
            print(f'Taking action "{escape(action)}" -> Reward = {reward}')
            if done:
                break
            global_step += 1
    finally:
        env.close()