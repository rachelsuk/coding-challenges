def play_war(player1_cards, player2_cards):
    cards = []
    while True:
        p1 = player1_cards.pop(0)
        p2 = player2_cards.pop(0)
        cards.extend([p1,p2])
        if p1 == p2:
            if len(player1_cards) > 1 and len(player2_cards) > 1:
                p1 = player1_cards.pop(0)
                p2 = player2_cards.pop(0)
                cards.extend([p1,p2])
        else:
            if p1 > p2:
                player1_cards.extend(cards)
            elif p1 < p2:
                player2_cards.extend(cards)
            cards = []

        if not player1_cards:
            print('Player 2 wins the game!')
            break
        elif not player2_cards:
            print('Player 1 wins the game!')
            break


game_1 = play_war([5,4,3,6,6],[5,4,3,6,7])
game_2 = play_war([2,3,2,5,6,1,10],[6,5,2,1,4,2,8])

# try, except, index error.
# check before everytime you pop, you break out of the while loop.


            