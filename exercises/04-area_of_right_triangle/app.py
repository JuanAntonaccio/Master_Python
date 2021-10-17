#Complete the function to return the area of the triangle.
b = int(input("Size of B"))
h = int(input("Size of H"))

def area_of_triangle(arg1, arg2):
    #your code here, please remove the "None"
    resultado=arg1*arg2/2 
    return resultado

# Testing your function
print(area_of_triangle(b, h))