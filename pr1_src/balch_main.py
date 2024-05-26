import numpy as np


def spin_wheel():
    return np.random.randint(0, 2)


def test_and_run():
    count = 0
    episode_winnings = 0
    while episode_winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            won = spin_wheel()
            count += 1
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount *=2
    return count


if __name__ == '__main__':
    length = test_and_run()
    print(length)