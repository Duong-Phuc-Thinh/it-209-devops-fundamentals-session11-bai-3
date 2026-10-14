# Bài 3: Tối ưu tốc độ CI bằng Gradle Dependency Caching

## Giới thiệu
Thư mục này chứa mã nguồn cấu hình GitHub Actions CI cho dự án Java sử dụng Gradle, tích hợp tính năng caching để tăng tốc độ thực thi pipeline.

## Các chức năng đã làm
- Cấu hình tệp `.github/workflows/ci.yml` sử dụng `actions/setup-java@v5` với tham số `cache: 'gradle'`.
- Tạo tệp báo cáo `report.md` so sánh thời gian thực thi giữa lần chạy đầu tiên và lần chạy thứ hai.
- Viết script Python `main.py` để kiểm tra sự tồn tại và tính hợp lệ của cấu hình CI.

## Hướng dẫn chạy
1. Đặt tệp cấu hình CI vào thư mục `.github/workflows/ci.yml` trong repository của bạn.
2. Push code lên GitHub để kích hoạt GitHub Actions.
3. Chạy script kiểm tra:
   ```bash
   python homework/session_11/ex3/main.py
   ```
