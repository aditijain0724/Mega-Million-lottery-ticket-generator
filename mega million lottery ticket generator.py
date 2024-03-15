import random as r
from tabulate import tabulate

#asking the user for number of tickets 
numOfTickets = int(input("How many tickets would you like? "))
print()
print("My {} Mega Millions ticket:".format(numOfTickets))
print()
# Initialize an empty list to store all tickets.
ticketsData = []

#giving the range for for loop as the user input
for n in range(numOfTickets):
    lottoNumbers = [] #initializing a empty list
    while len(lottoNumbers) < 5: 
        lottoNumber = r.randint(1, 76) #randomly generating a number
        if lottoNumber not in lottoNumbers: #giving the condition to check if the number is repeating
            lottoNumbers.append(lottoNumber) #if it passes the check then adding it into the lottonumbers list
            
    megaBallNumber = r.randint(1,25)
    
    lottoNumbers.sort() #sorting the list in ascending order
    
    ticketsData.append([n+1] + lottoNumbers + [megaBallNumber])

 #creating column names list   
colnames = ['Ticket', 'Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5', 'Mega Ball']  
#displaying table with style set to simple
print(tabulate(ticketsData, colnames, tablefmt="simple"))
