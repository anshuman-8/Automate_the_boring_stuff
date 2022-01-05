
def printTable(li):
    
    for r in range(4):
        for c in range(3):
            print(li[c][r].rjust(8,' ')," ", end='')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)

