x1_coord = int(input(" Enter coordinates of current location (x) from 1 to 8: "))
y1_coord = int(input(" Enter coordinates of current location (y) from 1 to 8: "))
x2_coord = int(input(" Enter coordinates of target location (x) from 1 to 8: "))
y2_coord = int(input(" Enter coordinates of target location (y) from 1 to 8: "))
x1 = x1_coord
y1 = y1_coord
x2 = x1_coord
y2 = y1_coord
if x1_coord == x2_coord or y1_coord == y2_coord:
    a = 1
else:
    a = 2
for i in range(8):
    x1 = x1 + 1
    y1 = y1 + 1
    x2 = x2 - 1
    y2 = y2 - 1
    if (x1 == x2_coord or x2 == x2_coord) and (y1 == y2_coord or y2 == y2_coord):
        b = 1
        break
    if x1 != x2_coord and x2 != x2_coord:
        b = 0
if a == 1 or b ==1:
    input(" YES")
else:
    input(" NO")
