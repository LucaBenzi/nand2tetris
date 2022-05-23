from source import *

class Converter(Source):
    def __init__(self, source, syntax_checker):
        self.binary = []
        self.address_solved = []
        super().__init__(source)
        self.syntax_checker = syntax_checker

    def get_source(self):
        return self.source

    def get_binary_code(self):
        self.__update_symbol_table()
        self.__solve_addresses()
        for i in self.address_solved:
            if "A-instruction" == self.syntax_checker.classify_instruction(i):
                self.binary.append(self.__transalte_a_instruction(i))
            if "C-instruction" == self.syntax_checker.classify_instruction(i):
                self.binary.append(self.__transalte_c_instruction(i))
        return self.binary

    def __update_symbol_table(self):
        ram = 16
        rom = 0
        # prima cercare i salti i rom, poi le variabili
        # aggiungere solo se necessario (controllare la SYMBOL_TABLE)
        for l in self.source:
            if len(l) > 0:
                if l[0] == "(":
                    l = l.replace("(", "").replace(")", "")
                    if l not in SYMBOL_TABLE.keys():
                        SYMBOL_TABLE[l] = str(rom)
                        rom = rom - 1
                rom = rom + 1

        # Adesso cercare le variabili
        for l in self.source:
            if len(l) > 0:
                if l[0] == "@" and not l.replace("@", "").isnumeric():
                    l = l.replace("@", "")
                    if l not in SYMBOL_TABLE.keys():
                        SYMBOL_TABLE[l] = ram
                        ram = ram + 1

    def __solve_addresses(self):
        # rimuove le righe con i riferimenti
        for i in self.source:
            if len(i) > 0 and i[0] == "@" and not i[1:].isnumeric():
                self.address_solved.append("@" + str(SYMBOL_TABLE[i[1:]]))
            else:
                self.address_solved.append(i)

    def __transalte_a_instruction(self, instruction: str):
        return "{0:016b}".format(int(instruction[1:]))


    def __transalte_c_instruction(self, instruction: str):
        dest, jump, comp = self.syntax_checker.split_c_instruction(instruction)
        if comp in A_FIELD_LIST:
            a = "1"
        else:
            a = "0"
        binary = (
                "111"
                + a
                + C_FIELD_MAP[comp]
                + D_FIELD_MAP[dest]
                + J_FIELD_MAP[jump]
        )
        return binary
