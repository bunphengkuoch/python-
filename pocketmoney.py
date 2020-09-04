#Set amount of pocket money
pocket_money = 40.00
#Ask the user for the price of items until they can't afford anymore
while pocket_money>0:
 price=float(input("How much do you want to spend on this item?"))
 pocket_money -= price
 print("you have ${:.2f}left".format(pocket_money))
