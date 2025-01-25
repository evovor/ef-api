from evolink_test import test_evolink_cmd

evolink_cmd = {
    "command": "ux_set",
    "ux": {
        "mode": "mobile",
        "viewport_width": 450,
        "viewport_height": 800
    }
}

if __name__ == "__main__":
    test_evolink_cmd(evolink_cmd, True)
