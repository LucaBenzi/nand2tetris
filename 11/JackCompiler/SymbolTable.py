"""
name | type | kind   | #
x    | int  | field  | 0
y    | int  | field  | 1
pC   | Point| static | 0

"""
var_kind = ["STATIC", "FIELD", "VAR", "ARG"]

class SymbolTable:

    def __init__(self):
        self.table = {}
        self.index = {"STATIC": 0,
                      "FIELD": 0,
                      "ARG": 0,
                      "VAR": 0}

    def reset(self):
        self.table = {}
        self.index = {"STATIC": 0,
                      "FIELD": 0,
                      "ARG": 0,
                      "VAR": 0}

    def define(self, name, type_, kind):
        """
        :param name: string
        :param type: string
        :param kind: STATIC, FIELD, ARG, VAR
        """
        if kind.upper() not in var_kind:
            raise BaseException(f"Error: provide one of the following kind: {var_kind}. Value provided: {kind.upper()}")
        self.table[name] = {"type": type_, "kind": kind, "index": self.index[kind.upper()]}
        self.index[kind.upper()] += 1

    def var_count(self, kind):
        if kind not in var_kind:
            raise BaseException(f"Error: provide one of the following kind: {var_kind}. Value provided: {kind}")
        return self.index[kind]

    def kind_of(self, name):
        if name not in self.table:
            raise BaseException(f"{name} variable not in Symbol Table")
        return self.table[name]["kind"]

    def type_of(self, name):
        if name not in self.table:
            raise BaseException(f"{name} variable not in Symbol Table")
        return self.table[name]["type"]

    def index_of(self, name):
        if name not in self.table:
            raise BaseException(f"{name} variable not in Symbol Table")
        return self.table[name]["index"]

    def in_table(self, name):
        if name in self.table.keys():
            return True
        return False
