from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = ['png', 'jpg', 'jpeg', 'gif']
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif', 'gif'} # set : unique list. 리스트와 기능은 동일, 그러나 공통 요소가 있으면 하나로 처리


os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#시작할 때 폴더가 없으면 만들어라!

def allowed_file(filename):
    if '.' not in filename:
        return False

    ext = filename.rsplit('.',1)[1].lower()

    if ext in ALLOWED_FILE_EXT:
        return True
    else: 
        False


@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods= ['POST'])
def upload_file():
    print(request.form) #파일명만 받기

    file = request.files['file'] #파일 내용을 FileStorage라는 객체로 받기

    if file.filename == '': 
        return '파일이 전송되지 않았습니다'
    print(file)


    # 파일 저장하기 : 현재 폴더의 uploads 안에 받은 파일명으로 저장하기

    filepath=os.path.join('./', UPLOAD_FOLDER, file.filename) 
    file.save(filepath)

    #비즈니스 로직 : 내가 정한 프로세싱 룰들을 구현하자
    #1. 사진 파일만 업로드 가능 - 확장자(jpg.jpeg.png.gif)

    if allowed_file(file.filename):
        filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return '파일 업로드에 성공하였습니다.'
    else:
        return '허용되지 않는 파일입니다.'


    return '파일 받았음'

if __name__ == '__main__':
    app.run(debug=True)