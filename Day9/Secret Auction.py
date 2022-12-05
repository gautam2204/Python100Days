from Day9.logo import logo

print(logo)

newBidder = True


def results(details):
    tempkey = ""
    tempVal = 0
    for key in details:
        val = details[key]
        if val>tempVal:
            tempVal=val
            tempkey=key

    print(f"{tempkey} won the bid his bid was {tempVal}")


bid_details = {}
while newBidder:
    name = input("Enter bidder's name")
    price = int(input("Enter bid"))

    bid_details[name] = price
    bool = input("Any more bidder").lower()
    if bool == "no":
        newBidder = False
        results(bid_details)
    elif bool == "yes":
        print("Continue")
