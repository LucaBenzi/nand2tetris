from source import *

class SyntaxChecker(Source):
    def check_a_syntax(self, instruction: str):
        if instruction[1] in ALLOWED_DIGITS and not instruction.replace("@","").isnumeric():
            raise Exception(f"ERROR at line {self.source.index(instruction)}:Label cannot start with a digit")
        for i in range(1,len(instruction)):
            if instruction[i] not in ALLOWED_DIGITS and instruction[i] not in ALLOWED_EXTRAS and instruction[i] not in ALLOWED_LETTERS:
                raise Exception(f"ERROR at line {self.source.index(instruction)}: symbol {instruction[i]} not allowed in C-instruction")

    def check_c_syntax(self, instruction: str):
        dest, jump, comp = self.split_c_instruction(instruction)
        if dest not in D_FIELD_MAP:
            raise Exception(f"ERROR at line {self.source.index(instruction)}: destination {dest} not allowed")
        if comp not in C_FIELD_MAP:
            raise Exception(f"ERROR at line {self.source.index(instruction)}: operation {comp} not allowed")
        if jump not in J_FIELD_MAP:
            raise Exception(f"ERROR at line {self.source.index(instruction)}: jump {jump} not allowed")

    def check_label_syntax(self, instruction: str):
        if not instruction.startswith("(") or not instruction.endswith(")"):
            raise Exception(f"ERROR at line {self.source.index(instruction)}: Label must be in round brackets ex: ({instruction.replace('(','').replace(')','')})")
        if instruction[1] in ALLOWED_DIGITS and not instruction.replace("(","").replace(")","").isnumeric():
            raise Exception(f"ERROR at line {self.source.index(instruction)}:Label cannot start with a digit")
        for i in range(1,len(instruction)-1):
            if instruction[i] not in ALLOWED_DIGITS and instruction[i] not in ALLOWED_EXTRAS and instruction[i] not in ALLOWED_LETTERS:
                raise Exception(f"ERROR at line {self.source.index(instruction)}: symbol {instruction[i]} not allowed in C-instruction")

    def split_c_instruction(self, instrusction):
        dest = "null"
        jump = "null"
        if("=" in instrusction):
            dest = instrusction.split("=")[0]
            if ";" in instrusction.split("=")[1]:
                comp = instrusction.split("=")[1].split(";")[0]
                jump = instrusction.split("=")[1].split(";")[1]
            else:
                comp = instrusction.split("=")[1]
            return dest, jump, comp
        if(";" in instrusction):
            comp = instrusction.split(";")[0]
            jump = instrusction.split(";")[1]
            return dest, jump, comp

    def check_source_code(self):
        for i in self.source:
            instruction_type = self.classify_instruction(i)
            if instruction_type == "A-instruction":
                self.check_a_syntax(i)
            if instruction_type == "C-instruction":
                self.check_c_syntax(i)
            if instruction_type == "Label":
                self.check_label_syntax(i)
            if instruction_type == "empty":
                pass
            if instruction_type == "not categorized":
                raise Exception(f"ERROR at line {self.source.index(i)}: {i} is not an allowed instruction")