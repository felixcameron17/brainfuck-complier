#brainfuck compiler

how does it work?

brianfuck is very simple. it only uses 8 different commands, and is in theory, albeit slow, turing complete

there are memory cells that exist, that can each store up to 8 bits of data

the commands are as follows:

> moves the cell pointer to the right
< moves the cell pointer to the left
+ increment the memory cell value by 1
- decrement the memory cell value by 1
. output the the memory cell that the pointer is on
, takes an input and overrides the current cell with the input
[ used to indicate the beginning of a loop, will jump to its corresponding ']' bracket if the cell selected is currently zero
] moves the pointer back to the open bracket as long as the memory cell selected doesnt equal zero. otherwise the loop is broken

any other text is treated as comment

see the code.bf file for a Hello World example. to test any code, paste it in the code.bf file and run the brainfuck.py file
the memory_adresses file will show the end result of the memory cells AFTER the program has run
