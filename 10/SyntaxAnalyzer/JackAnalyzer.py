import argparse
import os
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine

parserDescription = """Provide a single .jack file or an entire directory"""
parser = argparse.ArgumentParser(description=parserDescription)
parser.add_argument('dir', type=str, nargs='?', help='Provide .jack file or directory')
args = parser.parse_args()
print(args.dir)

file_list = []
if ".jack" in args.dir:
    file_list.append(args.dir)
else:
    for f in os.listdir(args.dir):
        if f.endswith(".jack"):
            file_list.append(args.dir+"/"+f)
print(file_list)



for f in file_list:
    tokenizer = JackTokenizer(f)
    compiler = CompilationEngine(f.split('/')[-1].replace(".jack","T.xml"))
    compiler.compile()
