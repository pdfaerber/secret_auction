# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo


print(logo)
name = input("What is your name? ")
bid = input("What is your Bid? ")

def get_bidder(name, bid):
    bidder_dictionary = {}
    bidder_dictionary["name"] = name
    bidder_dictionary["bid"] = bid

get_bidder(name, bid)

