from evolink_test import test_evolink_cmd

evolink_cmd = {
    "command": "backdrop_apply",
    "preset": {
        "backdrop_render_preset": {
            "scalar_map":{
                "Blend_Intensity" : 1.0,
                "SolidColourMode" : 0.0
            },
            "vector_map": {
                "TintColour": {"r":1.0,"g":1.0,"b":1.0,"a":1.0}
            },
            "texture_asset_map": {
                "Background": "/p/backdrop/sample_image.jpg"
            }
        }
    }
}
    
if __name__ == "__main__":
    test_evolink_cmd(evolink_cmd, True)