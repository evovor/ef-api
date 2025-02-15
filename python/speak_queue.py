import time
from evolink_test import test_evolink_cmd
from speak_base import evolink_cmd_speak

if __name__ == "__main__":
    evolink_cmd_speak("assets/hello_en.json")
    evolink_cmd_speak("assets/hello_zh.json")
