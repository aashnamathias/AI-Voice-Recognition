# AI-Based Voice Recognition System

This project is an **AI-based voice recognition system** built using **Wav2Vec2** model, which converts speech to text and also restores punctuation in the transcribed text. The system is implemented using **Python**, **Streamlit**, and **Hugging Face Transformers**.

## Key Features

- **Speech-to-Text**: The core functionality of the system is the ability to transcribe speech into text using the **Wav2Vec2** model.
- **Punctuation Restoration**: Using a pre-trained model, punctuation marks are restored to the transcription, improving readability.
- **Real-Time Voice Input**: The system allows users to upload `.wav` files for transcription and punctuation restoration.

## Technologies Used

- **Wav2Vec2**: Pre-trained model from Hugging Face for speech-to-text conversion.
- **DeepMultilingualPunctuation**: Model for restoring punctuation in text.
- **Streamlit**: Framework for building the app interface.
- **Python**: Programming language used to build the system.
- **Torch & Torchaudio**: Used for audio processing and model inference.
