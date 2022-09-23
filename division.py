nums = []
finished = False

print("Input any amount of positive integers (End with 0). Enter after each number. This will return the division of each number after the last.")

while (not finished):
    num = input()
    if (num.isnumeric()):
        num = int(num)
    else:
        print("Not a valid input. Try again.")
        continue
    if (num == 0):
        finished = True
    elif (num < 0):
        print("Not a valid input. Try again.")
    else:
        nums.append(num)

def division(ints):
    div = 1
    for i in ints:
        div /= i
    return div

d = division(nums)
print("The division of the numbers is {}".format(d))

#testing!