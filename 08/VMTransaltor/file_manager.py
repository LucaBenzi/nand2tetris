from typing import List
from argparse import Namespace
import os
from cleaner import *

# test directory option with command: python main.py ..\FunctionCalls\FibonacciElement\
# test file option with command: python main.py --file ..\ProgramFlow\BasicLoop\BasicLoop.vm


class FileManager:
    def __init__(self, args: Namespace):
        self.directory = args.directory_name # None if file is provided
        self.file_name = args.file # None if directory is provided
        self.use_directory = False
        self.source = []
        self.file_list = []
        if self.directory is not None:
            self.use_directory = True
        else:
            self.directory = self.file_name
            self.file_name = self.file_name.split('\\')[-1]
            self.directory = self.directory.replace(self.file_name,'')

    def get_instructions_list(self):
        if self.use_directory:
            return self.file_list_to_instructions()
        else:
            return self.file_to_string_list(self.file_name)

    def check_sys_file(self):
        for f in os.listdir(self.directory):
            if f.endswith(".vm"):
                self.file_list.append(f)
        if "Sys.vm" not in self.file_list:
            raise Exception("No Sys.vm file")

    def file_list_to_instructions(self):
        self.source = self.file_to_string_list("Sys.vm")
        for f in self.file_list:
            if f != "Sys.vm":
                self.source = self.source + self.file_to_string_list(f)
        return self.source

    def file_to_string_list(self, filename):
        with open(self.directory + filename, "r") as instruction_file:
            lines = instruction_file.readlines()
        return lines

    def string_list_to_binary_file(self, binary_instructions: List[str]):
        if self.use_directory:
            outfile = self.directory + self.directory.split("\\")[-2] + ".asm"
        else:
            outfile = self.directory + self.file_name.replace(".vm",".asm")
        text_file = open(outfile, "w")
        for instruction in binary_instructions:
            text_file.write(instruction + "\n")
        text_file.close()
