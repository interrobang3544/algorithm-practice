coordinate_x = int(input())
coordinate_y = int(input())
if coordinate_x > 0 and coordinate_y > 0:
    print('1')
elif coordinate_x < 0 and coordinate_y > 0:
    print('2')
elif coordinate_x < 0 and coordinate_y < 0:
    print('3')
else:
    print('4')