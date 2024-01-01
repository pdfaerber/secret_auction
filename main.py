# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(f"{logo} \n \n")

bidder_list = []
new_bidder = {}
auction = True

while auction:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    new_bidder = {"name": name, "bid": bid}
    bidder_list.append(new_bidder)
    # see dictionary items added to list
    print(bidder_list)
    additional_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if additional_bidders == 'yes':
        auction
    else:
        print(f"The winner is {bidder_list[0]['name']} with a bid of ${bidder_list[0]['bid']}")
        auction = False




