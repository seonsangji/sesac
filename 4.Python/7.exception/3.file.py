try:
    with open("hello.txt","r") as file:
        contents = file.read()

    print('파일내용:', contents)
except FileNotFoundError:
    print("어머! 파일이 존재하지 않습니다")
except IOError:
    print("파일이 안 읽혀염!")
except:
    print("알 수 가 없습니당")