---
layout: default
---

<div style="text-align:center;">
  <b>A scalable, simulated web environment with real-world data for developing grounded language agents</b>
</div>

<img src="assets/static/diagram.gif">

## Abstract

Existing benchmarks for grounding language in interactive environments either lack real-world linguistic elements, or prove difficult to scale up due to substantial human involvement in the collection of data or feedback signals. To bridge this gap, we develop WebShop – a simulated e-commerce website environment with 1.18 million real-world products and 12,087 crowd-sourced text instructions. Given a text instruction specifying a product requirement, an agent needs to navigate multiple types of webpages and issue diverse actions to find, customize, and purchase an item. WebShop provides several challenges for language grounding including understanding compositional instructions, query (re-)formulation, comprehending and acting on noisy text in webpages, and performing strategic exploration. We collect over 1,600 human demonstrations for the task, and train and evaluate a diverse range of agents using reinforcement learning, imitation learning, and pre-trained image and language models. Our best model achieves a task success rate of 29%, which outperforms rule-based heuristics (9.6%) but is far lower than human expert performance (59%). We also analyze agent and human trajectories and ablate various model components to provide insights for developing future agents with stronger language understanding and decision making abilities. Finally, we show that agents trained on WebShop exhibit non-trivial _sim-to-real_ transfer when evaluated on [amazon.com](https://www.amazon.com/), indicating the potential value of WebShop in developing practical web-based agents that can operate in the wild.

## WebShop Environment

<video controls width="100%">
  <source src="assets/static/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Try out the WebShop environment for yourself at the live site [here](http://3.83.245.205:3000/pnlp)!

The WebShop environment features a variety of <b>states</b> and a number of <b>actions</b> to transition from one state to the next. A state `s` represents one of four types of webpages:

* `search` page that contains a search bar
* `results` page that lists a set of products returned by a search engine
* `item` page that describes a product
* `item-detail` page that shows further information about the product

At each state, an agent has two choices of actions: to either <b>search</b> a text query (e.g. `search[Red shoes]`) or <b>choose</b> a text button (e.g. `choose[Size 9]`). The following table lists the full set of available actions and the state transitions they correspond to.

| Type | Argument | State &#8594; Next State |
| ----------- | ----------- | ----------- |
| search | [Query] | Search &#8594; Results |
| choose | Back to Search | * &#8594; Search |
| choose | Prev/Next Page | Results &#8594; Results |
| choose | [Product Title] | Results &#8594; Item |
| choose | [Option] | Item &#8594; Item |
| choose | Desc/Overview | Item-Detail &#8594; Item |
| choose | Buy | Item &#8594; Episode End |

Within this environment, an agent is given a human-provided text <b>instruction</b> and asked to purchase a product that matches the specifications. <b>Rewards</b> are automatically computed using a combination of programmatic matching functions that consider the attributes, type, options and price of the chosen product

In the WebShop environment setting, an agent is presented with a variety of challenges for language grounding, including understanding compositional instructions, query (re-)formulation, comprehending and acting on noisy text in webpages, and performing strategic exploration.

## Demo

### Interactive Web App

<iframe src="https://hf.space/gradioiframe/webshop/amazon_shop/+" width="100%" height=900></iframe>

### Trajectories

The below slides show the step-by-step actions of trajectories generated from different agents and entities performing the task of searching for a product based on a goal instruction.

**Goal Instruction**: I'm looking for a quick-release replacement fitness strap band; it should match my chic teal fitbit, and price lower than 40.00 dollars

These first four slideshows showcase trajectories by an MTurk worker, Rule Based Heuristic Imitation Learning Agent, and Imitation Learning + Reinforcement Learning Agent searching for a product on WebShop given the same goal instruction.

<div style="text-align:center;">
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRv8w_xsn8Y2dIH9bteRaR74gGv0TDdCYBa460JNefCa5pmbrwxc5FFUCzk2dx-ElVsy99dMcyme2Vh/embed?start=false&loop=false&delayms=10000" frameborder="0" width="49%" height="300" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQa-LV0_ElycuIjva2TLwj3LKdZfhbEgGX0rzZbt1a6Jjkl9t-pcakCJMGRiJV_wnUrfptvCN_x_cm0/embed?start=false&loop=false&delayms=10000" frameborder="0" width="49%" height="300" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>
<div style="text-align:center;">
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR2xraC_z1pX4J7Ajb00MmqFBj5HwXu88sLz7a8bp6rNTydoWJEWc1qUsfFLLgtUa1boM0Y3c8OhSN2/embed?start=false&loop=false&delayms=10000" frameborder="0" width="49%" height="300" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTZ8tS8jgniUgVw2MGLxmih5fj-8GQdxKNOM3gYpPlLY91Tj6bSM39qpqfdoqQI00I8QhyAae_7P1eM/embed?start=false&loop=false&delayms=10000" frameborder="0" width="49%" height="300" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>

_Sim-to-real Transfer_: This last slideshow shows a trajectory generated by an Imitation Learning agent searching on the www.amazon.com website, achieved via sim-to-real transfer logic.

<div style="text-align:center;">
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRmGmWmt5PInGy4qSG7JZg9LcDAHULrH8sGY2QIXyD55KsikNxMZ5nhlPHYrB_nOa8g8DtIIqJolfjD/embed?start=false&loop=false&delayms=10000" frameborder="0" width="49%" height="300" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>

## Citation

```
@inproceedings{yao2022webshop,
  bibtex_show = {true},
  title = {WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents},
  author = {Yao, Shunyu and Chen, Howard and Yang, John and Narasimhan, Karthik},
  booktitle = {ArXiv},
  year = {preprint},
  html = {https://arxiv.org/abs/2207.01206},
  tag = {NLP}
}
```
