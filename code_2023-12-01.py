import re
import time
with open("input_2023-12-01") as f:
	lines = f.readlines()

summation = 0
for x in lines:
	num1 = re.search(r'\d', x).group()
	num2 = re.findall(r'\d', x)[-1]
	num3 = int(num1)*10 + int(num2)
	summation = summation + num3
print(summation)