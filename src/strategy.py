import pandas as pd 


hard_double_df = pd.read_csv('../data/hard_double.csv')
hard_double_df.set_index('Unnamed: 0', inplace = True)
hard_double_df.index.name= None

hard_hit_df = pd.read_csv('../data/hard_hit.csv')
hard_hit_df.set_index('Unnamed: 0', inplace = True)
hard_hit_df.index.name= None

soft_double_df = pd.read_csv('../data/soft_double.csv')
soft_double_df.set_index('Unnamed: 0', inplace = True)
soft_double_df.index.name= None

soft_hit_df = pd.read_csv('../data/soft_hit.csv')
soft_hit_df.set_index('Unnamed: 0', inplace = True)
soft_hit_df.index.name= None

split_df = pd.read_csv('../data/split.csv')
split_df.set_index('Unnamed: 0', inplace = True)
split_df.index.name= None



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
