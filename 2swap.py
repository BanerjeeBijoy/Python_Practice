org_string = "12121212 Hello Bijoy."

single_char = [char for char in org_string]
print(single_char)

even_char = single_char[1: :2]
print(even_char)
odd_char = single_char[0: : 2]
print(odd_char)


make_char = []
for i in range(len(even_char)):
    make_char.append(even_char[i])
    make_char.append(odd_char[i])
print(make_char)

rvc2_string = "".join(make_char)
print(rvc2_string)