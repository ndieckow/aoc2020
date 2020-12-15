data = open("input.txt").read().strip().split('\n')

sample = [0,3,6]
input = [16,12,1,0,15,7,11]

start_num = input
last_spoken = {}
last_number = -1
turn = 0
for el in start_num:
    last_spoken[last_number] = turn
    turn += 1
    last_number = el

while True:
    num = turn - last_spoken.get(last_number, turn)
    #print(num)
    last_spoken[last_number] = turn
    # say num
    turn += 1
    last_number = num
    if turn == 2020:
        print("Part 1:", num)
    elif turn == 30000000:
        print("Part 2:", num)
        break
