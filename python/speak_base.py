import random
from evolink_test import test_evolink_cmd
from pathlib import Path
import json


def evolink_cmd_speak(json_filename):
    # read json with
    json_data = json.load(open(json_filename, 'r'))
    base_path = Path(json_filename)

    # read binary content
    text_string = open(base_path.with_name(json_data["text_file"]), encoding='utf-8').read()
    csv_data = open(base_path.with_name(json_data["face_driver_file"])).read()
    face_data = bytes(csv_data, encoding='utf-8')
    face_data_length = len(face_data)
    body_data = bytes("", encoding='utf-8')
    body_data_length = len(body_data)
    audio_data = open(base_path.with_name(json_data["audio_file"]), 'rb').read()
    audio_data_length = len(audio_data)

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
