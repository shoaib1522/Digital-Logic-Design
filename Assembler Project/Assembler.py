import sys
import os

def usage():
    print ("Usage: %s namefile.asm" %os.path.basename(sys.argv[0]))

def tobin(val, nbits):
  return bin((val + (1 << nbits)) % (1 << nbits))[2:]

def main():
    #command-line argument
    args = sys.argv[1:]
    if "-h" in args or "--help" in args or args==[]:
        usage()
        sys.exit(2)
    fw = open(args[0].split('.')[0]+".hack",'w')

    #init compTable
    compT = {
          '0':'0101010',  '1':'0111111', '-1':'0111010',  'D':'0001100',  'A':'0110000',
         '!D':'0001101', '!A':'0110001', '-D':'0001111', '-A':'0110011','D+1':'0011111',
        'A+1':'0110111','D-1':'0001110','D+A':'0000010','D-A':'0010011','A-D':'0000111',
        'D&A':'0000000','D|A':'0010101',  'M':'1110000', '!M':'1110001', '-M':'1110011',
        'M+1':'1110111','M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111',
        'D&M':'1000000','D|M':'1010101','A-1':'0110010'
        }
    #init destTable
    destT ={'null':'000','M':'001','D':'010','MD':'011',
            'A':'100','AM':'101','AD':'110','AMD':'111'}

    #init jumpTable
    jumpT ={'null':'000','JGT':'001','JEQ':'010','JGE':'011',
            'JLT':'100','JNE':'101','JLE':'110','JMP':'111'}

    #init SymbolTable
    SymbolTable ={'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576,
                  'R0':0,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,
                  'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15}

    #first pass
    instr_count = 0
    with open(args[0]) as f:
        for i, l in enumerate(f):
            line = l.strip() #strip space
            line = line.split('//')[0].strip() #strip comment
            if not line:
                continue
            if line[0]=='(':
                symbol = line[1:].split(')')[0] 
                SymbolTable[symbol] = instr_count #ignoring double symbol error
                continue
            #ignoring invalid A_COMMAND & C_COMMAND
            instr_count += 1

    #second pass
    instr_count = 0
    symbol_counter = 16
    with open(args[0]) as f:
        for i, l in enumerate(f):
            line = l.strip() #strip space
            line = line.split('//')[0].strip() #strip comment
            if not line:
                continue
            if line[0]=='(':
                continue
            #--------------A-COMMAND------------------
            if line[0]=='@': 
                token = line[1:]
                if not token.lstrip('-').isdigit(): 
                    if token not in SymbolTable:
                       SymbolTable[token] = symbol_counter
                       symbol_counter +=1
                    token = SymbolTable[token]
                    #print "0{0:015b}".format(token) #ignoring unknown symbol
                    fw.write("0{0:015b}\n".format(token))
                else:
                    #--- TODO: dealing with negative number
                    if token[0] == '-':
                        #print '0'+tobin(int(token),15)
                        fw.write('0'+tobin(int(token),15)+'\n')
                    else:
                        #print "0{0:015b}".format(int(token)) #ignoring unknown symbol
                        fw.write("0{0:015b}\n".format(int(token)))                        
                instr_count += 1
                continue
            #--------------C-COMMAND------------------
            comp = dest = jump = ""
            if '=' in line:
                token = line.split('=')
                dest = destT[token[0]]
                line = token[1]
            else:
                dest = destT['null']
            token = line.split(';')
            comp = compT[token[0]]
            if ';' in line:
                jump = jumpT[token[1]]
            else:
                jump = jumpT['null']
            #print '111'+comp+dest+jump
            fw.write('111'+comp+dest+jump+'\n')
            instr_count += 1
    fw.close()
if __name__ == "__main__":
    main()