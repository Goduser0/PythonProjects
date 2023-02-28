def now1():
    print('2021')


f = now1
a = f.__name__
print(a)
print()


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')
    print()


now()
