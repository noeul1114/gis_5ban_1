
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

print('\n\n-------------------\n1번째 실습\n-------------------\n\n')


def check_integer(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            raise ValueError('Input must be positive value')
    return decorated


@check_integer
def rect_area(width, height):
    return width * height


@check_integer
def tri_area(width, height):
    return width * height / 2


r_area = rect_area(10, 10)

print(r_area)

t_area = tri_area(10, 10)

print(t_area)


print('\n\n-------------------\n2번째 실습\n-------------------\n\n')


def check_integer(func):
    def decorated(user, width, height):
        if width >= 0 and height >= 0:
            return func(user, width, height)
        else:
            raise ValueError('Input must be positive value')
    return decorated


def login_required(func):
    def decorated(user, width, height):
        if user.is_authenticated:
            return func(user, width, height)
        else:
            raise PermissionError('Login required')
    return decorated


@login_required
@check_integer
def rect_area(user, width, height):
    return width * height


@login_required
@check_integer
def tri_area(user, width, height):
    return width * height / 2


class User:
    def __init__(self, auth):
        self.is_authenticated = auth


user = User(auth=True)

r_area = rect_area(user, 10, 10)
print(r_area)

t_area = tri_area(user, 10, 10)
print(t_area)


print('\n\n-------------------\n3번째 실습\n-------------------\n\n')


def check_integer(func):
    def decorated(**kwargs):
        if kwargs['width'] >= 0 and kwargs['height'] >= 0:
            return func(**kwargs)
        else:
            raise ValueError('Input must be positive value')
    return decorated


def login_required(func):
    def decorated(**kwargs):
        if kwargs['user'].is_authenticated:
            return func(**kwargs)
        else:
            raise PermissionError('Login required')
    return decorated


@login_required
@check_integer
def rect_area(**kwargs):
    return kwargs['width'] * kwargs['height']


@login_required
@check_integer
def tri_area(**kwargs):
    return kwargs['width'] * kwargs['height'] / 2


class User:
    def __init__(self, auth):
        self.is_authenticated = auth


user = User(auth=True)

r_area = rect_area(user=user, width=10, height=10)
print(r_area)

t_area = tri_area(user=user, width=10, height=10)
print(t_area)


