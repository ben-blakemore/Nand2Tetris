// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// To multiply do R0 added to itself R1 times

// Take value of R1
@R1
D=M

// Assign @times to this value
@times
M=D

// Initialise result inside R2
@R2
M=0

// Then loop, first check can be if @times is 0, if it is then loop has finished so exit
(LOOP)
	@times
	D=M
	@END
	D; JEQ

	// if still looping times-- and sum++
	@1
	D=D-A
	@times
	M=D

	@2
	D=M
	@0
	D=D+M // d = R0 + SUM
	@2
	M=D // SUM = SUM + R0

	@LOOP
	0;JMP

(END)
	@END
	0;JMP
