# -*- coding: utf-8 -*-
"""text-to-speech-ind-sundanese2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19HkbFAeIJEcsQAOCCgk41BAqEawLBQfS
"""

# !pip install transformers datasets soundfile speechbrain accelerate
# !pip install speechbrain
# !pip install git+https://github.com/huggingface/transformers.git

# !wget https://openslr.org/resources/44/su_id_female.zip

# !unzip /kaggle/working/su_id_female.zip

import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
import torch
import torchaudio
import pandas as pd
import datasets
import librosa

from functools import partial
from dataclasses import dataclass
from typing import Any, Dict, List, Union
from speechbrain.pretrained import EncoderClassifier
from IPython.display import Audio
from sklearn.model_selection import train_test_split
from huggingface_hub import notebook_login
from datasets import Dataset
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, Seq2SeqTrainingArguments, Seq2SeqTrainer, SpeechT5HifiGan
sns.set()

notebook_login()

data = pd.read_csv("/kaggle/working/su_id_female/line_index.tsv", names=["path_wav", "kosong_2", "text"], sep="\t")
data

data.drop(["kosong_2"], axis=1, inplace=True)
data

data["path_wav"] = "/kaggle/working/su_id_female/wavs/" + data["path_wav"] + ".wav"
data

def array(batch):
    array, _ = librosa.load(batch, sr=16000)
    return array

def sample_rate(batch):
    _, sample_rate = librosa.load(batch, sr=16000)
    return sample_rate

data["array"] = data["path_wav"].map(array)
data["sample_rate"] = data["path_wav"].map(sample_rate)
data

data["text"] = data["text"].map(lambda x: x.lower())
data

data["array"][0]

panjang = [len(data["array"][x]) for x in range(0, 10)]
panjang

for a in data["array"][:5]:
    print(a)

data.info()

data["array"][0]

sample_rate = data["sample_rate"][0]
sample_audio = data["array"][0]
sample_audio, sample_rate

sample_text = data["text"][0]
print(f"Text : {sample_text}")

Audio(sample_audio, rate=sample_rate)

sample_audio

waveform, sample_rate = torchaudio.load(data["path_wav"][0])

def plot_waveform(waveform, sample_rate=16000):
    waveform = waveform.numpy()

    num_channels, num_frames = waveform.shape
    time_axis = torch.arange(0, num_frames) / sample_rate

    figure, axes = plt.subplots(num_channels, 1)
    if num_channels == 1:
        axes = [axes]
    for c in range(num_channels):
        axes[c].plot(time_axis, waveform[c], linewidth=1)
        axes[c].grid(True)
        if num_channels > 1:
            axes[c].set_ylabel(f"Channel {c+1}")
    figure.suptitle("waveform")
    plt.show(block=False)

plot_waveform(waveform)

def plot_specgram(waveform, sample_rate=16000, title="Spectrogram"):
    waveform = waveform.numpy()

    num_channels, num_frames = waveform.shape

    figure, axes = plt.subplots(num_channels, 1)
    if num_channels == 1:
        axes = [axes]
    for c in range(num_channels):
        axes[c].specgram(waveform[c], Fs=sample_rate)
        if num_channels > 1:
            axes[c].set_ylabel(f"Channel {c+1}")
    figure.suptitle(title)
    plt.show(block=True)

plot_specgram(waveform)

data_train, data_test = train_test_split(data, test_size=0.1)

print(f"Data training : {data_train.shape}\nData Test : {data_test.shape}")

dataset_train = Dataset.from_dict(data_train)
dataset_test = Dataset.from_dict(data_test)
dataset = datasets.DatasetDict({"train": dataset_train, "test": dataset_test})
dataset

checkpoint = "microsoft/speecht5_tts"
processor = SpeechT5Processor.from_pretrained(checkpoint)

spk_model_name = "speechbrain/spkrec-xvect-voxceleb"

device = "cuda" if torch.cuda.is_available() else "cpu"
speaker_model = EncoderClassifier.from_hparams(
    source=spk_model_name,
    run_opts={"device": device},
    savedir=os.path.join("/tmp", spk_model_name),
)


def create_speaker_embedding(waveform):
    with torch.no_grad():
        speaker_embeddings = speaker_model.encode_batch(torch.tensor(waveform))
        speaker_embeddings = torch.nn.functional.normalize(speaker_embeddings, dim=2)
        speaker_embeddings = speaker_embeddings.squeeze().cpu().numpy()
    return speaker_embeddings

def prepare_dataset(example):

    proses = processor(
        text=example["text"],
        audio_target=example["array"],
        sampling_rate=16000,
        return_attention_mask=False,
    )

    # strip off the batch dimension
    proses["labels"] = proses["labels"][0]

    # use SpeechBrain to obtain x-vector
    proses["speaker_embeddings"] = create_speaker_embedding(example["array"])

    return proses

processed_example = prepare_dataset(dataset["train"][0])
list(processed_example.keys())

processed_example["labels"]

processed_example["speaker_embeddings"].shape

processed_example["labels"]

plt.figure()
plt.imshow(processed_example["labels"].T)
plt.show()

dataset["train"] = dataset["train"].map(prepare_dataset)
dataset["test"] = dataset["test"].map(prepare_dataset)

dataset["train"], dataset["test"]

@dataclass
class TTSDataCollatorWithPadding:
    processor: Any

    def __call__(
        self, features: List[Dict[str, Union[List[int], torch.Tensor]]]
    ) -> Dict[str, torch.Tensor]:
        input_ids = [{"input_ids": feature["input_ids"]} for feature in features]
        label_features = [{"input_values": feature["labels"]} for feature in features]
        speaker_features = [feature["speaker_embeddings"] for feature in features]

        # collate the inputs and targets into a batch
        batch = processor.pad(
            input_ids=input_ids, labels=label_features, return_tensors="pt"
        )

        # replace padding with -100 to ignore loss correctly
        batch["labels"] = batch["labels"].masked_fill(
            batch.decoder_attention_mask.unsqueeze(-1).ne(1), -100
        )

        # not used during fine-tuning
        del batch["decoder_attention_mask"]

        # round down target lengths to multiple of reduction factor
        if model.config.reduction_factor > 1:
            target_lengths = torch.tensor(
                [len(feature["input_values"]) for feature in label_features]
            )
            target_lengths = target_lengths.new(
                [
                    length - length % model.config.reduction_factor
                    for length in target_lengths
                ]
            )
            max_length = max(target_lengths)
            batch["labels"] = batch["labels"][:, :max_length]

        # also add in the speaker embeddings
        batch["speaker_embeddings"] = torch.tensor(speaker_features)

        return batch

data_collator = TTSDataCollatorWithPadding(processor=processor)
model = SpeechT5ForTextToSpeech.from_pretrained(checkpoint)

# disable cache during training since it's incompatible with gradient checkpointing
model.config.use_cache = False

# set language and task for generation and re-enable cache
model.generate = partial(model.generate, use_cache=True)

training_args = Seq2SeqTrainingArguments(
    output_dir=f"text_to_speech_ind_sundanese2",  # change to a repo name of your choice
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8,
    learning_rate=1e-5,
    warmup_steps=500,
    max_steps=4000,
    gradient_checkpointing=True,
    fp16=True,
    evaluation_strategy="steps",
    per_device_eval_batch_size=2,
    save_steps=1000,
    eval_steps=1000,
    logging_steps=25,
    report_to=["tensorboard"],
    load_best_model_at_end=True,
    greater_is_better=False,
    label_names=["labels"],
    push_to_hub=True,
)

trainer = Seq2SeqTrainer(
    args=training_args,
    model=model,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    data_collator=data_collator,
    tokenizer=processor,
)

trainer.train()

trainer.push_to_hub()

model = SpeechT5ForTextToSpeech.from_pretrained(
    "hendrimardani/text_to_speech_ind_sundanese2"
)

def sample():
    x = dataset["test"][0]
    hasil_speaker = torch.tensor(x["speaker_embeddings"]).unsqueeze(0)
    return hasil_speaker

speaker_embeddings = sample()

# example = dataset["test"][0]
# speaker_embeddings = torch.tensor(example["speaker_embeddings"]).unsqueeze(0)

text = "abdi orang sunda atuh"
inputs = processor(text=text, return_tensors="pt")

vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

Audio(speech.numpy(), rate=16000)

# save audio output

import soundfile as sf

audio = speech.numpy()
sf.write("output.wav", audio, 16000)
