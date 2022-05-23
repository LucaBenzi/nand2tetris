from file_manager import FileManager
from syntax_checker import SyntaxChecker
from converter import Converter
from cleaner import *
import sys


def convert(filename):
    fm = FileManager(filename)
    lines = fm.file_to_string_list()
    lines = remove_comments(lines)
    lines = remove_escapes(lines)
    instructions = remove_whitespaces(lines)
    sc = SyntaxChecker(instructions)
    sc.check_source_code()  # Raise exception if asm code is not valid
    converter = Converter(instructions, sc)
    lines = converter.get_binary_code()
    fm.string_list_to_binary_file(lines)


if __name__ == '__main__':
    convert(sys.argv[1])
