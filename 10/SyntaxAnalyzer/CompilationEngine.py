class CompilationEngine:

    def __init__(self, filename):
        self.filename = filename
        xml_file = open(filename, "r")
        self.filename = self.filename.replace("T.xml", ".xml").split("/")[-1]
        self.tokens = xml_file.readlines()  # source torkens
        self.tree = []  # destination tokens
        self.index = 0
        self.current_token = ""

    def __list_to_file__(self):
        with open(self.filename, 'w') as f:
            self.tree = [elem.replace("\n", '') for elem in self.tree]
            for item in self.tree:
                f.write("%s\n" % item)

    def __advance__(self):
        self.index = self.index + 1
        self.current_token = self.tokens[self.index]

    def compile(self):
        self.__advance__()
        self.compile_class()
        print(self.tokens)

    def process(self, word):
        if word in self.current_token:
            self.tree.append(self.current_token)
            self.__advance__()
        else:
            raise BaseException("Syntax error at token " + self.current_token)

    def process_identifier(self, word):
        if "identifier" in word:
            self.tree.append(self.current_token)
            self.__advance__()
        else:
            raise BaseException("Syntax error at token " + self.current_token)

    def process_type(self, word):
        if "int" in word or "char" in word or "boolean" in word:
            self.tree.append(self.current_token)
            self.__advance__()
        elif "identifier" in word:
            self.process_identifier(word)
        else:
            raise BaseException("Syntax error at token " + self.current_token)

    def process_multiple_vars(self):
        if "," in self.current_token:
            self.process(",")
            self.process_identifier(self.current_token)
            self.process_multiple_vars()

    def process_multiple_vars_and_types(self):
        if "," in self.current_token:
            self.process(",")
            self.process_type(self.current_token)
            self.process_identifier(self.current_token)
            self.process_multiple_vars_and_types()

    def compile_var_dec(self):
        if "static" in self.current_token or "field" in self.current_token:
            self.tree.append("<classVarDec>")
            if "static" in self.current_token:
                self.process("static")
            elif "field" in self.current_token:
                self.process("field")
            self.process_type(self.current_token)
            self.process_identifier(self.current_token)
            self.process_multiple_vars() # (, varName)*
            self.process(";")
            self.tree.append("</classVarDec>")
            self.compile_var_dec()

    def compile_parameterList(self):
        self.tree.append("<parameterList>")
        if ")" not in self.current_token:
            self.process_type(self.current_token)
            self.process_identifier(self.current_token)
            self.process_multiple_vars_and_types()
        self.tree.append("</parameterList>")

    def compile_subroutine_dec(self):
        """
        ('constructor'|'function'|'method') ('void'|type)subroutineName'('parameterList')'subroutineBody
        :return:
        """
        if "constructor" in self.current_token or "method" in self.current_token or "function" in self.current_token:
            self.tree.append("<subroutineDec>")
            # ('constructor'|'function'|'method')
            if "constructor" in self.current_token:
                self.process("constructor")
            elif "method" in self.current_token:
                self.process("method")
            elif "function" in self.current_token:
                self.process("function")
            if "void" in self.current_token:
                self.process("void")
            # ('void' | type)
            else:
                self.process_type(self.current_token)
            # subroutineName
            self.process_identifier(self.current_token)
            # '('parameterList')'
            self.process("(")
            self.compile_parameterList()
            self.process(")")
            self.tree.append("</subroutineDec>")
            self.compile_subroutine_dec()
            # todo: subroutineBody

    def compile_class(self):
        # scrivere class
        self.tree.append("<class>")
        self.process("class")
        self.process_identifier(self.tokens[self.index])
        self.process("{")
        self.compile_var_dec()
        self.compile_subroutine_dec()
        # self.process("}")
        self.tree.append("</class>")
        self.__list_to_file__()





