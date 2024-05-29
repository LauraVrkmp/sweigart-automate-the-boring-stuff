def column_width(data):
    colWidths = [0] * len(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if len(data[i][j]) > colWidths[i]:
                colWidths[i] = len(data[i][j])
    return colWidths

def printTable(data, colWidths):    
    for i in range(len(data[0])):
        for j in range(len(data)):
            if j == len(data) - 1:
                print(data[j][i].rjust(colWidths[j]) + ' ')
            else:
                print(data[j][i].rjust(colWidths[j]) + ' ', end='')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = column_width(tableData)
printTable(tableData, colWidths)