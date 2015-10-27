# -*- coding: utf-8 -*-

counter = 0
while counter < 10:
    counter += 1
    print(counter)
print("--------------------------")

counter = 0
while counter < 10:
    if counter % 2 == 0:
        print(counter)
    counter += 1
print("--------------------------")

for num in range(100):
    if num % 10 == 0:
        print(num)
print("--------------------------")

for num in range(10):
    print(num)
    if(num == 5):
        print("break")
        break
