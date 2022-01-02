
# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# print(stuff.keys[1])
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(v,k)
        item_total=item_total+v

    print("Total number of items: " + str(item_total))

displayInventory(stuff)
print(stuff['torch'])

def addToInventory(inventory, addedItems):
    # your code goes here
    for newItem in addedItems:
        if newItem not in inventory.keys():
            inventory[newItem]=1
        else:
            a=inventory[newItem]+1
            inventory[newItem]=a
    return inventory
        

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print()
displayInventory(inv)