from random import choice, randint

# Get Random Value from the List - Solution 1
friends = ['Sajid', 'Ayesha', 'Tausif', 'Ruksar']
# print(choice(friends))


# Solution 2
random_value_picker = randint(0, len(friends) - 1)
print(friends[random_value_picker])


# Add single value in the list
# friends.append("Shahid")

# Add multiple items to the list
# new_friends = ['Shahid', 'Nafisa']
# friends.extend(new_friends)

# Change the Value
# friends[0] = 'Sajid Shaikh'

# Remove 
# friends.remove('Sajid')

# Pop 
# friends.pop(0)

# Print List
# print(friends)



