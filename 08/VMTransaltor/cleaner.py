from typing import List

def remove_comments(instructions: List[str]):
    result = []
    for i in instructions:
        result.append(i.split('//')[0])
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


def remove_tabulations(instructions):
    result = []
    for i in instructions:
        result.append(i.replace("\t",""))
    return result
