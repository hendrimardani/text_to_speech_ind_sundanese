### Descriptions

This model is a fine-tuned version of microsoft/speecht5_tts.

### How to use

```
python3 utama.py
```

### For more information 

```
python3 utama.py --help
```

### Datasets

I uses datasets in [here](https://openslr.org/36/) 

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

- Loss : 0.4137

![Screenshot pada 2023-08-29 14-01-30](https://github.com/hendrimardani/text_to_speech_ind_sundanese/assets/49816104/ad05ab62-6b9d-4c0e-b782-5d3b6711d92f)


### Framework version

- Transformers 4.30.2
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.13.3


![vokoscreenNG-2023-08-29_17-31-48](https://github.com/hendrimardani/text_to_speech_ind_sundanese/assets/49816104/4595fd8a-7ed6-4095-90f2-72582f7c649d)

### ✉️ &nbsp; Get token for login or password file contact me:
<p>
    <a href="https://api.whatsapp.com/send?phone=6281388372075" target="_blank">
        <img src="https://www.stickpng.com/assets/images/580b57fcd9996e24bc43c543.png" width="100" alt=""/>
    </a>
</p>

