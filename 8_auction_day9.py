import os
import operator
from dataclasses import dataclass

@dataclass
class Bid:
    name: str
    bid: int
bids = []
sorted_bids = []

def main():
    print("Welcome to the auction program!")
    again = True
    while again:
        name = input("What is your name? ")
        bid = input("What is your bid? $")
        bids.append(Bid(name,bid))
        anybidders = input("Are there any other bidders? Type 'yes' or 'no' ")
        if anybidders != "yes":
            again = False
            sorted_bids = sorted(bids, key=operator.attrgetter('bid'))
            winner = sorted_bids[-1]
            print(f"Winner is {winner.name} with bid of ${winner.bid}")
        else:
            os.system("clear")
main()