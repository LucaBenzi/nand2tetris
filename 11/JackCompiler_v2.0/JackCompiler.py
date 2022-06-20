import argparse
import os
from ParserException import ParserException
from TokenizerException import TokenizerException
from CompilationEngine import CompilationEngine


def is_directory(args):
    if ".jack" in args:
        return False
    return True


def get_files():
    parserDescription = """Provide a single .jack file or an entire directory"""
    parser = argparse.ArgumentParser(description=parserDescription)
    parser.add_argument('dir', type=str, nargs='?', help='Provide .jack file or directory')
    args = parser.parse_args()
    file_list = []
    # print("Using path: " + os.getcwd() + '   /' + args.dir)
    if is_directory(args.dir):
        for f in os.listdir(args.dir):
            if f.endswith(".jack"):
                file_list.append(args.dir + "/" + f)
    else:
        file_list.append(args.dir)
    return file_list


def compile(file):
    print("[Compiling] " + file)
    try:
        engine = CompilationEngine(file)
        print(engine.get_file_name())
    except ParserException as e:
        # cancellare il codice scritto
        print("[Parsing Error] Line " + str(e.get_line()) + ": " + e.message())
    except TokenizerException as e:
        # cancellare il codice scritto
        print("[Tokenizer Error] Line " + str(e.get_line()) + ": " + e.message())



def main():
    file_list = get_files()
    print("File to compile: ")
    print(file_list)
    for f in file_list:
        compile(f)


if __name__ == "__main__":
    main()