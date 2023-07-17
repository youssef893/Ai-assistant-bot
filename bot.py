import subprocess
import time

import google.generativeai as palm
from AppOpener import open
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM


def open_windows_apps(application_name):
    try:
        start = time.perf_counter()
        # open app send the path or app name
        if ":" in application_name:
            subprocess.Popen(application_name, shell=True)
        else:
            open(application_name, match_closest=True)

        end = time.perf_counter()

        if (end - start) < 0.1:
            return True
        else:
            return False

    except FileNotFoundError:
        print(f"Application '{application_name}' not found or not in the system PATH")


def translate(text):
    """
        it is a function to translate string from english to arabic
        by loading pretrained model from hugging face

        :parameter text: string
        :return translated text
    """
    tokenizer = AutoTokenizer.from_pretrained("anibahug/marian-finetuned-kde4-en-to-ar")
    model = TFAutoModelForSeq2SeqLM.from_pretrained("anibahug/marian-finetuned-kde4-en-to-ar", from_pt=True)
    translated = model.generate(**tokenizer(text, return_tensors="tf", padding=True))

    translated_text = ''

    for t in translated:
        translated_text = translated_text.join(tokenizer.decode(t, skip_special_tokens=True))

    return translated_text


def chat_with_palm(message):
    """
    Connect with palm api to make chatbot
    :param message: string
    :return: last response from chatbot
    """
    palm.configure(api_key='AIzaSyBJQ4rjTPOiLJMWDmy0-J1-eodYGYEUfIM')
    response = palm.chat(messages='hi')
    response = response.reply(message=message)
    return response.last


def main(message):
    if "open" in message:
        return open_windows_apps(message[4:])
    elif "translate" in message:
        return translate(message[10:])
    else:
        return chat_with_palm(message)
