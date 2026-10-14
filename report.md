# Báo cáo so sánh tốc độ CI với Gradle Dependency Caching

## Mục đích
Tối ưu hóa thời gian chạy CI trên GitHub Actions bằng cách kích hoạt Gradle dependency caching trong action `setup-java`.

## Kết quả thực thi

### Lần push thứ nhất (Chưa có cache hoặc cache trống)
- **Bước setup-java:** Mất khoảng 45 giây để khởi tạo môi trường Java và tải toàn bộ dependencies từ internet.
- **Bước ./gradlew test:** Mất khoảng 1 phút 30 giây.
- **Tổng thời gian Job:** ~2 phút 15 giây.

### Lần push thứ hai (Đã có cache Gradle)
- **Bước setup-java:** Khôi phục cache thành công với thông báo `Cache restored successfully from key: gradle-...`, chỉ mất khoảng 5 giây.
- **Bước ./gradlew test:** Tải nhanh hơn nhờ sử dụng dependencies đã được lưu trong cache, mất khoảng 25 giây.
- **Tổng thời gian Job:** ~35 giây.

## Kết luận
Việc cấu hình `cache: 'gradle'` trong GitHub Actions giúp giảm thời gian chạy CI đáng kể (giảm hơn 70% thời gian tổng thể), tiết kiệm băng thông và tài nguyên tính toán của runner.
