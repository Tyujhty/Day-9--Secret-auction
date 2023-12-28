from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction.\nWho's going to win the auction?")

auction = []
keep_add_auction = True

def add_auction(name, bid):
    new_auction = {'name': name, 'bid': bid}
    auction.append(new_auction)

while keep_add_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    add_auction(name, bid)

    other_bidder = input("Are there any other bidders? Type 'Yes' or 'No':\n").lower()

    if other_bidder == 'no':
        keep_add_auction = False
        print("Goodbye!")
    
    clear()

highest_auction = 0
name_winner = ""

for bid in auction:
    if bid['bid'] > highest_auction:
        highest_auction = bid['bid']
        name_winner = bid['name']

print(f"The winner is {name_winner} with a bid of ${highest_auction}")
