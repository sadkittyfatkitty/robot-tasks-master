#!/usr/bin/python3

from pyrob.api import *

#Fill the cells. Distance to the wall is unknown.

@task
def task_8_11():
    while(wall_is_on_the_right()==False):
        if(wall_is_beneath()==True and wall_is_above()==False):
            move_up()
            fill_cell()
            move_down()
        if (wall_is_above()==True and wall_is_beneath()==False):
            move_down()
            fill_cell()
            move_up()
        if (wall_is_beneath()==False and wall_is_above()==False):
            move_up()
            fill_cell()
            move_down(n=2)
            fill_cell()
            move_up()
        if(wall_is_above()==True and wall_is_beneath()==True):
            fill_cell()
        move_right()
        
    # last cell check
    
    if(wall_is_beneath()==True and wall_is_above()==False):
        move_up()
        fill_cell()
        move_down()
    if (wall_is_above()==True and wall_is_beneath()==False):
        move_down()
        fill_cell()
        move_up()
    if (wall_is_beneath()==False and wall_is_above()==False):
        move_up()
        fill_cell()
        move_down(n=2)
        fill_cell()
        move_up()
    if(wall_is_above()==True and wall_is_beneath()==True):
        fill_cell()


if __name__ == '__main__':
    run_tasks()
