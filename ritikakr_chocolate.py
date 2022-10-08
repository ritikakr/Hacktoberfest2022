money=int(input('Money you have: '))
item=int(input('Money spend in purchasing an item: '))
chocolate=int(input('Price of chocolate: '))
map = money-item
if( map > chocolate):
    print('.....Yes we can purchase a chocloate.....')
elif(map == chocolate):
    print('.....exact money left for buying choclate....')
else:
    print('......No cmoney to purchase chocolate....')
print('______check_______')
if(map > 0):
    saving = map - chocolate
    print('saving=',saving)
else:
    print('No saving')

