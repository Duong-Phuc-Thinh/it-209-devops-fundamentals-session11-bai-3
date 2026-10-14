import os

def main():
    print("Bài 3: Tối ưu tốc độ CI bằng Gradle Dependency Caching")
    workflow_path = ".github/workflows/ci.yml"
    if os.path.exists(workflow_path):
        print(f"Tệp cấu hình CI đã tồn tại tại: {workflow_path}")
        with open(workflow_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "cache: 'gradle'" in content:
                print("Đã cấu hình thành công cache: 'gradle' trong setup-java.")
            else:
                print("Chưa tìm thấy cấu hình cache trong tệp CI.")
    else:
        print("Không tìm thấy tệp CI workflow.")

if __name__ == "__main__":
    main()
