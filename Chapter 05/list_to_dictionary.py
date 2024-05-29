def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('\nTotal number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)