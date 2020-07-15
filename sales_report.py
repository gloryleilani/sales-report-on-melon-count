"""Generate sales report showing total melons each salesperson sold.

Note: This is code provided to me in an assignment and my work is simply to add
comments to explain what the existing code is doing.
"""


salespeople = [] #List to capture sales people's names
melons_sold = [] #List to capture the number of melons sold per salesperson

f = open('sales-report.txt') #This opens the text file of melon sales info
for line in f: #This loops through the file, line by line
    line = line.rstrip() #This strips the trailing whitespace from each line
    entries = line.split('|') #This parses the data per line and put into a list

    #Get name of salesperson and number of melons sold
    salesperson = entries[0] #This takes the first item per line and assigns it
    melons = int(entries[2]) #This converts the 3rd item to int and assign it

    #If salesperson in the list, increment their # of melons sold at their index, 
    #otherwise add their name and melons sold. Ignore total amount $ in lines.
    if salesperson in salespeople: #For each salesperson in the list, get index
        position = salespeople.index(salesperson)
        melons_sold[position] += melons #This increments the melons sold/person.
    else:
        salespeople.append(salesperson) #If new salesperson, add to list
        melons_sold.append(melons) #If new salesperson, add their melons to list

#Loop over salespeople and use it to index 
#print("salespeople:", salespeople)
#print("melons:", melons)
#print("melons_sold:", melons_sold)
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #display sales/person
