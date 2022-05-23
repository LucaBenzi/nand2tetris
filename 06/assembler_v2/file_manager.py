from typing import List

class FileManager:
    def __init__(self, filename: str):
        if not filename.endswith('.asm'):
            raise Exception("Provide .asm file")
        else:
            self.filename = filename

    def file_to_string_list(self):
        with open(self.filename, "r") as grilled_cheese:
            lines = grilled_cheese.readlines()
            return lines

    def string_list_to_binary_file(self, binary_instructions: List[str]):
        text_file = open(self.filename.replace(".asm", ".hack"), "w")
        for instruction in binary_instructions:
            text_file.write(instruction + "\n")
        text_file.close()