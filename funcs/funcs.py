import inspect
import colorama

def getModules(module):
    modules = []
    for i in inspect.getmembers(module,inspect.ismodule):
        x = str(module)+"."+str(i[0])
        modules.append(x)
    return modules

def getClasses(module):
    classes = []
    for i in inspect.getmembers(module,inspect.ismodule):
        x = str(module)+"."+str(i[0])
        classes.append(x)
    return classes

def getFuncsInmod(module):
    funcs = []
    for i in inspect.getmembers(module):
        if "function" in str(i[1]):
            x = str(module)+"."+str(i[0])
            funcs.append(x)
        else:
            pass
    return funcs

def getFuncsInclass(class):
    funcs = []
    for i inspect.getmembers(class):
        if "function" in str(i[1]):
            x = str(clas)+"."+str(i[0])
            funcs.append(x)
        else:
            pass
    return funcs

def printInfo(info):
    print(colorama.Fore.WHITE,colorama.Style.BRIGHT,info)
    print(colorama.Style.Normal)

def printFuncs(funcs):
    print(colorama.Fore.GREEN)
    for i in funcs:
        print(i)
    print(colorama.Fore.WHITE)

def printModules(modules):
    print(colorama.Fore.YELLOW)
    for i in modules:
        print(i)
    print(colorama.Fore.WHITE)

def printClasses(classes):
    print(colorama.Fore.CYAN)
    for i in classes:
        print(i)
    print(colorama.Fore.WHITE)

def getChoose(modules,classes,FuncsInmod,FuncsInclass):
    x = input("Enter 1 for modules, enter 2 for classes, \nenter 3 for functions in modules , enter 4 for functions in classes \n:")
    if not x.isdigit():
        print("there is no {} option".format(x))
    elif int(x) == 1:
        printModules(modules)
    elif int(x) == 2:
        printClasses(classes)
    elif int(x) == 3:
        printfuncs(FuncsInmod)
    elif int(x) == 4:
        printfuncs(FuncsInclass)
    else:
        print("there is no {} option".format(x))
