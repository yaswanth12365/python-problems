import time
import pandas as pd
import numpy as np


recent_books = [11,55,55,54,55,45,2,45,25,2,5,25,12,5,24,2,5,2,5,215,25,5,25,25,2,21,25,255,52,255,645,52]
print(len(recent_books))
coding_books = [454,56,46,54,51,24,41,156,6,459,56,6,645,5,25,59,6,2525,2,12,45,52,69,55,5,25,55,25,25]
print(len(coding_books),"\n")
start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration 1: {} seconds'.format(time.time() - start))

## Tip #1: Use vector operations over loops when possible

start = time.time()
recent_coding_books = np.intersect1d(recent_books, coding_books)
print(len(recent_coding_books))
print('Duration 2: {} seconds'.format(time.time() - start))

## Tip #2: Know your data structures and which methods are faster

start = time.time()
recent_coding_books = set(recent_books).intersection(coding_books)
print(len(recent_coding_books))
print('Duration 3: {} seconds'.format(time.time() - start))