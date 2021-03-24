# coding: utf-8

# PROJECT: WALLBASE
# MODULE: setup
# DESCRIPTION: MÓDULO DE COMPILAÇÃO DO PROGRAMA
# AUTHOR: WALYSSON P. DOS REIS
# EMAIL: walyssondosreis@email.com

import cx_Freeze
import sys
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\walyssondosreis\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\walyssondosreis\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6"

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base)]
 # esse r na frente dos paths é para que uma junção \x não seja detectada como comando de string
cx_Freeze.setup(
    name = "MEI_SOLUTION",
    options = {"build_exe":
                   {"packages":["tkinter","cadframe","viewframe","meidb"],
                    "include_files": [
                        r"C:\Users\walyssondosreis\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                        r"C:\Users\walyssondosreis\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll",
                        r".\images",
                    ],
                    "include_msvcr":True, # O msvcr faz com que seja anexado todas as dlls necessarias para o programa rodar em outro pc
                    }
               },

    version = "1.0",
    description = "Beta MEI SOLUTION",
    executables = executables
    )

