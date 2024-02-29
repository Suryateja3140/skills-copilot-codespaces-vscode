import pandas as pd
userPlayData= pd.read_csv('UserGamePlayData.csv')
depositData= pd.read_csv('depositData.csv')
withdrawalData= pd.read_csv('withdrawalData.csv')

# 1. Find Playerwise Loyalty points earned by Players in the following slots:-
# a. 2nd October Slot S1

userPlayData['Datetime'] = pd.to_datetime(userPlayData['Datetime'], format="%d-%m-%Y %H:%M")
start_date = pd.Timestamp('2022-10-02')

# Filter data based on the time condition (greater than 12 AM and less than 12 PM)
time_condition = (userPlayData['Datetime'].dt.hour >= 0) & (userPlayData['Datetime'].dt.hour < 12) & (userPlayData['Datetime'].dt.date == start_date.date())
filtered_data = userPlayData[time_condition]
result = filtered_data[['User ID', 'Games Played', 'Datetime']]
result.to_excel("Test.xlsx", index=False)
depositData['Datetime'] = pd.to_datetime(depositData['Datetime'], format="%d-%m-%Y %H:%M")
depositData.rename(columns={'Amount': 'Deposit Amount'}, inplace=True)
withdrawalData.rename(columns={'Amount': 'WithDrawal Amount'}, inplace=True)
withdrawalData['Datetime'] = pd.to_datetime(withdrawalData['Datetime'], format="%d-%m-%Y %H:%M")
merged_data = pd.merge(depositData, result, left_on = ['User Id', 'Datetime'], right_on=['User ID', 'Datetime'], how='inner')
merged_data1 = pd.merge(withdrawalData, merged_data, left_on = ['User Id', 'Datetime'], right_on=['User ID', 'Datetime'], how='inner')
print(merged_data1)


#b. 16th October Slot S2

start_date_six = pd.Timestamp('2022-10-16')
time_condition_slot2= (userPlayData['Datetime'].dt.hour >= 12) & (userPlayData['Datetime'].dt.hour < 24) & (userPlayData['Datetime'].dt.date == start_date_six.date())
filtered_data1 = userPlayData[time_condition_slot2]
data = filtered_data1[['User ID', 'Games Played', 'Datetime']]
merged_data3 = pd.merge(depositData, data, left_on = ['User Id', 'Datetime'], right_on=['User ID', 'Datetime'], how='inner')
merged_data4 = pd.merge(withdrawalData, merged_data3, left_on = ['User Id', 'Datetime'], right_on=['User ID', 'Datetime'], how='inner')
print(merged_data4)


#c. 18th October Slot S1

start_date_six_1 = pd.Timestamp('2022-10-18')
time_condition_slot3= (userPlayData['Datetime'].dt.hour >= 0) & (userPlayData['Datetime'].dt.hour < 12) & (userPlayData['Datetime'].dt.date == start_date_six_1.date())
filtered_data2 = userPlayData[time_condition_slot3]
data1 = filtered_data2[['User ID', 'Games Played', 'Datetime']]
merged_data5 = pd.merge(depositData, data1, left_on = ['User Id', 'Datetime'], right_on=['User ID', 'Datetime'], how='inner')
merged_data6 = pd.merge(withdrawalData, merged_data5, left_on = ['User Id', 'Datetime'], right_on=['User ID', 'Datetime'], how='inner')
print(merged_data6)


#b. 26th October Slot S2

start_date_six_2 = pd.Timestamp('2022-10-18')
time_condition_slot4= (userPlayData['Datetime'].dt.hour >= 0) & (userPlayData['Datetime'].dt.hour < 12) & (userPlayData['Datetime'].dt.date == start_date_six_2.date())
filtered_data3 = userPlayData[time_condition_slot3]
data2 = filtered_data3[['User ID', 'Games Played', 'Datetime']]
merged_data7 = pd.merge(depositData, data2, left_on = ['User Id', 'Datetime'], right_on=['User ID', 'Datetime'], how='inner')
merged_data8 = pd.merge(withdrawalData, merged_data7, left_on = ['User Id', 'Datetime'], right_on=['User ID', 'Datetime'], how='inner')
print(merged_data6)





















