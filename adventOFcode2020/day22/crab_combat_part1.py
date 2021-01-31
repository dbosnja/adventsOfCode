#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/22 - part one


def get_decks(file_path):
    """read the input file

    :param file_path: file path to input file --> str
    :rtype: tuple
    """
    data_input = []
    with open(file_path) as f:
        for line in f:
            if not line.strip(): continue
            data_input.append(line.strip())
    pl2 = data_input.index("Player 2:")
    deckA = list(map(int, data_input[1:pl2]))
    deckB = list(map(int, data_input[pl2 + 1:]))
    return deckA, deckB


def play_the_game(deckA, deckB):
    """play the game according the rules and return
       the winning deck

    :param deckA: list
    :param deckB: list
    :rtype: list
    """
    while True:
        cardA = deckA[0]
        cardB = deckB[0]
        deckA.remove(cardA)
        deckB.remove(cardB)
        if cardA > cardB:
            deckA.append(cardA)
            deckA.append(cardB)
            if not deckB: return deckA
        else:
            deckB.append(cardB)
            deckB.append(cardA)
            if not deckA: return deckB


def main():
    file_path = "input.txt"
    deckA, deckB = get_decks(file_path)
    # data loaded
    resulting_deck = play_the_game(deckA, deckB)
    points = sorted(list(range(1, len(resulting_deck) + 1)), reverse=True)
    return sum([point * card for point, card in zip(points, resulting_deck)])


if __name__ == "__main__":
    print(main())
