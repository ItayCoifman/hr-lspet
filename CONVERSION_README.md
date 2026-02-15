# HR-LSPET to COCO Keypoints Conversion

This script converts the HR-LSPET dataset annotations from MATLAB format to COCO keypoints JSON format.

## Usage

```bash
python convert_to_coco.py
```

## Requirements

- Python 3.x
- scipy
- Pillow (PIL)
- numpy

Install dependencies:
```bash
pip install scipy Pillow numpy
```

## Output

The script generates `hr_lspet_coco_keypoints.json` with the following structure:

### COCO Format Structure
- **info**: Dataset metadata
- **licenses**: License information (empty)
- **images**: List of 9,428 image entries with id, file_name, width, height
- **annotations**: List of 9,428 annotation entries with keypoints, bbox, area
- **categories**: Single "person" category with 14 keypoints

### Keypoint Order (14 keypoints)
1. right_ankle (0)
2. right_knee (1)
3. right_hip (2)
4. left_hip (3)
5. left_knee (4)
6. left_ankle (5)
7. right_wrist (6)
8. right_elbow (7)
9. right_shoulder (8)
10. left_shoulder (9)
11. left_elbow (10)
12. left_wrist (11)
13. neck (12)
14. head_top (13)

### Keypoint Format
Each keypoint is represented as `[x, y, v]` where:
- `x`, `y`: Pixel coordinates
- `v`: Visibility flag (0 = not labeled, 2 = labeled and visible)

### Skeleton Connections
The skeleton defines limb connections between keypoints for visualization:
- Right leg: ankle → knee → hip
- Left leg: ankle → knee → hip
- Right arm: wrist → elbow → shoulder
- Left arm: wrist → elbow → shoulder
- Torso: hips connected, shoulders connected to neck, neck to head

## Notes

- Bounding boxes are automatically calculated from visible keypoints with 10% padding
- Missing images from the original dataset are handled gracefully
- Each image has exactly one person annotation (single-person poses)

