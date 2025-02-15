import random
from evolink_test import test_evolink_cmd
from pathlib import Path
import json


def evolink_cmd_speak(json_filename):
    # read json with
    json_data = json.load(open(json_filename, 'r'))
    base_path = Path(json_filename).parent

    # read binary content
    try:
        with open(base_path / json_data["text_file"], encoding='utf-8') as text_file:
            text_string = text_file.read()
    except OSError:
        text_string = ""

    try:
        with open(base_path / json_data["audio_file"], 'rb') as audio_file:
            audio_data = audio_file.read()
    except OSError:
        audio_data = bytes()
    audio_data_length = len(audio_data)

    try:
        with open(base_path / json_data["face_driver_file"]) as face_file:
            csv_data = face_file.read()
    except OSError:
        csv_data = ""
    face_data = bytes(csv_data, encoding='utf-8')
    face_data_length = len(face_data)

    body_data = bytes("", encoding='utf-8')
    body_data_length = len(body_data)

    # In case they are not specified in the source json_data
    id = random.randint(1, 10000)
    if "id" in json_data:
        id = json_data['id']

    face_driver = 'arkit'
    if "face_driver" in json_data:
        face_driver = json_data['face_driver']

    body_driver = 'sku'
    if "body_driver" in json_data:
        body_driver = json_data['body_driver']

    interrupt = False
    if "interrupt" in json_data:
        interrupt = json_data['interrupt']

    # assemble command
    evolink_cmd = {
        "command": "speak",
        'binary_content_length': face_data_length + body_data_length + audio_data_length,
        "content": {
            'id': str(id),
            'text': text_string,
            'face_driver': face_driver,
            'body_driver': body_driver,
            'face_data_length': face_data_length,
            'body_data_length': body_data_length,
            'audio_data_length': audio_data_length,
            'interrupt': interrupt,
            'frame_rate': json_data['frame_rate'],
            "animations": json_data['animations']
        }
    }

    test_evolink_cmd(evolink_cmd, True, [face_data, body_data, audio_data])
