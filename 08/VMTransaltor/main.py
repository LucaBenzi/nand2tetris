from file_manager import FileManager
from syntax_checker import SyntaxChecker
from converter import Converter
from cleaner import *
import argparse


def convert(arguments):
    fm = FileManager(arguments)
    fm.check_sys_file() if fm.use_directory else ""
    lines = fm.get_instructions_list()
    lines = remove_comments(lines)
    lines = remove_escapes(lines)
    lines = remove_tabulations(lines)
    sc = SyntaxChecker(lines)
    sc.check_source_code()
    converter = Converter(lines)
    asm_code = converter.get_asm_code()
    fm.string_list_to_binary_file(asm_code)


if __name__ == '__main__':
    parserDescription = """Use --file filename.vm to convert a single file,
    provide a directory to convert multiple files (Sys.vm file required)"""

    parser = argparse.ArgumentParser(description=parserDescription)
    # Optional argument
    parser.add_argument('--file', type=str, help='Provide filename.vm')
    # Optional positional argument
    parser.add_argument('directory_name', type=str, nargs='?', help='Provide directory name')
    args = parser.parse_args()
    convert(args)