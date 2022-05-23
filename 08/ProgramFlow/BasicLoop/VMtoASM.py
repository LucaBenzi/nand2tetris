from maps import SEGMENT_MAP
from useful_scrpts import *
import sys
import os


def vm_to_asm(filename):
    t = Transaltor()
    asm_code = []
    asm_code = t.init_vm()

    source_code = file_to_sting_list(filename)
    source_code = remove_comments(source_code)
    source_code = remove_while_lines(source_code)
    source_code = remove_escapes(source_code)

    for line in source_code:
        vm_instruction = get_instruction(line)
        asm_instruction = translate_instruction(vm_instruction, t)
        asm_code = asm_code + asm_instruction

    generate_file(asm_code, filename)
    print(asm_code)
    return asm_code


def main():
    asm_code = []
    file_list = os.listdir(sys.argv[1])
    if "Sys.vm" not in file_list:
        raise Exception("No Sys.vm file")
    asm_code.append(vm_to_asm("Sys.vm"))  # deve essere una directory
    file_list.pop("Sys.vm")
    for file in file_list:
        asm_code.append(vm_to_asm(file))
    # vm_to_asm("FibonacciSeries.vm")
    generate_file(asm_code, file_list[0])


if __name__ == "__main__":
    main()
