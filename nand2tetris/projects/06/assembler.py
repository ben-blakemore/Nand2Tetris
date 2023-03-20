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
    "D|A":"0010101"
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

def parse_a_instruction(instruction):
    register = int(instruction.rsplit("@")[1]) # Get register number to convert to binary
    register_binary = format(register, 'b').zfill(15)
    command_list.append("0" + register_binary)

def parse_c_instruction(instruction):
    instruction_split = instruction.split("=")
    dest = instruction_split[0]
    comp = instruction_split[1]
    binary = "111"
    return "binary"

def parse_file(input_file):
    for line in input_file.readlines():
        if line[0] == "/" or line[0] == "\n": # Is a comment
            continue
        if line[0] == "@":
            parse_a_instruction(line.strip())
        else:
            parse_c_instruction(line.strip())

if __name__ == "__main__":
    file = sys.argv[1]
    if file is None:
        print("Must pass in a .asm input file")
    # parse the file
    with open(file, 'r') as input_file:
        result = parse_file(input_file)