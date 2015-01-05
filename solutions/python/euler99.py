import sys
import math

result = []
for i, line in enumerate(open(sys.argv[1]).readlines(), 1):
    line = map(int, line.strip().split(","))
    result.append((math.log(line[0])*line[1], i))
print max(result)[1]
