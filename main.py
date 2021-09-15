from tabulate import tabulate

#In order for this app to work you will need to install "tabulate" to make Table
#For description how to install --->(https://pypi.org/project/tabulate/)

print("\n  ++-----------------------++")
print("   ++-------------------++")
print("Welcome To Interest Calculator ")
print("   ++-------------------++")
print("  ++-----------------------++\n")

#Ask user to input year,interest,capital amount

ask_typ_save = int(input('How do you want to save,'
                        'please choose an option below.\n1.Monthly\n2'
                        '.Once with capital for many years\n:'))
if ask_typ_save == 1:
  capital = float(input('What is your amount capital? '))
  monthly = float(input('The amount you want to save monthly? '))
  year = int(input("How many years you want to save? "))
  intrest = int(input("What interest rate do you have? ")) 
elif ask_typ_save == 2:
  capital = float(input('What is your amount capital? '))
  year = int(input("How many years you want to save? "))
  intrest = int(input("What interest rate do you have? ")) 
  monthly = 0

period = 1 #Yearly calculation
#Create empty lists
year_list=[]
f_amount_year_list=[]
f_amount_month_list=[]
intrest_list = []
b_amount_list = [capital]
table = []

#To get the final amount for each year with interest
def get_final_amount_list(capt,intres,year,month,period):
  if capt == 0:
    capt = 1
  count = 1
  while count <= year:
    if month != 0:
      #these formulas have been used from this website(https://rikatillsammans.se/ranta-pa-ranta-formler-excels-slutvarde-och-min-kalkylator/)
      f_amount_year = capt * (1+intres /100)**count
      #these formulas have been used from this website(https://rikatillsammans.se/ranta-pa-ranta-formler-excels-slutvarde-och-min-kalkylator/)
      f_amount_month = f_amount_year + ((month * 12)/period)*((1+intres/period*(1/100))**(period * year) - 1) * period/ (intres * 1/100)
      f_amount_month_list.append(f_amount_month)
      count +=1
    else:
      f_amount_year = capt * (1+intres /100)**count
      f_amount_year_list.append(f_amount_year)
      count +=1
  if monthly:
    return f_amount_month_list
  else:    
    return f_amount_year_list

#To get all interest for each year
def get_intrest_list():
  for a in get_final_amount_list(capital,intrest,year,monthly,period):
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
  for y,b,i,f in zip(get_year_list(year),get_b_amount_list(capital),get_intrest_list(),get_final_amount_list(capital,intrest,year,monthly,period)):
    table.append((y,b,i,f))
  headers = ["Year","At the beginning of the year",f"Return in {intrest} % Yearly","At the end of the year"]
    
  print(tabulate(table, headers, tablefmt="grid",numalign="left"))  

print_table()