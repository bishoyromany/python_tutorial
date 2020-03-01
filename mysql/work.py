import database

users = database.fetchAllUsers()

for i in users:
    print('Name : '+i[0]+' And Email : '+i[1])
