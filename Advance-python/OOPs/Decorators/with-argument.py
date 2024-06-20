# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello, {name}")

# # Usage
# greet("Alice")


def decorator(times):
    def first(function):
        def second(*args):
            for i in range(times):
                result = function(*args)
            return result
        return second
    return first

@decorator(10)
def hello(name):
    print(f"Hello {name}")

hello("Harsh Yadav")
