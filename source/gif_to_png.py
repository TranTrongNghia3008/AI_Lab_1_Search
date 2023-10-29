import os
from PIL import Image

# Đường dẫn đến thư mục chứa các file GIF
input_directory = "..\\output"

# Đường dẫn đến thư mục chứa các file PNG đầu ra
output_directory = "..\\png"

# Tạo thư mục đầu ra nếu nó chưa tồn tại
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Lấy danh sách tất cả các file GIF trong các thư mục con
gif_files = []
for root, dirs, files in os.walk(input_directory):
    for file in files:
        if file.endswith(".gif"):
            gif_files.append(os.path.join(root, file))

# Chuyển đổi các file GIF sang PNG và lưu vào thư mục đầu ra
for gif_file in gif_files:
    gif_image = Image.open(gif_file)

    # Tạo danh sách để lưu trữ các frame
    frames = []

    try:
        while True:
            frame = gif_image.copy()
            frames.append(frame)
            gif_image.seek(len(frames))
    except EOFError:
        pass

    # Tạo đường dẫn cho file PNG đầu ra dựa trên cấu trúc của thư mục input
    relative_path = os.path.relpath(gif_file, input_directory)
    output_folder = os.path.join(output_directory, os.path.dirname(relative_path))
    os.makedirs(output_folder, exist_ok=True)
    png_file = os.path.join(output_folder, os.path.basename(gif_file).replace(".gif", ".png"))
    png_file.replace("\\", "-")
    # Lưu frame cuối cùng dưới dạng file PNG
    frames[-1].save(png_file, format="PNG")

    # Đóng file GIF
    gif_image.close()
