#!/usr/bin/env python3

import keyboard
import pyaudio
import wave
import io
import time

# Add the ../../python directory to sys.path for importing evolink_test
import os
import sys
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../python"))
if module_path not in sys.path:
    sys.path.append(module_path)

from evolink_test import test_evolink_cmd

def record_and_send_in_chunks(rate=16000, channels=1, chunk_duration=1.0):
    """
    1) Waits until 'T' is pressed (suppressing its output).
    2) Then, as long as 'T' remains pressed, records audio in fixed-size chunks.
    3) After capturing each chunk, sends it to the system immediately.
    4) Once 'T' is released, the script stops recording and returns.

    :param rate: Audio sample rate (Hz).
    :param channels: Number of channels (1=mono, 2=stereo).
    :param chunk_duration: Seconds of audio captured per chunk before sending.
    """
    # PyAudio constants
    CHUNK = 1024
    FORMAT = pyaudio.paInt16

    # Calculate how many PyAudio reads to gather chunk_duration seconds
    frames_per_chunk = int(rate * chunk_duration / CHUNK)

    print("Press and hold 'T' to start streaming audio in 1-second chunks...")
    # Wait for 'T', suppressing the keystroke from appearing in the console
    keyboard.wait('t', suppress=True)
    print("[INFO] Starting audio stream. Keep holding 'T'...")

    audio_interface = pyaudio.PyAudio()
    stream = audio_interface.open(format=FORMAT,
                                  channels=channels,
                                  rate=rate,
                                  input=True,
                                  frames_per_buffer=CHUNK)

    try:
        while keyboard.is_pressed('t'):
            # Accumulate frames for chunk_duration seconds
            frames = []
            for _ in range(frames_per_chunk):
                data = stream.read(CHUNK)
                frames.append(data)

            # Convert the frames to an in-memory WAV
            wav_bytes = pcm_to_wav_bytes(frames, audio_interface, FORMAT, channels, rate)

            # Send the chunk immediately
            send_chunk_to_evolink(wav_bytes)

    finally:
        # Cleanup once 'T' is released or if an error/KeyboardInterrupt occurs
        stream.stop_stream()
        stream.close()
        audio_interface.terminate()
        print("[INFO] Stopped recording. Exiting stream loop.")

def pcm_to_wav_bytes(frames, audio_interface, fmt, channels, rate):
    """
    Convert a list of PCM frames to an in-memory WAV and return the bytes.
    """
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio_interface.get_sample_size(fmt))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    return wav_buffer.getvalue()

def send_chunk_to_evolink(audio_data):
    """
    Builds a minimal 'speak' command for the chunk and sends it to evolink.
    """
    audio_data_length = len(audio_data)

    # Minimal "speak" command. We only send the audio chunk, no face/body data.
    evolink_cmd = {
        "command": "speak",
        "binary_content_length": audio_data_length,
        "content": {
            "id": "streamChunk",
            "text": "",
            "face_driver": "arkit",
            "body_driver": "emote",
            "face_data_length": 0,
            "body_data_length": 0,
            "audio_data_length": audio_data_length,
            "interrupt": False,  # set True if you want each chunk to interrupt previous
            "frame_rate": 25,
            "animations": []
        }
    }

    # Debug info
    print(f"[DEBUG] Sending chunk of {audio_data_length} bytes to test_evolink_cmd...")

    # The third parameter is a list of binary parts: [face_data, body_data, audio_data]
    test_evolink_cmd(evolink_cmd, True, [b"", b"", audio_data])

def main():
    """
    Main entry point:
    - Streams audio in 1-second chunks while 'T' is pressed (suppressing the 'T').
    - Sends each chunk to test_evolink_cmd as soon as it's captured.
    - Exits once 'T' is released.
    """
    try:
        record_and_send_in_chunks(rate=16000, channels=1, chunk_duration=1.0)
    except KeyboardInterrupt:
        print("\n[INFO] Caught KeyboardInterrupt. Exiting.")

if __name__ == "__main__":
    main()
