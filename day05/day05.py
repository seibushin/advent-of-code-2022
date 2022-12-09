#!/usr/bin/env python3
import sys
import re
from collections import defaultdict

"""Excute by running:
$ cat input | python day05.py
"""


def parse_input(input):
    """Parse the input."""
    BOX_PATTERN = re.compile(r"\[(?P<content>.)\]")
    MOVE_PATTERN = re.compile(r"move (?P<moves>\d+) from (?P<from>\d+) to (?P<to>\d+)")

    stacks = defaultdict(list)
    moves = []

    for line in input:
        match list(line.rstrip("\n").lstrip()):
            case ["[", *_]:
                for box in BOX_PATTERN.finditer(line):
                    column = (box.start() // 4) + 1
                    stacks[column].append(box.group("content"))
            case ["1", *_]:
                [v.reverse() for v in stacks.values()]
            case ["m", "o", "v", "e", *_]:
                move = MOVE_PATTERN.search(line.rstrip("\n"))
                moves.append(
                    (
                        int(move.group("moves")),
                        int(move.group("from")),
                        int(move.group("to")),
                    )
                )

    return stacks, moves


def move_boxes(stacks, moves, crate_mover_model=9000):
    """Execute the moves on the given stacks."""
    for move_x, move_from, move_to in moves:
        if crate_mover_model == 9001:
            stacks[move_to] += stacks[move_from][-move_x:]
            stacks[move_from] = stacks[move_from][:-move_x]
        else:
            for _ in range(move_x):
                stacks[move_to].append(stacks[move_from][-1])
                stacks[move_from] = stacks[move_from][:-1]

    return stacks


def get_top_most_boxes(stacks):
    """Get the top most box per stack."""
    return "".join([([""] + v[:])[-1] for _, v in sorted(stacks.items())])


def main(input, crate_mover_model=9000):
    """Reorder container."""
    stacks, moves = parse_input(input)
    stacks = move_boxes(stacks, moves, crate_mover_model)
    top_most_boxes = get_top_most_boxes(stacks)

    print(top_most_boxes)
    return top_most_boxes


if __name__ == "__main__":
    crate_mover_model = 9000
    try:
        crate_mover_model = int(sys.argv[1])
    except:
        pass
    main(sys.stdin, crate_mover_model)
