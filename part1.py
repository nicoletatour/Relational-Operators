#NIKOLETA TOUROUNOGLOU AM:5106
import sys

def createRow(line):
    values = line.strip().split('\t')
    if len(values) == 2:
        return values[0], int(values[1])
    return None

def merge_join(input1, input2, output):
    with open(input1, 'r') as R_sorted, open(input2, 'r') as S_sorted, open(output, 'w') as RjoinS:

        lineR = R_sorted.readline()
        lineS = S_sorted.readline()

        max_buffer_size = 0

        while lineR != '' and lineS != '':
            valR1, valR2 = createRow(lineR)
            valS1, valS2 = createRow(lineS)

            if valR1 < valS1:
                lineR = R_sorted.readline()
            elif valR1 > valS1:
                lineS = S_sorted.readline()
            else:
                same_val1 = valR1

                bufferR = []
                
                while lineR:
                    tempR1, tempR2 = createRow(lineR)                   
                    if tempR1 == same_val1:
                        bufferR.append((tempR1, tempR2))
                        lineR = R_sorted.readline()
                    else:
                        break

                bufferS = []
                
                while lineS:
                    tempS1, tempS2 = createRow(lineS)
                    if tempS1 == same_val1:
                        bufferS.append((tempS1, tempS2))
                        lineS = S_sorted.readline()
                    else:
                        break

                if len(bufferS) > max_buffer_size:
                    max_buffer_size = len(bufferS)

                for (r1, r2) in bufferR:
                    for (s1, s2) in bufferS:
                        RjoinS.write(r1 + "\t" + str(r2) + "\t" + str(s2) + "\n")


        print("max buffer size: ", max_buffer_size)
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(0)
    else:
        merge_join(sys.argv[1], sys.argv[2], sys.argv[3])
