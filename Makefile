generateDS = ./generateDS.py
gendir = ./generateDS-1.18e
todolist_user= gends_todolist_user.py


genclasses:
$(shell cd $(gendir); $(generateDS) -f --super=todolist -o ../todolist.py -s ../todolist_sub.py --user-methods=gends_todolist_user ../resources/todolist_simple.xsd)
	#cp -i to working name
