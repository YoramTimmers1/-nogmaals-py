
from RobotArm import RobotArm
robotArm = RobotArm("exercise 2")

#EERSTE BLOKJE
for i in range(1,10):
    robotArm.grab()
    robotArm.moveRight()
robotArm.drop()

#TWEEDE BLOKJE
for x in range(1,6):
    robotArm.moveLeft()
robotArm.grab()

for y in range(1,6):
    robotArm.moveRight()
robotArm.drop()

#DERDE BLOKJE
for w in range(1,3):
    robotArm.moveLeft()
robotArm.grab()

for r in range(1,3):
    robotArm.moveRight()
robotArm.drop()


robotArm.wait()