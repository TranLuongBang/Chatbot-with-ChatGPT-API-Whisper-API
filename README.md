## Chatbot with OpenAI ChatGPT API and Whisper API
This is a chatbot application that uses ChatGPT API with `gpt-3.5-turbo` and Speech-to-Text by Whisper API with `whisper-1` for natural language processing and understanding. The chatbot can communicate with users via a web interface created using Gradio.

### Features

- Natural Language Processing (NLP) powered by ChatGPT API and GPT-2.5-turbo for generating responses to user input
- Speech-to-Text transcription using Whisper API for allowing users to speak to the chatbot via a microphone
- User-friendly web interface created with Gradio, a Python library for building customizable UI components
- Flexible customization options for Gradio UI components, including text inputs, voice inputs, and dropdown menus

### Requirements
- Python 
- openai
- gradio
- ffmpeg (for audio processing)
- A ChatGPT API key (sign up [here](https://auth0.openai.com/u/signup/identifier?state=hKFo2SAwZzlYR0pjYmpXNTZ4QTZYM2hISnZpVWM1OGRSclNLa6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEx5QzN1WTdSekxJRks1R0twRi1YajZkQ19rZ3RXR3ZJo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q) for a free account)

### Installation
1. Clone the repo `git clone https://github.com/TranLuongBang/Chatbot-with-ChatGPT-API-Whisper-API`
2. Navigate to the project directory: `cd Chatbot-with-ChatGPT-API-Whisper-API`
3. Create environment and Install the requirements
```python
python -m venv .venv
source .venv/bin/active
pip install -r requirements.txt
```
Install ffmpeg for audio precessing
```
sudo apt update && sudo apt upgrade
sudo apt install ffmpeg
ffmpeg -version
```

### Usage
1. Run the app: `python chatapp.py`

2. Open a web browser and go to http://127.0.0.1:7860

3. Type in a message or speak into the microphone to start a conversation with the chatbot
