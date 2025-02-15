from evolink_test import test_evolink_cmd

evolink_cmd = {
    "command": "ux_culture_set",
    "culture": "zh-CN"
}

# Chinese: zh-CN
# Japanese: ja-JP
# English: en-US
# Arabic: ar
# ...

if __name__ == "__main__":
    test_evolink_cmd(evolink_cmd, True)
