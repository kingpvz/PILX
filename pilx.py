import os
import string
import sys
import EModules.maths as maths
#start definitions
variables = {"key":"Identifier for key variables. Use key.help for all uses.",
             "key.letterlow": string.ascii_lowercase, "key.letterup": string.ascii_uppercase, "key.letters": string.ascii_letters, "key.numbers": string.digits,
             "key.bools": (False, True, None), "key.bool": (False, True),
             "key.help": """
             Use key.<command> to trigger a key variable.
             help = This data flow | letterlow = all lower ascii letters | letters = all ascii letters
             letterup = all upper ascii letters | numbers = all ascii numbers | bools = all default bool values
             bool = both bool values | variables (only usable with [out]) = print all variables
"""}
imports = {"base":True, "maths":False}
def command_basic(a,iter):
    if "]" not in a:
        print("Error!",a,"is a faulty expression, missing \"]\" token.")
    else:
        if a[1:4]=="out":
            if a[5]=='"':
                if a.count('"')==2:
                    tes = a[6:].find('"') + 6
                    if a[tes+1]!=";":
                        print("Error at line "+str(iter)+". Syntax error after parsing string at token \""+a[tes+1:-1]+"\". Remove this token.")
                    else:
                        print(a[6:tes])
                else:
                    print("Error at line "+str(iter)+". String declaration is incorrect.")
            elif a[5] in string.digits:
                print(a[5:-1])
            else:
                if a[5:-1].strip() == "key.variables": print(variables)
                elif a[5:-1].strip() in variables.keys(): print(variables[a[5:-1].strip()])
                else: print("Error at line "+str(iter)+". Referenced variable doesn't exist.")
        else:
            print("Error at line "+str(iter)+". This command does not exist or is mistyped.")

def command_insert(a,iter):
    if a[1]=="i":
        if a[2]==" ":
            if a[3:].strip()=="maths":imports["maths"]=True
            else: print("Failed to import", a[3:]+". Check if you haven't mispelled the module name.")
        else: print("Error at line {0}. Unresolved insert command or missing space.".format(iter))
    else: print("Unresolved insert command at line {0}.".format(iter))

def command_variable(a,iter):
    if "=" not in a and a[1] not in ["+", "-", "*", "/", "^", "!"]: print("Error!",a,"is a faulty expression. Declared variable has no value.")
    elif a[1]=="+": 
        if a[2:-1] in variables:
            if type(variables[a[2:-1]]) == type(1) or type(variables[a[2:-1]]) == type(1.2): variables[a[2:-1]]+=1
            else: print("Error! Can't increase the value of a non-integral value.")
        else: print("Error! Variable doesn't exist.")
    elif a[1]=="-": 
        if a[2:-1] in variables:
            if type(variables[a[2:-1]]) == type(1) or type(variables[a[2:-1]]) == type(1.2): variables[a[2:-1]]-=1
            else: print("Error! Can't decrease the value of a non-integral value.")
        else: print("Error! Variable doesn't exist.")
    elif a[1]=="*": 
        if a[2:-1] in variables:
            if type(variables[a[2:-1]]) == type(1) or type(variables[a[2:-1]]) == type(1.2): variables[a[2:-1]]**=2
            else: print("Error! Can't remultiply the value of a non-numeral value.")
        else: print("Error! Variable doesn't exist.")
    elif a[1]=="^": 
        if a[2:-1] in variables:
            if type(variables[a[2:-1]]) == type(1) or type(variables[a[2:-1]]) == type(1.2): 
                try:
                    variables[a[2:-1]]**=variables[a[2:-1]]
                except: variables[a[2:-1]]=sys.maxsize
            else: print("Error! Can't power up the value of a non-numeral value.")
        else: print("Error! Variable doesn't exist.")
    elif a[1]=="!":
        if imports["maths"]:
            if a[2:-1] in variables:
                if type(variables[a[2:-1]]) == type(1) or type(variables[a[2:-1]]) == type(1.2):
                    variables[a[2:-1]] = maths.factorial(int(variables[a[2:-1]]))
                else: print("Error! Can't apply factorial to a non-numeral value.")
            else: print("Error! Variable doesn't exist.")
        else:
            print("Error at line {0}. This operator is only available after a module is imported.".format(iter))
    elif a[a.find("+"):a.find("=")] == "": print("Error!",a,"is a faulty expression. Declared variable has no name.")
    elif a[1:-1].strip()[0] in string.digits: print("Error!",a,"is a faulty expression. A variable name cannot start with a digit.")
    elif (a[1:-1].strip()[0] not in string.ascii_letters) and a[1:-1].strip()[1] !="_": print("Error!",a,"is a faulty expression. A variable name cannot start with a special character.")
    elif all(False if j not in string.ascii_letters or j !="_" or j not in string.digits else True for j in a[1:a.find("=")].strip()): print("Error!",a,"is a faulty expression. A variable name can only contain numbers, letters and underscores.")
    else:
        tes = a.find("=")
        name = a[1:tes].strip()
        if name == "key": print("Variable name forbidden. The word \"key\" is a reserved name.")
        elif a[tes+1]=='"': 
            if '"' in a[tes+2:]: variables[name]=a[(tes+2):(a[tes+2:].find('"')+(tes+2))]
            else: print("Error at line "+str(iter)+". Cannot create string, missing \" token.")
        elif a[tes+1] in string.digits: 
            try:
                variables[name]=float(a[(tes+1):-1].strip())
            except:
                print("An error occured while trying to declare number at line",iter)
        elif a[tes+1:-1].strip()[0] in string.ascii_letters:
            if a[(tes+1):-1].strip().lower() == "true": variables[name]=True
            elif a[(tes+1):-1].strip().lower() == "false": variables[name]=False
            elif a[(tes+1):-1].strip().lower() == "none": variables[name]=None
            else:
                if a[(tes+1):-1].strip() in variables.keys():
                    variables[name]=variables[a[(tes+1):-1].strip()]
                else: print("Error at line "+str(iter)+". Assigned variable doesn't exist.")
        else: print("Error at line {0}. Requested variable type doesn't exist.".format(iter))

#end definitions

#start program
def reloader():
    print("Welcome to PILX Programming snapshot alpha 0.0.5")
    print("n = New File; o = Open File / Append to File; r = Run; e = Examples; Write \"help\" for all possible abbreviations.")
    print("\nTip: Edit files with the .plx extension using a text editor!")
    print("\nTo save code, write \"#SAVE\"! For more commands write \"#HELP\"\n")
    
    if True:
        if not os.path.exists("./Projects"):os.mkdir("./Projects")
        if not os.path.exists("./Projects/.backbone"):os.mkdir("./Projects/.backbone")
        try: 
            with open("Projects/.backbone/backbone.plx", "x") as a: a.write("/This file is not for using!")
        except FileExistsError: pass
        CURRENT_FILE_VARIABLE = "./Projects/backbone/backbone.plx"#file creation help
    INVEST_VARIABLE_LINE = 1
    INVEST_VARIABLE_EXECUTION = ""
    while True:
        TEMPORARY_VARIABLE_INSERT = input("Type command: ").lower().strip()
        if TEMPORARY_VARIABLE_INSERT == "help" or TEMPORARY_VARIABLE_INSERT == "?":
            print("""
            ###COMMAND ABBREVIATIONS###
            Help Command: help, ?
            New File: n, new, nf, newfile, new file
            Open/Append to File: o, open, of, openfile, open file, a, append, af
            Run file: r, run, start, compile, rf, runfile, run file, c, cf
            Examples: e, ex, example, examples\n""")
        elif TEMPORARY_VARIABLE_INSERT in ["n","new","nf","newfile","new file"]:
            TEMPORARY_VARIABLE_FILENAME = input("Input your new project name: ")
            try: 
                with open("Projects/"+TEMPORARY_VARIABLE_FILENAME+".plx", "x") as a: a.write("/This is the default line in the PILX Programming file.")
            except FileExistsError: print("This file already exists!")
            else: print("File created succesfully!\n")
        elif TEMPORARY_VARIABLE_INSERT in ["o" ,"open","of","openfile","open file","a","af","append"]:
            TEMPORARY_VARIABLE_FILENAME = input("Write the name of your project (without extension, make sure it's located in the Projects folder): ")+".plx"
            if os.path.exists("./Projects/"+TEMPORARY_VARIABLE_FILENAME):
                CURRENT_FILE_VARIABLE="./Projects/"+TEMPORARY_VARIABLE_FILENAME
                with open(CURRENT_FILE_VARIABLE, "r") as a:
                    INVEST_VARIABLE_EXECUTION = a.read()+"\n"
                    a.seek(0)
                    for line in a.readlines():
                        print(str(INVEST_VARIABLE_LINE)+":",line,end="")
                        INVEST_VARIABLE_LINE+=1
                    a.seek(0, 2)
                    a.seek(a.tell() - 2, 0)
                    if a.read()!="\n":print()
                break
            else: print("This file doesn't exist!")
        elif TEMPORARY_VARIABLE_INSERT in ["r", "run", "start","compile","rf","runfile","run file","c","cf"]:
            TEMPORARY_VARIABLE_FILENAME = input("Write the name of your project (without extension, make sure it's located in the Projects folder): ")+".plx"
            if os.path.exists("./Projects/"+TEMPORARY_VARIABLE_FILENAME):
                CURRENT_FILE_VARIABLE="./Projects/"+TEMPORARY_VARIABLE_FILENAME
                with open(CURRENT_FILE_VARIABLE, "r") as a:
                    INVEST_VARIABLE_EXECUTION = a.read()
                print("\n\n")
                TEMPORARY_VARIABLE_LINE = 1
                for i in INVEST_VARIABLE_EXECUTION.split("\n"):
                   if len(i)==0: pass
                   elif i[0]=="/": pass
                   elif i[0]==">":
                     command_insert(i,TEMPORARY_VARIABLE_LINE)
                   elif i[-1]!=";":
                       print("Error at line "+ str(TEMPORARY_VARIABLE_LINE) +" occured: Missing ; token on the end. Line reads: "+i)
                   elif i[0]=="[":
                     command_basic(i,TEMPORARY_VARIABLE_LINE)
                   elif i[0]=="+":
                     command_variable(i,TEMPORARY_VARIABLE_LINE)
                   TEMPORARY_VARIABLE_LINE += 1
                print("\n\n##END OF EXECUTION##")
                print("\n\n")
            else: print("This file doesn't exist!")
        elif TEMPORARY_VARIABLE_INSERT in ["e", "ex", "examples", "example"]:
            TEMPORARY_VARIABLE_FILENAME = input("\nYou can write \"list\" to see all examples possible.\nWrite the name of the example (without extension, make sure it's located in the Examples folder): ")+".plx"
            if TEMPORARY_VARIABLE_FILENAME == "list.plx":
                a=0
                for i in os.listdir("./Examples"):
                    a+=1
                    if a<4:
                        print(f"{i} | ",end="")
                    else:
                        print(f"{i}")
                        a=0
                print()
            elif os.path.exists("./Examples/"+TEMPORARY_VARIABLE_FILENAME):
                CURRENT_FILE_VARIABLE="./Examples/"+TEMPORARY_VARIABLE_FILENAME
                with open(CURRENT_FILE_VARIABLE, "r") as a:
                    INVEST_VARIABLE_EXECUTION = a.read()
                print("\n\n")
                TEMPORARY_VARIABLE_LINE = 1
                for i in INVEST_VARIABLE_EXECUTION.split("\n"):
                   if len(i)==0: pass
                   elif i[0]=="/": pass
                   elif i[0]==">":
                     command_insert(i,TEMPORARY_VARIABLE_LINE)
                   elif i[-1]!=";":
                       print("Error at line "+ str(TEMPORARY_VARIABLE_LINE) +" occured: Missing ; token on the end. Line reads: "+i)
                   elif i[0]=="[":
                     command_basic(i,TEMPORARY_VARIABLE_LINE)
                   elif i[0]=="+":
                     command_variable(i,TEMPORARY_VARIABLE_LINE)
                   TEMPORARY_VARIABLE_LINE += 1
                print("\n\n##END OF EXECUTION##")
                print("\n\n")
            else: print("This file doesn't exist!")
        else: print("Incorrect command. If you are trying to use runtime command (starting with # or ;)\nnote, that they can only be used with an open file you are editing.")
    
    #start editor
    while True:
        RUNVAR = input(str(INVEST_VARIABLE_LINE)+": ")
        if RUNVAR == "#SAVE" or RUNVAR == ";s":
            with open(CURRENT_FILE_VARIABLE, "w") as a:
                a.write(INVEST_VARIABLE_EXECUTION)
                print("--- Saved Succesfully! ---")
        elif RUNVAR == "#HELP" or RUNVAR == ";h":
            print("""
            Save: #SAVE / ;s | Help: #HELP / ;h | Restart without saving: #ABORT / ;a
            Restart (Saves current state and reloads the program): #RESTART / ;r
            """)
        elif RUNVAR == "#RESTART" or RUNVAR == ";r":
            with open(CURRENT_FILE_VARIABLE, "w", errors='backslashreplace') as a:
                a.write(INVEST_VARIABLE_EXECUTION)
                print("--- Saved Succesfully! Reloading... ---\n\n\nReloaded succesfully.\n\n\n\n\n")
            reloader()
        elif RUNVAR == "#ABORT" or RUNVAR == ";a":
            TEMPORARY_DECISION_BOOL = input("Are you sure? (Write 'YES' to proceed.): ").upper()
            if TEMPORARY_DECISION_BOOL == "YES":
                print("\n\n\n")
                reloader()
            else:
                print("Abort cancelled.")
        elif RUNVAR[0]=="/":
            INVEST_VARIABLE_LINE+=1
            INVEST_VARIABLE_EXECUTION += RUNVAR+"\n"
        elif RUNVAR[-1]!=";": print("Line "+str(INVEST_VARIABLE_LINE)+" declined. Endline symbol (;) obfuscated.")
        else:
            INVEST_VARIABLE_LINE+=1
            INVEST_VARIABLE_EXECUTION += RUNVAR+"\n"
    #end editor

reloader()
#end program
