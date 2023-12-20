import re
with open("test_input_2023-12-19") as f:
	lines = f.readlines()

for y in lines:
	if not y[0].isalpha():
		print(y)
		x = sum(map(int, re.findall(r"x=(\d+)", y)))
		m = sum(map(int, re.findall(r"m=(\d+)", y)))
		a = sum(map(int, re.findall(r"a=(\d+)", y)))
		s = sum(map(int, re.findall(r"s=(\d+)", y)))
		print(x, m, a, s)

def A():
	print(x + m + a + s)

def R():
	print("rejected")

rules = list()
for x in lines:
	if x[0].isalpha():
		print(x)
		rules.append(x.replace("{", "(x,m,a,s):"))
		print(rules)
