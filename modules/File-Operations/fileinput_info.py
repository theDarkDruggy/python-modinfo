import sys
sys.path.append("../../funcs")
import funcs
import fileinput

modules = []
##### GETTING CLASSES #####
classes = funcs.getClasses(fileinput,"fileinput")
#####=====#####
##### GETTING FUNCTIONS #####
FuncsInmod = funcs.getFuncsInmod(fileinput,"fileinput")
FuncsInclass = funcs.getFuncsInclass(fileinput.FileInput,"fileinput.FileInput")
#####=====#####
##### CHOOSING #####
info = """
This module implements a helper class and functions to quickly write a
loop over standard input or a list of files. If you just want to read
or write one file see open().
"""
funcs.printInfo(info)
funcs.getChoose(modules,classes,FuncsInmod,FuncsInclass)
#####=====#####
