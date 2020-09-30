

a = [1, 1, 2, 3, 5]

num = int(raw_input("Choose a number: "))

new_list = []

for i in a:
	if i < num:
		new_list.append(i)

print (new_list)


