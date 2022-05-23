// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
//24576 <- keyboard address
//16384 <- first screen address
//24575 <- last  screen address

//blackens the screen
@16384
D = A
@R0				//R0 contains the address of the memory to put to -1
M = D
(BLACK)
@R0
A = M
D = -1
M = D
D = A + 1
@R0
M = D

//if D = 24576 go to END
@24576
D = D - A
@END
D;JEQ

//go to BLACK
@BLACK
D;JMP

(END)
@END
D;JMP
