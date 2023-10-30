'''
 A secret auction program
'''
# Import the modules 
print("Welcome to the secret auction program")

# Create an empty dictionary
all_bids = {}

#Check if the bid is still on 
bid_finished = False

while not bid_finished:
    # Ask the user for the name and the bid amount
    name = input("What is your name? \n")
    amount = int(input("How much do you want to place for the auction? \n"))
    # Append to the empty dictionary
    all_bids[name] = amount
    is_on = input("Are there other bidders? Please type 'yes' or 'no' \n").lower()
    if is_on == 'no':
        #clear screen
        bid_finished = True

print(all_bids)
# Create a function to loop through the dict 

def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for name,bid_amount in bids.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with an amount of {highest_bid}")
    
highest_bidder(all_bids)





