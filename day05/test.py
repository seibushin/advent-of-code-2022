from day05 import day05

input = (
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
)

expected_stacks = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}
expected_moves = [
    (1, 2, 1),
    (3, 1, 3),
    (2, 2, 1),
    (1, 1, 2),
]
expected_stacks_moved = {1: ["C"], 2: ["M"], 3: ["P", "D", "N", "Z"]}


def test_day05_main():
    assert day05.main(input) == "CMZ"


def test_day05_main():
    assert day05.main(input, 9001) == "MCD"


def test_day05_parse():
    stacks, moves = day05.parse_input(input)

    assert stacks == expected_stacks
    assert moves == expected_moves


def test_day05_move():
    stacks = day05.move_boxes(expected_stacks, expected_moves)

    assert stacks == expected_stacks_moved


def test_day05_top_most_boxes():
    top_most_boxes = day05.get_top_most_boxes(expected_stacks_moved)
    assert top_most_boxes == "CMZ"

    top_most_boxes = day05.get_top_most_boxes({1: [], 2: ["A"], 3: ["B"]})
    assert top_most_boxes == "AB"
