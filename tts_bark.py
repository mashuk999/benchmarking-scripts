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

[clears throat] Good day, everyone. We've got some breaking news from Manipur that's sure to bring a sigh of relief to its residents. Chief Minister N Biren Singh has announced the restoration of mobile internet services in the state after nearly five long months of blackout.

[laughs] Yes, you heard it right! The internet services, both mobile and broadband, were cut off in Manipur on May 3 due to the outbreak of violence. Initially, it was meant to be a short-lived measure, lasting just five days. But with the ongoing law-and-order concerns, the ban kept getting extended in five-day increments.

Now, a member of CM Singh's team has informed The Indian Express that the decision to restore mobile internet services has been communicated to the relevant teams, and it's expected to be up and running within a few hours.

[sighs]

I can only imagine how the people of Manipur must have felt during these months of disconnectedness.

[clears throat]

The situation got so dire that even broadband services, which had been conditionally restored back in July, came with certain restrictions. The government was concerned about the spread of disinformation and false rumors through social media platforms. Bulk SMS was also a concern, as it could potentially mobilize agitators and demonstrators, posing risks to life and property.

[gasps]

But the winds of change seem to be blowing in Manipur. Just last month, the Manipur High Court directed the state government to find a way to provide internet services through mobile phones, albeit through a case-to-case whitelisting process and in phases.

[music]

[laughs] It appears the people's voices were heard, and connectivity is on its way back to the state. This is certainly a significant development, and we'll be keeping a close eye on the situation as it unfolds.

[laughter]

That's it for now, folks. Stay tuned for more updates, and remember, a connected world is a powerful world.

[outro music]"""

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
