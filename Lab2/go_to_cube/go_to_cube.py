import cozmo
import findCube
from cozmo.util import degrees, distance_mm, speed_mmps

#def findCube(robot):
#    return 1.0

def cozmo_program(robot: cozmo.robot.Robot):
    robot.set_head_angle(degrees(-10)).wait_for_completed()
    speed = 30
    while True:
        cube_position = findCube.findCube(robot)
        if (cube_position < 0.0):
            #robot.turn_in_place(degrees(5)).wait_for_completed()
            robot.drive_wheels(speed, -speed)
        else:
            cube_position = cube_position - 0.5
            cube_angle = 20.0 * cube_position
            robot.drive_wheels(speed + cube_angle, speed - cube_angle)

cozmo.run_program(cozmo_program)