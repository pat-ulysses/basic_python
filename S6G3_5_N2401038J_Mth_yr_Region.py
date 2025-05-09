"""
Recording link: tbd
Password (if any) : https://drive.google.com/file/d/1gvl6zihMWdGtVNxbwygstjoy5_ng9khc/view?usp=sharing

Scenario 5: 5.	Analysis on Monthly Electricity Consumption for all regions over 
                last 5 years of data collected (inclusive of Year 2023)
                
You are given AvgHouseholdElectricity.csv file by the interviewer during an
interview for an intern position in a department. 
The dataset contains electricity consumption data collected between the year 
2010 and 2023. You are to conduct analysis based on the dataset given, and 
provide some insights to the marketing director of the company from the output 
of the analysis.

The following are the deliverables of your analysis:
1.  Accept user input for Month.

2.  Tabulate as per following format (note: the year must be in ascending order):
 ____________________________________________________________________
        Jan consumption summary         
 ____________________________________________________________________
|        |Central    |North      |West       |North East |East       |
 ____________________________________________________________________
|2019    |       0.00|       0.00|       0.00|       0.00|       0.00|
|2020    |       0.00|       0.00|       0.00|       0.00|       0.00|
|2021    |       0.00|       0.00|       0.00|       0.00|       0.00|
|2022    |       0.00|       0.00|       0.00|       0.00|       0.00|
|2023    |       0.00|       0.00|       0.00|       0.00|       0.00|
 ____________________________________________________________________
	
3.	Your program should include capability to provide a summary of the insights 
based on the results of your table in part 2.

4.	Your program should allow for analysis in part 2 to be continued if required.

5.  To value add to the analysis, you are required to think of one additional 
analysis that the marketing director may be interested to find out after 
part 4 is completed. Present the solution and explain how such analysis 
adds value the insights.

IMPORTANT: You must use the original dataset given, you are not allowed to use 
excel or any other application software to modify the data before importing 
it to your python program.

"""

# Reading CSV file contents
with open("AvgHouseHoldElectricity.csv", "r") as f:
    csv_content = f.readlines()

# Function to get the user input for the month
def get_month():
    while True:
        month = input('Please input a month (1-12): ')
        try:
            month = int(month)
            if 1 <= month <= 12:
                return month
            else:
                print("Please enter a valid month number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 12.")

def continue_or_not():
    while True:
        cont = input("Do you want to continue with another analysis? (y/n): ").lower()
        if cont == 'y':
            return "y"
        elif cont == 'n':
            return "n"
        else:
            print("Invalid input, please enter 'y' to continue or 'n' to stop.")
    

# Function to tabulate the results for the selected month
def tabulate_results(data, month_input):
    filtered_data = {}
    for line in csv_content[1:]:
        line.replace("\n","")
        dwelling_type, year, month, region, location, kwh_per_acc = line.strip().split(',')
        
        year = int(year)
        month = int(month)
        kwh_per_acc = float(kwh_per_acc)
        region=region.strip().lower()

        if 2019 <= year <= 2023 and month==month_input:
            if year not in filtered_data:
                filtered_data[year] = {"central region": 0, "north region": 0, "west region": 0, "north east region": 0, "east region": 0}

            if region in filtered_data[year]:
                filtered_data[year][region] += kwh_per_acc

    return filtered_data

# Function to display the results
def display_table(data, month_name):
    print(f"________________________________________________________________________")
    print(f"|       {month_name + ' consumption summary':^41}                       |")
    print(f"________________________________________________________________________")
    print(f"|Year       |Central    |North      |West       |North East |East       |")
    print(f"________________________________________________________________________")
    
    for year in sorted(data):
        central = data[year]["central region"]
        north = data[year]["north region"]
        west = data[year]["west region"]
        northeast = data[year]["north east region"]
        east = data[year]["east region"]
        print(f"|{year:>11}|{central:>11.2f}|{north:>11.2f}|{west:>11.2f}|{northeast:>11.2f}|{east:>11.2f}|")
    
    print(f"________________________________________________________________________")
    

def summary(data, month_input):
    region_data = {}
    
    for line in csv_content[1:]:
        line = line.replace("\n", "")
        dwelling_type, year, month, region, location, kwh_per_acc = line.strip().split(',')

        year = int(year)
        month = int(month)
        kwh_per_acc = float(kwh_per_acc)
        region = region.strip().lower()

        if 2019 <= year <= 2023 and month == month_input:       
            if region not in region_data:
                region_data[region] = {2019: 0, 2020: 0, 2021: 0, 2022: 0, 2023: 0}
            
            region_data[region][year] += kwh_per_acc

    # Calculate maximum for each region
    maximum = {"central region": 0, "north region": 0, "west region": 0, "north east region": 0, "east region": 0}
    for region in region_data:
        temp = 0
        for year in region_data[region]:
            if region_data[region][year] >= temp:
                temp = region_data[region][year]
        maximum[region] = float(temp)

    #Calculating min for each region
    minimum={"central region":0,"north region":0,"west region":0,"north east region":0,"east region":0}
    for region in region_data:
        temp=1000000
        for year in region_data[region]:
            if region_data[region][year]<=temp and region_data[region][year]>0:
                temp=region_data[region][year]
            else :
                continue
        minimum[region]=float(temp)
    
    # Calculate the mean aggregated by region
    mean_region = {"central region": 0, "north region": 0, "west region": 0, "north east region": 0, "east region": 0}
    
    if month_input<=6:
        count_years=5
    else:
        count_years=4
        
    for region in region_data:
        total = 0
        for year in region_data[region]:
            total += region_data[region][year]
        avg = total / count_years
        mean_region[region] = avg

    # Calculate maximum for each year
    maximum_year = {2019:0, 2020:0, 2021:0, 2022:0, 2023:0}
    for year in data:
        temp = 0
        for region in data[year]:
            if data[year][region] >= temp:
                temp = data[year][region]
        maximum_year[year] = float(temp)
        
    # Calculate minimum for each year
    minimum_year = {2019: 0, 2020: 0, 2021: 0, 2022: 0, 2023: 0}
    for year in data:
        temp = 1000000
        for region in data[year]:
            if data[year][region] <= temp and data[year][region]>0:
                temp = data[year][region]
        minimum_year[year] = float(temp)

    #Calculating Mean Aggregated by Year
    mean_year={2019:0,2020:0,2021:0,2022:0,2023:0} 
    for year in data:
        total=0
        for region in data[year]:
            total+=data[year][region]
        avg=total/5
        mean_year[year]=avg
        
    return maximum, minimum, mean_region, maximum_year, minimum_year, mean_year

def display_summary(maximum,minimum,mean_region,maximum_year,minimum_year,mean_year,month_names):
    # Insights by region
    print("\n")
    print("="*75)
    print(f"{'Summary Insights Table':^75}")
    print('_'*75)
    print(f"|{month_names + ' insights by region':^74}|")
    print('_'*75)
    print(f"|{'Region':18}|{'Maximum':13}|{'Minimum':13}|{'Average':13}|{'Range':13}|")
    print('_'*75)
    
    for region in maximum:
        print(f"|{region:<18}|{maximum[region]:>13.2f}|{minimum[region]:>13.2f}|{mean_region[region]:>13.2f}|{maximum[region]-minimum[region]:>13.2f}|")
    print('_'*75)
    
    #Insights by Year
    print('_'*62)
    print(f"|{month_names + ' insights by years':^60}|")
    print('_'*62)
    print(f"|{'Year':18}|{'Maximum':13}|{'Minimum':13}|{'Average':13}|")
    print('_'*62)
    
    for year in maximum_year:
        print(f"|{year:<18}|{maximum_year[year]:>13.2f}|{minimum_year[year]:>13.2f}|{mean_year[year]:>13.2f}|")
    print('_'*62)
    

def additional_analysis():
    additional_data={"central region":[],"north region":[],"west region":[],"north east region":[],"east region":[]}
    for line in csv_content[1:]:
        line.replace("\n","")
        dwelling_type, year, month, region, location, kwh_per_acc = line.strip().split(',')
        
        year = int(year)
        month = int(month)
        kwh_per_acc = float(kwh_per_acc)
        region=region.strip().lower()
        
        if 2019 <= year <= 2023:
            additional_data[region].append(kwh_per_acc)
        
    additional_summary={"central region":{"average":0,"standard deviation":0,"q1":0,"median":0,"q3":0},
                        "north region":{"average":0,"standard deviation":0,"q1":0,"median":0,"q3":0},
                        "west region":{"average":0,"standard deviation":0,"q1":0,"median":0,"q3":0},
                        "north east region":{"average":0,"standard deviation":0,"q1":0,"median":0,"q3":0},
                        "east region":{"average":0,"standard deviation":0,"q1":0,"median":0,"q3":0}}

    for region in additional_summary:
        # Calculate the Mean
        mean = sum(additional_data[region]) / len(additional_data[region])
        additional_summary[region]["average"] = mean
    
        # Calculate the standard deviation
        sum_of_squared_diffs = 0
        for value in additional_data[region]:
            squared_diff = (value - mean) ** 2
            sum_of_squared_diffs += squared_diff
        std = (sum_of_squared_diffs / len(additional_data[region])) ** 0.5
        additional_summary[region]["standard deviation"] = std
    
    def rundown_quantile(sorted_data, q):
        n = len(sorted_data)
        pos = int(q * n)  
        return sorted_data[pos - 1]  
    
    for region in additional_summary:
        sorted_data = sorted(additional_data[region])
        
        # Q1
        q1 = rundown_quantile(sorted_data, 0.25)
        additional_summary[region]["q1"] = q1
        
        # Median
        median = rundown_quantile(sorted_data, 0.50)
        additional_summary[region]["median"] = median
        
        # Q3
        q3 = rundown_quantile(sorted_data, 0.75)
        additional_summary[region]["q3"] = q3

    print('_' * 89)
    print(f"|{'Region Summary Statistics':^88}|")
    print('_' * 89)
    print(f"|{'Region':18}|{'Average':13}|{'Std Dev':13}|{'Q1':13}|{'Median':13}|{'Q3':13}|")
    print('_' * 89)
    
    for region in additional_summary:
        avg = additional_summary[region]["average"]
        std = additional_summary[region]["standard deviation"]
        q1 = additional_summary[region]["q1"]
        median = additional_summary[region]["median"]
        q3 = additional_summary[region]["q3"]
        
        print(f"|{region:<18}|{avg:>13.2f}|{std:>13.2f}|{q1:>13.2f}|{median:>13.2f}|{q3:>13.2f}|")
        
    print('_' * 89)
            
        
def main():
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    while True:
        month_input = get_month()
        filtered_data = tabulate_results(csv_content, month_input)
        display_table(filtered_data, month_names[month_input - 1])
        maximum, minimum, mean_region, maximum_year,minimum_year,mean_year = summary(filtered_data, month_input)
        display_summary(maximum, minimum, mean_region,maximum_year,minimum_year,mean_year,month_names[month_input - 1])
        choice=continue_or_not()
        if choice=="n":
            break
        else:
            continue
        
main()

print("\n")
print("Bonus Analysis!")

additional_analysis()