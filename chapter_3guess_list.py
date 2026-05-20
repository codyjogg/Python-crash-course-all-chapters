guest_list = ['grandpa', 'mom', 'dad']

message_1 = f"{guest_list[1].title()} I understand you can't make it, we will hangout soon!"
print(message_1)

guest_list[1] = 'alex'

print(guest_list)

message_2 = f"{guest_list[0].title()} You're invited to the dinner!"
message_3 = f"{guest_list[1].title()} Hey babe I invited you to dinner with the fam!"
message_4 = f"Hey {guest_list[2].title()} You're invited to the dinner with {guest_list[0].title()}, {guest_list[1].title()}, and I!"

print(message_2)
print(message_3)
print(message_4)

print('We found a bigger table everyone!')

guest_list.insert(0, 'michelle')
guest_list.insert(2, 'zack')
guest_list.append('ana')
guest_list.append('mom')
print(guest_list)

new_message_1 = f"Hey {guest_list[0].title()} You're invited to the upcoming dinner this Friday!"
new_message_2 = f"Hi {guest_list[1].title()} I hope this finds you well! You're invited to Friday's dinner!"
new_message_3 = f"{guest_list[2].title()} What's up bro i'm inviting you to dinner with the fam bam! Friday be there!"
new_message_4 = f"{guest_list[3].title()} Hey babe I know were married and you already know this lol. But you're coming with me to dinner Friday!"
new_message_5 = f"{guest_list[4].title()} It's been a few weeks! Come enjoy a nice steak dinner with the family!"
new_message_6 = f"{guest_list[5].title()} I love that you're now part of our wonderful family! Come to dinner, hangout, and have fun!"
new_message_7 = f"{guest_list[6].title()} Hey I'm glad you're able to come back and make it! Let's go! we all can have a big family dinner!"


print(new_message_1)
print(new_message_2)
print(new_message_3)
print(new_message_4)
print(new_message_5)
print(new_message_6)
print(new_message_7)

# we made a message to all guests that the dinner table wont arrive in time
new_message_8 = f"Hey {guest_list} sadly the other dinner table won't arrive in time. So I can only invite two people."
print(new_message_8)
# okay now we need to start removing guest from the list because we wont have enough spots
old_guest1 = guest_list.pop()
print(guest_list)
print(f"I'm sorry {old_guest1.title()} but due to the table arriving late we won't be able to have you attend dinner.")
old_guest2 = guest_list.pop()
print(guest_list)
print(f"I apologize {old_guest2.title()} sadly we won't have a seat available for dinner.")
old_guest3 = guest_list.pop()
print(guest_list)
print(f"Hey {old_guest3.title()} I am sorry but we won't have enough spots at dinner.")
old_guest4 = guest_list.pop()
print(guest_list)
print(f"Hey {old_guest4.title()} babe i'm sorry but you're no longer invited to dinner lol")
old_guest5 = guest_list.pop()
print(guest_list)
print(f"Hey {old_guest5.title()} we won't have enough seats at dinner.")
print(guest_list)

# now that all other guest have been un-invited we can message two remaining guest that they are still invited

print(f"{guest_list[0].title()} Hey you're still invited to dinner! Can't wait to see you!")
print(f"{guest_list[1].title()} You're still invited to dinner!")

# Now that we messaged the remaining guests we can move forward to delete both their names from the list
# and then make sure that they are actually deleted from the list
print(guest_list)
del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)
