# initialize variables
f = open('code.bf', 'r')
code = f.read()

memory = [0]
memory_ptr = 0

user_input = []

# get all bracket locations ahead of time
loop_table = {}
loop_stack = []
for ptr, instruction in enumerate(code):
    if instruction == '[':
        loop_stack.append(ptr)
    elif instruction == ']':
        loop_beginning_index = loop_stack.pop()
        loop_table[loop_beginning_index] = ptr
        loop_table[ptr] = loop_beginning_index

# begin loop
ptr = 0
while ptr < len(code):
    instruction = code[ptr]

    # add 1 to the current memory cell
    if instruction == '+':
        memory[memory_ptr] += 1
        if memory[memory_ptr] == 256:
            memory[memory_ptr] = 0

    # subtract 1 to the current memory cell
    elif instruction == '-':
        memory[memory_ptr] -= 1
        if memory[memory_ptr] == -1:
            memory[memory_ptr] = 255

    # move the memory pointer back 1
    elif instruction == '<':
        memory_ptr -= 1

    # move the memory pointer forward 1
    elif instruction == '>':
        memory_ptr += 1
        if memory_ptr == len(memory):
            memory.append(0)

    # print memory cell into ascii
    elif instruction == '.':
        print(chr(memory[memory_ptr]), end='')

    # convert ascii input into 8 bit value
    elif instruction == ',':
        if user_input == []:
            user_input = list(input() + '\n')
        memory[memory_ptr] = ord(user_input.pop(0)) % 256

    # start loop
    elif instruction == '[':
        if not memory[memory_ptr]:
            ptr = loop_table[ptr]

    # end loop
    elif instruction == ']':
        if memory[memory_ptr]:
            ptr = loop_table[ptr]

    # move pointer over 1
    ptr += 1

memory_final = ''

for cell in memory:
    memory_final = memory_final + '[ ' + str(cell) + ' ] '

f = open('memory_adresses.txt', 'w')
f.write(memory_final)
f.close()
