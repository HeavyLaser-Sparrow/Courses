from Account import *
from Lock import *

Joe = vault(143, 2000)
Asdf = vault(674, 1000000)
NotPhoney = vault(718, 100)

lockCheck()

remId = int(input("Please enter your id again: "))
changeMoney(remId)
