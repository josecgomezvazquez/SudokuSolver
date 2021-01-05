# -*- coding: utf-8 -*-
"""
This program creates a 9x9 sudoku puzzle, randomly takes away numbers, and
proceeds to fill it out by trial-and-error and uses backtracking.
"""

from random import sample

base = 3
side = base * base

# Pattern for a baseline solution
# r = rows
# c = columns
def pattern(r, c):
    return (base * (r % base) + r // base + c) % side

# Randomize rows and columns (of valid base return)
def shuffle(s):
    return sample(s, len(s))

rBase = range(base)
rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base * base + 1))

# Produce sudoku board using randomized baseline pattern
board = [[nums[pattern(r, c)] for c in cols] for r in rows]

for line in board:
    print(line)






















