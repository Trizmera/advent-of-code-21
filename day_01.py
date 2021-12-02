
with open('inputs/day_one.txt', 'r') as f:
    sea_floor_depth = [int(number.strip()) for number in f.readlines()]

depth_increased = sum([1 for i in range(1, len(sea_floor_depth)) if sea_floor_depth[i] > sea_floor_depth[i-1]])

print("Number of times the depth increases:", depth_increased)