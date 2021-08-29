import sys
import readchar

filepath = sys.argv[1]

code = ''
with open(filepath, 'r') as f:
   code = f.read()

cells = [0]
program_ptr = 0
reader_ptr = 0

def find_next_bracket(left_index):
    count = 0
    for i in range(left_index, len(code)):
        if code[i] == '[':
            count += 1
        elif code[i] == ']':
            count -= 1
            if count == 0:
                return i

def find_prev_bracket(right_index):
    count = 0
    for i in range(right_index, -1, -1):
        if code[i] == ']':
            count += 1
        elif code[i] == '[':
            count -= 1
            if count == 0:
                return i

while reader_ptr < len(code):
    command = code[reader_ptr]
    if command == '>':
        program_ptr += 1
        if program_ptr >= len(cells):
            cells.append(0)
    elif command == '<':
        program_ptr -= 1
        
    elif command == '+':
        cells[program_ptr] += 1
    elif command == '-':
        cells[program_ptr] -= 1

    elif command == '.':
        char = chr(cells[program_ptr])
        sys.stdout.write(char)
    elif command == ',':
        char = readchar.readchar()
        cells[program_ptr] = ord(char)

    elif command == '[':
        if cells[program_ptr] == 0:
            reader_ptr = find_next_bracket(reader_ptr)
            continue
    elif command == ']':
        if cells[program_ptr] != 0:
            reader_ptr = find_prev_bracket(reader_ptr)
            continue

    reader_ptr += 1
