import sys, getopt

class Alignment(object):
	def __init__(self, refLine, uReadLine, cReadLine):
				

def readInput(mafInputPath):
	with open(mafInputPath, 'r') as file:
		alignments = []
		for line in file:
			line = line.split()
			if len(line) > 0 and line[0] != "#":
				if line[0] == 'a':
					if None not in [refLine, uReadLine, cReadLine]:
						alignment = Alignment(refLine, uReadLine, cReadLine)
						alignments.append( alignment )
					refLine = None
					uReadLine = None
					cReadLine = None
				elif refLine is None:
					refLine = line
				elif uReadLine is None:
					uReadLine = None
				elif cReadLine is None:
					cReadLine = None
	return alignments

helpMessage = "Reads three-way alignment MAF files and outputs another three-way MAF file without extended segments on reads and a second MAF file with only alignment between the reference and the extended segment of the read."
usageMessage = "[-h help and usage] [-i three-way MAF file] [-r reference FASTA] [-m unextended MAF output path] [-e extension segments MAF output path]"

options = "hi:r:m:e:"

try:
	opts, args = getopt.getopt(sys.argv[1:], options)
except getopt.GetoptError:
	print "Error: unable to read command line arguments."
	sys.exit(2)

if len(sys.argv) == 1:
	print usageMessage
	sys.exit(2)

mafInputPath = None
refPath = None
unextendedPath = None
extensionPath = None

for opt, arg in opts:
	if opt == '-h':
		print helpMessage
		print usageMessage
		sys.exit()
	elif opt == '-i':
		mafInputPath = arg
	elif opt == '-r':
		refPath = arg
	elif opt == '-m':
		unextendedPath = arg
	elif opt == '-e':
		extensionPath = True

if mafInputPath is None or refPath is None or unextendedPath is None or extensionPath is None:
	print "Missing argument - please double check your command."
	sys.exit(2)

alignments = readInput( mafInputPath )
writeUnextended(unextendedAlignments)
extendedSegments = findExtendedAlignments(extendedSegments)
writeExtendedMaf(extendedSegments)