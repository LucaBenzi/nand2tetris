from typing import List, Dict
from constant import *

class Source():
    def __init__(self, source: List[str]):
        self.source = source
        self.instructions = []
        self.source_to_instructions()

    def classify_instruction(self, instruction: Dict):
        if len(instruction) == 0:
            return "empty"
        if instruction["instruction"] in STACK_OPERATIONS:
            return "stack"
        if instruction["instruction"] in MATH_OPERATIONS:
            return "math"
        if instruction["instruction"] in FLOW_CONTROL_OPERATIONS:
            return "flow_control"
        return "error"

    def source_to_instructions(self):
        for s in self.source:
            line = s.split(" ")
            while '' in line:
                line.remove('')
            instruction = dict(zip(INSTRUCTION_FIELDS, line))  # crea un dizionario partendo da una lista
            self.instructions.append(instruction)