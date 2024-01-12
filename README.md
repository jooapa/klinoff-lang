# klinoff-lang

<img src="https://raw.githubusercontent.com/jooapa/klinoff-lang/main/logo.png" width="200" height="200">

## Table of contents
- [Introduction](#introduction)
- [IMPORTANT!!](#important)
- [file extension](#file-extension)
- [Features](#features)
- [Documentation](#documentation)
    - [Starting](#starting)
    - [Variables](#variables)
    - [Comments](#comments)
    - [Printing](#printing)
    - [Creating a pig (function)](#creating-a-pig-function)
    - [Slingshot (jump to line)](#slingshot-jump-to-line)
    - [If statements](#if-statements)
    - [For loops](#for-loops)
    - [Input](#input)
    - [Data types](#data-types)
    - [Built-in secret functions](#built-in-secret-functions)
    - [all keywords](#all-keywords)
        - [Operators](#operators)
        - [Keywords](#keywords)
        - [Variable modifiers](#variable-modifiers)
- [Using the interpreter](#using-the-interpreter)
    - [Installation](#installation)
    - [Usage](#usage)
- [Examples](#examples)
    - [Cubic root Example](#cubic-root-example)
    - [Simple if statement Example](#simple-if-statement-example)
    - [Simple for loop Example](#simple-for-loop-example)
    - [Simple input Example](#simple-input-example)

## Syntax highlighting
- [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=Jooapa.klinoff-lang-syntax-highlighting)
- [Github](https://github.com/jooapa/klinoff-lang-syntax-higlighting)

## Introduction
klinoff-lang is a huge step in the evolution of programming languages. It is a language that is easy to learn and use, but really powerful.

Klinoff-lang is a interpreted language, one known interpreter is found on this repository.

## IMPORTANT!!
Your code must be coded with SPACES and is case sensitive with clear difference between words. The code must be written exactly like in this documentation. **DONT USE SPACES JUST HERE AND THERE, USE SPACES VERY CAREFULLY.**

do this:
```bash
oink "Hello World!"
```
not this:
```bash
oink"Hello World!"
```

And also Happy to tell youu guys, that klinoff-lang is partnered with EcmaScript, so you HAVE TO leave a empty line at the end of the file.

## file extension
The file extension for klinoff language is
- `.kln`
- `.nöff`

and just in case for everybodys sanity, if you want some working color syntax highlighting, use `.sh` extension for some reason `.nöff` works but not as good. INTRODUCING THE NEW VS CODE EXTENSION FOR KLINOFF-LANG, WITH THE EXTENSION YOU GET FULL CONTROL OF THE COLOR SYNTAX HIGHLIGHTING

## Features
- Easy to learn
- Easy to use
- Powerful
- Fast

## Documentation
Documentation for klinoff-lang can be found here

klinoff-lang reads the file from top to bottom, and executes the code line by line.


### Starting
To start a klinoff-lang file, you need to use the `nöff` keyword. This keyword is used to start the program, and follows the name of your program.

```bash
nöff my_program
```

### Variables
Variables are used to store data. Variables can be created by using the `nöf` keyword. 
```bash
nöf variable = value
```

```bash
nöf num1 = 5
nöf word = Hello World!
```
you can also modify variables by using the `modify` keyword.
```bash
nöf num1 = 5
nöf num2 = 6
modify $num1 $num2
// num1 == 6
```
using `add`, `subtract`, `multiply`, `divide`, `modulo`, and `power`.
```bash
add $num1 5
sub $num2 $num1
multiply $num3 5
divide $num4 0.5
modulo $num5 5
power $num6 $num1
```

### Comments
Comments are used to explain the code. Comments are ignored by the compiler. Comments can be created by using the `//` character.

```c
// This is a comment

//this doesnt work
```

### Printing
Printing is used to print text to the console. Printing can be done by using the `oink` keyword.
The future is here so that the oink function will always remove letter `§` from the output.

```bash
oink "Hello World!"
// Prints "Hello World!" to the console
```
```bash
nöf money = -5000

oink "I have $money§€ in my bank account"
// Prints "I have -5000€ in my bank account" to the console
```

### Creating a pig (function)
You can create a line receiver by using the `pig` keyword. Use `gip` to end the function.
```bash
pig possu
    oink "Hello World!"
gip
```

### Slingshot (jump to line)
You can jump to the line you want by using the `slingshot` keyword. It works like a angry bird, you slingshot to the pig. You can jump to the line by providing only number
```bash
//jump to pig
slingshot possu

// jumps to line
slingshot 5
```

### If statements
If statements can be created by using the `niff` keyword. else if statements can be created by using the `nilf` keyword. klinoff-lang is so advanced that it doesnt need the `else` statements.

After make the statemt in given line, you can use `slingshot` keyword to jump to the line you want.

```bash
nöf num1 = 1
nöf num2 = 1

niff $num1 > $num2 : slingshot possu1
nilf $num1 < $num2 : slingshot possu2
nilf $num1 == $num2 : slingshot possu3

```

### For loops
For loops can be created by using the `nör` keyword. Second parameter is for the loop name. and the third parameter is the times the loop will run. Use `når` to end the loop.

Be careful, you cannot use the same loop name twice.

```bash
nör oink 5
    oink "oinking 5 times"
når 

```
```bash
nöf times = 5
    nör oink $times
    oink "oinking $times times"
når 

```

### Input
The input will be saved to the variable you give to the input function. last parameter is the question you want to ask.
```bash
nöf name = pig

input $name "why is your name $name§? Change it to: "

oink "Hello $name§!"
```


## Data types
- `string` - text

## Built-in secret functions
- `nöffnöff` - return the program name __not working yet__

## all keywords
### Operators
- `==` - equal to
- `!=` - not equal to
- `>` - greater than
- `<` - less than
- `>=` - greater than or equal to
- `<=` - less than or equal to

### Keywords
- `nöff` - start of program
- `nöf` - create variable
- `oink` - print
- `niff` - if statement
- `nilf` - else if statement
- `nör` - start for loop 
- `når` - end   loop
- `slingshot` - jump to line or function
- `pig` - create function
- `gip` - end function
- `input` - input

### Variable modifiers
- `modify`
- `add`
- `sub` - subtract
- `multiply`
- `divide`
- `modulo`
- `power`

## Using the interpreter
## Installation
To install the interpreter, you need to have python3 installed. You can install python3 from [here](https://www.python.org/downloads/).

After installing python3, you need to install the interpreter. by cloning this repository.
## Usage
```bash
python interpeter/interpret.py example.nöff
```
you can you the `--debug` or `-d` flag to see the debug information.
```bash
python interpeter/interpret.py example.nöff -d
```


## Examples
## Cubic root Example
```bash
nöff cubic_root_example

nöf num1 = 16
nöf num2 = 2

slingshot cubic_root_num1

// function to cubic root the num1
pig cubic_root_num1

    multiply $num1 $num2
    power $num1 0.333

    oink "$num1"

gip

```
## Simple if statement Example
```bash
nöff if_example

nöf num1 = 16
nöf num2 = 2

niff $num1 > $num2 : slingshot possu1
nilf $num1 < $num2 : slingshot possu2
nilf $num1 == $num2 : slingshot possu3

pig possu1
    oink "$num1 is bigger than $num2"
gip

pig possu2
    oink "$num1 is smaller than $num2"
gip

pig possu3
    oink "$num1 is equal to $num2"
gip

```
## Simple for loop Example
```bash
nöff loop_example

nöf num = 5

nör oink 5
    sub $num 1
    oink "oinking $num times"
når 

```
## Simple input Example
```bash
nöff input_example

nöf name = pig

input $name "why is your name $name§? Change it to: "

oink "Hello $name§!"

```

# Contributors
## Creator
- [Jooapa](https://github.com/jooapa)

## Contributors
- [miskamero](https://github.com/miskamero)