import os
from time import sleep

# variables
f = open('code.bf', 'r')
bf_code = f.read()

pointer = -1
memory = [0]
memory_pointer = 0
open_bracket_pointers = [0]
print_text = ''

debug = True


while pointer < len(bf_code) - 1:

    os.system('cls')
    pointer += 1

    if bf_code[pointer] == ']' and len(open_bracket_pointers) != 0:
        if memory[memory_pointer] == 0:
            open_bracket_pointers.pop()

        else:
            pointer = open_bracket_pointers[-1]

    elif bf_code[pointer] == '[':
        if len(open_bracket_pointers) < 1:
            open_bracket_pointers.append(pointer)

        elif open_bracket_pointers[-1] != pointer:
            open_bracket_pointers.append(pointer)

    elif bf_code[pointer] == '>':
        memory_pointer += 1

    elif bf_code[pointer] == '<':
        memory_pointer -= 1

    elif bf_code[pointer] == '+' and memory_pointer > -1:
        memory[memory_pointer] += 1

        while memory[memory_pointer] > 255:
            memory[memory_pointer] -= 256

    elif bf_code[pointer] == '-' and memory_pointer > -1:
        memory[memory_pointer] -= 1

        while memory[memory_pointer] == -1:
            memory[memory_pointer] += 256

    elif bf_code[pointer] == '.':
        print_text += chr(memory[memory_pointer])
        os.system('cls')
        print(print_text)

    elif bf_code[pointer] == ',':
        os.system('cls')
        print(print_text + '\n')

        try:
            comma_input = input('input: ')[0]
            memory[memory_pointer] = ord(comma_input)

        except:
            comma_input = 0
            memory[memory_pointer] = 0

    if memory_pointer > len(memory) - 1:
        memory.append(0)

    print(print_text)

    if debug == True:

        print('\nPointer: ' + str(pointer))
        print('Reading: ' + bf_code[pointer])
        print('Memory Pointer: ' + str(memory_pointer))
        print('Memory Value: ' + str(memory[memory_pointer]))
        print('Percentage:' + str(round(pointer / len(bf_code) * 100, 2)) + '%')
        os.system('cls')
        # sleep(0.01)

os.system('cls')
print('\nPointer: ' + str(pointer))
print('Reading: ' + bf_code[pointer])
print('Memory Pointer: ' + str(memory_pointer))
print('Memory Value: ' + str(memory[memory_pointer]))
print('Percentage: ' + str(round(pointer / len(bf_code) * 100, 2)) + '%')
print('\n\n' + print_text)


memory_final = ''

for cell in memory:
    memory_final = memory_final + '[ ' + str(cell) + ' ] '

f = open('memory_adresses.txt', 'w')
f.write(memory_final)
f.close()
