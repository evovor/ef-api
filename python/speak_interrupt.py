from evolink_test import test_evolink_cmd

cmd_interrupt = {
    "command": "speak",
    'binary_content_length': 0,
    "content": {
        'id': -1,
        'text': "",
        'face_driver': 'arkit',
        'body_driver': 'sku',
        'face_data_length': 0,
        'body_data_length': 0,
        'audio_data_length': 0,
        'interrupt': True,
        'frame_rate': 0,
        "animations": []
    }
}

if __name__ == "__main__":
    test_evolink_cmd(cmd_interrupt, True, [])
