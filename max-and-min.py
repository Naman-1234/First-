#The special Thing about this program is that use the concept of none variable which is not present in other languages i have learnt


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else :
        try:
            num=float(num)
        except:
            print('Invalid input')
            continue
    if largest is None:
        largest=num
    if smallest is None:
        smallest=num
    if largest<num:
        largest=num
    if smallest>num:
        smallest=num

print("Maximum is", largest)
print("Minimum is",smallest)
