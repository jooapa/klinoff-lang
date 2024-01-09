# klinoff-lang

## Introduction
klinoff-lang is a huge step in the evolution of programming languages. It is a language that is easy to learn and use, but really powerful.

Klinoff-lang is a interpreted language, one known interpreter is found on this repository.

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
To start a klinoff-lang file, you need to use the `nöff` keyword. This keyword is used to start the program, and follows the name of the program.

```bash
nöff my_program
```

### Variables
Variables are used to store data. Variables can be created by using the `nöf` keyword. 
```bash
nöf variable value
```

```bash
nöf number 5
nöf word Hello World!
```

### Comments
Comments are used to explain the code. Comments are ignored by the compiler. Comments can be created by using the `//` character.

```c
// This is a comment

//this doesnt work
```

### Printing
Printing is used to print text to the console. Printing can be done by using the `oink` keyword.

```bash
oink "Hello World!"
// Prints "Hello World!" to the console
```
```bash
nöf word best
nöf variable klinoff-lang is the $word language

oink variable
// Prints "klinoff-lang is the best language" to the console
```

### If statements
If statements can be created by using the `niff` keyword. 
Else statements can be created by using the `niffel` keyword. 
Else if statements can be created by using the `nilf` keyword. 


```bash
nöf x 5
nöf y 3

niff x == y {
    oink "$x is equal to $y"
} nilf x > y {
    oink "$x is greater than $y"
} niffel {
    oink "$x is less than $y"
}
```

### for loops
For loops can be created by using the `nör` keyword. and the second parameter is the times the loop will run.

```bash
nör 5 {
    oink("Hello World!")
}
```

### Operators
- `+` - addition
- `-` - subtraction
- `*` - multiplication
- `/` - division
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
- `niffel` - else statement
- `nilf` - else if statement
- `nör` - for loop

