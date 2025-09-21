#NIKOLETA TOUROUNOGLOU AM:5106
import sys

def createRow(line):
    values = line.strip().split('\t')
    if len(values) == 2:
        return values[0], int(values[1])
    return None

def intersection(input1, input2, output):
    with open(input1, 'r') as R_sorted, open(input2, 'r') as S_sorted, open(output, 'w') as RintersectionS:
        lineR = R_sorted.readline()
        lineS = S_sorted.readline()

        if lineR != "": 
            rowR = createRow(lineR)
        else:
            rowR = None

        if lineS != "": 
            rowS = createRow(lineS)
        else:
            rowS = None    
        while rowR != None and rowS != None:
            if rowR < rowS:
                current_row = rowR
                while rowR != None and rowR == current_row:
                    lineR = R_sorted.readline()
                    if lineR != '':
                        rowR = createRow(lineR)
                    else:
                        rowR = None
            elif rowR > rowS:
                current_row = rowS
                while rowS != None  and rowS == current_row:
                    lineS = S_sorted.readline()
                    if lineS != "": 
                        rowS = createRow(lineS)
                    else:
                        rowS = None
            else:
                RintersectionS.write(rowR[0] + "\t" + str(rowR[1])+ "\n")
                current_row = rowR
                while rowR != None and rowR == current_row:
                    lineR = R_sorted.readline()
                    if lineR != "": 
                        rowR = createRow(lineR)
                    else:
                        rowR = None
                current_row = rowS
                while rowS != None and rowS == current_row:
                    lineS = S_sorted.readline()
                    if lineS != "": 
                        rowS = createRow(lineS)
                    else:
                        rowS = None
                    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(0)
    else:
        intersection(sys.argv[1], sys.argv[2], sys.argv[3]) 