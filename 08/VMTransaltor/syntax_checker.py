from typing import List, Dict
from constant import *
from source import Source


class SyntaxChecker(Source):
    def __init__(self, source: List[str]):
        super().__init__(source)

    def __check_stack_instructions(self, instruction: Dict):
        # first parameter don't need to be checked because it's classified as stack operation
        # second parameter must be a string which doesn't start with a digit
        if instruction["argument"] not in STACK_ARGUMENTS:
            raise Exception(f"ERROR at line {self.instructions.index(instruction)}: {instruction['argument']} is not an argument")
        # third parameter must be a number
        if not instruction["value"].isnumeric():
            raise Exception(f"ERROR at line {self.instructions.index(instruction)}: value must be a number")
        # lenght of instructions must be 3 otherwise too many argument
        if len(instruction) != 3:
            raise Exception(f"ERROR at line {self.instructions.index(instruction)}: stack operations needs exactrly 3 parameters: instruction, argument, value")
        return "ok"

    def __check_math_instructions(self, instruction: Dict):
        # first parameter don't need to be checked because it's classified as math operation
        if len(instruction) != 1:
            raise Exception(
                f"ERROR at line {self.instructions.index(instruction)}: math operations needs exactrly 1 parameters: instruction")
        return "ok"

    def __check_flow_control_instructions(self, instruction: Dict):
        # if instruction is return parameters must be 1 otherwise too many arguments
        if instruction["instruction"] == "return":
            if len(instruction) != 1:
                raise Exception(
                    f"ERROR at line {self.instructions.index(instruction)}: return needs exactrly 1 parameters: instruction")
            return "ok"
        # if label or goto 2 arguments, second doesn't start with digit
        if instruction["instruction"] == "label" or instruction["instruction"] == "goto":
            if len(instruction) != 2:
                raise Exception(
                    f"ERROR at line {self.instructions.index(instruction)}: {instruction['instruction']} needs exactrly 2 parameters")
            if instruction["argument"][0].isnumeric():
                raise Exception(f"ERROR at line {self.instructions.index(instruction)}: label cannot start with digit")
            return "ok"
        # all other commands 3 arguments: second parameter must be a string which doesn't start with a digit
        if instruction["argument"][0].isnumeric():
            raise Exception(f"ERROR at line {self.instructions.index(instruction)}: label {instruction['argument']} cannot start with digit")
        return "ok"
        # third parameter must be a number
        pass

    def check_source_code(self):
        for i in self.instructions:
            conversion = "blank line"
            instruction_type = self.classify_instruction(i)
            if instruction_type == "error":
                raise Exception(f"ERROR at line {self.source.index(i)}: {i['instruction']} is not an allowed instruction")
            if instruction_type == "stack":
                conversion = self.__check_stack_instructions(i)
            if instruction_type == "math":
                conversion = self.__check_math_instructions(i)
            if instruction_type == "flow_control":
                conversion = self.__check_flow_control_instructions(i)
            print(i, conversion)

    def get_instructions(self):
        return self.instructions

