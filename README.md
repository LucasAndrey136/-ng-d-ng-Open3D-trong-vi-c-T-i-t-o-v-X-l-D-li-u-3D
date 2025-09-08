# Dự án: Tái tạo và Xử lý Dữ liệu 3D với Open3D

## 📜 Giới thiệu chung

Dự án này tập trung vào việc ứng dụng thư viện Open3D để thực hiện các tác vụ xử lý và tái tạo mô hình 3D từ dữ liệu đám mây điểm (point cloud). Mục tiêu chính là khám phá các thuật toán tiền xử lý dữ liệu, tái tạo bề mặt và trực quan hóa các đối tượng 3D một cách hiệu quả.

**Tài liệu tham khảo và dữ liệu:**
*   **Notion:** [Tài liệu tổng quan dự án](https://tamnguyen1213519.notion.site/23e4f5da2dbf80c98362c251778ca80e?v=23e4f5da2dbf80c69eff000c1c03785d&p=2514f5da2dbf80a78de9e49f7fe51472&pm=s)
*   **Google Colab:** [Notebook thực thi chính](https://colab.research.google.com/drive/18e-Fkwpns_9BtoG7_EqqyNMpBuc1OE7S)
*   **Google Drive:** [Bộ dữ liệu sử dụng](https://drive.google.com/drive/folders/1WbRAecSF3pgWnaA4k1x2tdt-2nU4AHbm)

---

## ✨ Các tính năng chính

*   **Đọc và Trực quan hóa:** Đọc nhiều định dạng file 3D (ví dụ: `.pcd`, `.ply`, `.obj`) và trực quan hóa đám mây điểm.
*   **Tiền xử lý dữ liệu:**
    *   Downsampling (Giảm mật độ điểm) bằng Voxel Grid.
    *   Loại bỏ điểm ngoại lai (outlier removal).
    *   Ước tính pháp tuyến (normal estimation).
*   **Tái tạo bề mặt (Surface Reconstruction):**
    *   Áp dụng thuật toán Ball Pivoting.
    *   Áp dụng thuật toán Poisson Surface Reconstruction.
*   **Căn chỉnh (Registration):** Căn chỉnh và ghép nối nhiều đám mây điểm với thuật toán ICP (Iterative Closest Point).

---

## 🛠️ Công nghệ sử dụng

*   **Ngôn ngữ:** Python 3
*   **Thư viện chính:**
    *   [Open3D](http://www.open3d.org/): Thư viện mã nguồn mở cho xử lý dữ liệu 3D.
    *   [NumPy](https://numpy.org/): Thư viện cho tính toán khoa học.
    *   [Matplotlib](https://matplotlib.org/): Thư viện để vẽ biểu đồ và trực quan hóa (nếu có).

---

## 🚀 Hướng dẫn cài đặt và sử dụng

### 1. Yêu cầu
*   Python >= 3.8

### 2. Cài đặt môi trường
Đầu tiên, clone repository này về máy của bạn:
```bash
git clone [URL-repository-cua-ban]
cd [ten-repository]
```

Tạo một môi trường ảo (khuyến khích) để quản lý các thư viện:
```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```


### 3. Dữ liệu
Tải bộ dữ liệu từ [Google Drive](https://drive.google.com/drive/folders/1WbRAecSF3pgWnaA4k1x2tdt-2nU4AHbm) và giải nén vào thư mục `data/raw/`.

### 4. Chạy dự án
Bạn có thể xem và chạy toàn bộ quy trình xử lý trong file notebook:
`notebooks/Xu_ly_3D_Open3D.ipynb`

## 📈 Kết quả minh họa

Dưới đây là một số hình ảnh kết quả từ dự án.

**1. Đám mây điểm gốc (Raw Point Cloud)**
*(Bạn hãy chèn ảnh đám mây điểm gốc vào đây)*
`![Raw Point Cloud](results/images/raw_point_cloud.png)`

**2. Đám mây điểm sau khi xử lý (Processed Point Cloud)**
*(Bạn hãy chèn ảnh đám mây điểm đã lọc nhiễu, giảm mật độ vào đây)*
`![Processed Point Cloud](results/images/processed_point_cloud.png)`

**3. Mô hình 3D sau khi tái tạo (Reconstructed 3D Model)**
*(Bạn hãy chèn ảnh mô hình 3D hoàn chỉnh vào đây)*
`![Reconstructed Model](results/images/reconstructed_model.png)`

---
