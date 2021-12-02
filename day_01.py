
with open('inputs/day_01.txt', 'r') as f:
    depth = [int(number.strip()) for number in f.readlines()]

increased = sum([1 for i in range(1, len(depth)) if depth[i] > depth[i-1]])

print("Number of times the depth increases:", increased)

increased = sum([1 for i in range(3, len(depth)) if depth[i] > depth[i-3]])


print("Number of times the sliding window:", increased)