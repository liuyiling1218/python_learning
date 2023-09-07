def displayInventory(inventory):
    count = 0
    print("Inventory:")
    for k, v in inventory.items():
        print('%d %s' % (v, k))
        count += v
    print('Total number of items:%d' % count)


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
# 第三题


def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)
    print(inventory)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inv, dragonLoot)
displayInventory(inventory)
