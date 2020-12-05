data = open("input.txt").read().strip().split('\n')

def decode_seat(seat):
    rowstr = seat[:7].replace('F','0').replace('B','1')
    row = int(rowstr, 2)
    colstr = seat[-3:].replace('R','1').replace('L','0')
    col = int(colstr, 2)
    return (row,col)

max_id = 0
seat_ids = []
for seat in data:
    (row,col) = decode_seat(seat)
    seat_id = row * 8 + col
    seat_ids.append(seat_id)
    if seat_id > max_id: max_id = seat_id
    prev_id = seat_id

seat_ids.sort()
prev_id = 0
for sid in seat_ids:
    if sid != prev_id + 1: print("candidate:", sid-1)
    prev_id = sid
