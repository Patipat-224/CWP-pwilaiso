#!/usr/bin/env python3

original_arr =[2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for i in original_arr :
    if i > 5 : 
        new_set.add(i + 2)

print(f"{original_arr}")
print(f"{new_set}")