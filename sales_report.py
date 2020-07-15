"""Generate sales report showing total melons each salesperson sold.

Note: This is code provided to me in an assignment and my work is simply to add
comments to explain what the existing code is doing.
"""

def get_melons_sold_per_salesperson(log_file_path):

    melon_sales = {}


    with open('sales-report.txt') as f: #This opens the text file of melon sales info
    
        for line in f: #This loops through the file, line by line
            line = line.rstrip() #This strips the trailing whitespace from each line
            entries = line.split('|') #This parses the data per line and put into a list
            #print("entries:", entries)
            #Get name of salesperson and number of melons sold, add to dictionary
            
            #If salesperson in the list, increment their # of melons sold at their index, 
            #otherwise add their name and melons sold. Ignore total amount $ in lines.
            
            salesperson = entries[0]
            total_amount_sold = entries[1]
            number_melons_sold = entries[2]
            #Or could do: salesperson, total_amount_sold, number_melons_sold = line.split("|")

            if salesperson in melon_sales:
                melon_sales[salesperson] = melon_sales[salesperson] + int(number_melons_sold)
            else:
                melon_sales[salesperson] = int(number_melons_sold) 
            
            #Or could do: melon_sales[salesperson] = melon_sales.get(salesperson, int(number_melons_sold) + int(number_melons_sold))

    return melon_sales
    
    
#Loop over salespeople and use it to index 
#print("salespeople:", salespeople)
#print("melons:", melons)
#print("melons_sold:", melons_sold)

def print_sales_report(melon_sales):
    for salesperson, number_melons_sold in melon_sales.items():
        print(f'{salesperson} sold {number_melons_sold} melons') #display sales/person
    
print_sales_report(get_melons_sold_per_salesperson("sales-report.txt"))

#ABOVE IS REFACTORED CODE FOR CODING EXERCISE. WE STARTED WITH THE CODE BELOW.
#Note: This is code provided to me in an assignment and my work is simply to add
#comments to explain what the existing code is doing.
#"""


# salespeople = [] #List to capture sales people's names
# melons_sold = [] #List to capture the number of melons sold per salesperson

# f = open('sales-report.txt') #This opens the text file of melon sales info
# for line in f: #This loops through the file, line by line
#     line = line.rstrip() #This strips the trailing whitespace from each line
#     entries = line.split('|') #This parses the data per line and put into a list

#     #Get name of salesperson and number of melons sold
#     salesperson = entries[0] #This takes the first item per line and assigns it
#     melons = int(entries[2]) #This converts the 3rd item to int and assign it

#     #If salesperson in the list, increment their # of melons sold at their index, 
#     #otherwise add their name and melons sold. Ignore total amount $ in lines.
#     if salesperson in salespeople: #For each salesperson in the list, get index
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons #This increments the melons sold/person.
#     else:
#         salespeople.append(salesperson) #If new salesperson, add to list
#         melons_sold.append(melons) #If new salesperson, add their melons to list

# #Loop over salespeople and use it to index 
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons') #display sales/person

