from evolink_test import test_evolink_cmd
from speak_base import evolink_cmd_speak

cmd_interrupt = {
    "command": "speak",
    'binary_content_length': 0,
    "content": {
        'id': -1,
        'text': "This is a text only command, the audio and face expressions a procedurally generated",
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
                'body_anim_sku': 'Hello',
                'loop': False,
                'blend': 0.5
            }
        ]
    }
}

if __name__ == "__main__":
    test_evolink_cmd(cmd_interrupt, True, [])