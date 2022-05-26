from Jack import op, unaryOp, statements
import re

def list_of_symbols_in_string(lista, token):
    token = re.findall(r'> (.*) <', token)[0]
    for o in lista:
        if o in token:
            return o
    return False


class CompilationEngine:

    def __init__(self, filename):
        self.filename = filename
        xml_file = open(filename, "r")
        self.filename = self.filename.replace("T.xml", ".xml").split("/")[-1]
        self.tokens = xml_file.readlines()  # source torkens
        self.tree = []  # destination tokens
        self.index = 0
        self.current_token = ""

    def look_ahead(self):
        return self.tokens[self.index+1]

    def type_of_identifier(self):
        # variable array subroutineCall
        if "identifier" in self.current_token:
            if "[" in self.look_ahead():
                return "array"
            if "("  in self.look_ahead() or "." in self.look_ahead():
                return "subroutineCall"
            else:
                return "variable"
        return ""


    def __list_to_file__(self):
        with open(self.filename, 'w') as f:
            self.tree = [elem.replace("\n", '') for elem in self.tree]
            for item in self.tree:
                f.write("%s\n" % item)

    def __advance__(self):
        self.index = self.index + 1
        self.current_token = self.tokens[self.index]

    def process(self, word):
        if word == '/':
            word = " / "
        if word in self.current_token:
            self.tree.append(self.current_token)
            self.__advance__()
        else:
            raise BaseException(f"{self.filename}: Syntax error at line {self.index}, expected: {word}, found {self.current_token}")

    def process_type(self, word):
        if "int" in word or "char" in word or "boolean" in word:
            self.process(word)
        else:
            self.process("identifier")

    def process_multiple_vars(self):
        if "," in self.current_token:
            self.process(",")
            self.process("identifier")
            self.process_multiple_vars()

    def process_multiple_vars_and_types(self):
        if "," in self.current_token:
            self.process(",")
            self.process_type(self.current_token)
            self.process("identifier")
            self.process_multiple_vars_and_types()


    def process_statement(self):
        if 'let' in self.current_token or "if" in self.current_token or "while" in self.current_token or "do" in self.current_token or "return" in self.current_token:
            if 'let' in self.current_token:
                self.compile_let_statement()
            if 'if' in self.current_token:
                self.compile_if_statement()
            if 'while' in self.current_token:
                self.compile_while_statement()
            if 'do' in self.current_token:
                self.compile_do_statement()
            if 'return' in self.current_token:
                self.compile_return_statement()
            self.process_statement()

    def process_subroutine_call(self):
        if "." in self.look_ahead():
            self.process("identifier")
            self.process(".")
            self.process("identifier")
            self.process("(")
            self.compile_expression_list()
            self.process(")")
        else:
            self.process("identifier")
            self.process("(")
            self.compile_expression_list()
            self.process(")")

    def process_multiple_terms(self):
        operator = list_of_symbols_in_string(op, self.current_token)
        if operator != False:
            self.process(operator)
            self.compile_term()
            self.process_multiple_terms()

    def process_multiple_expressions(self):
        if "," in self.current_token:
            self.process(",")
            self.compile_expression()
            self.process_multiple_expressions()

    def compile_expression_list(self):
        self.tree.append("<expressionList>")
        if "integerConstant" in self.current_token or "stringConstant" in self.current_token or "keyword" in self.current_token or "identifier" in self.current_token or "(" in self.current_token or list_of_symbols_in_string(unaryOp, self.current_token) != False :
            self.compile_expression()
            self.process_multiple_expressions()
        self.tree.append("</expressionList>")

    def compile_term(self):
        self.tree.append('<term>')
        if "integerConstant" in self.current_token:
            self.process("integerConstant")
        elif "stringConstant" in self.current_token:
            self.process("stringConstant")
        elif "keyword" in self.current_token:
            self.process("keyword")
        elif "identifier" in self.current_token:
            if self.type_of_identifier() == "variable":
                self.process("identifier")
            elif self.type_of_identifier() == "array":
                self.process("identifier")
                self.process("[")
                self.compile_expression()
                self.process("]")
            elif self.type_of_identifier() == "subroutineCall":
                # logica per il varName
                self.process_subroutine_call()
        elif "(" in self.current_token:
            self.process("(")
            self.compile_expression()
            self.process(')')
        else:
            operator = list_of_symbols_in_string(unaryOp,self.current_token)
            if operator != False:
                self.process(operator)
                self.compile_term()
        self.tree.append('</term>')

    def compile_expression(self):
        self.tree.append("<expression>")
        self.compile_term()
        self.process_multiple_terms()
        self.tree.append("</expression>")


    def compile_return_statement(self):
        self.tree.append("<returnStatement>")
        self.process("return")
        if ";" in self.current_token:
            self.process(";")
        else:
            self.compile_expression()
            self.process(";")
        self.tree.append("</returnStatement>")
        pass

    def compile_do_statement(self):
        self.tree.append("<doStatement>")
        self.process("do")
        self.process_subroutine_call()
        self.process(";")
        self.tree.append("</doStatement>")


    def compile_while_statement(self):
        self.tree.append("<whileStatement>")
        self.process("while")
        self.process("(")
        self.compile_expression()
        self.process(")")
        self.process("{")
        self.compile_statements()
        self.process("}")
        self.tree.append("</whileStatement>")

    def compile_if_statement(self):
        self.tree.append("<ifStatement>")
        self.process("if")
        self.process("(")
        self.compile_expression()
        self.process(")")
        self.process("{")
        self.compile_statements()
        self.process("}")
        if "else" in self.current_token:
            self.process("else")
            self.process("{")
            self.compile_statements()
            self.process("}")
        self.tree.append("</ifStatement>")
        pass

    def compile_let_statement(self):
        self.tree.append("<letStatement>")
        self.process("let")
        self.process("identifier") #varName
        if '[' in self.current_token:
            self.process('[')
            self.compile_expression()
            self.process(']')
        self.process("=")
        self.compile_expression()
        self.process(";")
        self.tree.append("</letStatement>")

    def compile_statements(self):
        self.tree.append("<statements>")
        if list_of_symbols_in_string(statements, self.current_token):
            self.process_statement()
        self.tree.append("</statements>")


    def compile_var_dec(self):
        if "var" in self.current_token:
            self.tree.append("<varDec>")
            self.process("var")
            self.process_type(self.current_token)
            self.process("identifier")
            self.process_multiple_vars() # (, varName)*
            self.process(";")
            self.tree.append("</varDec>")
            self.compile_var_dec()

    def compile_subroutine_body(self):
        self.tree.append("<subroutineBody>")
        self.process("{")
        self.compile_var_dec() # varDec*
        self.compile_statements()
        self.process("}")
        self.tree.append("</subroutineBody>")

    def compile_parameter_list(self):
        self.tree.append("<parameterList>")
        if ")" not in self.current_token:
            self.process_type(self.current_token)
            self.process("identifier")
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
            else: # case function
                self.process("function")
            if "void" in self.current_token:
                self.process("void")
            # ('void' | type)
            else:
                self.process_type(self.current_token)
            # subroutineName
            self.process("identifier")
            # '('parameterList')'
            self.process("(")
            self.compile_parameter_list()
            self.process(")")
            self.compile_subroutine_body()
            self.tree.append("</subroutineDec>")
            self.compile_subroutine_dec()

    def compile_class_var_dec(self):
        if "static" in self.current_token or "field" in self.current_token:
            self.tree.append("<classVarDec>")
            if "static" in self.current_token:
                self.process("static")
            elif "field" in self.current_token:
                self.process("field")
            self.process_type(self.current_token)
            self.process("identifier")
            self.process_multiple_vars() # (, varName)*
            self.process(";")
            self.tree.append("</classVarDec>")
            self.compile_class_var_dec()

    def compile_class(self):
        # scrivere class
        self.tree.append("<class>")
        self.process("class")
        self.process("identifier")
        self.process("{")
        self.compile_class_var_dec()
        self.compile_subroutine_dec()
        self.process("}")
        self.tree.append("</class>")
        self.__list_to_file__()


    def compile(self):
        self.__advance__()
        self.compile_class()
        print(self.tokens)



