#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-ttt-player.py (C) myke 2015-10-17 0.3
# Tic-tak-toe player

import pprint, pickle, random

log = []
que = need = 0
b = []
all = {0, 1, 2, 3, 4, 5, 6, 7, 8}

def main(args):
    """main dispatcher"""
    print ("This is Tic-Tak-Toe player.")
    if restoreall():
        return playall()
    return 1


def restoreall():
    """restore data from pickle"""
    global log
    print ("Restoring data from pickle...")
    try:
        with open ('mk-ttt.pickle', 'rb') as r:
            log = pickle.load(r)
        print ("Restored, maybe")
        return True
    except:
        print ("Cannot restore :(")
        return False


def playall():
    """main player"""
    global que, need, notneed, b
    que = input ("Let us play. Your turn? (12Yyq) [q]]")
    que = que.strip()
    if que in 'qQ':
        print ("Bye-bye.")
        return 0
    if que != "" and que not in '12':
        que = random.choice('12')
    que = 3 - int (que)
    need = [1, -1] [que-1]
    notneed = [-1, 1] [que-1]
    b = [0, 0, 0,   0, 0, 0,   0, 0, 0]
    print ("My move is %d, I need %d\n" % (que, need))
    play ()
    return 0


def play ():
    """play the game using log table"""
    global b, log, need, notneed, que
    turn = 3 - que
    gama = []
    showtable()

    # game loop
    while True:
        turn = 3 - turn

        if len(gama) == 9:  # full board
            res = 0
            break

        res = endp()
        if res: break
        done = tuple(gama)

        if turn == 1:       # computer moves

            best = [x for x in log if x[0][:-1] == done and x[1] == need]
            if best:
                m = best[0][-1]
                b [m] = need
                gama.append(m)
                print ("Computer finally moves:", m+1)
                show()
                continue

            llog = len(log)
            best = [x for x in log if x[0][:llog] == done and x[1] == need]
            if best:
                best = random.choice(best)
                m = best[0][-1]
                b [m] = need
                gama.append(m)
                print ("Computer best moves:", m+1)
                show()
                continue

            best = tuple(all - set(gama))
            if len(best):
                m = random.choice(best)
                b [m] = need
                gama.append(m)
                print ("Computer randomly moves:", m+1)
                show()
                continue

            print ("Somethign went wrong :(")
            break

        else:               # player moves
            while True:
                m = input("Enter your move or 'q' for quit:")
                m = m.strip()
                if m in 'qQ':
                    print ("Quitting...")
                    return 0

                try:
                    m = int (m) - 1
                except:
                    print ("Illegal move. Please repeat!")
                    continue

                if m < 0 or m > 8:
                    print ("Outside move. Please repeat!")
                    continue

                if m in gama:
                    print ("Same move. Please repeat!")
                    continue

                break

            gama.append(m)
            b [m] = notneed
            show()

            log = [x for x in log if len(gama) >= len(x[0]) and x[0][len(gama)] == m]

    # game over
    res = endp()
    if res == need:
        print ("Computer won!")
    elif res == notneed:
        print ("Player won!")
    else:
        print ("Draw!")


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


def showtable():
    """show board cells numbers"""
    print ("""The board is:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")


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


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
