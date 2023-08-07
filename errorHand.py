#Error Handling

filename="John.txt"

try:
    with open(filename, "r") as f_obj:
        content=f_obj.read()

except FileNotFoundError:
    msg="Sorry, the file" + filename +  "doesn't exist"
    print(msg)



#formating system

num=1.458349074537654
print("%.5f" %num)

# dot format

num=1.458349074537654

sliced="{:.2f}".format(num)
print(sliced)

num=1.458349074537654
print("(:.3f)".format(num))