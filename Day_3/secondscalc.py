#Seconds calculator

years = int(input("Enter the number of years:"))

def totalsecs(years):
    return 60*60*24*365*years

print(f"There are {totalsecs(years):,} seconds  in {years} years")