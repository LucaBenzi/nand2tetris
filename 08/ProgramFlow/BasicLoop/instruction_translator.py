from dis import Instruction
from maps import *


class Transaltor:
    def __init__(self):
        self.count = 0

    def init_vm(self):
        # 20 commands
        asm = []
        asm.append("// prepare SP")
        asm.append("@256")
        asm.append("D=A")
        asm.append("@R0")
        asm.append("M=D")

        # call Sys.init

        return asm

    def generate_comment(self, instruction):
        return f"//INSTRUCTION: {instruction}"

    def pop_to_asm(self, instruction):  # questa pop è scritta male e andrebbe rifatta
        # NB: praticamente appoggia l'indirizzo in cui salvare in memoria in R13
        # pop segmento indirizzo
        # 14 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        # 0. preparo il posto in cui salvare il valore
        if instruction["segment"] == "temp":
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append(
                f"@{SEGMENT_MAP[instruction['segment'].capitalize() + instruction['value']]}"
            )
            asm.append("D=A")
            asm.append("@R13")
            asm.append("M=D")
        if instruction["segment"] == "pointer":
            # se pop pointer 0 metti l'r13 a 3
            if instruction["value"] == "0":
                asm.append("@3")
            else:
                asm.append("@4")
            asm.append("D=A")
            asm.append("@R13")
            asm.append("M=D")
            # se pop pointer 1 metti l'r13 a 4
        else:
            asm.append(f"@{SEGMENT_MAP[instruction['segment']]}")
            asm.append("D=M")
            asm.append(f"@{instruction['value']}")
            asm.append("D=D+A")
            asm.append("@R13")
            asm.append("M=D")

        # 1. decrementare lo SP
        asm.append("// descrmento SP")
        asm.append("@R0")
        asm.append("M=M-1")

        # 2. prelevo il valore e lo parcheggio in D
        asm.append("// pop in D")
        asm.append("@R0")
        asm.append("A=M")
        asm.append("D=M")

        # 3. salvo il valore
        asm.append("@R13")
        asm.append("A=M")
        asm.append("M=D")

        return asm

    def push_to_asm(self, instruction):
        # command segment value
        # 10 command lines
        asm = []
        asm.append(self.generate_comment(instruction))
        if instruction["segment"] == "constant":
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append(f"@{instruction['value']}")
            asm.append("D=A")
            asm.append(f"@{SEGMENT_MAP[instruction['segment']]}")
            asm.append("A=M")
            asm.append("M=D")
            asm.append(f"@{SEGMENT_MAP[instruction['segment']]}")
            asm.append("M=M+1")
        elif instruction["segment"] == "temp":
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append(
                f"@{SEGMENT_MAP[instruction['segment'].capitalize() + instruction['value']]}"
            )
            asm.append("D=M")
            asm.append("@R0")
            asm.append("A=M")
            asm.append("M=D")
            asm.append("@R0")
            asm.append("M=M+1")
        elif instruction["segment"] == "pointer":
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append("@0")  # per tenere uguale il conteggio
            asm.append("@0")  # per tenere uguale il conteggio
            if instruction["value"] == "0":
                asm.append(f"@{SEGMENT_MAP['this']}")
            else:
                asm.append(f"@{SEGMENT_MAP['that']}")
            asm.append("D=M")
            asm.append("@R0")
            asm.append("A=M")
            asm.append("M=D")
            asm.append("@R0")
            asm.append("M=M+1")

        else:
            asm.append(f"@{instruction['value']}")
            asm.append("D=A")
            asm.append(f"@{SEGMENT_MAP[instruction['segment']]}")
            asm.append("A=D+M")
            asm.append("D=M")
            asm.append("@R0")
            asm.append("A=M")
            asm.append("M=D")
            asm.append("@R0")
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

    def label_to_asm(self, instruction):
        # 0 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append(f"({instruction['location']})")
        return asm

    def ifgoto_to_asm(self, instruction):
        # 6 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("M=M-1")
        asm.append("A=M")
        asm.append("D=M")
        asm.append(f"@{instruction['location']}")
        asm.append("D;JNE")
        return asm

    def goto_to_asm(self, instruction):
        # 5 commands
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append("@R0")
        asm.append("A=M")
        asm.append("M=M-1")
        asm.append(f"@{instruction['location']}")
        asm.append("0;JEQ")
        return asm

    def function_to_asm(self, instruction):
        asm = []
        asm.append(self.generate_comment(instruction))
        asm.append(f"({instruction['label']})")
        for push in range(0, instruction["value"]):
            asm.append(self.push_to_asm({"segment": "local", "value": "0"}))

    def return_to_asm(self, instruction):
        pass

    def call_to_asm(self, instruction):
        pass
