#NIKOLETA TOUROUNOGLOU AM:5106
import sys

def createRow(line):
    values = line.strip().split('\t')
    if len(values) == 2:
        return values[0], int(values[1])
    return None

def union(input1, input2, output):
    with open(input1, 'r') as R_sorted, open(input2, 'r') as S_sorted, open(output, 'w') as RunionS:

        lineR = R_sorted.readline()
        lineS = S_sorted.readline()
        previous_row = ('',0)

        while lineR != '' or lineS !='' :

            if lineR == '':
                rowS = createRow(lineS)
                if rowS and rowS != previous_row:
                    RunionS.write(rowS[0] + "\t" + str(rowS[1]) + "\n")
                    previous_row = rowS
                lineS = S_sorted.readline()
                continue

            if lineS == '':
                rowR = createRow(lineR)
                if rowR and rowR != previous_row:
                    RunionS.write(rowR[0] + "\t" + str(rowR[1]) + "\n")
                    previous_row = rowR
                lineR = R_sorted.readline()
                continue

            rowR = createRow(lineR)
            rowS = createRow(lineS)

            if rowR[0] < rowS[0] or (rowR[0] == rowS[0] and rowR[1] < rowS[1]):
                if rowR != previous_row:
                    RunionS.write(rowR[0] + "\t" + str(rowR[1]) + "\n")
                    previous_row = rowR
                lineR = R_sorted.readline()
            elif rowR[0] > rowS[0] or (rowR[0] == rowS[0] and rowR[1] > rowS[1]):
                if rowS != previous_row:
                    RunionS.write(rowS[0] + "\t" + str(rowS[1]) + "\n")
                    previous_row = rowS
                lineS = S_sorted.readline()
            else:
                if rowR != previous_row:
                    RunionS.write(rowR[0] + "\t" + str(rowR[1]) + "\n")
                    previous_row = rowR
                lineR = R_sorted.readline()
                lineS = S_sorted.readline()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(0)
    else:
        union(sys.argv[1], sys.argv[2], sys.argv[3])
