from evolink_test import test_evolink_cmd

evolink_cmd = {
  "command": "camera_cut_apply",
  "preset": {
    "modelTransform": {
      "rotation": {
        "x": 0,
        "y": 0,
        "z": 0,
        "w": 1
      },
      "translation": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "scale3D": {
        "x": 1,
        "y": 1,
        "z": 1
      }
    },
    "location": {
      "x": 34.9370047397338,
      "y": -48.529113092866375,
      "z": -4.390010601060153
    },
    "targetOffset": {
      "x": 0,
      "y": 0,
      "z": 100
    },
    "socketOffset": {
      "x": 0,
      "y": 24.959533275336653,
      "z": -9.229698254126854
    },
    "targetArmLength": 321.67010498046875,
    "armRotate": {
      "pitch": -8.360043525695803,
      "yaw": -40.86133193969727,
      "roll": -6.46961261607088e-14
    },
    "filmbackPresetName": "16:9 DSLR",
    "filmbackSettings": {
      "sensorWidth": 36,
      "sensorHeight": 20.25,
      "sensorAspectRatio": 1.7777777910232544
    },
    "lensPresetName": "85mm Prime f/1.8",
    "lensSettings": {
      "minFocalLength": 85,
      "maxFocalLength": 85,
      "minFStop": 1.7999999523162842,
      "maxFStop": 22,
      "minimumFocusDistance": 15,
      "squeezeFactor": 1,
      "diaphragmBladeCount": 7
    },
    "focalLength": 85,
    "aperture": 2.799999952316284,
    "focusSettings": {
      "focusMethod": "Disable",
      "manualFocusDistance": 100000,
      "trackingFocusSettings": {
        "actorToTrack": "None",
        "relativeOffset": {
          "x": 0,
          "y": 0,
          "z": 0
        }
      },
      "debugFocusPlaneColor": {
        "b": 204,
        "g": 26,
        "r": 102,
        "a": 153
      },
      "bSmoothFocusChanges": False,
      "focusSmoothingInterpSpeed": 8,
      "focusOffset": 0
    }
  }
}

if __name__ == "__main__":
    test_evolink_cmd(evolink_cmd)