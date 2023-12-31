# PILX
Python Interpreted Language X (PILX) is my own try to make a programming language.

To use PILX, simply download the entirety of this repository and run pilx.py<br>
You can take a peek at examples - my way of making a documentation, in the Examples folder. You can run these in the pilx.py by using the "e" command.

Currently in very early phases, literally useless. Can only store variables, do basic math operations and print the variables to the screen. But still fun!

<hr>

# DOCUMENTATION
## Syntax
There are four types of commands you can perform: Comments (use the `/` symbol), Variables (use the `+` symbol), Inclusion (use the `>` symbol) and Regular Commands (surround the command name with square brackets). <br>
Every command except for comments and inclusions need to end with a semicolon (`;`). You canno have more than one command per line.

Examples:
```
1  /I'm a comment!
2  +var="I'm a variable!";
3  >i im_a_library
4  [out]"I'm a command!";
```
## Variables
You create the + symbol to create variables.<br>
`+hi="Hello World!";`<br>
You can create Strings (`"Hello"`), Numbers (`17`, note: all numbers in PILX are saved as floats) and Booleans (`true`, booleans are not case sensitive).
```
1  +string = "Hello!";
2  +number = 17.84;
3  +bool = false;
```
### Math
You can quickly perform operations with numbers by adding another character after the `+` before the variable name.
```
1   +a=1;
2   ++a;
3   /a now countains 2
4   +*a;
5   /a now contains 4 (* is the square operator)
6   +-a;
7   /a now contains 3
8   +^a;
9   /a now contains 27 (^ raises the number to its power)
10  >i math;
11  +a=5;
12  +!a;
13  /a now contains 120 (! is the factorial operator, only works when math is imported, as we did using >i math)
```

### Key Variables
You can access special values using key variables. These are formed by using the `key` keyword, followed by a dot and the variable name. Here are some examples:
```
key.help - Basic information about the key variables and lists all possible variables you can access.
key.variables - Only usable in [out]; Prints all variables defined thus far, including all key variables and their values.
```

## Libraries and Modules
You can import libraries/modules using the inclusion operator (`>`) and using the command `i`, which stands for import.<br>
Syntax: `>i module_name`<br>
Available modules as of now: math

### Math `>i math`
Math allows the usage of the factorial operator (`+!variable;`)

## Commands
All commands must be surrounded with square brackets, their parameters come after.

### Out
Used to print a single value to the console. The value can be a literal or a variable.<br>
Syntax: `[out]value;`<br>
Example:
```
1              [out]"Hello World";
Output from 1  Hello World
2              +v=72;
3              [out]v;
Output from 3  72.0
```
