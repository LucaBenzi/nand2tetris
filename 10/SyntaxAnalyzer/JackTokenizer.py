import re
from Jack import *

class JackTokenizer:
    tokens = []
    content = ""
    filename = ""

    def __init__(self, filename):
        self.filename = filename
        self.tokens.append("<tokens>")
        jack_file = open(filename, "r")
        self.content = jack_file.read()
        self.__remove_single_line_comments()
        self.__remove_multiline_comments()
        self.__manage_double_quotes()
        self.__fix_symbols()
        self.__insert_keyword()
        self.__insert_symbol()
        self.__insert_string_constants()
        self.__insert_integer_constants()
        self.__insert_identifiers()
        self.tokens.append("</tokens>")
        jack_file.close()
        self.__save_tokens()

    def __remove_single_line_comments(self):
        # removes comments //
        comments = re.findall(r'//(.*)', self.content)
        comments.sort(key=len, reverse=True)  # sorts by descending length: ripetere nelle altre rimozioni
        for f in comments:
            self.content = self.content.replace("//" + f, " ")

    def __remove_multiline_comments(self):
        # removes comments /* */ also multiline
        comments = re.findall(r'/\*[\s\S]*?\*/', self.content)
        for c in comments:
            self.content = self.content.replace(c, " ")

    def __manage_double_quotes(self):
        double_quotes = re.findall(r'\"(.*)\"', self.content)
        for d in double_quotes:
            self.content = self.content.replace(d, d.replace(" ", "_"))

    def __fix_symbols(self):
        self.content = self.content.replace("\n", " ")
        self.content = self.content.replace("\t", " ")
        for s in symbols:
            self.content = self.content.replace(s, " " + s + " ")
        for c in self.content.split(" "):
            self.tokens.append(c)
        self.tokens = list(filter(None, self.tokens))

    def __insert_keyword(self):
        for i in range(0, len(self.tokens)):
            for w in keywords:
                if self.tokens[i] == w:
                    self.tokens[i] = "<keyword> " + w + " </keyword>"

    def __insert_symbol(self):
        for i in range(0, len(self.tokens)):
            for s in symbols:
                if self.tokens[i] == s:
                    if s == "<":
                        self.tokens[i] = "<symbol> " + '&lt;' + " </symbol>"
                    elif s == ">":
                        self.tokens[i] = "<symbol> " + '&gt;' + " </symbol>"
                    elif s == "&":
                        self.tokens[i] = "<symbol> " + '&amp;' + " </symbol>"
                    else:
                        self.tokens[i] = "<symbol> " + s + " </symbol>"

    def __insert_string_constants(self):
        # string constant
        for i in range(0, len(self.tokens)):
            if self.tokens[i][0] == '"' and self.tokens[i][-1] == '"':
                self.tokens[i] = "<stringConstant> " + self.tokens[i].replace('"', '').replace("_", ' ') + " </stringConstant>"

    def __insert_integer_constants(self):
        # integer constant
        for i in range(0, len(self.tokens)):
            if self.tokens[i].isnumeric():
                self.tokens[i] = "<integerConstant> " + self.tokens[i] + " </integerConstant>"

    def __insert_identifiers(self):
        for i in range(0, len(self.tokens)):
            if self.tokens[i][0] != '<' and self.tokens[i][-1] != '>':
                self.tokens[i] = "<identifier> " + self.tokens[i].replace('"', '').replace("_", ' ') + " </identifier>"

    def __save_tokens(self):
        with open(self.filename.split("/")[-1].replace(".jack","T.xml"), 'w') as fp:
            for item in self.tokens:
                fp.write("%s\n" % item)
