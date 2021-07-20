
def decorator(func):
    def decorated():
        print('함수 시작!')
        func()
        print('함수 끝!')
    return decorated


@decorator
def hello_world():
    print('Hello World!')

hello_world()
