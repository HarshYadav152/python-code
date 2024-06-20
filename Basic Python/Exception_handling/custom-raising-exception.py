class CustomError(Exception):
    pass
def check_value(value):
    if value < 0:
        raise CustomError("Negative value is not allowed.")
    
try:
    check_value(-1)
except CustomError as e:
    print(e)