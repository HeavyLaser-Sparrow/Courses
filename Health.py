print("What is the original health")

import random

health = int(input()) 

print("What is the difficulty")

difficulty = int(input())

potionHealth = int(random.randint(25,50) / difficulty)   

health = health + potionHealth

print(health)