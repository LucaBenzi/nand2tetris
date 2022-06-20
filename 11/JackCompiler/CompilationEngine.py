from Jack import op, unaryOp, statements
from SymbolTable import *
from VMWriter import *
import re


def list_of_symbols_in_string(lista, token):
    token = re.findall(r'> (.*) <', token)[0]
    for o in lista:
        if o in token:
            return o
    return False


def get_tag_content(tag: str):
    return re.findall(r'> (.*) <', tag)[0]


class CompilationEngine:

    def __init__(self, filename):
        self.filename = filename
        xml_file = open(filename, "r")
        self.filename = self.filename.replace("T.xml", ".xml").split("/")[-1]
        self.tokens = xml_file.readlines()  # source torkens
        self.tokens = [s.replace('\n', '') for s in self.tokens]
        self.tree = []  # destination tokens
        self.index = 0
        self.current_token = ""
        self.class_name = ""
        self.class_symbol_table = SymbolTable()
        self.string_open = False
        self.writer = VMWriter(self.filename.replace(".xml", ".vm"))

    def look_ahead(self):
        return self.tokens[self.index+1]

    def look_for_variable(self, name, symbol_table: SymbolTable):
        if symbol_table is not None and symbol_table.in_table(name):
            return "local"
        elif self.class_symbol_table.in_table(name):
            return "class"
        else:
            return False

    def type_of_identifier(self):
        # variable array subroutineCall
        if "identifier" in self.current_token:
            if "[" in self.look_ahead():
                return "array"
            if "(" in self.look_ahead() or "." in self.look_ahead():
                return "subroutineCall"
            else:
                return "variable"
        return ""

    def __get_variable_info__(self, name, symbol_table: SymbolTable = None):
        if self.look_for_variable(name, symbol_table) == "local":
            kind = symbol_table.kind_of(name)
            index = symbol_table.index_of(name)
        elif self.look_for_variable(name, symbol_table) == "class":
            kind = self.class_symbol_table.kind_of(name)
            index = self.class_symbol_table.index_of(name)
        else:
            if self.string_open:
                kind = "string"
                index = -1
            else:
                raise BaseException(f"Variable {name} not declared")
        return kind, index

    def __transform_identifier__(self, name, category, index, usage):
        self.tree[-1] = self.tree[-1].replace("<identifier>",
                                              f'<identifier name="{name}" category="{category}" index="{index}" usage="{usage}">')


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
            raise BaseException(
                f"{self.filename}: Syntax error at line {self.index}, expected: {word}, found {self.current_token}")

    def process_type(self, word):
        if "int" in word or "char" in word or "boolean" in word:
            type_ = get_tag_content(self.current_token)
            self.process(word)
            return type_
        else:
            type_ = get_tag_content(self.current_token)
            name = get_tag_content(self.current_token)
            kind = "class"
            index = -1
            self.process("identifier")
            self.__transform_identifier__(name, kind, index, "used")
            return type_

    def process_multiple_vars(self, type_, kind, symbol_table=None):
        if "," in self.current_token:
            self.process(",")
            name = get_tag_content(self.current_token)

            if symbol_table is not None:
                symbol_table.define(name, type_, kind)
                index = symbol_table.index_of(name)
            else:
                self.class_symbol_table.define(name, type_, kind)
                index = self.class_symbol_table.index_of(name)
            self.process("identifier")
            self.__transform_identifier__(name, kind, index, "declared")
            self.process_multiple_vars(type_, kind, symbol_table)

    def process_multiple_vars_and_types(self, local_variables):
        if "," in self.current_token:
            self.process(",")
            type_ = self.process_type(self.current_token)
            name = get_tag_content(self.current_token)
            self.process("identifier")
            local_variables.define(name, type_, "arg")
            index = local_variables.index_of(name)
            self.__transform_identifier__(name, "arg", index, "declared")
            self.process_multiple_vars_and_types(local_variables)

    def process_statement(self, local_variables: SymbolTable):
        if 'let' in self.current_token or "if" in self.current_token or "while" in self.current_token or "do" in self.current_token or "return" in self.current_token:
            if 'let' in self.current_token:
                self.compile_let_statement(local_variables)
            if 'if' in self.current_token:
                self.compile_if_statement(local_variables)
            if 'while' in self.current_token:
                self.compile_while_statement(local_variables)
            if 'do' in self.current_token:
                self.compile_do_statement(local_variables)
            if 'return' in self.current_token:
                self.compile_return_statement(local_variables)
            self.process_statement(local_variables)

    def process_subroutine_call(self, local_variables):
        if "." in self.look_ahead():
            name = get_tag_content(self.current_token)
            self.process("identifier")
            self.__transform_identifier__(name, "class", -1, "used")
            self.process(".")
            name = get_tag_content(self.current_token)
            self.process("identifier")
            self.__transform_identifier__(name, "subroutine", -1, "used")
            self.process("(")
            self.compile_expression_list(local_variables)
            self.process(")")
        else:
            name = get_tag_content(self.current_token)
            self.process("identifier")
            self.__transform_identifier__(name, "subroutine", -1, "used")
            self.process("(")
            self.compile_expression_list(local_variables)
            self.process(")")

    def process_multiple_terms(self, local_variables):
        operator = list_of_symbols_in_string(op, self.current_token)
        if operator != False:
            self.process(operator)
            self.compile_term(local_variables)
            self.process_multiple_terms(local_variables)

    def process_multiple_expressions(self, local_variables):
        if "," in self.current_token:
            self.process(",")
            self.compile_expression(local_variables)
            self.process_multiple_expressions(local_variables)

    def compile_expression_list(self, local_variables):
        self.tree.append("<expressionList>")
        if "integerConstant" in self.current_token or "stringConstant" in self.current_token or "keyword" in self.current_token or "identifier" in self.current_token or "(" in self.current_token or list_of_symbols_in_string(unaryOp, self.current_token) != False :
            self.compile_expression(local_variables)
            self.process_multiple_expressions(local_variables)
        self.tree.append("</expressionList>")

    def compile_term(self, local_variables):
        self.tree.append('<term>')
        if "integerConstant" in self.current_token:
            self.process("integerConstant")
        elif "stringConstant" in self.current_token:
            self.process("stringConstant")
        elif "keyword" in self.current_token:
            self.process("keyword")
        elif "identifier" in self.current_token:
            if self.type_of_identifier() == "variable":
                name = get_tag_content(self.current_token)
                kind, index = self.__get_variable_info__(name, local_variables)
                self.process("identifier")
                self.__transform_identifier__(name, kind, index, "used")
            elif self.type_of_identifier() == "array":
                name = get_tag_content(self.current_token)
                kind, index = self.__get_variable_info__(name, local_variables)
                self.process("identifier")
                self.__transform_identifier__(name, kind, index, "used")
                self.process("[")
                self.compile_expression(local_variables)
                self.process("]")
            elif self.type_of_identifier() == "subroutineCall":
                # logica per il varName
                self.process_subroutine_call(local_variables)
        elif "(" in self.current_token:
            self.process("(")
            self.compile_expression(local_variables)
            self.process(')')
        else:
            operator = list_of_symbols_in_string(unaryOp,self.current_token)
            if operator != False:
                self.process(operator)
                self.compile_term(local_variables)
        self.tree.append('</term>')

    def compile_expression(self, local_variables: SymbolTable):
        self.tree.append("<expression>")
        self.compile_term(local_variables)
        self.process_multiple_terms(local_variables)
        self.tree.append("</expression>")

    def compile_return_statement(self, local_variables: SymbolTable):
        self.tree.append("<returnStatement>")
        self.process("return")
        if ";" in self.current_token:
            self.process(";")
        else:
            self.compile_expression(local_variables)
            self.process(";")
        self.tree.append("</returnStatement>")
        pass

    def compile_do_statement(self, local_variables: SymbolTable):
        self.tree.append("<doStatement>")
        self.process("do")
        self.process_subroutine_call(local_variables)
        self.process(";")
        self.tree.append("</doStatement>")


    def compile_while_statement(self, local_variables: SymbolTable):
        self.tree.append("<whileStatement>")
        self.process("while")
        self.process("(")
        self.compile_expression(local_variables)
        self.process(")")
        self.process("{")
        self.compile_statements(local_variables)
        self.process("}")
        self.tree.append("</whileStatement>")

    def compile_if_statement(self, local_variables: SymbolTable):
        self.tree.append("<ifStatement>")
        self.process("if")
        self.process("(")
        self.compile_expression(local_variables)
        self.process(")")
        self.process("{")
        self.compile_statements(local_variables)
        self.process("}")
        if "else" in self.current_token:
            self.process("else")
            self.process("{")
            self.compile_statements(local_variables)
            self.process("}")
        self.tree.append("</ifStatement>")
        pass

    def compile_let_statement(self, local_variables: SymbolTable):
        self.tree.append("<letStatement>")
        self.process("let")
        name = get_tag_content(self.current_token)
        kind, index = self.__get_variable_info__(name, local_variables)
        self.process("identifier") #varName
        self.__transform_identifier__(name, kind, index, "used")
        if '[' in self.current_token:
            self.process('[')
            self.compile_expression(local_variables)
            self.process(']')
        self.process("=")
        self.compile_expression(local_variables)
        self.process(";")
        self.tree.append("</letStatement>")

    def compile_statements(self, local_variables: SymbolTable):
        self.tree.append("<statements>")
        if list_of_symbols_in_string(statements, self.current_token):
            self.process_statement(local_variables)
        self.tree.append("</statements>")


    def compile_var_dec(self, local_variables: SymbolTable):
        if "var" in self.current_token:
            kind = "var"
            self.tree.append("<varDec>")
            self.process("var")
            type_ = get_tag_content(self.current_token)
            self.process_type(self.current_token)
            name = get_tag_content(self.current_token)
            self.process("identifier")
            local_variables.define(name, type_, kind)
            index = local_variables.index_of(name)
            self.__transform_identifier__(name, "var", index, "declared")
            self.process_multiple_vars(type_,kind, local_variables) # (, varName)*
            self.process(";")
            self.tree.append("</varDec>")
            self.compile_var_dec(local_variables)

    def compile_subroutine_body(self, local_variables):
        self.tree.append("<subroutineBody>")
        self.process("{")
        self.compile_var_dec(local_variables) # varDec*
        self.compile_statements(local_variables)
        self.process("}")
        self.tree.append("</subroutineBody>")
        print(f"method\t{local_variables.table}")

    def compile_parameter_list(self, local_variables):
        self.tree.append("<parameterList>")
        if ")" not in self.current_token:
            type_ = self.process_type(self.current_token)
            name = get_tag_content(self.current_token)
            self.process("identifier")
            local_variables.define(name, type_, "arg")
            index = local_variables.index_of(name)
            self.__transform_identifier__(name, "arg", index, "declared")
            self.process_multiple_vars_and_types(local_variables)
        self.tree.append("</parameterList>")

    def compile_subroutine_dec(self):
        """
        ('constructor'|'function'|'method') ('void'|type)subroutineName'('parameterList')'subroutineBody
        :return:
        """
        local_variables = SymbolTable()
        local_variables.define("this", self.class_name, "arg")
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
                name = get_tag_content(self.tree[-1])
                self.__transform_identifier__(name, "class", None, "used")
            # subroutineName
            name = get_tag_content(self.current_token)
            self.process("identifier")
            self.__transform_identifier__(name, "subroutine", None, "declared")
            # '('parameterList')'
            self.process("(")
            self.compile_parameter_list(local_variables)
            self.process(")")
            self.compile_subroutine_body(local_variables)
            self.tree.append("</subroutineDec>")
            self.compile_subroutine_dec()

    def compile_class_var_dec(self):
        if "static" in self.current_token or "field" in self.current_token:
            self.tree.append("<classVarDec>")
            kind = get_tag_content(self.current_token)
            kind = kind.replace("<identifier> ","").replace(" </identifier>","")
            if "static" in self.current_token:
                self.process("static")
            elif "field" in self.current_token:
                self.process("field")
            type_ = self.process_type(self.current_token)
            name = get_tag_content(self.current_token)
            self.class_symbol_table.define(name, type_, kind)
            index = self.class_symbol_table.index_of(name)
            self.process("identifier")
            self.__transform_identifier__(name, kind, index, "declared")
            self.process_multiple_vars(type_, kind) # (, varName)*s
            self.process(";")
            self.tree.append("</classVarDec>")
            self.compile_class_var_dec()

    def compile_class(self):
        # scrivere class
        self.tree.append("<class>")
        self.process("class")
        self.class_name = get_tag_content(self.current_token)
        name = get_tag_content(self.current_token)
        self.process("identifier")
        self.__transform_identifier__(name, "class", None, "declared")
        self.process("{")
        self.compile_class_var_dec()
        self.compile_subroutine_dec()
        self.process("}")
        self.tree.append("</class>")

    def compile(self):
        print("\nnew class")
        self.__advance__()
        self.compile_class()
        # print(self.tokens)
        print(f"class:\t{self.class_symbol_table.table}")
        self.writer.close()
        return self.tree
