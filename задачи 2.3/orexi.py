A

right = "Три!"
n = input()
while n != right:
    n = input("Режим ожидания..." + '\n')
print("Ёлочка, гори!")

B 

count = 0
line = input()
while line != "Приехали!":
    if "зайка" in line:
        count += 1
    line = input()
print(count)

C 

n = int(input())
k = int(input())
for i in range(n, k + 1):
    print(i, end=" ")

D 

start = int(input())
end = int(input())
if start <= end:
    for i in range(start, end + 1):
        print(i, end=" ")
else:
    for i in range(start, end - 1, -1):
        print(i, end=" ")

E 

price = float(input())
total = 0
while price != 0:
    if price >= 500:
        total += price * 0.9
    else:
        total += price
    price = float(input())
print(f"{total:.1f}")

F 

a = int(input())
b = int(input())
while b != 0:
    a, b = b, a % b
print(a)

G 

a = int(input())
b = int(input())
A = a
B = b
while b != 0:
    a, b = b, a % b
arbuz = (A * B) // a
print(arbuz)

H 

info = input()
n = int(input())
for a in range(n):
    print(info)

I 

n = int(input())
f = 1
for i in range(1, n + 1):
    f = f * i
print(f)

J

x, y = 0, 0
d = input()
while d != "СТОП":
    steps = int(input())
    if d == "СЕВЕР":
        y += steps
    if d == "ЮГ":
        y -= steps
    if d == "ВОСТОК":
        x += steps
    if d == "ЗАПАД":
        x -= steps
    d = input()
print(y)
print(x)

# d это direction но мне лень его писать

K 

number = input()
sumD = 0
for d in number:
    sumD += int(d)
print(sumD)

L 

n = input()
m = max(n)
print(int(m))

M 

N = int(input())
first = input()
for a in range(N - 1):
    name = input()
    if name < first:
        first = name
print(first)

M

n = int(input())
if n <= 1:
    print("NO")
else:
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            print("NO")
        else:
            print("YES")

N 

n = int(input())
if n <= 1:
    print("NO")
else:
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            print("NO")
        else:
            print("YES")

# он пишет мне 7 YES, НО СЕМЬ ЛУЧШЕ ЧЕМ ОДИН, так намного убедительнее чем всего лишь одно 

O

N = int(input())
count = 0
for a in range(N):
    line = input()
    if 'зайка' in line:
        count = count + 1
print(count)

P 

n = input()
if n == n[::-1]:
    print("YES")
else:
    print("NO")

Q 

n = input()
b = ""
for a in n:
    if int(a) % 2 != 0:
        b = b + a
print(b)

R 

n = int(input())
b = ""
a = 2
while n > 1:
    while n % a == 0:
        if b:
            b += " * " + str(a)
        else:
            b = str(a)
        n //= a
    a = a + 1
print(b)

S 

low = 1
high = 1000
attempts = 0
while attempts < 10:
    guess = (low + high) // 2
    print(guess)
    otvet = input()
    attempts = attempts + 1
    if otvet == "Угадал!":
        print("Число отгадано")
        break
    elif otvet == "Больше":
        low = guess + 1
    elif otvet == "Меньше":
        high = guess - 1

T 

N = int(input())
blocks = [0] * N
for i in range(N):
    blocks[i] = int(input())
hash = 0
invalid_block = -1
for i in range(N):
    block = blocks[i]
    h_n = block % 256
    r_n = (block // 256) % 256 
    m_n = block // (256 ** 2) 
    expected_h_n = (37 * (m_n + r_n + hash)) % 256
    if h_n >= 100 or h_n != expected_h_n:
        invalid_block = i
    hash = h_n
print(invalid_block)

# ИНВАЛИД ЭТО Я 
# тройки в ответе не будет. тройка приняла ислам