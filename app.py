# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-q3bABvYx_c-UUyUN-Ep5BHoKysyeDhj
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
# from deepmultilingualpunctuation import PunctuationModel
# import torch
# import torchaudio
# import tempfile
# import re
# 
# st.title("🎙️ Voice Recognition")
# 
# @st.cache_resource
# def load_model():
#     processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
#     model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
#     return processor, model
# 
# @st.cache_resource
# def load_punct_model():
#     return PunctuationModel()
# 
# processor, model = load_model()
# punct_model = load_punct_model()
# 
# uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])
# 
# if uploaded_file is not None:
#     st.audio(uploaded_file)
# 
#     with tempfile.NamedTemporaryFile(delete=False) as tmp:
#         tmp.write(uploaded_file.read())
#         tmp_path = tmp.name
# 
#     speech_array, sampling_rate = torchaudio.load(tmp_path)
#     resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16000)
#     speech = resampler(speech_array).squeeze().numpy()
# 
#     inputs = processor(speech, sampling_rate=16000, return_tensors="pt", padding=True)
# 
#     with st.spinner("Transcribing... please wait ⏳"):
#         with torch.no_grad():
#             logits = model(**inputs).logits
#         predicted_ids = torch.argmax(logits, dim=-1)
#         transcription = processor.decode(predicted_ids[0])
# 
#     st.markdown("### ✏️ Raw Transcription:")
#     st.success(transcription)
#     st.markdown(f"**🔢 Word Count:** {len(transcription.split())}")
# 
#     with st.spinner("Restoring punctuation... ✍️"):
#         punctuated_text = punct_model.restore_punctuation(transcription)
# 
#         # Capitalize the first word of each sentence
#         punctuated_text = re.sub(r'([.?!]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), punctuated_text)
#         punctuated_text = punctuated_text[0].upper() + punctuated_text[1:]
# 
#     st.markdown("### 📝 Transcription with Punctuation:")
#     st.info(punctuated_text)
#