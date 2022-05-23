from os import popen
from maps import SEGMENT_MAP
from useful_scrpts import *
import sys


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


def main():
    vm_to_asm("StackTest.vm")

    # print(sys.argv[1])
    # vm_to_asm(sys.argv[1])


if __name__ == "__main__":
    main()
