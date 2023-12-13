import re
with open("input_2023-12-02") as f:
	lines = f.readlines()

num = 0

for x in lines:
	red = list()
	green = list()
	blue = list()
	game = x.split(":")[0]
	x = x.split(":")[-1]
	for i in x.split(";"):
		red.append(sum(map(int, re.findall(r"(\d+) red", i))))
		green.append(sum(map(int, re.findall(r"(\d+) green", i))))
		blue.append(sum(map(int, re.findall(r"(\d+) blue", i))))
	redmax = max(red)
	greenmax = max(green)
	bluemax = max(blue)
	num = num + redmax * greenmax * bluemax
print(num)

