# def hello(name = 'Jose'):
#     print('Hello')
    
#     def greet():
#         return 'this is inside Greet'
    
#     def welcome():
#         return 'inside welcome'
    
#     if name == 'Jose':
#         return greet
#     else:
#         return welcome

# x = hello('Jai')
# print(x())

# def hello():
#     return 'hello world'


# def other(func):
#     print("Some Other Function")
#     print(func())

# other(hello)

from functools import wraps

def new_decorator(func):
    @wraps(func)
    def wrapper():
        print('Inside another function')
        func()
        print('After Executing func()')
    return wrapper

@new_decorator
def func_needs_decorator():
    print('Please decorate me')

# new_decorator(func_needs_decorator)()
func_needs_decorator()
print(func_needs_decorator.__name__) # Because of Wraps it will show the actual Function name