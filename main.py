# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo


print(f"{logo} \n \n")
name = input("What is your name? ")
bid = int(input("What is your bid? "))
auction = True
while auction:
    bidder_dictionary = {"name": name, "bid": bid}
    additional_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if additional_bidders == 'no':
        print(f"The winner is {bidder_dictionary['name']} with a bid of ${bidder_dictionary['bid']}")
    auction = False

print(f"\n\n{bidder_dictionary}")


# add_bidder(name, bid)

