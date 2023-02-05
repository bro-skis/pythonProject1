print("please enter number of days you travelled:")
days_travelled = int(input())

full_weeks = days_travelled // 7
days_remaining = days_travelled % 7

print( days_travelled, "days are", full_weeks, "weeks and", days_remaining, "days" )