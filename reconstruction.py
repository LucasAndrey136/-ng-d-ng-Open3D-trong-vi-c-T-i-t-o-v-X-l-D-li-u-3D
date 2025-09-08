# reconstruction.py

import open3d as o3d
from .processing import compute_and_orient_normals # Import từ module processing

def reconstruct_with_poisson(pcd, depth=9):
    """
    Tái tạo bề mặt 3D từ point cloud bằng thuật toán Poisson.
    Yêu cầu point cloud phải có pháp tuyến (normals).
    """
    print(f"Running Poisson surface reconstruction with depth: {depth}")
    
    # Đảm bảo pcd đã có pháp tuyến
    if not pcd.has_normals():
        print("Point cloud has no normals. Computing them now.")
        pcd = compute_and_orient_normals(pcd)

    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
            pcd, depth=depth
        )
    return mesh

def reconstruct_with_ball_pivoting(pcd, radii=[0.05, 0.1, 0.2, 0.4]):
    """
    Tái tạo bề mặt 3D bằng thuật toán Ball Pivoting.
    Yêu cầu point cloud phải có pháp tuyến (normals).
    """
    print(f"Running Ball Pivoting reconstruction with radii: {radii}")
    
    if not pcd.has_normals():
        print("Point cloud has no normals. Computing them now.")
        pcd = compute_and_orient_normals(pcd)
        
    radii_vector = o3d.utility.DoubleVector(radii)
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, radii_vector)
    return mesh