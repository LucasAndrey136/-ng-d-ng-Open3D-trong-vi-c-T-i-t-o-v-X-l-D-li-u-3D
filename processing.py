#processing.py

import open3d as o3d
import numpy as np
from .data_loader import get_camera_positions # Import hàm từ module cùng cấp

def downsample(pcd, voxel_size=0.02):
    """Giảm mật độ điểm của point cloud bằng Voxel Grid."""
    print(f"Downsampling with voxel size: {voxel_size}")
    down_pcd = pcd.voxel_down_sample(voxel_size)
    return down_pcd

def remove_statistical_outlier(pcd, nb_neighbors=100, std_ratio=2.0):
    """Loại bỏ các điểm nhiễu (outlier) dựa trên phân tích thống kê."""
    print(f"Removing statistical outliers with nb_neighbors={nb_neighbors}, std_ratio={std_ratio}")
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=nb_neighbors, std_ratio=std_ratio)
    inlier_cloud = pcd.select_by_index(ind)
    return inlier_cloud

def remove_hidden_points(pcd, camera_file):
    """Loại bỏ các điểm bị che khuất dựa trên vị trí camera."""
    print("Removing hidden points...")
    cams = get_camera_positions(camera_file)
    
    # Tham số HPR (Hidden Point Removal)
    diam = np.linalg.norm(pcd.get_max_bound() - pcd.get_min_bound())
    radius = diam * 100.0  # Bán kính lớn để bao hết mô hình
    
    # Hợp nhất các điểm 'visible' từ nhiều camera
    keep = set()
    for c in cams:
        _, pt_map = pcd.hidden_point_removal(c, radius)
        keep.update(pt_map)
        
    pcd_visible = pcd.select_by_index(list(keep))
    print(f"Kept: {len(pcd_visible.points)} / Total: {len(pcd.points)}")
    return pcd_visible

def compute_and_orient_normals(pcd):
    """Ước tính và định hướng pháp tuyến cho point cloud."""
    print("Computing and orienting normals...")
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    pcd.orient_normals_consistent_tangent_plane(100)
    return pcd