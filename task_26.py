#!/usr/bin/python3

from pyrob.api import *

#Fill in the cels.

@task(delay=0.02)
def task_2_4():
    def startPosition():
        move_right()
    def cross():
        for i in range(2):
            fill_cell()
            move_down()
            fill_cell()
        move_right()
        move_up()
        for i in range(2):
            fill_cell()
            move_left()
            fill_cell()
    def shiftLeft():
        move_right(n=4)
        move_up()
    def shiftDown():
        move_down(3)
        move_left(36)

    for j in range (5):
        for i in range(10):
            startPosition()
            cross()
            if(i<9):
                shiftLeft()
        if j<4:
            shiftDown()
    move_left(36)
    move_up()


if __name__ == '__main__':
    run_tasks()
