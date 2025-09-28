name = 'Олександр'
birth_year = 2005

def greeting(name):
    print('Привіт,', name)

greeting(name)

print()

def range_func(start, end):
    result = []
    for i in range(start, end + 1):
        result.append(i)
    return result

def range_odd(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 2 == 1:
            result.append(i)
    return result

numbers = range_func(15, 30)
print('Діапазон чисел:', numbers)

odd_numbers = range_odd(15, 30)
print('Непарні числа:', odd_numbers)

print()

def average(a, b):
    result = (a + b) / 2
    return result

def square(x):
    result = x * x
    return result

def cube(x):
    result = x * x * x
    return result

def calculate():
    results = []
    for i in range(0, 10):
        sq = square(i)
        cb = cube(i)
        avg = average(sq, cb)
        results.append(avg)
    return results

calc_results = calculate()
print('Результати обчислень:', calc_results)

print()

def fn():
    obj1 = {'name': 'Іван'}
    obj2 = {'name': 'Петро'}
    
    obj1['name'] = 'Микола'
    obj2['name'] = 'Сергій'
    
    print('obj1:', obj1)
    print('obj2:', obj2)

fn()

def create_user(name, city):
    user = {}
    user['name'] = name
    user['city'] = city
    return user

user = create_user('Marcus Aurelius', 'Roma')
print('Користувач:', user)

print()

phone_book = [
    {'name': 'Marcus Aurelius', 'phone': '+380445554433'},
    {'name': 'Іван Петренко', 'phone': '+380501234567'},
    {'name': 'Марія Іваненко', 'phone': '+380679876543'}
]

def find_phone_by_name(name):
    for i in range(len(phone_book)):
        person = phone_book[i]
        if person['name'] == name:
            return person['phone']
    return None

phone = find_phone_by_name('Іван Петренко')
print('Телефон Івана:', phone)

print()

phone_hash = {
    'Marcus Aurelius': '+380445554433',
    'Іван Петренко': '+380501234567',
    'Марія Іваненко': '+380679876543'
}

def find_phone_by_name_hash(name):
    if name in phone_hash:
        return phone_hash[name]
    else:
        return None

phone2 = find_phone_by_name_hash('Марія Іваненко')
print('Телефон Марії:', phone2)
