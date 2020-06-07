import cs50
num = cs50.get_int("Height: ")
while True:
    if num > 8 or num < 1:
        num = cs50.get_int("Height: ")
    else:
        for i in range(1,num+1):
            print(" "*(num-i),end="")
            print("#"*i)
        break
