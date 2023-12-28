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
    bid = input("What is your bid?: $")

    add_auction(name, bid, keep_add_auction)

    other_bidder = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    
    if other_bidder == 'no':
        keep_add_auction = False

    clear()
print(auction)