#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/22#part2


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
    # saves the order of the cards for ervery round per one game
    round_records = []
    while True:
        if [deckA, deckB] in round_records:
            return "A"
        # else continue to play the same game
        # first add this configuration to be known
        round_records.append([deckA, deckB])
        cardA = deckA[0]
        deckA.remove(cardA)
        cardB = deckB[0]
        deckB.remove(cardB)
        if len(deckA) >= cardA and len(deckB) >= cardB:
            winner = play_the_game(deckA, deckB)
        else:
            if cardA > cardB:
                winner = "A"
            else:
                winner = "B"



def main():
    file_path = "input.txt"
    deckA, deckB = get_decks(file_path)
    # data loaded
    resulting_deck = play_the_game(deckA, deckB)
    points = sorted(list(range(1, len(resulting_deck) + 1)), reverse=True)
    return sum([point * card for point, card in zip(points, resulting_deck)])


if __name__ == "__main__":
    print(main())
