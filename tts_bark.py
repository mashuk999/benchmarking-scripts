import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from scipy.io.wavfile import write as write_wav

import nltk  # we'll use this to split into sentences
nltk.download('punkt')
import numpy as np

from bark.generation import (
    generate_text_semantic,
    preload_models,
)
from bark.api import semantic_to_waveform
from bark import generate_audio, SAMPLE_RATE

preload_models()

print('Started Generating Audio')

# generate audio from text
text_prompt = """[intro music]

We've got some breaking news from Manipur that's sure to bring a sigh of relief to its residents.
"""

script = text_prompt.replace("\n", " ").strip()

sentences = nltk.sent_tokenize(script)

SPEAKER = "v2/en_speaker_6"
GEN_TEMP = 0.6
silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

pieces = []
for sentence in sentences:
    semantic_tokens = generate_text_semantic(
        sentence,
        history_prompt=SPEAKER,
        temp=GEN_TEMP,
        min_eos_p=0.05,  # this controls how likely the generation is to end
    )

    audio_array = semantic_to_waveform(semantic_tokens, history_prompt=SPEAKER,)
    pieces += [audio_array, silence.copy()]

write_wav("bark_generation.wav", SAMPLE_RATE, np.concatenate(pieces))
