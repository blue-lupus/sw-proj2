import pandas as pd
import numpy as np

def the_top_10_players_2015to2018(dataset_df):
	years = np.arange(2015, 2019)
	for year in years:
		df_year = dataset_df[dataset_df['year'] == year]
		print(f"<year: {year}>")
		for category in ['H', 'avg', 'HR', 'OBP']:
			print(f"Top 10 players in {category}: ")
			print(df_year.nlargest(10, category)[['batter_name', category]])

def the_highest_war_in_2018(dataset_df):
	df_2018 = dataset_df[dataset_df['year'] == 2018]
	positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
	for position in positions:
		df_position = df_2018[df_2018['cp'] == position]
		highest_war_player = df_position.nlargest(1, 'war')
		print(f"The player with the highest war by position {position} in 2018:")
		print(highest_war_player[['batter_name', 'war']])

def the_highest_salary(dataset_df):
	categorise = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
	correlations = dataset_df[categorise + ['salary']].corr()['salary'].drop('salary')
	highest_corr_category = correlations.idxmax()
	highest_corr_value = correlations.max()
	return highest_corr_category, highest_corr_value



if __name__=='__main__':
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	print(the_top_10_players_2015to2018(data_df))
	print(the_highest_war_in_2018(data_df))
	print("among R, H, HR, RBI, SB, war, avg, OBP, SLG, the highest correlation with salary: ",
		  the_highest_salary(data_df))