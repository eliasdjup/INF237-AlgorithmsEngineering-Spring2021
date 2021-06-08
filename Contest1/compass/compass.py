
current_angle = int(input())
final_angle = int(input())

def minimumDistance(current_angle, final_angle):
    f = current_angle - final_angle
    if f < 0:
        f += 360
    
    if f >= 180:
        return 360 - f
    return -f
    
print(minimumDistance(current_angle, final_angle))

'''
315
45
- > 90

315 - 45 = 270
if x >= 180: return 360 - x


180
270
- > 90
180 - 270 = -90 = 270
if x >= 180: return 360 - x


45
270
- > -135
45 - 270 = -225 = 135
if >= 180: return 360 - x
else return x

'''