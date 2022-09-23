#Cube function

def cube(x):
    return x * x * x

n = int(input(" Enter the number : "))
cube_output = cube(n)
print("The Cube of {0}  = {1}".format(n, cube_output))