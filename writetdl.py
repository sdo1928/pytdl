import sys, os
import todolist_sub as todolist
from todolist_sub import TODOLISTSub as TODOLIST
from todolist_sub import TASKSub as TASK

## test to read nested tdl, change and then write back
tdl = todolist.parse('./resources/test_tdl.tdl')
newTask = TASK(TITLE='First add task test')
tdl.add_TASK(newTask)

fileOut = open('tmp.tdl', 'w')
tdl.export(fileOut, 3, '')
fileOut.close()


