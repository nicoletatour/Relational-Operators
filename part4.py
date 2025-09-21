#NIKOLETA TOUROUNOGLOU AM:5106
import sys

def createRow(line):
    values = line.strip().split('\t')
    if len(values) == 2:
        return (values[0], int(values[1]))
    return None

def next_different_row(file, last):
    while True:
        line = file.readline()
        if line == '':
            return None
        row = createRow(line)
        if row == None:
            continue
        if row != last:
            return row

def difference(input1, input2, output):
    with open(input1, 'r') as R_sorted, open(input2, 'r') as S_sorted, open(output, 'w') as RdifferenceS:

        r = next_different_row(R_sorted, None)
        s = next_different_row(S_sorted, None)

        while r != None and s != None:

            if r < s:

                RdifferenceS.write(r[0] + "\t" + str(r[1]) + "\n")
                r = next_different_row(R_sorted, r)

            elif r > s:
                s = next_different_row(S_sorted, s)
                
            else:
                r = next_different_row(R_sorted, r)
                s = next_different_row(S_sorted, s)

        while r != None:
            RdifferenceS.write(r[0] + "\t" + str(r[1]) + "\n")
            r = next_different_row(R_sorted, r)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(0)
    difference(sys.argv[1], sys.argv[2], sys.argv[3])
