A

print("Как Вас зовут?")
name = input()
print(f'Здравствуйте, {name}!')
print('Как дела?')
answer = input()
if (answer == 'хорошо'):
    print('Я за вас рада!')
elif (answer == 'плохо'):
    print('Всё наладится!')


B

speed1 = int(input())
speed2 = int(input())
length = 43872
if (length / speed1) < (length / speed2):
    print('Петя')
elif (length / speed1) > (length / speed2):
    print('Вася')

C

speed1 = int(input())
speed2 = int(input())
speed3 = int(input())
if (speed1 > speed3) and (speed1 > speed2):
    print('Петя')
elif (speed3 > speed1) and (speed3 > speed2):
    print('Толя')
elif (speed2 > speed1) and (speed2 > speed3):
    print('Вася')

D

speed1 = int(input())
speed2 = int(input())
speed3 = int(input())
length = 43872
Petya_time = length / speed1
Vasya_time = length / speed2
Tolya_time = length / speed3
if Petya_time < Vasya_time and Petya_time < Tolya_time:
    first = 'Петя'
    if Vasya_time < Tolya_time:
        second, third = 'Вася', 'Толя'
    else:
        second, third = 'Толя', 'Вася'
elif Vasya_time < Petya_time and Vasya_time < Tolya_time:
    first = 'Вася'
    if Petya_time < Tolya_time:
        second, third = 'Петя', 'Толя'
    else:
        second, third = 'Толя', 'Петя'
else:
    first = 'Толя'
    if Petya_time < Vasya_time:
        second, third = 'Петя', 'Вася'
    else:
        second, third = 'Вася', 'Петя'
print(f'1. {first}')
print(f'2. {second}')
print(f'3. {third}')


E

ap1, ap2 = int(7 - 3 + 2), int(6 + 5 - 2)
N = int(input())
M = int(input())
if (ap1 + N) > (ap2 + M):
    print('Петя')
elif (ap2 + M) > (ap1 + N):
    print('Вася')


F

year = int(input())
if (year % 4 == 0) and (year % 100 != 0):
    print('YES')
else:
    print('NO')

    
G

number = input()
if number[0] == number[3] and number[1] == number[2]:
    print('YES')
else:
    print('NO')


H

text = input()
if 'зайка' in text:
    print('YES')
else:
    print('NO')


I

player1 = input()
player2 = input()
player3 = input()
PLAYER = min(player1, player2, player3)
print(PLAYER)


J

number = int(input())
a = number // 100
b = (number // 10) % 10
c = number % 10
sum = b + c
SUM = a + b
if sum >= SUM:
    result = str(sum) + str(SUM)
else:
    result = str(SUM) + str(sum)
print(result)


K

number = input()
a = int(number[0])
b = int(number[1])
c = int(number[2])
min_digit = min(a, b, c)
max_digit = max(a, b, c)
middle_digit = a + b + c - min_digit - max_digit
if min_digit + max_digit == middle_digit * 2:
    print('YES')
else:
    print('NO')


L

a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')


M

elf = input()
dwarf = input()
human = input()
if elf[0] == dwarf[0] == human[0]:
    print(elf[0])
elif elf[1] == dwarf[1] == human[1]:
    print(elf[1])
else:
    print('Черти все поломали')


N

number = input()
a = number[0]
b = number[1]
c = number[2]
numberS = [ 
    int(a + b), int(a + c), 
    int(b + a), int(b + c), 
    int(c + a), int(c + b) 
]
min_number = min(numberS)
max_number = max(numberS)
print(min_number, max_number)

#надо исправить чтоб минимальный ответ был от 10

number = input()
a = number[0]
b = number[1]
c = number[2]
numberS = [ 
    int(a + b) if a != '0' else 10, 
    int(a + c) if a != '0' else 10,
    int(b + a) if b != '0' else 10, 
    int(b + c) if b != '0' else 10, 
    int(c + a) if c != '0' else 10, 
    int(c + b) if c != '0' else 10
]
min_number = min(numberS)
max_number = max(numberS)
print(min_number, max_number)

#исправила. только все равно что-то не так это невыносимо.


O

number1 = input()
number2 = input()
MAX = max(number1 + number2)
MIN = min(number1 + number2)
SUM = int(number1[0]) + int(number1[1]) + int(number2[0]) + int(number2[1])
middle = (SUM - int(MAX) - int(MIN)) % 10 
print(MAX, middle, MIN, sep='')


P 

petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())
distance = 43872
petya_time = distance / petya_speed
vasya_time = distance / vasya_speed
tolya_time = distance / tolya_speed
if petya_time < vasya_time and petya_time < tolya_time:
    first = 'Петя'
    if vasya_time < tolya_time:
        second = 'Вася'
        third = 'Толя'
    else:
        second = 'Толя'
        third = 'Вася'
elif vasya_time < petya_time and vasya_time < tolya_time:
    first = 'Вася'
    if petya_time < tolya_time:
        second = 'Петя'
        third = 'Толя'
    else:
        second = 'Толя'
        third = 'Петя'
else:
    first = 'Толя'
    if petya_time < vasya_time:
        second = 'Петя'
        third = 'Вася'
    else:
        second = 'Вася'
        third = 'Петя'
print(f'{first:^20}')
print(f'{second:<20}')
print(f'{third:>20}')
print(' II      I      III ')


Q

a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b == 0:
    print('No solution')
elif a == 0:
    x = -c / b
    print(f'{x:.2f}')
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print('No solution')
    elif D == 0:
        x = -b / (2 * a)
        print(f'{x:.2f}')
    else:
        x1 = (-b - D**0.5) / (2 * a)
        x2 = (-b + D**0.5) / (2 * a)
        print(f'{min(x1, x2):.2f} {max(x1, x2):.2f}')


R 

a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a + b <= c:
    print('Колобок повесился')
else:
    if a**2 + b**2 == c**2:
        print('100%')
    elif a**2 + b**2 > c**2:
        print('крайне мала')
    else:
        print('велика')


S 

x = float(input())
y = float(input())
r_island = 8
r_sand = 5
x_sand, y_sand = 2, -2
island_center = (x**2 + y**2)**0.5
sand_center = ((x - x_sand)**2 + (y - y_sand)**2)**0.5
if island_center > r_island:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif sand_center <= r_sand:
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')

#я не понимаю что не так :(


T 

line1 = input()
line2 = input()
line3 = input()
smallest_line = None
if 'зайка' in line1:
    smallest_line = line1
if 'зайка' in line2:
    if smallest_line is None or line2 < smallest_line:
        smallest_line = line2
if 'зайка' in line3:
    if smallest_line is None or line3 < smallest_line:
        smallest_line = line3
if smallest_line is not None:
    print(f'{smallest_line} {len(smallest_line)}')
else:
    print('Строк с зайкой нет.')