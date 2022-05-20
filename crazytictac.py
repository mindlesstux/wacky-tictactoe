
class game:
    def __init__(self, boardwidth, boardheight):
        self.boardwidth = boardwidth
        self.boardheight = boardheight
        self.board = [ [ "A" * self.boardwidth ] * self.boardheight ]
        self.won = False

    def checkWin(self):
        pass

    def printBoard(self):
        rowstr = ""
        for rows in self.board:
            for idxRow, row in enumerate(rows, start=1):
                if idxRow == 1:
                    pass
                else:
                    dashes = "-" * ((3*self.boardwidth) + (self.boardwidth - 1))
                    rowstr = "%s%s\n" % (rowstr, dashes)
                for idxCol in range(len(row)):
                    if idxCol == 0:
                        rowstr = "%s %s" % (rowstr, row[idxCol])
                    else:
                        rowstr = "%s | %s" % (rowstr, row[idxCol])
                rowstr = "%s\n" % (rowstr)

        print("%s" % rowstr)

mygame = game(3,3)
mygame.printBoard()
