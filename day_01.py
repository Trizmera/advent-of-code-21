
with open('inputs/day_one.txt', 'r') as readings:
    depths = [int(number.strip()) for number in readings.readlines()]

increased = sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-1]])

# Answer One
print("Number of times the depth increases:", increased)

increased = sum([1 for i in range(3, len(depths)) if depths[i] > depths[i-3]])