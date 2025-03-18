#!/usr/bin/env python3

import speech_recognition as sr
import requests
import re

# Add the ../../python directory to sys.path for importing evolink_test
import os
import sys
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../python"))
if module_path not in sys.path:
    sys.path.append(module_path)

from evolink_test import test_evolink_cmd

# DeepSeek API endpoint
DEEPSEEK_API_URL = "http://192.168.0.107:11434/v1/chat/completions"

# Your API key
API_KEY = "your_api_key_here"

# Set the request headers, including the API key
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def recognize_speech_from_mic(recognizer, microphone):
    """
    Listen from the microphone and recognize the speech as text.
    """
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please start speaking...")
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio, language="zh-CN")
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API is unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def process_text(text):
    """
    Build a prompt using the recognized text, send it to the DeepSeek API,
    clean the response, and call test_evolink_cmd() to process the result.
    """
    # Append a requirement for the answer to not exceed 50 characters.
    prompt = text + ", keep answer within 50 words"  
    print(f"Prompt sent to DeepSeek: {prompt}")

    # Build the request body
    data = {
        "model": "deepseek-r1:32b",  # Replace with the DeepSeek model you want to use
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False  # Make sure streaming is disabled; get the full result
    }

    # Send the POST request to the DeepSeek API
    response = requests.post(DEEPSEEK_API_URL, json=data)
    if response.status_code == 200:
        # Parse the response
        result = response.json()
        # Extract the model's reply
        model_reply = result['choices'][0]['message']['content']

        # Remove <think></think> tags and their content
        cleaned_reply = re.sub(r'<think>.*?</think>', '', model_reply, flags=re.DOTALL)

        # Strip extra whitespace/newlines
        cleaned_reply = cleaned_reply.strip()

        cmd_interrupt = {
            "command": "speak",
            'binary_content_length': 0,
            "content": {
                'id': -1,
                'text': cleaned_reply,
                'face_driver': 'arkit',
                'body_driver': 'emote',
                'face_data_length': 0,
                'body_data_length': 0,
                'audio_data_length': 0,
                'interrupt': True,
                'frame_rate': 0,
                'animations': [
                    {
                        'timestamp': 0.0,
                        'body_anim_sku': 'TALK',
                        'loop': False,
                        'blend': 0.5
                    }
                ]
            }
        }

        # Pass the command to test_evolink_cmd
        test_evolink_cmd(cmd_interrupt, True, [])
    else:
        print(f"Error: Received status code {response.status_code} from DeepSeek")

def main():
    """
    Main entry point:
    1. Initialize the speech recognizer and microphone.
    2. Perform speech recognition.
    3. Process the recognized text with the DeepSeek API.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Speech recognition program started...")
    result = recognize_speech_from_mic(recognizer, microphone)

    if result["success"]:
        recognized_text = result["transcription"]
        print("Recognition result: {}".format(recognized_text))
        process_text(recognized_text)
    else:
        print("Recognition failed: {}".format(result["error"]))

if __name__ == "__main__":
    main()
