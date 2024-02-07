shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# continue
for item in shopping_list:
    if item == 'spam':
        continue
    print("Buy " + item)

# break
for item in shopping_list:
    if item == 'spam':
        break
    print("Buy " + item)

item_to_find = "spam"
found_at = None

for item in shopping_list:
    if item == item_to_find:
        found_at = shopping_list.index(item)
        break

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

# Different ways to loop through the list
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

