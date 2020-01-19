import mysql.connector

def connectDatabase(database=False):
    if database == False:
        return mysql.connector.connect(host="localhost" , user="root" , passwd="")
    else:
        global mydb
        global cursor

        mydb = mysql.connector.connect(host="localhost" , user="root" , passwd="" , database=database)
        cursor = mydb.cursor()

        return True

def databases():
    connection = connectDatabase(False)
    mycursor = connection.cursor()
    mycursor.execute('show databases')
    result = mycursor.fetchall()
    return result

def insertUser(values):
    for i in values:
        query = 'INSERT INTO `users` (name , email)  VALUES(%s , %s)'
        val   = i
        cursor.execute(query , val)
        mydb.commit()

def inserUserInput():
    username = str(input('Please Write Your Name '))
    email = str(input('Please Write Your Email '))
    insertUser([(username , email)])
    print('User {} Inserted Successfully'.format(username))
    allUsers = fetchAllUsers()
    print('We Have Now {} Users And This is The Full List {}'.format(len(allUsers) , allUsers))

    return True


def fetchAllUsers():
    cursor.execute('SELECT * FROM `users`')
    result = cursor.fetchall()
    return result

if __name__ == '__main__':

    try:
        mydb
        cursor
    except NameError:
        connectDatabase('python')

    print(vars())


