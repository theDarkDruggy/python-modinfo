import sys
sys.path.append('../../funcs')
import funcs as func
import os

##### GETTNG MODULES #####
modules = ["os.path","os.st"]
#####=====#####
##### GETTING CLASSES #####
classes = func.getClasses(os,"os")
#####=====#####
##### GETTING FUNCTIONS #####
FuncsInmod = func.getFuncsInmod(os,"os") + func.getFuncsInmod(os.path,"os.path") + func.getFuncsInmod(os.st,"os.st")

FuncsInclass = []

fnc2 = func.getFuncsInclass(os.MutableMapping,"os.MutableMapping")
fnc3 = func.getFuncsInclass(os.PathLike,"os.PathLike")
fnc4 = func.getFuncsInclass(os._Environ,"os._Environ")
fnc5 = func.getFuncsInclass(os._wrap_close,"os._wrap_close")
FuncsInclass = fnc2 + fnc3 + fnc4 + fnc5
##### CHOOSING #####
info = """
This module provides a portable way of using operating system dependent
functionality. If you just want to read or write a file see open(), if
you want to manipulate paths, see the os.path module, and if you want
to read all the lines in all the files on the command line see the
fileinput module. For creating temporary files and directories see the
tempfile module, and for high-level file and directory handling see
the shutil module.
"""
func.printInfo(info)
func.getChoose(modules,classes,FuncsInmod,FuncsInclass)
#####=====#####
