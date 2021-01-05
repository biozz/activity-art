#!/usr/bin/env/python
#
# Copyright (c) 2021 Ivan Elfimov <ielfimov@gmail.com>
# released under The MIT license (MIT) http://opensource.org/licenses/MIT
#
# This is a simple script, that will make commit messages look like a text
# on activity graph.
import datetime as dt
from git import Repo

# Change me
phrase = "AAA"
start_date = dt.datetime(2020, 2, 2, 12, 00)
repo = Repo("repo")

en_us = {
    "A": [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
    ],
    # TODO: (@biozz) add more letters and symbols
}

sep = [
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
]

index = repo.index
phrase_encoded = []

# this will insert separators in between letters
# so AAA becomes [A, sep, A, sep, A]
# this loop also encodes letters, so they are transposed
# for easier dates traversal
for i, letter in enumerate(phrase):
    next_letter = None
    if i + 1 < len(phrase):
        next_letter = phrase[i + 1]
    phrase_encoded.append([*zip(*en_us[letter])])
    if next_letter and next_letter != " ":
        phrase_encoded.append([*zip(*sep)])

# this will go though all of the encoded letters
# generate date and make commit
for item_encoded in phrase_encoded:
    for col in item_encoded:
        for row in col:
            for commit_count in range(row):
                commit_date = start_date.isoformat()
                index.commit(
                    phrase,
                    author_date=commit_date,
                    commit_date=commit_date,
                )
            start_date += dt.timedelta(days=1)
