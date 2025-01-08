bids = {}
loop = True

while loop:
    tempname = input("What is your name?")
    tempbid = input("What is your bid?")
    bids[tempname] = tempbid
    choose = input("Is there anyone else? yes/no")
    if choose == "no":
        topbid = max(bids, key=lambda x: int(bids[x]))
        print(f'The winner is {topbid}')
        loop = False