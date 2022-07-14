from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

#
# tello = Tello()
#
# tello.connect()
# tello.takeoff()
#
# tello.move_left(100)
# tello.rotate_counter_clockwise(90)
# tello.move_forward(100)
#
# tello.land()
#
#
