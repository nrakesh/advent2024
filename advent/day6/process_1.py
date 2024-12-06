import sys

from advent import common as util
cycle_ctr = 0

def traverse(dir, pos, visit_pos_dir, visit_pos,new_hurdle):
    global field,cycle_ctr,visit_ctr
    next_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(field) or next_pos[1] >= len(field[0]):
        return
    pos_dir = (next_pos[0], next_pos[1], dir[0], dir[1])
    if pos_dir in visit_pos_dir:
        print("cycle found at ", pos)
        cycle_ctr += 1
        return
    # can i naviagate to the next position
    next_value = field[next_pos[0]][next_pos[1]]
    if next_value != '#' and new_hurdle != next_pos:
        #yes i can
        visit_pos_dir.add(pos_dir)
        if next_pos not in visit_pos:
            visit_pos.add(next_pos)
        traverse(dir, next_pos, visit_pos_dir,visit_pos,new_hurdle)
    else:
        # figure out the direction
        if dir == (-1, 0): #Up -> Turn Right
            dir = (0,1)
        elif dir == (0, 1): #Right --> Turn Down
            dir = (1,0)
        elif dir == (1, 0): #Down --> Turn Left
            dir = (0,-1)
        elif dir == (0, -1): # Left ---> Trun up
            dir = (-1,0)
        visit_pos_dir.add(pos_dir)
        traverse( dir, pos, visit_pos_dir,visit_pos,new_hurdle)

f = "test.txt"
f1 = "2024-6-input.txt"

field = util.read_input_as_char_array(f1)
# loop over s
sum = 0
# find the ^
r = 0
c = 0
for row_index, row in enumerate(field):
    for col_index, element in enumerate(row):
        if element == '^':
            r = row_index
            c = col_index
            break


print("^ location=" + str(r) + "," + str(c))

#
#
sys.setrecursionlimit(10000)
#part 1
# visit_pos_dir = set()
# visit_pos_dir.add((r, c,-1,0))
# visit_pos = set()
# visit_pos.add((r, c))
# traverse((-1, 0), (r, c), visit_pos_dir, visit_pos, None)
# print("visit", len(visit_pos))
# print("cycle =", cycle_ctr)
# print("visit", len(visit_pos))

#part 2

for i in range(len(field)):
    for j in range(len(field[i])):
        if (r, c) != (i, j):
            visit_pos_dir = {(r, c,-1,0)}
            visit_pos = {(r,c)}
            traverse((-1, 0), (r, c), visit_pos_dir, visit_pos, (i,j))

print("cycle =", cycle_ctr)

