day=int(input("enter the date (1 to 31):"))
month=int(input("enter the month(1 to 12):"))
year=int(input("enter the year(eg-2012):"))
print(f"entered date:{day:02d}-{month:02d}-{year}")
if(year%4==0 and year%100!=0)or(year%400==0):
    print(f"{year}, is a leap year")
else:
    print("it is not leap year")