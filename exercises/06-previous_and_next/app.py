#Complete the function to return the previous and next number of a given numner.".
def previous_next(num):
  a=num-1
  b=num+1
  return a,b


#Invoke the function with any interger at its argument. 
number=int(input("ingrese un numero: "))
print(previous_next(number))