### How to use

```
python3 utama.py
```

### For more information 

```
python3 utama.py --help
```

### Training hyperparameters

- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000

### Training results

| Training Loss  |  Epochs  |  Step  | Validation Loss  |
| :---:          |  :---:   |  :---: | :------:         |
|  0.4846        |  14.81   |  1000  |  0.4323          |
|  0.4549        |  29.63   |  2000  |  0.4176          |
|  0.4437        |  44.44   |  3000  |  0.4135          |
|  0.4396        |  59.26   |  4000  |  0.4137          |
