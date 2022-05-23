# todo: al momento in caso di errori i riferimenti alle righe non sono corretti
# perché viene fatto riferimento alla riga avendo tolto commenti e spazi vuoi
# solution: mettere il file in una lista globale, fare una ricerca e stampare il relativo numero di riga

import sys

SYMBOL_TABLE = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
}

A_FIELD_MAP = {"0": "0"}  # capire come settarlo a zero o a 1

C_FIELD_MAP = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "D+A": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "D&A": "000000",
    "D|A": "010101",
    "M": "110000",
    "!M": "110001",
    "-M": "110011",
    "M+1": "110111",
    "M-1": "110010",
    "D+M": "000010",
    "D-M": "010011",
    "M-D": "000111",
    "D&M": "000000",
    "D|M": "010101",
}

D_FIELD_MAP = {
    "null": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

J_FIELD_MAP = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

ALLOWED_SYMBOLS = ["M", "D", "A"]

ALLOWED_DIGITS = "0123456789"
ALLOWED_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtsuvwxyz"
ALLOWED_EXTRAS = "_.$:"

# porta il file in una lista di stringhe
def file_to_sting_list(file_name):
    if ".asm" in file_name:
        with open(file_name, "r") as grilled_cheese:
            lines = grilled_cheese.readlines()
            return lines
    else:
        raise Exception("file must be .asm format")


def remove_comments(lines):
    result = []
    for l in lines:
        result.append(l.split("//")[0])
    return result


def remove_whitespaces(lines):
    result = []
    for l in lines:
        if l.replace(" ", "").replace("\n", "") != "":
            result.append(l.replace(" ", "").replace("\n", ""))
    return result


def check_reference_syntax(line):
    l = line.replace("(", "").replace(")", "").replace("@", "")
    line = line + "\n"
    if l[0] in ALLOWED_DIGITS:
        raise Exception(
            f"ERROR at line {ORIGINAL_FILE.index(line)}: Label cannot start with number"
        )
    for i in range(1, len(l)):
        if (
            l[i] not in ALLOWED_DIGITS
            and l[i] not in ALLOWED_EXTRAS
            and l[i] not in ALLOWED_LETTERS
        ):
            raise Exception(
                f"ERROR: charcater '{l[i]}' not allowed at line {ORIGINAL_FILE.index(line)}"
            )


def update_symbol_table(lines):
    ram = 16
    rom = 0

    # prima cercare i salti i rom, poi le variabili
    # aggiungere solo se necessario (controllare la SYMBOL_TABLE)
    for l in lines:
        if l[0] == "(":
            check_reference_syntax(l)
            l = l.replace("(", "").replace(")", "")
            if l not in SYMBOL_TABLE.keys():
                SYMBOL_TABLE[l] = rom
                rom = rom - 1
        rom = rom + 1

    # Adesso cercare le variabili
    for l in lines:
        if l[0] == "@" and not l.replace("@", "").isnumeric():
            check_reference_syntax(l)
            l = l.replace("@", "")
            if l not in SYMBOL_TABLE.keys():
                SYMBOL_TABLE[l] = ram
                ram = ram + 1


def replace_symbols(lines):
    # rimuove le righe con i riferimenti
    newlist = [x for x in lines if not x.startswith("(")]
    count = 0
    for n in newlist:
        if n[0] == "@":
            if not n.split("@")[1].isnumeric():
                ref = SYMBOL_TABLE[n.split("@")[1]]
                newlist[count] = "@" + str(ref)
        count = count + 1
    return newlist


# traduci istruzioni A
def transalte_a_instructions(lines):
    count = 0
    for l in lines:
        if l[0] == "@":
            lines[count] = "{0:016b}".format(int(l[1:]))
        count = count + 1
    return lines


def get_instructions_operators(instruction):
    # dest=comp;jump
    comp = "0"
    destination = "null"
    jump = "null"
    a = "0"
    if "=" in instruction:
        destination = instruction.split("=")[0]
        comp = instruction.split("=")[1]
    if ";" in instruction:
        comp = instruction.split(";")[0]
        jump = instruction.split(";")[1]

    if "M" in comp:
        a = "1"
    return destination, comp, jump, a


def check_c_operands(destination, comp, jump, instruction):
    original = remove_whitespaces(ORIGINAL_FILE)
    if destination not in D_FIELD_MAP:
        raise Exception(
            f"Error at line {original.index(instruction)}: destination {destination} not valid"
        )
    if comp not in C_FIELD_MAP:
        raise Exception(
            f"Error at line {original.index(instruction)}: operation {comp} not valid"
        )
    if jump not in J_FIELD_MAP:
        raise Exception(
            f"Error at line {original.index(instruction)}: jump {jump} not valid"
        )


def transalte_c_instructions(lines):
    # dest=operation;jump
    count = 0
    for l in lines:
        if "=" in l or ";" in l:
            destination, comp, jump, a = get_instructions_operators(l)
            check_c_operands(destination, comp, jump, l)
            instruction = (
                "111"
                + a
                + C_FIELD_MAP[comp]
                + D_FIELD_MAP[destination]
                + J_FIELD_MAP[jump]
            )
            lines[count] = instruction
        count = count + 1
    return lines


def generate_file(lines, filename):
    textfile = open(filename.replace(".asm", ".hack"), "w")
    for element in lines:
        textfile.write(element + "\n")
    textfile.close()


def main():
    try:
        # lines = file_to_sting_list(sys.argv[0])
        lines = file_to_sting_list("Mult.asm")
        lines = remove_comments(lines)
        lines = remove_whitespaces(lines)
        update_symbol_table(lines)
        lines = replace_symbols(lines)
        lines = transalte_a_instructions(lines)
        lines = transalte_c_instructions(lines)
        generate_file(lines, sys.argv[0])
        print(lines)
    except Exception as err:
        print(err)


ORIGINAL_FILE = file_to_sting_list("Mult.asm")
main()
