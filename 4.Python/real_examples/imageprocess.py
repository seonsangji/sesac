#pip install pillow

from PIL import Image

# 이미지 열기
image = Image.open("cats.jpg")


# 크기 줄이기
resized_image = image.resize((400,300))

resized_image.save("small_cats.jpg")
