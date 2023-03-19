import openai
import gradio as gr
from pydub import AudioSegment


openai.api_key = "add-your-api-key"

message_history = []
audio_history = []


def predict(input):
    global message_history

    message_history.append({"role": "user", "content": input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message_history
    )

    reply_content = completion.choices[0].message.content
    print(reply_content)

    message_history.append({"role": "user", "content": reply_content.strip()})

    response = [
        (message_history[i]["content"], message_history[i + 1]["content"])
        for i in range(0, len(message_history) - 1, 2)
    ]

    return response


def transcribe(audio_file):
    global audio_history

    audio = AudioSegment.from_file(audio_file)
    audio_file_wav = "./tmp/" + "record" + str(len(audio_history)) + ".wav"

    audio.export(audio_file_wav, format="wav")

    audio_file = open(audio_file_wav, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print("user", transcript["text"])

    audio_history.append({"role": "user", "content": transcript["text"]})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=audio_history
    )

    reply_content = completion.choices[0].message.content

    audio_history.append({"role": "user", "content": reply_content.strip()})

    response = [
        (audio_history[i]["content"], audio_history[i + 1]["content"])
        for i in range(0, len(audio_history) - 1, 2)
    ]

    return response


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("### Chatbot with Openai ChatGPT API and Whisper API!")
    with gr.Tab("Text"):
        chatbot = gr.Chatbot()
        with gr.Row():
            txt = gr.Textbox(
                show_label=False, placeholder="Type your message here"
            ).style(container=False)
            txt.submit(predict, txt, chatbot)
            txt.submit(None, None, txt, _js="() => {''}")

    with gr.Tab("Audio"):
        chatbot = gr.Chatbot()
        with gr.Row():
            audio = gr.Audio(source="microphone", type="filepath")
            greet_btn = gr.Button("Send")
            greet_btn.click(fn=transcribe, inputs=audio, outputs=chatbot)

demo.launch()
