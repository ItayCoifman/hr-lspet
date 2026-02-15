"""
Convert HR-LSPET annotations to COCO keypoints format
"""
import json
import os
from datetime import datetime
import scipy.io
import glob


def load_joints_mat(mat_path):
    """Load joints from .mat file"""
    mat_data = scipy.io.loadmat(mat_path)
    joints = mat_data['joints']  # Shape may vary - need to check actual shape
    print(f"Original joints shape: {joints.shape}")
    # Transpose if needed to get shape (3, 14, N) where 3 = [x, y, visibility]
    if joints.shape[0] == 14 and joints.shape[1] == 3:
        # Shape is (14, 3, N) - transpose to (3, 14, N)
        joints = joints.transpose(1, 0, 2)
        print(f"Transposed joints shape: {joints.shape}")
    return joints


def create_coco_keypoints_json(joints_data, images_dir, output_path):
    """
    Convert HR-LSPET annotations to COCO keypoints format

    Args:
        joints_data: numpy array of shape (3, 14, N) where N is number of images
        images_dir: path to images directory
        output_path: path to save COCO JSON file
    """

    # COCO format structure
    coco_output = {
        "info": {
            "description": "HR-LSPET Dataset in COCO Format",
            "url": "https://sam.johnson.io/research/lspet.html",
            "version": "1.0",
            "year": 2015,
            "contributor": "Leonid Pishchulin, Mykhaylo Andriluka, Bernt Schiele",
            "date_created": datetime.now().strftime("%Y/%m/%d")
        },
        "licenses": [],
        "images": [],
        "annotations": [],
        "categories": [{
            "supercategory": "person",
            "id": 1,
            "name": "person",
            "keypoints": [
                "right_ankle",  # 0
                "right_knee",  # 1
                "right_hip",  # 2
                "left_hip",  # 3
                "left_knee",  # 4
                "left_ankle",  # 5
                "right_wrist",  # 6
                "right_elbow",  # 7
                "right_shoulder",  # 8
                "left_shoulder",  # 9
                "left_elbow",  # 10
                "left_wrist",  # 11
                "neck",  # 12
                "head_top"  # 13
            ],
            "skeleton": [
                [0, 1], [1, 2],  # right leg
                [3, 4], [4, 5],  # left leg
                [6, 7], [7, 8],  # right arm
                [9, 10], [10, 11],  # left arm
                [2, 3],  # hips
                [8, 9],  # shoulders
                [8, 12], [9, 12],  # shoulders to neck
                [12, 13]  # neck to head
            ]
        }]
    }

    # Get list of images
    image_files = sorted(glob.glob(os.path.join(images_dir, "*.png")))

    num_images = joints_data.shape[2]

    for img_idx in range(num_images):
        if img_idx >= len(image_files):
            print(f"Warning: More annotations than images. Stopping at image {img_idx}")
            break

        img_path = image_files[img_idx]
        img_filename = os.path.basename(img_path)

        # Get image dimensions (you may want to use PIL to get actual dimensions)
        from PIL import Image
        img = Image.open(img_path)
        width, height = img.size

        image_id = img_idx + 1

        # Add image entry
        coco_output["images"].append({
            "id": image_id,
            "file_name": img_filename,
            "width": width,
            "height": height,
            "license": 0,
            "flickr_url": "",
            "coco_url": "",
            "date_captured": ""
        })

        # Extract keypoints for this image
        # joints_data shape: (3, 14, N) -> (x, y, visibility, num_keypoints, num_images)
        keypoints = []
        num_visible = 0

        for joint_idx in range(14):
            x = float(joints_data[0, joint_idx, img_idx])
            y = float(joints_data[1, joint_idx, img_idx])
            visibility = int(joints_data[2, joint_idx, img_idx])

            # COCO format: v=0: not labeled, v=1: labeled but not visible, v=2: labeled and visible
            # HR-LSPET: 0 or 1 for visibility
            v = 2 if visibility == 1 else 0

            keypoints.extend([x, y, v])
            if v > 0:
                num_visible += 1

        # Calculate approximate bounding box from keypoints
        visible_x = [joints_data[0, j, img_idx] for j in range(14) if joints_data[2, j, img_idx] == 1]
        visible_y = [joints_data[1, j, img_idx] for j in range(14) if joints_data[2, j, img_idx] == 1]

        if visible_x and visible_y:
            x_min, x_max = min(visible_x), max(visible_x)
            y_min, y_max = min(visible_y), max(visible_y)
            bbox_width = x_max - x_min
            bbox_height = y_max - y_min
            # Add some padding
            padding = 0.1
            x_min = max(0, x_min - bbox_width * padding)
            y_min = max(0, y_min - bbox_height * padding)
            bbox_width = min(width - x_min, bbox_width * (1 + 2 * padding))
            bbox_height = min(height - y_min, bbox_height * (1 + 2 * padding))

            bbox = [float(x_min), float(y_min), float(bbox_width), float(bbox_height)]
            area = float(bbox_width * bbox_height)
        else:
            bbox = [0, 0, 0, 0]
            area = 0.0

        # Add annotation entry
        coco_output["annotations"].append({
            "id": image_id,
            "image_id": image_id,
            "category_id": 1,
            "keypoints": keypoints,
            "num_keypoints": num_visible,
            "bbox": bbox,
            "area": area,
            "iscrowd": 0,
            "segmentation": []
        })

    # Save to JSON file
    with open(output_path, 'w') as f:
        json.dump(coco_output, f, indent=2)

    print(f"Conversion complete!")
    print(f"Total images: {len(coco_output['images'])}")
    print(f"Total annotations: {len(coco_output['annotations'])}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    # Paths
    mat_file = "joints.mat"
    images_dir = "images"
    output_file = "hr_lspet_coco_keypoints.json"

    # Load joints data
    print("Loading joints.mat...")
    joints = load_joints_mat(mat_file)
    print(f"Loaded joints with shape: {joints.shape}")

    # Convert to COCO format
    print("Converting to COCO format...")
    create_coco_keypoints_json(joints, images_dir, output_file)
