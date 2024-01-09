# klinoff-lang

## Introduction
klinoff-lang is a huge step in the evolution of programming languages. It is a language that is easy to learn and use, but really powerful.

Klinoff-lang is a interpreted language, one known interpreter is found on this repository.

## IMPORTANT!!
Your code must be coded with spaces with clear differene between words. the code must be written exactly like in this documentation.

do this:
```bash
oink "Hello World!"
```
not this:
```bash
oink"Hello World!"
```

## EVEN MORE IMPORTANT!!
klinoff-lang is case sensitive, so you must write the code exactly like in this documentation.

and also Happy to tell youu guys, that klinoff-lang is parthnered with EcmaScript, so you HAVE TO leave a empty line at the end of the file.

## file extension
The file extension for klinoff language is
- `.klinoff`
- `.kln`
- `.nöff`

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

### If statements
If statements can be created by using the `niff` keyword. else if statements can be created by using the `nilf` keyword.

After make the statemt in given line, you can use `slingshot` keyword to jump to the line you want.

```bash
nöf num1 = 1
nöf num2 = 1

niff $num1 > $num2 : slingshot possu1
nilf $num1 < $num2 : slingshot possu2
nilf $num1 == $num2 : slingshot possu3

```

### Creating a pig (function)
You can create a line receiver by using the `pig` keyword.
```bash
pig possu
oink "Hello World!"
gip
```

### Slingshot (jump to line)
You can jump to the line you want by using the `slingshot` keyword. It works like a angry bird, you slingshot to the pig 
```bash
slingshot possu
```


### For loops
For loops can be created by using the `nör` keyword. and the second parameter is the times the loop will run. Use `når` to end the loop.

```bash
nör 5
oink "oinking 5 times"
når // to end the loop

```

### Operators
- `+` - addition
- `-` - subtraction
- `*` - multiplication
- `/` - division
- `%` - modulo
- `^` - power

- `==` - equal to
- `!=` - not equal to
- `>` - greater than
- `<` - less than
- `>=` - greater than or equal to
- `<=` - less than or equal to

### Data types
- `string` - text

## all keywords
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

- `modify` - modify variable
- `add` - add to variable
- `sub` - subtract from variable
- `multiply` - multiply variable
- `divide` - divide variable
- `modulo` - modulo variable
- `power` - power variable

## Example
## Cubic root Example
```bash
nöff my_program

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
nöff my_program

nöf num1 = 16
nöf num2 = 2

niff $num1 > $num2 : slingshot possu1
nilf $num1 < $num2 : slingshot possu2
nilf $num1 == $num2 : slingshot possu3

pig possu1
oink "num1 is bigger than num2"
gip

pig possu2
oink "num1 is smaller than num2"
gip

pig possu3
oink "num1 is equal to num2"
gip

```
