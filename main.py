from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction. \nWho's going to win the auction ?")

auction =  []
keep_add_auction = True

def add_auction(name, bid, keep_add_auction):
    new_auction = {'name': name, 'bid': bid}
    auction.append(new_auction)

while keep_add_auction != False:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    add_auction(name, bid, keep_add_auction)
    
    highest_auction = auction[0]['bid']
    name_winner = auction[0]['name']
    
    if bid > highest_auction:
        highest_auction = bid
        name_winner = name

    other_bidder = input("Are there any other bidders? Type 'Yes' or 'No':\n").lower()
    
    if other_bidder == 'no':
        keep_add_auction = False
        print("Goodbye !")

    clear()

print(f"The winner is {name} with a bid of ${bid}")