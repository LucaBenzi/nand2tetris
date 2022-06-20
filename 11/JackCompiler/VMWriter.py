import VM
from VM import *


class VMWriter:

    def __init__(self, output_file):
        self.output_file = open(output_file, "w")

    def write_push(self, segment, index):
        if segment in VM.segments:
            self.output_file.write("push " + segment + " " + index)
        else:
            raise BaseException(f"push: {segment}: not in {VM.segments}")

    def write_pop(self, segment, index):
        if segment in VM.segments:
            self.output_file.write("pop " + segment + " " + index)
        else:
            raise BaseException(f"pop: {segment}: not in {VM.segments}")

    def write_arithmetic(self, command):
        if command not in VM.arithmetic:
            raise BaseException(f"arithmetic: {command} not in {VM.arithmetic}")
        self.output_file.write(command.lower())

    def write_label(self, label):
        self.output_file.write("label " + label)

    def write_goto(self, label):
        self.output_file.write("goto " + label)

    def write_if(self, label):
        self.output_file.write("if-goto " + label)

    def write_call(self, name, n_args):
        self.output_file.write("call " + name + " " + str(n_args))

    def write_function(self, name, n_vars):
        self.output_file.write("function " + name + " " + str(n_vars))

    def write_return(self):
        self.output_file.write("return")

    def close(self):
        self.output_file.close()