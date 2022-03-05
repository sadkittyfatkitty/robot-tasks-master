#!/usr/bin/python3

from pyrob.api import *

# Paint over the corridors and return.
# The number and length of the corridors are unknown.

@task(delay=0.01)
def task_6_6():
    while(wall_is_on_the_right()==False): 
        move_right()
        if(wall_is_above()==False):
            move_up()
            while(wall_is_above()==False):
                fill_cell()
                move_up()
                fill_cell()
            if(wall_is_beneath()==False and wall_is_on_the_right()==True and wall_is_on_the_left()==True):
                fill_cell()
                while(wall_is_beneath()==False):
                    move_down()
    if(wall_is_on_the_right()==True):
        while(wall_is_beneath()==True):
            move_left()
            


if __name__ == '__main__':
    run_tasks()
