def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    pass

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)