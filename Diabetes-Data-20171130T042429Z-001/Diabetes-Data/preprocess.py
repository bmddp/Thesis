import pandas as pd
import numpy as np

np.random.seed(42)

fileNumbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70']

def get_time_table(time):
    time = time.replace(":", "")
    time = int(time)
    if time < 1200:
        return "Breakfast"
    elif 1200 <= time < 1600:
        return "Lunch"
    elif 1600 <= time < 2000:
        return "Dinner"
    elif 2000 <= time < 2400:
        return "Bedtime"


def get_presented_data(temp_data, _code):
    data_list = []
    for row in temp_data.iterrows():
        if row[1][2] == _code:
            single = {"date": row[1][0], "time": get_time_table(row[1][1]), "code": row[1][2], "level": row[1][3]}
            data_list.append(single)
    
    temp_all_data = [
        {'date': data_list[0]['date'], 'code': str(data_list[0]['code']), 'Breakfast': 0, 'Lunch': 0, 'Dinner': 0, 'Bedtime': 0}]
    i = 0
    for data in data_list:
        if temp_all_data[i]['date'] != data['date']:
            temp_all_data.append(
                {'date': data['date'], 'code': str(data['code']), 'Breakfast': 0, 'Lunch': 0, 'Dinner': 0, 'Bedtime': 0})
            i += 1
        temp_all_data[i][data['time']] = data['level']
    return temp_all_data

all_data = []

temp_data01 = pd.read_csv('datasets/data-'+fileNumbers[16], header=None, delim_whitespace=True)
all_data.extend(get_presented_data(temp_data01, 33))

data_frame = pd.DataFrame.from_dict(data=all_data, orient='columns')
loaded_frame = pd.read_csv('person.csv')

frames = [data_frame, loaded_frame]
result_frame = pd.concat(frames)

result_frame.to_csv('person.csv', index=0)
