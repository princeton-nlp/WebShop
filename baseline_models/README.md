# WebShop Baseline Models

## Extra Dependencies

```bash
pip install datasets accelerate transformers faiss-gpu wandb
```
## Data

Unzip choice IL training data:
```bash
cd data
unzip il_trajs_finalized_images.zip
cd ..
```

## Experiments

Trained model checkpoints can be downloaded [here](https://drive.google.com/drive/folders/1liZmB1J38yY_zsokJAxRfN8xVO1B_YmD?usp=sharing).

- Train the search IL model (BART Transformer):
```bash
python train_search.py
```

- Train the choice IL model (BERT Transformer):
```bash
python train_choice.py
```

- Train the choice RL mdoels:
```bash
python train_rl.py
```

- Test the model on WebShop:
```bash
python test.py
```

Notes about testing:
1. You can specify the choice model path (`--model_path`) and the search model path (`--bart_path`) to load different models. 
    
2. While the rule baseline result is deterministic, model results could have variance due to the softmax sampling of the choice policy. `--softmax 0` will use a greedy policy and yield detministic (but worse) results.

3. `--bart 0` will use the user instruction as the only search query.

- (Optional) Generate the search IL model's top-10 queries on all WebShop instructions:
```bash
# Will generate ./data/goal_query_predict.json
python generate_search.py
```

