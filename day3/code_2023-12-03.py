import re
with open("test_input_2023-12-03") as f:
	lines = f.readlines()

special_characters = "!@#$%^&*()-+?_=,<>/" #https://stackoverflow.com/a/63173907
j = 0
for k in range(len(lines)):
	locspecial = list()
	m = list()
	x = lines[k]
	print(x)
	print(list(map(list, enumerate(x))))
	m.append([(i, c) for i, c in enumerate(x) if c.isdigit()])
	print(m)  # https://stackoverflow.com/questions/4510709/find-the-index-of-the-first-digit-in-a-string
	for c in x:
		if c.isdigit():
			start = x.find(c)
		if c in special_characters:
			locspecial.append(x.find(c))
			print(locspecial)
		if len(locspecial) == 1:
			print(x[locspecial[0] - 1].isnumeric())
	# for c in y:
	# 	if c in special_characters:
	# 		print(j+1, y.find(c))
	# 		print(x[x.find(c) - 1].isnumeric())
	# 		numbers = re.findall(r'\d+', x)
	# 		result = list(map(int, numbers))
	# 		print(result)
	# for c in z:
	# 	if c in special_characters:
	# 		print(j+2, z.find(c))
	# 		print(y[y.find(c) - 1].isnumeric())
	# 		numbers = re.findall(r'\d+', y)
	# 		result = list(map(int, numbers))
	# 		print(result)
	j = j + 1

