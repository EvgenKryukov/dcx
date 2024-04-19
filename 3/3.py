# Заданные значения для x и y
x = 3
y = 2

if x + y < x - 3*y:
    min_val = x + y
else:
    min_val = x - 3*y

if x + 6*y > x - y:
    max_val = x + 6*y
else:
    max_val = x - y


u = min_val / max_val


print(f"x = {x}, y = {y}")
print(f"min(x+y, x-3y) = {min_val}")
print(f"max(x+6y, x-y) = {max_val}")
print(f"u = {u}")
