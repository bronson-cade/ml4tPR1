""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Bronson Lim (replace with your name)  		  	   		 	   			  		 			 	 	 		 		 	
GT User ID: blim45 (replace with your User ID)  		  	   		 	   			  		 			 	 	 		 		 	
GT ID: 903951342 (replace with your GT ID)  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
np.set_printoptions(threshold=np.inf)

  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def author():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The GT username of the student  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: str  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    return "blim45"  # replace tb34 with your Georgia Tech username.
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def gtid():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The GT ID of the student  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: int  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    return 903951342  # replace with your GT ID number  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def get_spin_result(win_prob):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param win_prob: The probability of winning  		  	   		 	   			  		 			 	 	 		 		 	
    :type win_prob: float  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The result of the spin.  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: bool  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    result = False  		  	   		 	   			  		 			 	 	 		 		 	
    if np.random.random() <= win_prob:  		  	   		 	   			  		 			 	 	 		 		 	
        result = True  		  	   		 	   			  		 			 	 	 		 		 	
    return result


def run_episode_balch(win_prob):
    results = [0]
    episode_winnings = 0
    episode_counter = 0

    """Code from Project Description"""
    while (episode_winnings < 80) and (episode_counter < 1000):
        won = False
        bet_amount = 1
        while not won:
            won = get_spin_result(win_prob)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount *= 2
            results.append(episode_winnings)
            episode_counter += 1
    """In case we won early"""
    if episode_counter < 1000:
        results.extend([80]*(1000-episode_counter))
    return results


def run_episode_bankroll_limit(win_prob):
    results = [0]
    episode_winnings = 0
    episode_counter = 0
    while (episode_winnings < 80) and (episode_counter < 1000):
        won = False
        bet_amount = 1
        while not won:
            won = get_spin_result(win_prob)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = min(2*bet_amount, episode_winnings+256)
                print(f"Bet amount is {bet_amount} and current cash is {episode_winnings}")
            results.append(episode_winnings)
            episode_counter += 1
        if bet_amount == 0:
            break
        """In case we won early"""
    if episode_counter < 1000:
        if episode_winnings <= -256:
            results.extend([-256] * (1000 - episode_counter))
        else:
            results.extend([episode_winnings] * (1000 - episode_counter))

    return results

def experiment1_figs(win_prob):
    spins = np.arange(0, 1001)
    episodes = []
    for i in range(10):
        episode = run_episode_balch(win_prob)
        episodes.append(episode)
    """Experiment 1.1"""
    fig, ax = plt.subplots()
    for i in range(10):
        ax.plot(spins, episodes[i], label="Episode {i}".format(i=i))

    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.xticks(rotation=25)
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Martingale Strategy Simulations")
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend()
    plt.savefig("martingale_no_limits_simulation.png", format="png")

    """Experiment 1.2"""
    fig, ax = plt.subplots()
    episodes = np.array(episodes)
    episode_mean = np.mean(episodes, axis=0)
    episode_std = np.std(episodes, axis=0)
    plt.plot(spins, episode_mean, label="Spin Mean")
    plt.plot(spins, episode_mean + episode_std, label="Spin Mean + Std. Dev.")
    plt.plot(spins, episode_mean - episode_std, label="Spin Mean - Std. Dev.")
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.xticks(rotation=25)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Martingale Strategy without Limit (Mean)")
    plt.legend()
    plt.savefig("martingale_no_limits_mean.png", format="png")

    """Experiment 1.3"""
    episode_median = np.median(episodes, axis=0)
    fig, ax = plt.subplots()
    ax.plot(spins, episode_median, label="Spin Median")
    ax.plot(spins, episode_median + episode_std, label="Spin Median + Std. Dev.")
    ax.plot(spins, episode_median - episode_std, label="Spin Median - Std. Dev.")
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.xticks(rotation=25)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Martingale Strategy without Limit (Median)")
    plt.legend()
    plt.savefig("martingale_no_limits_median.png", format="png")


def experiment2_figs(win_prob):
    spins = np.arange(0, 1001)
    episodes = []
    for i in range(10):
        episode = run_episode_bankroll_limit(win_prob)
        episodes.append(episode)

    wins = 0
    for episode in episodes:
        if episode[1000] == 80:
            wins += 1
    print(wins)

    """Experiment 2.1"""
    fig, ax = plt.subplots()
    episode_mean = np.mean(episodes, axis=0)
    episode_std = np.std(episodes, axis=0)
    plt.plot(spins, episode_mean, label="Mean Winnings")
    plt.plot(spins, episode_mean + episode_std, label="Mean + Standard Deviation")
    plt.plot(spins, episode_mean - episode_std, label="Mean - Standard Deviation")
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.xticks(rotation=25)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Martingale Strategy with Bankroll Limit (Mean)")
    plt.legend()
    plt.savefig("martingale_with_limits_mean.png", format="png")

    "Experiment 2.1"
    fig, ax = plt.subplots()
    episode_median = np.median(episodes, axis=0)
    plt.plot(spins, episode_median, label="Median Winnings")
    plt.plot(spins, episode_median + episode_std, label="Median + Standard Deviation")
    plt.plot(spins, episode_median - episode_std, label="Median - Standard Deviation")
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.xticks(rotation=25)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Martingale Strategy with Bankroll Limit (Median)")
    plt.legend()
    plt.savefig("martingale_with_limits_median.png", format="png")

def test_code():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Method to test your code  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    win_prob = 0.474  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		 	   			  		 			 	 	 		 		 	"""
    experiment1_figs(win_prob)
    experiment2_figs(win_prob)


if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    test_code()  		  	   		 	   			  		 			 	 	 		 		 	
