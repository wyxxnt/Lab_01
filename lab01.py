def inc(n):
    n = n + 1
    return n

def inc_object(num):
    num['n'] += 1

a = 5
b = inc(a)
print("a:", a)
print("b:", b)

obj = {'n': 5}
inc_object(obj)
print("obj:", obj)

my_list = [True, 'test', 7, 'hello', False, 23, 'world', True, 8, False, 'python', 15, True, 'code', 42]

count_dict = {'int': 0, 'str': 0, 'bool': 0}

for x in my_list:
    if type(x) == int:
        count_dict['int'] += 1
    elif type(x) == str:
        count_dict['str'] += 1
    elif type(x) == bool:
        count_dict['bool'] += 1

print(count_dict)

new_dict = {}
for item in my_list:
    item_type = str(type(item)).split("'")[1]
    if item_type not in new_dict:
        new_dict[item_type] = 0
    new_dict[item_type] += 1

print(new_dict)
