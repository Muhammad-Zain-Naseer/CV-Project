import numpy as np
import json
import os
import glob

# ============================================================
# STEP 1: EXTRACT CAMERA DATA FROM YOUR NOTEBOOK
# ============================================================
# After running your notebook (11.ipynb), you will have these variables:
# - K: Camera intrinsic matrix (3x3)
# - R: Rotation matrix for camera 2 (3x3) 
# - t: Translation vector for camera 2 (3x1)
# - Image filenames from your dataset

# This script shows you HOW to save camera data
# You need to ADD this code at the END of your notebook

def save_camera_poses(K, R, t, image1_name, image2_name, output_file="cameras.json"):
    """
    Save camera poses to JSON file
    
    From your notebook you have:
    - Camera 1 is at origin: R1 = Identity, t1 = [0,0,0]
    - Camera 2 has: R2 = R (from recoverPose), t2 = t (from recoverPose)
    
    Args:
        K: 3x3 camera intrinsic matrix
        R: 3x3 rotation matrix of camera 2
        t: 3x1 translation vector of camera 2
        image1_name: filename of first image
        image2_name: filename of second image
        output_file: where to save JSON
    """
    
    # Camera 1: Identity pose (at origin)
    R1 = np.eye(3)
    t1 = np.zeros((3, 1))
    
    # Camera 2: From your reconstruction
    R2 = R
    t2 = t.reshape(3, 1)  # Ensure column vector
    
    # Calculate camera centers in world coordinates
    # Formula: C = -R^T * t
    C1 = -R1.T @ t1
    C2 = -R2.T @ t2
    
    cameras_data = {
        "intrinsics": K.tolist(),
        "cameras": [
            {
                "id": 0,
                "image": image1_name,
                "rotation": R1.tolist(),
                "translation": t1.flatten().tolist(),
                "center": C1.flatten().tolist()
            },
            {
                "id": 1,
                "image": image2_name,
                "rotation": R2.tolist(),
                "translation": t2.flatten().tolist(),
                "center": C2.flatten().tolist()
            }
        ]
    }
    
    with open(output_file, 'w') as f:
        json.dump(cameras_data, f, indent=2)
    
    print(f"\n✓ Saved {len(cameras_data['cameras'])} cameras to {output_file}")
    print(f"  Camera 1: {image1_name}")
    print(f"  Camera 2: {image2_name}")
    return cameras_data


# ============================================================
# EXAMPLE: How to use in your notebook
# ============================================================
# Add this code at the END of your notebook after you have R, t, K

"""
# Get your image filenames
import os
image_files = sorted(os.listdir('your_images_folder'))
image1_name = image_files[0]  # First image you used
image2_name = image_files[1]  # Second image you used

# Save camera poses
save_camera_poses(K, R, t, image1_name, image2_name, "cameras.json")
"""

print("="*60)
print("HOW TO USE THIS SCRIPT:")
print("="*60)
print("\n1. Run your notebook (11.ipynb) completely")
print("\n2. After the cell where you get R and t from cv2.recoverPose()")
print("   Add a NEW CELL with this code:")
print("\n" + "-"*60)
print("""
import json
import numpy as np

def save_camera_poses(K, R, t, image1_name, image2_name, output_file="cameras.json"):
    # Camera 1: Identity pose (at origin)
    R1 = np.eye(3)
    t1 = np.zeros((3, 1))
    
    # Camera 2: From reconstruction
    R2 = R
    t2 = t.reshape(3, 1)
    
    # Calculate camera centers: C = -R^T * t
    C1 = -R1.T @ t1
    C2 = -R2.T @ t2
    
    cameras_data = {
        "intrinsics": K.tolist(),
        "cameras": [
            {
                "id": 0,
                "image": image1_name,
                "rotation": R1.tolist(),
                "translation": t1.flatten().tolist(),
                "center": C1.flatten().tolist()
            },
            {
                "id": 1,
                "image": image2_name,
                "rotation": R2.tolist(),
                "translation": t2.flatten().tolist(),
                "center": C2.flatten().tolist()
            }
        ]
    }
    
    with open(output_file, 'w') as f:
        json.dump(cameras_data, f, indent=2)
    
    print(f"✓ Saved cameras to {output_file}")

# Use it (replace with your actual image names)
save_camera_poses(K, R, t, "image_001.jpg", "image_002.jpg", "cameras.json")
""")
print("-"*60)
print("\n3. This will create 'cameras.json' file with your camera data")
print("\n4. Then you can use the Three.js viewer to visualize it!")
