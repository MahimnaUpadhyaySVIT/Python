import mysql.connector as mysql

# Connect to Database
def DB_CONNECTION():
    return mysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="starwars"
    )

# Creating a cursor object
DB_CONFIG = DB_CONNECTION()
cursor = DB_CONFIG.cursor()

# Fetch JEDI
def FetchJEDI():
    getJEDI = """SELECT * FROM JEDI;"""
    result = cursor.execute(getJEDI)
    for jedi in cursor.fetchall():
        print(jedi)
    DB_CONFIG.close()

# Add JEDI
def AddJEDI(name, rank, saber_color):
    addJEDI = """
        INSERT INTO JEDI(name, rank, saber_color) VALUES(%s, %s, %s);
    """
    result = cursor.execute(addJEDI, (name, rank, saber_color))
    print(result)
    DB_CONFIG.commit()
    DB_CONFIG.close()

# Delete Employees
def deleteJEDI(jedi_ID):
    deleteJEDI = """
        DELETE FROM JEDI WHERE jedi_ID = %s;
    """
    result = cursor.execute(deleteJEDI, (jedi_ID,))
    print(result)
    DB_CONFIG.commit()
    DB_CONFIG.close()

# DB OPERATIONS
while True:
    print("Choose which Operation to perform: \n")
    print("1. Select \n 2. Insert \n 3. Delete \n 4. Exit")
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        FetchJEDI()
    elif(choice == 2):
        jedi_name = input("Enter Jedi Name: ")
        jedi_rank = input("Enter Jedi Rank: ")
        jedi_saber_color = input("Enter Saber Color: ")
        AddJEDI(name=jedi_name,rank=jedi_rank, saber_color=jedi_saber_color)
    elif(choice == 3):
        id = int(input("Enter jedi id number: "))
        deleteJEDI(jedi_ID=id)
    elif(choice == 4):
        print("Exiting...")
        break
    else:
        print("Enter valid operation number")