import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

#Setting Environment Variable
import os

import argparse
parser = argparse.ArgumentParser()


parser.add_argument('--modelname', type=str, required=True)

args = parser.parse_args()

currentModel = args.modelname

print('Using Model' + currentModel)

os.environ['COQUI_STUDIO_TOKEN'] = 'mN39kHqpomiGUp3gdNq6FbF13SUAQ9DpO2U23y0IyW1TwwFfnZUMCFdZDZzRM4z8'
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:32'

torch.cuda.empty_cache()

fileName = "output.wav"

tts = TTS(model_name=currentModel, progress_bar=True).to(device)

if len(tts.speakers) > 0:
    tts.tts_to_file(text="Explore innovative solutions, analyze their BENEFITS and COSTS, and RANK them.", speaker=tts.speakers[0] ,language="en", file_path=fileName)
else:
    tts.tts_to_file(text="Explore innovative solutions, analyze their BENEFITS and COSTS, and RANK them.",language="en", file_path=fileName)
