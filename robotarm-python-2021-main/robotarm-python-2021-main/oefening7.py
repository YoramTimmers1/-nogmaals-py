from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 3 #voor snelheid
for y in range(5):
    robotArm.moveRight()
    for x in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
robotArm.wait()
