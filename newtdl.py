import sys, os
import mx.DateTime as DateTime
import todolist_sub as todolist
from todolist_sub import TODOLISTSub as TODOLIST
from todolist_sub import TASKSub as TASK

#attempt to match todolist.exe new file behavior
#New TODOLIST
newTodolist = TODOLIST()

#newTodolist.set_CATEGORY
#newTodolist.set_STATUS
#newTodolist.set_PERSON
#newTodolist.set_ALLOCATEDBY
#newTodolist.set_VERSION
newTodolist.set_FILEVERSION(1)
newTodolist.set_PROJECTNAME('')
#newTodolist.set_FILENAME
#newTodolist.set_CUSTOMCOMMENTSTYPE
td = DateTime.today()
newTodolist.set_LASTMODIFIED(td.strftime('%m/%d/%Y'))
newTodolist.set_EARLIESTDUEDATE('0.0000000')
newTodolist.set_NEXTUNIQUEID(1)
newTodolist.set_FILEFORMAT(9)

#New TASK
newTask = TASK()
newTask.set_TITLE('Sample Task')

newTodolist.add_TASK(newTask)

fileOut = open('new.tdl', 'w')
newTodolist.export(fileOut, 1, '')
fileOut.close()
