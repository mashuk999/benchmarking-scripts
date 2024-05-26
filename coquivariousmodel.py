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

texTTS = """
स्टॉक मार्केट के उतार-चढ़ाव बाजार के स्वभाव का हिस्सा हैं और निवेशकों के लिए सावधानी बरतना आवश्यक होता है। निवेशकों को निवेश करने से पहले बाजार के नियमों और नियमावलियों को समझना चाहिए। विभिन्न कंपनियों के संदर्भ में अच्छे अनुसंधान के साथ, विशेषज्ञों की सलाह लेना भी महत्वपूर्ण है। स्टॉक मार्केट में निवेश करते समय ध्यान देना चाहिए कि निवेश के लिए उपलब्ध संसाधनों का प्रबंधन कैसे किया जाए। अंततः, निवेशकों को धीरे-धीरे बाजार के कारोबार की प्रक्रिया को समझते हुए अपने निवेशों को बढ़ाना चाहिए।
"""

print(os.system('pwd'))

print(os.system('ls -alrth'))

tts.tts_to_file(text=texTTS, file_path=fileName)
