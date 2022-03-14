import pandas as pd 

# table representing a hard hand with option to double
hard_double_df = pd.read_csv('../data/hard_double.csv')
hard_double_df.set_index('Unnamed: 0', inplace = True)
hard_double_df.index.name= None

# table representing a hard hand without option to double
hard_hit_df = pd.read_csv('../data/hard_hit.csv')
hard_hit_df.set_index('Unnamed: 0', inplace = True)
hard_hit_df.index.name= None

# table representing a soft hand with option to double
soft_double_df = pd.read_csv('../data/soft_double.csv')
soft_double_df.set_index('Unnamed: 0', inplace = True)
soft_double_df.index.name= None

# table representing a soft hand without option to double
soft_hit_df = pd.read_csv('../data/soft_hit.csv')
soft_hit_df.set_index('Unnamed: 0', inplace = True)
soft_hit_df.index.name= None

# table representing a paired hand
split_df = pd.read_csv('../data/split.csv')
split_df.set_index('Unnamed: 0', inplace = True)
split_df.index.name= None


"""---------------------------------------------
Each method below returns the ideal move to play
given the players hand and the dealers show card
---------------------------------------------"""

def hard_double(player_score, dealer_score):
	return int(hard_double_df.loc[player_score, str(dealer_score)])

def hard_hit(player_score, dealer_score):
	return int(hard_hit_df.loc[player_score, str(dealer_score)])

def soft_double(player_score, dealer_score):
	return int(soft_double_df.loc[player_score, str(dealer_score)])

def soft_hit(player_score, dealer_score):
	return int(soft_hit_df.loc[player_score, str(dealer_score)])

def split(player_score, dealer_score):
	return int(split_df.loc[player_score, str(dealer_score)])
