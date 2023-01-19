first_name = str(input())
last_name = str(input())
Full_name = first_name + last_name
print(Full_name)


def string_alternative(name):
    result = '';
    length = len(name)
    for idx in range(length):
        if not idx % 2:
            result += name[idx]
    return result;


Str = "Good evening"
result = string_alternative(Str)
print(result)
