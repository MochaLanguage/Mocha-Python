# Overview
Mocha is a simple procedural programming language that has many different interpreters.

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
You can also add no argument to just print a newline.
```out "Hello world!\n"
out "How are you today?"
var str name set "John Smith"
out "Whats your name?\n"
out "Mine is "
out name
out
out "How do you do?"
```
This code would print out to the terminal:
```Hello world!
How are you today?Whats your name?
Mine is John Smith
How do you do?
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
### Strings
#### Methods
Setting: `set` to set a string, to either another variable or a string.  
Concatenating: `cct` to concatenate two strings or variables.  
Replacing: `rpl` to replace every instance of a substring in a string with another string.  
Getting length: `len` to get the length of a string.  
Substring: `sub` to get a substring of a string.
Lowercasing: `low` to lowercase a string.  
Uppercasing: `upp` to uppercase a string.
#### Example
```
var str firstName set "John "
var str lastName set "Doe"
var str fullName cct firstName lastName
out fullName
out "\n"
var str fullName rpl "John" "Jane"
out fullName
out "\n"
var str nameLength len firstName
out nameLength
out "\n"
var str greeting set "Hello there!"
var str greeting sub 1 5
out greeting
out "\n"
var str greeting set "Hello there!"
var str greeting low
out greeting
out "\n"
var str greeting upp
out greeting
out "\n"
```
would return:
```
John Doe
Jane Doe
5
ello
hello there!
HELLO THERE!
```
### Integers
#### Methods
Setting: `set` to set an integer to either another variable or new integer value.  
Addition: `add` to add a value to an integer.  
Subtraction: `sub` to subtract a value from an integer.  
Multiplication: `mlt` to multiply an integer by a value.  
Division: `div` to divide an integer by a value.  
Modulus: `mod` to get the remainder of an integer division.  
Power: `pow` to raise an integer to the power of a value.  
Random: `rng` to set an integer to a random value within a specified range.  

#### Example
```
var int number set 10
var int number add 5
var int number sub 3
var int number mlt 2
var int number div 4
var int number mod 3
var int number pow 2
var int randomNumber rng 1 100
out number
out "\n"
out randomNumber
out "\n"
```
would return:
```
16
(random number between 1 and 100)
```

### Doubles
#### Methods
Setting: `set` to set a double to either another variable or new double value.  
Addition: `add` to add a value to a double.  
Subtraction: `sub` to subtract a value from a double.  
Multiplication: `mlt` to multiply a double by a value.  
Division: `div` to divide a double by a value.  
Modulus: `mod` to get the remainder of a double division.  
Power: `pow` to raise a double to the power of a value.  
Round: `rnd` to round a double to the nearest integer.  

#### Example
```
var dbl number set 10.5
var dbl number add 5.2
out number
out "\n"
var dbl number sub 3.7
var dbl number mlt 2
var dbl number div 4
var dbl number pow 2
var dbl number rnd
out number
```
would return:
```
15.7
36
```

### Arrays
#### Methods
Setting: `set` to initialize an array with values.  
Inserting: `ins` to insert an element at a specific index.  
Appending: `app` to add an element to the end of the array.  
Popping: `pop` to remove an element at a specific index.  
Length: `len` to get the number of elements in the array.  
Getting: `get` to retrieve an element by index.  

#### Example
```
var arr colors set ["red" "green" "blue"]
var arr colors ins "yellow" 2
out colors
out "\n"
var arr colors app "purple"
var arr colors pop 1
out colors
out "\n"
var arr colorsLength len colors
var arr firstColor get colors 1
out colors
out "\n"
out colorsLength
out "\n"
out firstColor
out "\n"
```
would return:
```
['red', 'green', 'yellow', 'blue']
['red', 'yellow', 'blue', 'purple']
['red', 'yellow', 'blue', 'purple']
4
red
```
<sup>* Printing of arrays will change depending on the interpreter language.</sup>

### Booleans
#### Methods
String equality: `str eql` to check if two strings are equal.  
Numeric equality: `num eql` to check if two numbers are equal.  
Greater than: `num grt` to check if one number is greater than another.  
Less than: `num lss` to check if one number is less than another.  
Logical AND: `bln and` to perform a logical AND operation.  
Logical OR: `bln or` to perform a logical OR operation.  
Logical XOR: `bln xor` to perform a logical XOR operation.  
Logical NOT: `bln not` to perform a logical NOT operation.  

#### Example
```
var str firstName set "John"
var bln isSameName str eql firstName "John"
out isSameName
out ", they are the same name!\n"

var int number set 10
var bln isEqual num eql number 20
var bln isGreater num grt number 5
var bln isLess num lss number 5
out isEqual
out ", 10 and 20 are not equal!\n"
out isGreater
out ", 10 is greater than 5!\n"
out isLess
out ", 10 is not less than 5!\n"

var bln trueValue num eql 1 1
var bln falseValue num eql 1 2
var bln andResult bln and trueValue falseValue
var bln orResult bln or trueValue falseValue
var bln xorResult bln xor trueValue falseValue
var bln notResult bln not trueValue
out andResult
out "\n"
out orResult
out "\n"
out xorResult
out "\n"
out notResult
```
would return:
```
True, they are the same name!
False, 10 and 20 are not equal!
True, 10 is greater than 5!
False, 10 is not less than 5!
False
True
True
False
```
<sup>* Printing of booleans will change depending on the interpreter language.</sup>

### Opening Files
The `fil` method is used to read the contents of a file into a variable. The file contents are split into lines and stored as an array.

#### Example
```
var fil fileContents "example.txt"
var arr firstLine get fileContents 1
out firstLine
```
would return the first line of the file `example.txt`.

### Getting User Input
The `inp` method is used to get input from the user and store it in a variable.

#### Example
```
var inp userInput "Enter your name: "
out "Hello, "
out userInput
out "!"
```
would prompt the user to enter their name and then greet them.

### Type Changing
The `typ` method is used to change the type of a variable.

#### Example
```
var str numberStr set "123"
var typ numberStr int
var int number add numberStr 10
out number
```
would return:
```
133
```

### Line Getting
The `lin` method is used to get the current line number and store it in a variable.

#### Example
```
out "Hi there.\n"
var lin currentLine
out "Current line: "
out currentLine
```
would output the current line number.  
Assuming this is the start of the program:
```
Hi there.
Current line: 2
```
## `jmp`
The `jmp` command is used to jump to a specific line number or relative line number in the script.
```
out "This is the start.\n"
jmp +2
out "This will be skipped.\n"
out "This is after the jump.\n"
jmp 1
```
would output:
```
This is the start.
This is after the jump.
This is the start.
This is after the jump.
...
```
This will loop forever.

## `try`
The `try` command is used to conditionally jump to a specific line number if a boolean variable is true.

#### Example
```
var bln condition num eql 1 1
try 5 condition
out "This will be skipped if condition is true.\n"
out "This will also be skipped if condition is true.\n"
out "This will always be executed."
```
would output:
```
This will always be executed.
```

## `err`
The `err` command is used to handle errors by jumping to a specific line number if an error occurs.

#### Example
```
var int number set 10
err 5
var int result div number 0
out "This will be skipped if an error occurs.\n"
out "This will always be run."
```
would output:
```
This will always be run..
```
## `slp`
The `slp` command pauses the program for a certain amount of time.  
It takes one argument, an integer or variable, and pauses for that many milliseconds.
```
var int number set 0
var int number add 1
out number
out
slp 1000
jmp 2
```
would return a new number every second.