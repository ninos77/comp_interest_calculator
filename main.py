from tabulate import tabulate

#In order for this app to work you will need to install "tabulate" to make Table
#For description how to install --->(https://pypi.org/project/tabulate/)

print("\n  ++-----------------------++")
print("   ++-------------------++")
print("Welcome To Interest Calculator ")
print("   ++-------------------++")
print("  ++-----------------------++\n")

#Ask user to input year,interest,capital amount
year = int(input("How many years you want to save? "))
intrest = int(input("What interest rate do you have? "))
capital = float(input('The amount you want to save? '))

#Create empty lists
year_list=[]
f_amount_list=[]
intrest_list = []
b_amount_list = [capital]
table = []

#To get the final amount for each year with interest
def get_final_amount_list(capt,intres,year):
  count = 1
  while count <= year:
    f_amount = capt * (1+intres /100)**count
    f_amount_list.append(f_amount)
    count +=1
  return f_amount_list

#To get all interest for each year
def get_intrest_list():
  for a in get_final_amount_list(capital,intrest,year):
    i_amount = a - capital
    intrest_list.append(i_amount)
  return intrest_list  

#fetching user's input year and put them on a list
def get_year_list(year):
  for n in range(1,year+1):
    year_list.append(n)
  return year_list   

#fetching the new capital amount in the beginning of the year
def get_b_amount_list(capt):
  for i in get_intrest_list():
    b_amount_list.append(capt + i)
  return b_amount_list  

# prints table as mentioned you need to install 'tabulate'--->(https://pypi.org/project/tabulate/) 
def print_table():
  for y,b,i,f in zip(get_year_list(year),get_b_amount_list(capital),get_intrest_list(),get_final_amount_list(capital,intrest,year)):
    table.append((y,b,i,f))
  headers = ["Year","At the beginning of the year",f"Return in {intrest} % ","At the end of the year"]
    
  print(tabulate(table, headers, tablefmt="grid",numalign="left"))  

print_table()