total = 0 

for num in range(1, 51):
    if num % 3 == 0:
        continue 

    print(num, end=" ")
    total += num 

print ()
print("Sum:", total)