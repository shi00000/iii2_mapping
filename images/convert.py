import os
from PIL import Image

# 画像を再帰的に処理するルートディレクトリ
root_dir = "images"
# 縮小倍率（10%）
scale = 0.1

# 処理対象の拡張子
extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith(extensions):
            file_path = os.path.join(subdir, file)
            try:
                with Image.open(file_path) as img:
                    new_size = (int(img.width * scale), int(img.height * scale))
                    resized_img = img.resize(new_size, Image.ANTIALIAS)
                    resized_img.save(file_path)  # 上書き保存
                    print(f"Resized: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
