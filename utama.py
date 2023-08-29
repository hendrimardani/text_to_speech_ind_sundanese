import argparse
import torch
import sys
import time
import random
import soundfile as sf
from tensor import speaker_embeddings as speaker1
from tensor import speaker_embeddings2 as speaker2
from transformers import SpeechT5ForTextToSpeech, SpeechT5HifiGan, SpeechT5Processor

PRETRAINED_MODEL = "hendrimardani/text_to_speech_ind_sundanese"
PRETRAINED_MODEL2 = "hendrimardani/text_to_speech_ind_sundanese2"
CHECKPOINT = "microsoft/speecht5_tts"
CHECKPOINT_HIFIGANS = "microsoft/speecht5_hifigan"

speaker_embeddings = speaker1()
speaker_embeddings2 = speaker2()

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.03)

def proses(text, jk, output, sample_rate):
    if jk == 1:
        model = SpeechT5ForTextToSpeech.from_pretrained(PRETRAINED_MODEL)
        processor = SpeechT5Processor.from_pretrained(CHECKPOINT)
        inputs = processor(text=text, return_tensors="pt")
        
        vocoder = SpeechT5HifiGan.from_pretrained(CHECKPOINT_HIFIGANS)
        speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
        audio = speech.numpy()
        sf.write(output + "Pria" + str(sample_rate) + ".wav", audio, sample_rate)
    else:
        model2 = SpeechT5ForTextToSpeech.from_pretrained(PRETRAINED_MODEL2)
        processor = SpeechT5Processor.from_pretrained(CHECKPOINT)
        inputs = processor(text=text, return_tensors="pt")
        
        vocoder = SpeechT5HifiGan.from_pretrained(CHECKPOINT_HIFIGANS)
        speech = model2.generate_speech(inputs["input_ids"], speaker_embeddings2, vocoder=vocoder)
        audio = speech.numpy()
        sf.write(output + "Wanita" + str(sample_rate) + ".wav", audio, sample_rate)

def main():
    class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'
    try:   
        parser = argparse.ArgumentParser(description=f"Model has been trained by {color.GREEN}Hendri Mardani{color.END}")
        parser.add_argument("-sR", "--sample_rate", type=int, default=16000, help=f"Sample rate semakin besar nilai Hz semakin berisik. Default:[{color.YELLOW}16000 Hz{color.END}]")
        parser.add_argument("-o", "--output", type=str, default="output_", help=f"Output file audio extension:[{color.RED}.wav{color.END}]. Default:{color.RED}direktori saat ini{color.END}")
        args = parser.parse_args()
        
        
        sample_rate = args.sample_rate
        output = args.output
        print()
        
        mengetik(f"Model pretrained by {color.GREEN}Hendri Mardani{color.END} tasik tea\nUntuk mengganti frekuensi pakai argumen {color.RED}-sR{color.END}\nContoh penggunaan kode jenis kelamin:\n{color.RED}[1] Pria{color.END}\n{color.BLUE}[2] Wanita{color.END}")
        jk = int(input(f"{color.GREEN}Kode Jenis Kelamin #> {color.END}"))
        print(f"{color.PURPLE}Frekuensi = {sample_rate} Hz{color.END} ")
        text = input(f"{color.YELLOW}Masukkan Text #>{color.END} ")    
        proses(text, jk, output, sample_rate)
        print(f"{color.CYAN}Selesai!!! silahkan cek hasil outputnya{color.END}")
    except:
        print(f"Masukkan nilai yang valid ketikan perintah {color.RED}python3 utama.py --help{color.END} untuk bantuan")
        
if __name__ == "__main__":
    main()
       
