from maps import *


class Transaltor:
    def __init__(self):
        self.count = 0

    def init_vm(self):
        # 4 commands
        asm = []
        asm.append("@256")
        asm.append("D=A")
        asm.append("@R0")
        asm.append("M=D")
        return asm

    def generate_comment(self, instruction):
        return f"// {instruction['command']} {instruction['segment']} {instruction['value']}"

    def pop_to_asm(self, instruction):
        # 0 command
        asm = ""
        return asm

    def push_to_asm(self, instruction):
        # command segment value
        # 7 command lines
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append(f"@{instruction['value']}")
        asm.append("D=A")
        asm.append(f"@{SEGMENT_MAP[instruction['segment']]}")
        asm.append("A=M")
        asm.append("M=D")
        asm.append(f"@{SEGMENT_MAP[instruction['segment']]}")
        asm.append("M=M+1")
        return asm

    def add_to_asm(self, instruction):
        # 12 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// descrmento SP")
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in M")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("// eseguo calcolo")
        asm.append("M=D+M")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")
        return asm

    def sub_to_asm(self, instruction):
        # 12 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// descrmento SP")
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in M")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("// eseguo calcolo")
        asm.append("M=M-D")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")
        return asm

    def and_to_asm(self, instruction):
        # 12 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// descrmento SP")
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in M")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("// eseguo calcolo")
        asm.append("M=D&M")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")
        return asm

    def or_to_asm(self, instruction):
        # 12 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// descrmento SP")
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in M")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("// eseguo calcolo")
        asm.append("M=D|M")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")
        return asm

    def not_to_asm(self, instruction):
        # 8 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// eseguo calcolo")
        asm.append("M=!D")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")
        return asm

    def neg_to_asm(self, instruction):
        # 8 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// eseguo calcolo")
        asm.append("M=-D")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")
        return asm

    def eq_to_asm(self, instruction):
        # 26 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// descrmento SP")
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in M")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("// eseguo calcolo")
        asm.append("D=M-D")
        asm.append(f"@TRUE{self.count}")
        asm.append("D;JEQ")
        asm.append(f"@FALSE{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(TRUE{self.count})")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("M=-1")
        asm.append(f"@END_EQ{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(FALSE{self.count})")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("M=0")
        asm.append(f"@END_EQ{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(END_EQ{self.count})")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")

        self.count = self.count + 1
        return asm

    def gt_to_asm(self, instruction):
        # 26 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// descrmento SP")
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in M")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("// eseguo calcolo")
        asm.append("D=M-D")
        asm.append(f"@TRUE{self.count}")
        asm.append("D;JGT")
        asm.append(f"@FALSE{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(TRUE{self.count})")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("M=-1")
        asm.append(f"@END_EQ{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(FALSE{self.count})")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("M=0")
        asm.append(f"@END_EQ{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(END_EQ{self.count})")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")

        self.count = self.count + 1
        return asm

    def lt_to_asm(self, instruction):
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")
        asm.append("// descrmento SP")
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("// pop in M")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("// eseguo calcolo")
        asm.append("D=M-D")
        asm.append(f"@TRUE{self.count}")
        asm.append("D;JLT")
        asm.append(f"@FALSE{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(TRUE{self.count})")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("M=-1")
        asm.append(f"@END_EQ{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(FALSE{self.count})")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("M=0")
        asm.append(f"@END_EQ{self.count}")
        asm.append("0;JEQ")

        asm.append(f"(END_EQ{self.count})")
        asm.append("// incremento SP")
        asm.append("@R0")
        asm.append("M=M+1")

        self.count = self.count + 1
        return asm
