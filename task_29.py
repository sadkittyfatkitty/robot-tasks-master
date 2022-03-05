#!/usr/bin/python3

from pyrob.api import *

#To stop at the third in a row filled cell.
#If there are no three consecutive filled cells, then stop at the right wall.
#The distance to the wall is unknown.

@task
def task_7_7():
    n=0
    while(n<3 and wall_is_on_the_right()==False):
        move_right()
        if(cell_is_filled()==False):
            n=0
        else:
            n+=1
                


if __name__ == '__main__':
    run_tasks()
