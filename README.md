# robot-tasks-master
Set of tasks for graphic executor robot. Source: http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html

Robot is a graphic executor. Robot can move on field of cells, confined with walls. Between the cells might be walls. 
Possible cell states:

empty;
marked to be painted;
painted over;
the cell marked with a black dot, where the robot should come after the algorithm has been executed.

Robot commandes: 
move_left(n=1) Move n cells to the left (default n = 1)
move_right(n=1) Move n cells to the right (default n = 1)
move_up(n=1) Move n cells up (default n = 1)
move_down(n=1) Move n cells down (default n = 1)
wall_is_above() returns True if there is a wall above, False otherwise
wall_is_beneath() returns True if the wall is below, False otherwise
wall_is_on_the_left() returns True if the wall is on the left, False otherwise
wall_is_on_the_right() returns True if the wall is on the right, False otherwise
fill_cell() Fill in the current cell
cell_is_filled() Returns True if the current cell is filled
