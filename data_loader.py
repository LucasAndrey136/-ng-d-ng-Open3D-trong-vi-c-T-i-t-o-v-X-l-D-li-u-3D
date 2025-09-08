#data_loader.py

import open3d as o3d
import json
import numpy as np

def load_point_cloud(path):
    """Đọc file point cloud từ đường dẫn."""
    print(f"Loading point cloud from: {path}")
    pcd = o3d.io.read_point_cloud(path)
    if not pcd.has_points():
        raise ValueError(f"Could not read point cloud from {path}")
    return pcd

def get_camera_positions(camera_file):
    """Đọc và trích xuất vị trí camera từ file JSON."""
    print(f"Loading camera positions from: {camera_file}")
    cams = []
    with open(camera_file, "r") as f:
        data = json.load(f)
        for it in data:
            # Giả sử file json có cấu trúc chứa key 'position'
            if 'position' in it:
                cams.append(it["position"])
    
    if not cams:
        raise ValueError("No camera positions found in the JSON file.")
        
    return np.array(cams)