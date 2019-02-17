# *args

def new_function(a,b,c):
    return a,b,c

new_function("Hello", 10, "Hi")

def args_function(*args):
    return args

args_function("Hello", 10)

def cal_per(a,b):
    return sum((a,b)) * 0.4

cal_per(70,30)

def args_cal_per(*args):
    return sum((args)) * 0.4

args_cal_per(70,30,40)

def args_with_othername_cal_per(*tom):
    return sum((tom)) * 0.4

args_with_othername_cal_per(70,30,40)

# kwargs

def my_function(**asdf):
    print(asdf)
    if "flower" in asdf:
        print("We have {} for you !".format(asdf["flower"]))
    else:
        print("There is no flower for you !")
        
my_function(color = "Orange", flower = "Rose")

## args and kwargs together

def function_with_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like to have {} {} ".format(args[0],kwargs["fruit"]))

function_with_args_and_kwargs(1,2,3, color = "Green", fruit = "Apple")
