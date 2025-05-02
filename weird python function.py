import random
def say_hello(_2):
    def ret_1():
        try: _2()
        except ZeroDivisionError: print("Don't divide by zero!")
        finally: print("Hi!")
        if random.randint(1,2)==2:
            print("Hello!")
    return ret_1

def print_smiley(_1):
    def ret_2():
        if random.randint(1,2)==2:
            print(":D")
        _1()
    return ret_2

@say_hello
@print_smiley
def cool_function():
    a=10/random.randint(0,1)
    
cool_function()