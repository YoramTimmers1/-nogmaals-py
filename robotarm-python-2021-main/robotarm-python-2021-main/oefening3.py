from RobotArm import RobotArm
robotArm = RobotArm("exercise 3")

for i in range(1,2):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

for w in range(1,2):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

for q in range(1,2):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

for a in range(1,2):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()



robotArm.wait()