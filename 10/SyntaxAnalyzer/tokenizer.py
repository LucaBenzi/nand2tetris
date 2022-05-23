from typing import List
import re
import argparse
import os
"""
This module takes in input a .jack file, provides as output a .xml file
with the list of tokens.
"""

"""
todo:
- buttare i \n \t \r
- eliminare commenti // /* /**
- gestire le virgolette (da capire come fare: utilizzo di una mappa)?
- sostituire i caratteri con carattere - spazio - carattere

"""

parserDescription = """Provide a single .jack file or an entire directory"""
parser = argparse.ArgumentParser(description=parserDescription)
parser.add_argument('dir', type=str, nargs='?', help='Provide .jack file or directory')
args = parser.parse_args()
print(args.dir)

symbols = ["{","}","(",")","[","]",".",",",";","+","-","*","/","&","|",">","<","=","~"]
keywords = ["class", "constructor", "function", "method", "field", "static", "var", "int", "char", "boolean", "void", "true", "false", "null", "this", "let", "do", "if", "else", "while", "return"]
# fare il dizionario del tipo di token


# def remove_escapes(content: List[str]):
#     # buttare i \n \t
#     c = [s.replace("\n", " ") for s in content]
#     return [s.replace("\t", " ") for s in c]

file_list = []
if ".jack" in args.dir:
    file_list.append(args.dir)
else:
    for f in os.listdir(args.dir):
        if f.endswith(".jack"):
            file_list.append(args.dir+"/"+f)
print(file_list)


def tokenizeSource(filename):
    str_list = []
    str_list.append("<tokens>")


    jack_file = open(filename, "r")
    content = jack_file.read()

    # toglie commenti //
    comments = re.findall(r'//(.*)', content)
    comments.sort(key=len, reverse=True) # sorts by descending length: ripetere nelle altre rimozioni
    for f in comments:
           content = content.replace("//" + f," ")
    # content = content.replace("//"," ")
    # toglie commenti /* */ multiriga
    comments = re.findall(r'/\*[\s\S]*?\*/', content)
    for c in comments:
        content = content.replace(c," ")

    # \"(.*)\"

    double_quotes = re.findall(r'\"(.*)\"', content)
    for d in double_quotes:
        content = content.replace(d,d.replace(" ", "_"))

    content = content.replace("\n", " ")
    content = content.replace("\t", " ")
    for s in symbols:
        content = content.replace(s, " " + s + " ")
    for c in content.split(" "):
        str_list.append(c)
    str_list = list(filter(None, str_list))


    for i in range(0,len(str_list)):
        for w in keywords:
            if str_list[i] == w:
                str_list[i] = "<keyword> " + w + " </keyword>"

    for i in range(0,len(str_list)):
        for s in symbols:
            if str_list[i] == s:
                if s == "<":
                    str_list[i] = "<symbol> " + '&lt;' + " </symbol>"
                elif s == ">":
                    str_list[i] = "<symbol> " + '&gt;' + " </symbol>"
                elif s == "&":
                    str_list[i] = "<symbol> " + '&amp;' + " </symbol>"
                else:
                    str_list[i] = "<symbol> " + s + " </symbol>"

    # string constant
    for i in range(0,len(str_list)):
        if str_list[i][0] == '"' and str_list[i][-1] == '"':
            str_list[i] = "<stringConstant> " + str_list[i].replace('"','').replace("_",' ') + " </stringConstant>"
    #integer constant
    for i in range(0,len(str_list)):
        if str_list[i].isnumeric():
            str_list[i] = "<integerConstant> " + str_list[i] + " </integerConstant>"

    for i in range(0,len(str_list)):
        if str_list[i][0] != '<' and str_list[i][-1] != '>':
            str_list[i] = "<identifier> " + str_list[i].replace('"','').replace("_",' ') + " </identifier>"

    str_list.append("</tokens>")
    print(str_list)
    jack_file.close()

    with open(filename.split("/")[-1].replace(".jack","T.xml"), 'w') as fp:
        for item in str_list:
            fp.write("%s\n" % item)


for f in file_list:
    tokenizeSource(f)