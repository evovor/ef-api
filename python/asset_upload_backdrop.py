from evolink_test import test_evolink_cmd

img_data = open("assets/backdrop.jpg", "rb").read()
img_data_len = len(img_data)

evolink_cmd = {
    "command": "asset_upload",
    "binary_content_length": img_data_len,
    "body": {
        "display_name": "Sample Image",
        "usage": "backdrop",
        "filename": "sample_image.jpg",
        "image_content_length": img_data_len,
    },
}
    
if __name__ == "__main__":
    test_evolink_cmd(evolink_cmd, True, [img_data])