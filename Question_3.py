data = input("enter customer heights : ")

def inchToCent(value):
    return value * 2.54

height = data.split()

new_list = []

for x in height:
    value = int(x)
    new_list.append(inchToCent(value))

print("output:", new_list)