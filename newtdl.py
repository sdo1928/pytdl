import todolist_sub as todolist
import mx.DateTime as DateTime
import sys, os
from todolist_sub import TODOLISTSub as TODOLIST
from todolist_sub import TASKSub as TASK

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
newTodolist.set_NEXTUNIQUEID(2)
newTodolist.set_FILEFORMAT(9)


newTask = TASK()
PRIORITYCOLOR="15732480"
PRIORITYWEBCOLOR="#000FF0"

newTask.set_TITLE('Task')

#newTask.set_ALLOCATEDBY
newTask.set_CALCCOST('0.00000000')
#newTask.set_CALCPERCENTDONE
#newTask.set_CALCTIMEESTIMATE
#newTask.set_CALCTIMESPENT
#newTask.set_CATEGORY
#newTask.set_CATEGORY1
#newTask.set_CATEGORY2
#newTask.set_CATEGORY3
#newTask.set_CATEGORY4
#newTask.set_CATEGORY5
#newTask.set_CATEGORY6
#newTask.set_CATEGORY7
#newTask.set_CATEGORY8
#newTask.set_CATEGORY9
#newTask.set_COLOR
#newTask.set_COMMENTS
#newTask.set_COMMENTSTYPE
newTask.set_COST('0.00000000')
newTask.set_CREATIONDATE(td.COMDate())
newTask.set_CREATIONDATESTRING(td.strftime('%m/%d/%Y'))
#newTask.set_CUSTOMCOMMENTS
#newTask.set_DEPENDS
#newTask.set_DEPENDS1
#newTask.set_DEPENDS2
#newTask.set_DEPENDS3
#newTask.set_DEPENDS4
#newTask.set_DEPENDS5
#newTask.set_DEPENDS6
#newTask.set_DEPENDS7
#newTask.set_DEPENDS8
#newTask.set_DEPENDS9
#newTask.set_DONEDATE
#newTask.set_DONEDATESTRING
#newTask.set_DUEDATE
#newTask.set_DUEDATESTRING
#newTask.set_EXTERNALID
#newTask.set_FILEREFPATH
#newTask.set_FLAG
newTask.set_ICONINDEX(-1)
newTask.set_ID(1)
#newTask.set_LASTMOD
#newTask.set_LASTMODSTRING
#newTask.set_NUMCATEGORY
#newTask.set_NUMDEPENDS
#newTask.set_NUMPERSON
newTask.set_PERCENTDONE(0)
#newTask.set_PERSON
#newTask.set_PERSON1
#newTask.set_PERSON2
#newTask.set_PERSON3
#newTask.set_PERSON4
#newTask.set_PERSON5
#newTask.set_PERSON6
#newTask.set_PERSON7
#newTask.set_PERSON8
#newTask.set_PERSON9
newTask.set_POS(1)
newTask.set_PRIORITY(5)
newTask.set_PRIORITYCOLOR(PRIORITYCOLOR)
newTask.set_PRIORITYWEBCOLOR(PRIORITYWEBCOLOR)
newTask.set_RISK(0)
newTask.set_STARTDATE(td.COMDate())
newTask.set_STARTDATESTRING(td.strftime('%m/%d/%Y'))
#newTask.set_STATUS
#newTask.set_TEXTCOLOR
#newTask.set_TEXTWEBCOLOR
#newTask.set_TIMEESTIMATE
#newTask.set_TIMEESTUNITS
#newTask.set_TIMESPENT
#newTask.set_TIMESPENTUNITS
#newTask.set_TITLE
#newTask.set_VERSION
#newTask.set_WEBCOLOR









newTodolist.add_TASK(newTask)

fileOut = open('tmp.tdl', 'w')

newTodolist.export(fileOut, 1, '')

fileOut.close()


