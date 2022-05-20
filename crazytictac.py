
class game:
    def __init__(self, boardwidth, boardheight):
        self.setup(boardheight=boardheight, boardwidth=boardwidth)
        self.rowId = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def setup(self, boardwidth=3, boardheight=3):
        self.boardwidth = boardwidth
        self.boardheight = boardheight
        self.board = [ [ " " * self.boardwidth ] * self.boardheight ]
        self.won = False

    def checkWin(self):
        pass

    def printBoard(self):
        print()

        rowstr = ""
        for rows in self.board:
            for idxRow, row in enumerate(rows, start=1):
                if idxRow == 1:
                    pass
                else:
                    dashes = "-" * ((3*self.boardwidth) + (self.boardwidth - 1))
                    rowstr = "%s     %s\n" % (rowstr, dashes)
                for idxCol in range(len(row)):
                    if idxCol == 0:
                        rowstr = "%s %s    %s" % (rowstr, self.rowId[idxRow - 1], row[idxCol])
                    else:
                        rowstr = "%s | %s" % (rowstr, row[idxCol])
                rowstr = "%s\n" % (rowstr)

        print("%s" % rowstr)

mygame = game(3,3)
mygame.printBoard()
