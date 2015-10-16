#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-ttt-maker.py (C) myke 2015-10-16 1.5
# Tic-tak-toe maker

import pprint

log = []        # list opf all games as [(moves, result)]
                # moves = (4, 0, 1) = points
                # result= +1 for X wins, 0 = draw, -1 = 0 wins
                # points = ((0, 1, 2), (3, 4, 5), (6, 7, 8))

b = []          # board
gama = []       # moves in current game
etc = resxo = 0
who = {1:0, -1:0}

def main(args):
    """main dispatcher"""
    print ("This is Tic-Tak-Toe maker.")
    playall()
    calcall()
    saveall()
    print ("All done with trace=%d and results=%d, which of total=%d gives %5.2f percents,\nX won %d times, O won %d times, with ratio %5.2f\n\n" % (trace, resxo, (etc + resxo), (100. * resxo / (etc + resxo)), who[1], who[-1], (1.0 * who[1] / who[-1]) ))
    return 0


def playall():
    """play all games and save logs in log"""
    global b
    print ("Playing")
    b = [0, 0, 0,   0, 0, 0,   0, 0, 0]
    put (1)
    pprint.pprint (log)
    showone ()


def put (p):
    """make move, recursively"""
    global b, gama, log, resxo, etc

    piece = p % 2 * 2 - 1

    lom = [x[0] for x in enumerate(b) if x[1] == 0]   # list of possible moves

    for m in lom:
        b [m] = piece
        gama.append (m)

        res = endp ()
        if res != 0:
            log.append ((tuple(gama), piece))
            resxo += 1
            k = gama.pop()
            b [k] = 0
            who [piece] += 1
            return

        if p < 9:
            put (p+1)

        k = gama.pop()
        b [k] = 0
        etc += 1


def endp ():
    """test if we have end of game: None, -1, 0, +1"""
    global b
    if (
        (b[0] == b[1] == b[2] == 1) or
        (b[3] == b[4] == b[5] == 1) or
        (b[6] == b[7] == b[8] == 1) or
        (b[0] == b[3] == b[6] == 1) or
        (b[1] == b[4] == b[7] == 1) or
        (b[2] == b[5] == b[8] == 1) or
        (b[0] == b[4] == b[8] == 1) or
        (b[2] == b[4] == b[6] == 1)):
            return 1
    if (
        (b[0] == b[1] == b[2] == -1) or
        (b[3] == b[4] == b[5] == -1) or
        (b[6] == b[7] == b[8] == -1) or
        (b[0] == b[3] == b[6] == -1) or
        (b[1] == b[4] == b[7] == -1) or
        (b[2] == b[5] == b[8] == -1) or
        (b[0] == b[4] == b[8] == -1) or
        (b[2] == b[4] == b[6] == -1)):
            return -1
    return 0


def calcall():
    """using log calculate optimal moves for X and O"""
    print ("Calculating...")


def saveall():
    """save tables of optimal moves to files"""
    print ("Saving...")


def show():
    """show board"""
    print ("""
%2s | %1s | %1s
---+---+---
%2s | %1s | %1s
---+---+---
%2s | %1s | %1s
""" % (*(xo()),))


def xo():
    """show XO pretty"""
    s = "0.X"
    p = [s[x+1] for x in b]
    return p


def showone():
    """show any sample solution (say, 1st)"""
    global b, log
    print ("\nsample solution:")
    if log:
        for i, p in enumerate(log[0][0]):
            b[p] = i%2 *2 -1
        show()
    else:
        print ("none available :(")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
