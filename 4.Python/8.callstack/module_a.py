def function_a1():
    print("module_a 의 function_a1 호출")
    function_a2()

def function_a2():
    print("module_a 의 function_a2 호출")
    function_a3()

def function_a3():
    print("module_a 의 function_a3 호출")
    test_1234()

def test_1234():
    print("module_a의 text_1234 호출")

def deep_call_1():
    print("module_a의 deep_call_1 호출")
    raise RuntimeError("의도적으로 발생한 나의 예외;/")

def call_test():
    print("나(module_a) 실행됨")


if __name__ == '_main_':
    call_test()

    # 파이썬이 나를 직접 호출했을 때 실행 되는 것 !! = 메인 함수