import cx_Freeze
import os

executables = [cx_Freeze.Executable('game.py')]
os.environ['TCL_LIBRARY'] = r'C:\Users\HP\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\HP\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

cx_Freeze.setup(
                name='Slither',
                options={'build_exe':{'packages':['pygame'],'include_files':['apple.png','snakehead.png']}},
                description = 'SlitherGame',
                executables = executables
                )
