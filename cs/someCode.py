# module level variable
modvar = 15

def helloWorld(arg):
    print("Hello world")
    print("argument is "+repr(arg))
    # to read/access module level variable you do not need to declar global
    print("module level variable value is %f" % modvar)

def accessModVar(newval):
    global modvar
    # to modify you must declar global
    modvar = newval

def accessModVarWrong(newval):
    # to modify you must declar global
    modvar = newval
