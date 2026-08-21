def NameError():
    print(a) #causes NameError due to undefined variable 'a'

def TypeError():
    print(1+'1') #causes TypeError due to unsupported operand types

def KeyError():
    d = {}
    print(d['key']) #causes KeyError due to missing key in dictionary

def FileNotFoundError():
    with open('non_existent_file.txt', 'r') as f:
        content = f.read() #causes FileNotFoundError due to missing file        

def IndexError():
    lst = [1, 2, 3]
    print(lst[5]) #causes IndexError due to index out of range

def ValueError():
    int('string') #causes ValueError due to invalid literal for int() with base 10

def calculationsExamples():
    print(5/2); type(5/2)
    print(5//2); type(5//2)
    print(5%2); type(5%2)
    try:
        "5" + "5" #causes TypeError due to unsupported operand types
    except TypeError:
        print("TypeError would have occurred here due to unsupported operand types for string concatenation with numbers.")
        print("Instead use int() or numeric characters.")
        print(5+5)
    print(0.1 + 0.2) #causes floating point precision issue
    print(0.1 + 0.2 == 0.3) #causes floating point precision issue
    print("ATGC".upper()) #causes no error, but demonstrates string method usage
    print("ATGC".lower()) #causes no error, but demonstrates string method usage    
    print("ATGC".count("A")) #causes no error, but demonstrates string method usage#
    print("ATGC"[::-1]) #causes no error, but demonstrates string slicing and reversing
    print("ATGC"[1:3]) #causes no error, but demonstrates string slicing
    print("ATGC"[:-1])
    
calculationsExamples()