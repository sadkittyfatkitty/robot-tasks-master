#!/usr/bin/python3

from pyrob.api import *

# Get out of the trap. The exit can be either on the right or on the left.
# There may be no way out, in this case, stop at the right dead end.

@task
def task_8_29():
    if(wall_is_on_the_left()==False):
        while(wall_is_on_the_left()==False):
            move_left()
        if(wall_is_above()==False):
            while(wall_is_above()==False):
                move_up()
                
    if(wall_is_on_the_left()==True):
        while(wall_is_on_the_right()==False):
            move_right()
        if(wall_is_above()==False):
            while(wall_is_above()==False):
                move_up()
    if(wall_is_above()==True and wall_is_beneath()==False):
        while(wall_is_on_the_left()==False):
            move_left()

    elif(wall_is_on_the_right()==True and wall_is_beneath()==True):
        fill_cell()
    
        


if __name__ == '__main__':
    run_tasks()
