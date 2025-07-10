# 업로드한 파일 목록 보이기 (main라우트에서)
# 파일명 옆에 삭제 버튼 추가하기

# 삭제 기능 탑재한다

from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_FILE_EXT'] = {'png', 'jpg', 'jpeg', 'gif', 'gif'} 
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    if '.' not in filename:
        return False

    ext = filename.rsplit('.',1)[1].lower()

    if ext in app.config['ALLOWED_FILE_EXT']:
        return True
    else: 
        False


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    print(files)
    return render_template('upload.html', files = files)


# requested_files = []

@app.route('/upload', methods= ['POST'])
def upload_file():
    print(request.form) #파일명만 받기

    file = request.files['file'] #파일 내용을 FileStorage라는 객체로 받기

    if file.filename == '': 
        return '파일이 전송되지 않았습니다'
    print(file)

    def get_file_size(file):
        pos = file.stream.tell()
        file.stream.seek( 0, os.SEEK_END)
        size = file.strea.tell()
        file.stream.seek(pos)
        return size

    # 파일 저장하기 : 현재 폴더의 uploads 안에 받은 파일명으로 저장하기

    # filepath=os.path.join('./', UPLOAD_FOLDER, file.filename) 
    # file.save(filepath)

    #비즈니스 로직 : 내가 정한 프로세싱 룰들을 구현하자
    #1. 사진 파일만 업로드 가능 - 확장자(jpg.jpeg.png.gif)

    max_size = 1 * 1024 * 1024
    file_size = get_file_size(file)
    print('파일 용량:', file_size)
    if file_size > max_size :
        return '파일 용량이 너무 큽니다. 1MB 보다 작은 파일을 올려주세요.'



    if allowed_file(file.filename):
        filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return redirect(url_for('index'))
    else:
        return '허용되지 않는 파일입니다.'
    

@app.route('/delete/<filename>')
def delete_file(filename):
    filepath = os.path.join('./', 'uploads', filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return redirect(url_for('index'))
    else:
        return '해당 파일은 존재하지 않습니다.'

@app.errorhandler(413)
def too_large(e):
    size_mb = app.config['MAX_CONTENT_LENGTH'] / (1024 * 1024)
    return f"업로드한 파일이 너무 큽니다. 최대 {size_mb}MB 까지만 허용합니다."

if __name__ == '__main__':
    app.run(debug=True)