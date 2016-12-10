import logging

logging.basicConfig(level=logging.DEBUG)

startfile_path = "start.log"
finishfile_path = "finish.log"
outputfile_path = "output.log"

title1 =  "------------------------------------"
title2 = "#p opt b3lyp/6-31g geom=connectivity"
title3 = "------------------------------------ \n"
title4 = "-------------------"
title5 = " Title Card Required"
title6 = " -------------------\n"

header1 = "                         Standard orientation:"
header2 = "---------------------------------------------------------------------"
header3 = " Center     Atomic      Atomic             Coordinates (Angstroms)"
header4 = " Number     Number       Type             X           Y           Z"
header5 = " ---------------------------------------------------------------------"

footer1 = "---------------------------------------------------------------------"

footer2 = " GradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGrad"

footer3 = " GradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGrad"

footer4 = "---------------------------------------------------------------------"
footer5 = "Normal termination of Gaussian 09"

stepsNumber = 10

class Atom(object):
	def __init__(self, atom_number, nuclear_number, zero, x, y, z):
		self.x = x
		self.y = y
		self.z = z

		self.atom_number = atom_number
		self.nuclear_number = nuclear_number
		self.zero = zero

	def _print(self):
		logging.info("atom_number: %s", self.atom_number)
		logging.info("nuclear_number: %s", self.nuclear_number)
		logging.info("zero: %s", self.zero)
		logging.info("x: %s", self.x)
		logging.info("y: %s", self.y)
		logging.info("z: %s", self.z)

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def _read_atoms_positions(textfile):
	atoms = []
	counter = 0

	for line in textfile:
		if hasNumbers(line):
			x = line.strip().split()
			atom = Atom(float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(x[5]))
			atoms.append(atom)
			counter += 1

	return atoms	

with open(startfile_path) as inputfile:
	startFile = inputfile.readlines()

with open(finishfile_path) as inputfile:
	endFile = inputfile.readlines()

atoms_start = _read_atoms_positions(startFile)
atoms_end = _read_atoms_positions(endFile)

output = open(outputfile_path, mode = 'w')

output.write(title1 + '\n' +
			 title2 + '\n' + 
			 title3 + '\n' + 
			 title4 + '\n' + 
			 title5 + '\n' + 
			 title6 + '\n')

for i in range(0, stepsNumber):

	atoms_interim = [] 

	for j in range(0, len(atoms_start)):
		atom_pos_x = atoms_start[j].x + (atoms_end[j].x - atoms_start[j].x) / stepsNumber * i
		atom_pos_y = atoms_start[j].y + (atoms_end[j].y - atoms_start[j].y) / stepsNumber * i
		atom_pos_z = atoms_start[j].z + (atoms_end[j].z - atoms_start[j].z) / stepsNumber * i	
		atom = Atom(atoms_start[j].atom_number, atoms_start[j].nuclear_number, atoms_start[j].zero, atom_pos_x, atom_pos_y, atom_pos_z)
		atoms_interim.append(atom)

	output.write(header1 + '\n' + 
				 header2 + '\n' + 
				 header3 + '\n' +
				 header4 + '\n' +
				 header5 + '\n')

	for k in range(0, len(atoms_interim)):
		output.write('      ' + 
			 		 str(int(atoms_interim[k].atom_number)) + "\t\t" +
					 str(int(atoms_interim[k].nuclear_number)) + "\t\t" + 
					 str(int(atoms_interim[k].zero)) + "\t\t" +
					 str(atoms_interim[k].x) + "\t" +
					 str(atoms_interim[k].y) +  "\t" +
					 str(atoms_interim[k].z) + "\n")

	if (i != (stepsNumber - 1)):
		output.write(footer1 + '\n\n' + 
					 footer2 + '\n')
		if (i > 0):
			output.write(' Step Number  ' + str(i) + '\n\n')
		else:
			output.write('\n')
	
		output.write(footer3 + '\n\n')

	else:
		output.write(footer1 + '\n\n' + 
					 footer2 + '\n' + 
					 'Step Number  ' + str(i + 1) + '\n\n')
		
		output.write(footer3 + '\n\n')

		output.write(header1 + '\n' + 
				 	 header2 + '\n' + 
				 	 header3 + '\n' +
				 	 header4 + '\n' +
				 	 header5 + '\n')
		
		for k in range(0, len(atoms_end)):
			output.write('      ' + 
			 		 	str(int(atoms_end[k].atom_number)) + "\t\t" +
					 	str(int(atoms_end[k].nuclear_number)) + "\t\t" + 
					 	str(int(atoms_end[k].zero)) + "\t\t" +
					 	str(atoms_end[k].x) + "\t" +
					 	str(atoms_end[k].y) +  "\t" +
					 	str(atoms_end[k].z) + "\n")

		output.write(footer4 + '\n' + 
					 footer5)

output.close()










