import sys

comp_table = {
    "0":  "0101010",
    "1":  "0111111",
    "-1": "0111010",
    "D":  "0001100",
    "A":  "0110000",
    "M":  "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1":"0011111",
    "A+1":"0110111",
    "M+1":"1110111",
    "D-1":"0001110",
    "A-1":"0110010",
    "M-1":"1110010",
    "D+A":"0000010",
    "D+M":"1000010",
    "D-A":"0010011",
    "D-M":"1010011",
    "A-D":"0000111",
    "M-D":"1000111",
    "D&A":"0000000",
    "D&M":"1000000",
    "D|A":"0010101",
    "D|M":"1010101"
}

dest_table = {
    "":   "000",
    "M":  "001",
    "D":  "010",
    "MD": "011",
    "A":  "100",
    "AM": "101",
    "AD": "110",
    "AMD":"111"
}

jump_table = {
    "":   "000",
    "JGT":"001",
    "JEQ":"010",
    "JGE":"011",
    "JLT":"100",
    "JNE":"101",
    "JLE":"110",
    "JMP":"111"
}

command_list = []
symbol_table = {}
symbol_count = 0

def convert_to_binary(number):
    return format(int(number), 'b').zfill(16)

def parse_a_instruction(instruction):
    symbol = instruction.split("@")[1] # @R0 -> R0 in order to look up in symbol table
    if symbol in symbol_table:
        command_list.append(convert_to_binary(symbol_table[symbol]))
        return
    # Not in symbol table so either @3 or @i symbol. If @i then want to add to symbol table
    if not symbol.isnumeric():
        global symbol_count
        symbol_table[symbol] = symbol_count + 16
        # command_list.append(convert_to_binary(symbol_table[symbol]))
        symbol_count += 1
        return
    register = int(instruction.rsplit("@")[1]) # Get register number to convert to binary#
    register_binary = convert_to_binary(register)
    command_list.append(register_binary)

def parse_c_instruction(instruction):
    comp_command, dest_command, jump_command = "", "", ""
    jump_next = False

    for char in instruction:
        if char == " ":
            break # Some lines have a C instruction and then comment, we want to ignore that
        if jump_next:
            jump_command += char
        elif char == "=":
            dest_command = comp_command
            comp_command = ""
        elif char == ";":
            jump_next = True
        else:
            comp_command += char
    
    try:
        comp = comp_table[comp_command]
    except:
        print(f"{comp_command} is not a valid comp value")
    try:
        dest = dest_table[dest_command]
    except:
        print(f"{dest_command} is not a valid dest value")
    try:
        jump = jump_table[jump_command]
    except:
        print(f"{jump_command} is not a valid jump value")

    command_list.append(f"111{comp}{dest}{jump}")

def parse_file(input_file):
    for line in input_file.readlines():
        line = line.strip()
        if line == "" or line[0] == "/": # Is a comment
            continue
        elif line[0] == "(": # Is a symbol - already done in first pass
            continue
        elif line[0] == "@":
            parse_a_instruction(line)
        else:
            parse_c_instruction(line)

def initialise_symbol_table():
    # Initialise symbol table with predefined symbols
    symbol_table = {
        "SCREEN": 16384,
        "KBD": 24576,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS":3,
        "THAT":4
    }

    for i in range(16):
        symbol_table[f"R{i}"] = i
    
    return symbol_table

def first_pass(input_file):
    count = 0
    for line in input_file.readlines():
        count += 1
        line = line.strip()
        if line == "":
            continue
        if line[0] == "(": # Is a symbol
            symbol_table[line] = count + 1

if __name__ == "__main__":
    symbol_table = initialise_symbol_table()

    file = sys.argv[1]
    if file is None:
        print("Must pass in a .asm input file")
    # parse the file
    with open(file, 'r') as input_file:
        first_pass(input_file)
        input_file.seek(0)
        result = parse_file(input_file)
    with open(f'{file.split(".")[0]}.hack', 'w') as output_file:
        for line in command_list:
            output_file.write(line + "\n")
    print(symbol_table)