
# Build My Own wc tool

This challenge is provided by [John Crickett ](https://www.linkedin.com/in/johncrickett/)


The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.

Language used : Python




## Features

This tool counts the total bytes, total lines, total words, and total characters of a given file. Also read from standard input if no filename is specified
Command line option for
- total bytes : **-c**
- total lines : **-l**
- total words : **-w**
- total characters : **-m**


## How to run

- run : ```python <python filename> <option> <text file>```
- for stdin : ```cat <file name> | python <python filename> <option>```