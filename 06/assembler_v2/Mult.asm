// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[3], respectively.)

// Put your code here.

//R2 = 0
@R2
M = 0

(MAIN)
//D = R0
@0
D = M

//if D = 0 goto END
@END
D; JEQ

//D = R1
@1
D = M

//R2 = R2 + D
@2
M = D+M

//R0 = R0 - 1
@0
M = M - 1

//goto MAIN
@MAIN
D;JMP
(END)
@END
D;JMP
