import re
import time
from numpy import argsort
with open("input2_2023-12-01") as f:
	lines = f.readlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

summation = 0

for x in lines:
	alist = []
	num=0
	x = x.replace("twone", str(21))
	x = x.replace("oneight", str(18))
	x = x.replace("eightwo", str(82))
	x = x.replace("eighthree", str(83))
	x = x.replace("threeight", str(38))
	x = x.replace("fiveight", str(58))
	x = x.replace("sevenine", str(79))
	x = x.replace("nineight", str(98))
	for i in range(len(numbers)):
		x = x.replace(str(numbers[i]), str(i + 1))
	num1 = re.search(r'\d', x).group()
	num2 = re.findall(r'\d', x)[-1]
	num3 = int(num1)*10 + int(num2)
	summation = summation + num3
print(summation)