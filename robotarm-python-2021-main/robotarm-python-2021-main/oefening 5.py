from RobotArm import RobotArm
robotArm = RobotArm("exercise 6")
for i in range(1,8):
    robotArm.moveRight()
for x in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()





robotArm.wait()