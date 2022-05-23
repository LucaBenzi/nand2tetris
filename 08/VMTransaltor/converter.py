from source import Source
from typing import Dict, List
from argparse import Namespace
from file_manager import FileManager
from cleaner import *
from constant import *


class Converter(Source):
    def __init__(self, source:  List[str]):
        super().__init__(source)
        self.asm = []
        self.fm = FileManager(Namespace(directory_name="static/", file=None))
        self.jump = 0
        self.return_address = 0
        self.function_name = ""
        self.filename = "default"

    def get_asm_code(self):
        instructions = [i for i in self.instructions if i]
        for i in instructions:
            self.asm = self.asm + self.get_asm_vm_instruction(i)
        return self.asm

    def get_asm_vm_instruction(self, vm_instruction):
        """
        Converts a single vm instruction into the related asm code
        :return: list of string
        """
        instructions = []
        file_path_name = self.generate_file_path(vm_instruction)
        instructions_number = self.get_number_of_instructions(file_path_name)
        instructions.append(self.generate_comment(vm_instruction, instructions_number))
        # todo: pensare ad una funzione vm_to_asm_instruction che controlla se la funzione è call, function o altre.
        # se sono altre basta andare a prendere il file. Se è call o function bisogna impostare dei loop
        if vm_instruction['instruction'] not in ADVANCED_OPERATIONS:
            instructions = instructions + self.fm.file_to_string_list(file_path_name)
        else:
            instructions = instructions + self.get_asm_advanced_instruction(vm_instruction, file_path_name)
        instructions = self.set_jump_values(vm_instruction, instructions)
        instructions = self.set_instructions_values(vm_instruction, instructions)
        instructions = self.set_label_values(vm_instruction, instructions)
        instructions = self.set_return_addess_values(vm_instruction, instructions)
        instructions = self.set_filename_values(vm_instruction, instructions)
        instructions = remove_escapes(instructions)
        instructions = remove_tabulations(instructions)

        if vm_instruction['instruction'] == 'call':
            self.return_address = self.return_address + 1
        return instructions

    def get_asm_advanced_instruction(self, vm_instruction, file_path_name):
        self.function_name = vm_instruction['argument']
        self.filename = self.function_name.split('.')[0]
        file_lines = self.fm.file_to_string_list(file_path_name)
        file_lines.remove("[init]\n")
        file_lines.pop(0)
        init = []
        repeat = []
        init_repeat = True
        for f in file_lines:
            if f == "[repeat]\n":
                init_repeat = False
                continue
            if init_repeat:
                init.append(f)
            else:
                repeat.append(f)
        file_lines = init
        for i in range(0,int(vm_instruction['value'])):
            file_lines = file_lines + repeat
        return file_lines

    def generate_comment(self, instruction: Dict, get_number_of_instructions: int):
        return ("// " + str(instruction) + "--> " + str(get_number_of_instructions) + " lines")

    def get_number_of_instructions(self, path):
        with open("static/" + path, 'r') as fp:
            instructions = fp.readlines()
            instructions = remove_comments(instructions)
            instructions = remove_escapes(instructions)
            instructions = remove_tabulations(instructions)
            instructions = remove_blanklines(instructions)
            x = len(instructions)
        return x

    def generate_file_path(self, instruction: Dict):
        category = self.classify_instruction(instruction)
        path = category + "/"
        if instruction["instruction"] == "pop":
            path = path + "pop/"
        elif instruction["instruction"] == "push":
            path = path + "push/"
        if category == "stack":
            path = path + instruction["argument"]
        else:
            path = path + instruction["instruction"]
        path = path + ".asm"
        return path

    def set_jump_values(self,vm_instruction: Dict, instructions: List[str]):
        if 'instruction' in vm_instruction.keys():
            instructions = [s.replace('[jump]', str(self.jump)) for s in instructions]
        self.jump = self.jump + 1
        return instructions

    def set_instructions_values(self,vm_instruction: Dict, instructions: List[str]):
        if 'value' in vm_instruction.keys():
            instructions = [s.replace('[value]', vm_instruction['value']) for s in instructions]
        return instructions

    def set_label_values(self, vm_instruction: Dict, instructions: List[str]):
        if 'argument' in vm_instruction.keys():
            if vm_instruction['instruction'] == "function":
                instructions = [s.replace('[label]', vm_instruction['argument']) for s in instructions]
            elif vm_instruction['instruction'] == "call":
                instructions = [s.replace('[label]', vm_instruction['argument']) for s in instructions]
            else:
                instructions = [s.replace('[label]', self.function_name + "$" + vm_instruction['argument']) for s in instructions]
        return instructions

    def set_return_addess_values(self, vm_instruction: Dict, instructions: List[str]):
        if 'instruction' in vm_instruction.keys():
            return_address = self.function_name + "$" + str(self.return_address)
            instructions = [s.replace('[return_address]', return_address) for s in instructions]
        return instructions

    def set_filename_values(self, vm_instruction: Dict, instructions: List[str]):
        if 'instruction' in vm_instruction.keys():
            instructions = [s.replace('[filename]', self.filename) for s in instructions]
        return instructions