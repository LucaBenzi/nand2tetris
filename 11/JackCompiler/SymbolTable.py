"""
name | type | kind   | #
x    | int  | field  | 0
y    | int  | field  | 1
pC   | Point| static | 0

"""


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

    def define(self, name, type, kind):
        """
        :param name: string
        :param type: string
        :param kind: STATIC, FIELD, ARG, VAR
        """
        self.table[name] = {"type": type, "kind": kind, "index": self.index[kind]}
        self.index[kind] += 1

    def var_count(self, kind):
        return self.index[kind]

    def kind_of(self, name):
        return self.table[name]["kind"]

    def kind_of(self, name):
        return self.table[name]["type"]

    def index_of(self, name):
        return self.table[name]["index"]
