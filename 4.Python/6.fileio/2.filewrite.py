file_path = "test.txt"

# 파일을 읽을 때의 모드
# r - read, w - write(새로 쓰기), a - append(이어서 쓰기) 
with open(file_path, "w", encoding='utf-8') as file:
    file.write("Hello\n")

    file.write("It's, me")
