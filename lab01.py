# функція для збільшення числа на 1
def inc(n):
    result = n + 1
    return result

def inc_object(num):
    num['n'] = num['n'] + 1

a = 10
b = inc(a)
print("a =", a, "b =", b)

obj = {'n': 5}
inc_object(obj)
print("obj =", obj)

print()

data = [True, 'hello', 5, 12, -200, False, False, 'word', 3.14, 'python', 42, 'test', True, 0, 'example', -15, 'code', False, 100, 'string']

types_count = {}
types_count['int'] = 0
types_count['str'] = 0
types_count['bool'] = 0
types_count['float'] = 0

for i in range(len(data)):
    element = data[i]
    element_type = type(element).__name__
    if element_type == 'int':
        types_count['int'] = types_count['int'] + 1
    if element_type == 'str':
        types_count['str'] = types_count['str'] + 1
    if element_type == 'bool':
        types_count['bool'] = types_count['bool'] + 1
    if element_type == 'float':
        types_count['float'] = types_count['float'] + 1

print(types_count)

print()

empty_dict = {}

for i in data:
    t = type(i).__name__
    if t in empty_dict:
        empty_dict[t] = empty_dict[t] + 1
    else:
        empty_dict[t] = 1

print(empty_dict)
