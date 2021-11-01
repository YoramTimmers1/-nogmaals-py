from RobotArm import RobotArm
robotArm = RobotArm("exercise 4")

for i in range(1,4,):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
    
robotArm.moveRight()
for x in range(1,4):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    


robotArm.wait()