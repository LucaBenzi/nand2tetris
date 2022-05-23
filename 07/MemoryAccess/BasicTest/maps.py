SEGMENT_MAP = {
    "constant": "R0",
    "local": "R1",
    "argument": "R2",
    "this": "R3",
    "that": "R4",
    "Temp0": "R5",
    "Temp1": "R6",
    "Temp2": "R7",
    "Temp3": "R8",
    "Temp4": "R9",
    "Temp5": "R10",
    "Temp6": "R11",
    "Temp7": "R12",
    "static": "16",
}

MATH_INSTRUCTIONS = [
    "add",
    "sub",
    "neg",
    "eq",
    "gt",
    "lt",
    "and",
    "or",
    "not",
]

STACK_INSTRUCTIONS = ["push", "pop"]

PROGRAM_FLOW_INSTRUCTIONS = ["label", "goto", "if-goto"]

FUNCTION_CALLING_INSTUCTIONS = ["function", "call", "return"]
