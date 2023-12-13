import re
with open("input_2023-12-02") as f:
	lines = f.readlines()

colors = ["red", "green", "blue"]
bag = [12, 13, 14]
game2prev = 0

for x in lines:
	game = x.split(":")[0]
	x = x.split(":")[-1]
	ncall = len(x.split(";"))
	ncall2 = 0
	for i in x.split(";"):
		red = sum(map(int, re.findall(r"(\d+) red", i)))
		green = sum(map(int, re.findall(r"(\d+) green", i)))
		blue = sum(map(int, re.findall(r"(\d+) blue", i)))
		if red <= bag[0] and green <= bag[1] and blue <= bag[2]:
			ncall2 = ncall2 + 1
	if ncall == ncall2:
		game2 = game2prev + sum(map(int, re.findall(r"Game (\d\d)", game)))
		if game2 == game2prev:
			game2 = game2prev + sum(map(int, re.findall(r"Game (\d)", game)))
		game2prev = game2
print(game2)

