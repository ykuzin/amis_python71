children_count = int(input(" Enter count of children: "))
children_height = [int(input(" Enter "+str(element+1)+" child height (up to 200): ")) for element in range(children_count-1)]
children_height.sort()
children_height = children_height[::-1]
petya_height = int(input(" Enter Petya's height (up yo 200): "))
i = 0
position = 0
while i <= children_count:
    if petya_height > children_height[i]:
        i = i + 1
        position += 1
        break
    i += 1
    position += 1
print(position)
input()
