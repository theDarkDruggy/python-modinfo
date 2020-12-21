import inspect
import colorama
import stat

def getModules(module,modulestr):
    modules = []
    for i in inspect.getmembers(module,inspect.ismodule):
        x = modulestr+"."+str(i[0])
        modules.append(x)
    return modules

def getClasses(module,modulestr):
    classes = []
    for i in inspect.getmembers(module,inspect.isclass):
        x = modulestr+"."+str(i[0])
        classes.append(x)
    return classes

def getFuncsInmod(module,modulestr):
    funcs = []
    for i in inspect.getmembers(module):
        if "function" in str(i[1]):
            x = modulestr+"."+str(i[0])
            funcs.append(x)
        else:
            pass
    return funcs

def getFuncsInclass(clas,classtr):
    funcs = []
    for i in inspect.getmembers(clas):
        if "function" in str(i[1]):
            x = classtr+"."+str(i[0])
            funcs.append(x)
        else:
            pass
    return funcs

def printInfo(info):
    print(colorama.Fore.WHITE,colorama.Style.BRIGHT,info)
    print(colorama.Style.NORMAL)

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
        printFuncs(FuncsInmod)
    elif int(x) == 4:
        printFuncs(FuncsInclass)
    else:
        print("there is no {} option".format(x))
