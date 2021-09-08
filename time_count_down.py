import datetime

user_input = input("enter your goal with a deadline seperated by colon \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
#calculate how many days from now till deadline
time_till = deadline_date - today_date
print (f" dear user time to reach your goal:{goal} is {time_till.days} days")


