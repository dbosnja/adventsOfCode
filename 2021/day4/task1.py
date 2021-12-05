#!/bin/python3


def get_input(file_path):
    boards = []
    with open(file_path) as f:
        numbers = [int(c) for c in f.readline().strip().split(',')]
        while True:
            line = f.readline().strip()
            assert line == ''
            board = []
            for _ in range(5):
                board.append([int(c) for c in f.readline().strip().split()])
            if not any(b for b in board):
                break
            boards.append(board)
    return numbers, boards


def mark_x(number, boards):
    for board in boards:
        for row in board:
            for i, num in enumerate(row[:]):
                if num == number:
                    row[i] = -1


def is_winner(board):
    winning_pot = set([-1])
    if any(set(row) == winning_pot for row in board):
        return True
    col_cnt = len(board[0])
    for col in range(col_cnt):
        if {row[col] for row in board} == winning_pot:
            return True
    return False


def find_winner(boards):
    for board in boards:
        if is_winner(board):
            return board


def main():
    file_path = 'input.txt'
    numbers, boards = get_input(file_path)
    for number in numbers:
        mark_x(number, boards)
        winner = find_winner(boards)
        if winner:
            win_number = number
            break
    unmark_sum = 0
    for row in winner:
        for number in row:
            if number != -1:
                unmark_sum += number
    print(unmark_sum * win_number)


if __name__ == '__main__':
    main()