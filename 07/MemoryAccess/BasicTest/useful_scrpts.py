from re import T
from maps import *
from instruction_translator import Transaltor


file_format = ".vm"


def init_vm():
    init_code = []
    init_code.append("@256")
    init_code.append("D=A")
    init_code.append("@R0")
    init_code.append("M=D")
    return init_code


def is_not_blank(s):
    return bool(s and not s.isspace())


def remove_comments(lines):
    result = []
    for l in lines:
        result.append(l.split("//")[0])
    return result


def remove_while_lines(lines):
    result = []
    for l in lines:
        if is_not_blank(l):
            result.append(l)
    return result


def generate_file(lines):
    textfile = open("SimpleAdd.asm", "w")
    textfile.write(lines + "\n")
    textfile.close()


# porta il file in una lista di stringhe
def file_to_sting_list(file_name):
    print(file_format, file_name)
    if file_format in file_name:
        with open(file_name, "r") as grilled_cheese:
            lines = grilled_cheese.readlines()
            return lines
    else:
        raise Exception(f"file must be {file_format} format")


def remove_escapes(source_code):
    result = []
    for line in source_code:
        result.append(
            line.replace("\n", "").replace("\t", "").replace("\r", "").replace("\b", "")
        )
    return result


def check_instruciton_syntax(line):
    if line in STACK_INSTRUCTIONS and len(line) != 3:
        raise Exception("Wrong number of parameters in line")
    if line in MATH_INSTRUCTIONS and len(line) != 1:
        raise Exception("Wrong number of parameters in line")
    if (
        line[0] not in STACK_INSTRUCTIONS
        and line[0] not in MATH_INSTRUCTIONS
        and line[0] not in PROGRAM_FLOW_INSTRUCTIONS
        and line[0] not in FUNCTION_CALLING_INSTUCTIONS
    ):
        raise Exception("Unknown command line")


def get_instruction(source_line):
    """
    A VM instruction is a dict with 3 fields:
    operation [PUSH, POP or 9 Math aritmetic functions]
    segment [constant, tempo, argument, local,this, that, pointer, static]
    value
    returns a dict with this 3 fields compiled
    """
    # instruction control
    instruction = {}
    line = source_line.split(" ")
    check_instruciton_syntax(line)
    if line[0] in STACK_INSTRUCTIONS:
        instruction["command"] = line[0]
        instruction["segment"] = line[1]
        instruction["value"] = line[2]

    if line[0] in MATH_INSTRUCTIONS:
        instruction["command"] = line[0]
        instruction["segment"] = ""
        instruction["value"] = ""

    if line[0] in PROGRAM_FLOW_INSTRUCTIONS:
        instruction["command"] = line[0]
        instruction["location"] = line[1]

    if line[0] in FUNCTION_CALLING_INSTUCTIONS:
        pass

    return instruction


def translate_instruction(instruction, transaltor):
    if instruction["command"] == "pop":
        return transaltor.pop_to_asm(instruction)
    if instruction["command"] == "push":
        return transaltor.push_to_asm(instruction)
    if instruction["command"] == "add":
        return transaltor.add_to_asm(instruction)
    if instruction["command"] == "sub":
        return transaltor.sub_to_asm(instruction)
    if instruction["command"] == "and":
        return transaltor.and_to_asm(instruction)
    if instruction["command"] == "or":
        return transaltor.or_to_asm(instruction)
    if instruction["command"] == "neg":
        return transaltor.neg_to_asm(instruction)
    if instruction["command"] == "not":
        return transaltor.not_to_asm(instruction)
    if instruction["command"] == "eq":
        return transaltor.eq_to_asm(instruction)
    if instruction["command"] == "gt":
        return transaltor.gt_to_asm(instruction)
    if instruction["command"] == "lt":
        return transaltor.lt_to_asm(instruction)
    if instruction["command"] == "label":
        return transaltor.label_to_asm(instruction)
    if instruction["command"] == "if-goto":
        return transaltor.ifgoto_to_asm(instruction)
    if instruction["command"] == "goto":
        return transaltor.goto_to_asm(instruction)


def generate_file(lines, filename):
    textfile = open(filename.replace(".vm", ".asm"), "w")
    for element in lines:
        textfile.write(element + "\n")
    textfile.close()
