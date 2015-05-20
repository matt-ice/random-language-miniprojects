
# 111 ac1c2c3c4c5c6 d1d2d3 j1j2j3
#dest = comp; jump

jump_string={"JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}

def parser(instr):
	global instr_dest, instr_comp, instr_jump, instr_type,
	#handle A
	if(instr[0]="@"):
		instr_type="A"
		A_res = "0" + {"0:15b"}.format(int(bin(instr[1:])[2:]))
		return 

	#prepare variables for C instruction
	eq = instr.find("=",0,len(instr))
	semicol = instr.find(";",0,len(instr))
	
	#getting comp part of expression
	if semicol>0:
		comp = instr[eq:semicol]
	else:
		comp=instr[eq:]
	
	#handle integers
	if(comp in ("0","1","-1")):
		#begin and handle 0
		instr_comp[0]="1"
		instr_comp[2]="1"
		instr_comp[4]="1"
		if(comp.find("1")>0):
			instr_comp[1]="1"
			if(comp="1"):
				instr_comp[3]="1"
				instr_comp[5]="1"


	#destination ADM 
	if(instr.find("A",0,eq)>0):
		instr_dest[0] = "1"
	if(instr.find("D",0,eq)>0):
		instr_dest[1] = "1"
	if(instr.find("M",0,eq)>0):
		instr_dest[2] = "1"
	
	# Jump
	if semicol>0:
		instr_jump=jump_string[instr[:3]]

	#computation ADM +-&| ADM
	if(comp.find("M",0,len(instr))>0):
		instr_a="1"

	#check if only one input
	if((comp.find("M")>0 || comp.find("A")>0) != comp.find("D")>0):
		#prepare instruction part based on AM or D
		if(comp.find("D")>0):
			instr_comp[2..3]="11"
		else:
			instr_comp[0..1]="11"
		
		#!D and !AM
		if(comp[0]="!"):
			instr_comp[5]="1"
		
		#-AMD and AMD-1
		if(comp.find("-")>0):
			instr_comp[4..5]="11"
			if(comp_find("1")>0):
				instr_comp[5]="0"
		#AM+1 and DM+1
		if(comp.find("+1")>0):
			instr_comp[1]="1"
			instr_comp[3..5]="111"
			if(comp[0]="D"):
				instr_comp[2]="1"
			else:
				instr_comp[0]="1"
		return

	#handle D+A, D&A, 
	if(comp[1]="+"):
		instr_comp[4]="1"
	elif(comp[1]="&"):
		return

	#bruteforce the rest
	if(comp="A-D"):
		instr_comp="000111"
	elif(comp="D|A"):
		instr_comp="010101"
	elif(comp="D-A"):
		instr_comp="010011"




def code:
	if(instr_type=="A"):
		return A_res
	else:
		return "111" + instr_a + instr_comp + instr_dest + instr_jump

def main():
	global instr_type, A_res, instr_dest, instr_comp, instr_jump,instr_a
	instr_type="C"
	A_res=""
	instr_dest="000"
	instr_comp="000000"
	instr_jump="000"
	instr_a="0"
	asm_in = open(file.asm,"r")
	load output.hack
	while line.len()<2:
		line = readline.trim()	
	parser(line)
	output.writeline = code()
