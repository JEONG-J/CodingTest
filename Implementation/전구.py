import sys

def solve(light, save):
    if save[0] == 1:
        light[save[1] - 1] = save[2]
    elif save[0] == 2:
        for x in range(save[1] - 1, save[2]):
            if light[x] == 0:
                light[x] = 1
            else:
                light[x] = 0
    elif save[0] == 3:
        for x in range(save[1] - 1, save[2]):
            light[x] = 0
    elif save[0] == 4:
        for x in range(save[1] - 1, save[2]):
            light[x] = 1

    return light

light_num, input_num = map(int, sys.stdin.readline().split())
lights = list(map(int, sys.stdin.readline().split()))
for _ in range(input_num):
    save_operation = list(map(int, sys.stdin.readline().split()))
    lights = solve(lights, save_operation)

for light in lights:
    print(light, end=" ")