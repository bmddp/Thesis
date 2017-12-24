import pandas as pd

data_frame = pd.read_csv('person.csv')

alldata = []

for index, data in data_frame.iterrows():
	single = {'Bedtime': str(int(data['Bedtime'])) + 'B', 'Breakfast': str(int(data['Breakfast'])) + 'M', 'Dinner': str(int(data['Dinner'])) + 'D', 'Lunch': str(int(data['Lunch'])) + 'L'}
	alldata.append(single)

data_frame = pd.DataFrame.from_dict(data=alldata, orient='columns')
data_frame.to_csv('person_apiori.csv', index=0)


