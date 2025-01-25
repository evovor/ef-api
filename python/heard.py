from evolink_test import test_evolink_cmd

evolink_cmd = {
    "command": "heard",
    "content": {
        "id": "Heard12345",
        "type": "question",  # This can be "questoin" / "answer" .... etc
        "inquiries": "English & 中文"
    }
}
    
if __name__ == "__main__":
    test_evolink_cmd(evolink_cmd, False)