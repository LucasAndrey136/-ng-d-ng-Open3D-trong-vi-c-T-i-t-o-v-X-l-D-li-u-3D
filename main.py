# main.py 
import os
import open3d as o3d
from src.data_loader import load_point_cloud
from src.processing import remove_hidden_points, remove_statistical_outlier, downsample
from src.reconstruction import reconstruct_with_poisson

# --- Cấu hình ---
WORKING_DIR = "đường/dẫn/tới/folder/No-face-2.4"
camera_file = os.path.join(WORKING_DIR, "cameras.json")

# --- Bước 0: Đường dẫn file ---
input_original = os.path.join(WORKING_DIR, "point_cloud_orig.ply")
output_step1 = os.path.join(WORKING_DIR, "point_cloud_no_hidden_step1.ply")
output_step2 = os.path.join(WORKING_DIR, "point_cloud_remove_outlier_step2.ply")
output_step3 = os.path.join(WORKING_DIR, "point_cloud_downsampled_step3.ply")
output_step4 = os.path.join(WORKING_DIR, "point_cloud_poisson_reconstruct_final.ply")


# --- STEP 1: REMOVE HIDDEN POINTS ---
print("--- BẮT ĐẦU BƯỚC 1: LOẠI BỎ ĐIỂM BỊ CHE KHUẤT ---")
pcd_orig = load_point_cloud(input_original)
pcd_no_hidden = remove_hidden_points(pcd_orig, camera_file)
o3d.io.write_point_cloud(output_step1, pcd_no_hidden)


# --- STEP 2: REMOVE OUTLIER ---
print("\n--- BẮT ĐẦU BƯỚC 2: LOẠI BỎ NHIỄU ---")
pcd_no_outlier = remove_statistical_outlier(pcd_no_hidden, nb_neighbors=30, std_ratio=2.0)
o3d.io.write_point_cloud(output_step2, pcd_no_outlier)


# --- STEP 3: DOWN SAMPLE ---
print("\n--- BẮT ĐẦU BƯỚC 3: GIẢM MẬT ĐỘ ĐIỂM ---")
pcd_downsampled = downsample(pcd_no_outlier, voxel_size=0.02)
o3d.io.write_point_cloud(output_step3, pcd_downsampled)


# --- STEP 4: RECONSTRUCTION ---
print("\n--- BẮT ĐẦU BƯỚC 4: TÁI TẠO BỀ MẶT ---")
# Hàm reconstruct_with_poisson đã tự tính normals nếu chưa có
reconstructed_mesh = reconstruct_with_poisson(pcd_downsampled, depth=9)
o3d.io.write_triangle_mesh(output_step4, reconstructed_mesh)


# --- Hiển thị kết quả cuối cùng ---
print("\n--- QUÁ TRÌNH HOÀN TẤT! ---")
print("Hiển thị mô hình 3D đã tái tạo...")
o3d.visualization.draw_geometries([reconstructed_mesh])