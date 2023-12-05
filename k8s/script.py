import os


image_folder = 'images/lab14'
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

print("here")
for file in os.listdir(image_folder):
    if any(file.endswith(ext) for ext in image_extensions):
        markdown = f"![{file}]({image_folder}/{file})"
        print(markdown)
