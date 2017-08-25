import sys

class Table:
    table = []
    tableCordenadas = []
    numColumns =6
    player1 = 'X'
    player2 = 'O'
    turn = player1
    state = 'InGame'
    NInlineToWin = 4
    winChips = []


    def __init__(self):
        self.table = [0 ,1 ,2 ,3 ,4 ,5 ,
                      6 ,7 ,8 ,9 ,10,11,
                      12,13,14,15,16,17,
                      18,19,20,21,22,23,
                      24,25,26,27,28,29,
                      30,31,32,33,34,35]
        self.numColumns = 6
        self.turn = 'X'
        self.player1 = 'X'
        self.player2 = 'O'
        self.state = 'InGame'
        self.NInlineToWin = 4
        self.winChips = []

    def __init__(self,numColumns,state,NInLineToWin):
        self.table = self.buildTable(numColumns)
        self.numColumns = numColumns
        self.turn = self.player1
        self.state = state
        self.NInlineToWin = NInLineToWin
        self.winChips = []

    def buildTable(self,numero):
        table = []
        i = 0
        while i < numero * numero:
            table.append(i)
            i += 1
        print(table)

        tableCordenadas = []
        o=0
        while o < numero:
            x = 0
            while x < numero:
                tableCordenadas.append(str(o) + str(x))
                x+=1
            o+=1
        print(tableCordenadas)
        return table;

    def play(self):
        self.state = ''
        self.winChips = []
        self.turn = ''

    def MakeMove(self,cordenadaX,cordenadaY):
        valido = True
        i = 0
        while i < len(self.table):
            if self.table[i] != i:
                i += 1

    def printTable(self):
        i = 0
        while i < len(self.table):
            sys.stdout.write(str(self.table[i])+', ')
            i+=1

juego = Table(4,'NULL',9)
#juego.printTable()