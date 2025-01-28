import pandas as pd 
screen_time = [2,4,6,7,8]
sleep_hours = [7,7,8,6,3]
stu_name = ["Srujan","Ajay","Venky","Manu","Mani"]
dict1 = {
    "screen_time":screen_time,
    "sleep_hours":sleep_hours,
    "stu_name":stu_name
}
print(dict1)
df = pd.DataFrame(dict1)
print(df)
