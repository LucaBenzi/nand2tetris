from typing import List
from source import *

def remove_comments(instructions: List[str]):
    result = []
    for i in instructions:
        if i.startswith("//"):
            result.append("")
        else:
            result.append(i)
    return result


def remove_whitespaces(instructions):
    result = []
    for i in instructions:
        result.append(i.replace(" ",""))
    return result


def remove_blanklines(instructions):
    result = []
    for i in instructions:
        if i != "":
            result.append(i)
    return result


def remove_escapes(instructions):
    result = []
    for i in instructions:
        result.append(i.replace("\n",""))
    return result
