main_str = ""
undo_stack = []
redo_stack = []
def edit(str) :
    global main_str
    undo_stack.append(main_str)
    redo_stack.clear
    main_str += str
def undo() :
    global main_str
    if undo_stack:
        redo_stack.append(main_str)
        main_str = undo_stack.pop()
    else :
        print("nothing to undo")
        return
def redo():
    global main_str
    if redo_stack:
        undo_stack.append(main_str)
        main_str = redo_stack.pop()
    else :
        print("nothing to redo")
        return

        


while True :
    print("1.Edit \n 2.Undo \n 3.Redo \n 4.show \n 5.exit")
    opt = int(input("enter option : \n"))
    if opt == 1:
        edit(input("text : \n"))
    elif opt == 2:
        undo()
    elif opt == 3:
        redo()
    elif opt == 4:
        print(main_str)
    elif opt == 5:
        break;
    else:
        print("invalid")
        continue

        
