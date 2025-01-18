# Overview
Mocha is a simple procedural programming language that has many different interpretors.

# Syntax
## Strings
Are defined by having double quotes at the start and end of the string:  
```
"This is a string!"
This is not a string :(
```
## Comments
To write comments in your program, there are 2 options:  
1. To start and end your comment with `/`. No matter where it is in the program, even in the middle of setting a variable name, it will work!   
You can also escape the `/` character using `\`.
2. Start a new line with a word that is not a recognized command: the line will get skipped. This is not recommended, however!

```
out "Hi\n" /prints out Hi to the screen/
out "He/test/llo\n"
The previous line would print out "Hello\n"
out "Hi \/ there\n" /Escapes the character, printing out "Hello / there"/
```
## Instantiation Lines
Lines that begin with "." are always run at the beginning of the program, in order of line.  
This is useful for defining where functions are placed, with functions typically being at the end of the file.  
It is also a good idea to have a variable to store where you jumped from, otherwise you would be stuck at the function. In this example, `goBack` is used.
```
.var lin coolFunctionName /This is run at the beginning of the file!/
out "This is pretty cool."
jmp goBack

.var lin otherFunction /This is run right after!/
out "Okay we get it"
jmp goBack
```
These lines are still able to be run when going through the program again.

# Commands
## `out`: Printing to the console
The `out` command takes one argument, being either a string or variable.  
A newline character is required at the end of the argument.  
```out "Hello world!\n"
out "How are you today?"
var str name set "John Smith"
out "Whats your name?\n"
out "Mine is "
out name
```
This code would print out to the terminal:
```Hello world!
How are you today?Whats your name?
Mine is John Smith
```
## `var`: Variables
The `var` command is the most versatile command in Mocha and is the backbone of the language.  
There are a couple variable types:  
1. Strings, `str`
2. Integers, `int`
3. Doubles, `dbl`
4. Arrays, `arr`
5. Booleans, `bln`  

There are also multiple methods to create or change a varible:
1. Opening files, `fil`
2. Getting a user input, `inp`
3. Changing the variable type, `typ`
4. Getting the current line, `lin`

