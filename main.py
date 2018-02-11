import pymysql

f = open(r"students.csv", "r")

fString = f.read()

# print(fString)

fList = []

for i in fString.split('\n'):
    fList.append(i.split(','))

# print(fList[1][0])

#FIRST PARAM = LOCALHOST 
#SECOND PARAM = USER
#THIRD PARAM = USER PASSWORD 
#FOURTH PARAM = NAME OF DB
db = pymysql.connect("localhost", "root", "", "TEST")
cursor = db.cursor()

# cursor.execute("DROP TABLE IF EXISTS STUDENTS")

# FIRST_NAMEOne = fList[0][0]; LAST_NAME = fList[0][1]; AGE = fList[0][2]; GENDER = fList[0][3]; DEGREE =  fList[0][4]

# QS = """CREATE TABLE STUDENTS(
#                     {} VARCHAR(255) NOT NULL, 
#                     {} VARCHAR(255) NOT NULL, 
#                     {}  INT,
#                     {}  CHAR(1),
#                     {}  CHAR(2)
#                  )""".format(FIRST_NAMEOne, LAST_NAME, AGE, GENDER, DEGREE)

# cursor.execute(QS)

# # del 
# del fList[0]

# #generate multiple values from the list to be placed in a query
# rows = ''

# for i in range(len(fList) - 1):
#     rows += "('{}', '{}', '{}', '{}', '{}')".format(fList[i][0], fList[i][1], fList[i][2], fList[i][3], fList[i][4])
#     if i != len(fList) - 2:
#         rows += ','

# # print(rows)

# #used to make sure the last value is not comma 
# QS2 = "INSERT INTO STUDENTS VALUES" + rows

# try:
#     cursor.execute(QS2)
#     db.commit()
# except:
#     db.rollback()

name = ''; lastName = ''; age = 0; gender = ''; degree = ''
enterQ = ''

print("\nPRESS 1 TO ADD A NEW STUDENTS")
print("PRESS 2 TO SELECT * FROM STUDENTS")
print("PRESS 3 TO DELETE A STUDENT FROM DATABASE")
print("PRESS 4 TO UPDATE A STUDENTS")
print("PRESS 5 TO EXIT")
var = int(input("\nENTER A NUMBER: "))

#WHILE THE OPTION IS NOT 3 THE LOOP COUNTINUES TO RUN
while var != 5:
    #THIS OPTION ALLOWES THE USER TO ADD A STUDENT TO THE DATABASE 
    if var == 1:
        name = input("Enter a First name: ")
        lastName = input("Enter a Lastname: ")
        age = int(input("Enter a age: "))
        gender = input("Enter Gender: ")
        degree = input("Enter degree: ")
        #PRINTS OUT THE ENTERED VALUES 
        print(name, lastName, age, gender, degree)

        #THE QUERY WHICH ENTERS VALUES INTO THE DATABASE 
        enterQ += "('{}', '{}', '{}', '{}', '{}')".format(name, lastName, age, gender,degree)
        QS3 = "INSERT INTO STUDENTS VALUES" + enterQ
        #TRY AND CATCH 
        try:
            cursor.execute(QS3)
            db.commit()
        except:
            db.rollback()
    #THIS IS THE SECOND OPTION WHICH DISPLAYS ALL THE STUDENTS IN THE DATABASE 
    elif var == 2:
        sql = "SELECT * FROM STUDENTS"
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        print("\n")
        i =0

        for row in results:
            i += 1
            print("Student: ", i, " " , row)
    #this will delete a student from databases
    elif var == 3:

        #ask for the name that is going to be deleted 
        NAME = input("Enter a First name that you'd like to delete: ")
        #query to delete from database
        query = "DELETE FROM STUDENTS WHERE FIRST_NAMEOne like '%s'" % (NAME,)

        #TRY AND CATCH 
        try:
            cursor.execute(query)
            db.commit()
        except:
            db.rollback() 
    #this will update the student 
    if var == 4:
        #ask for the name that is going to be updated 
        NAME = input("Enter a First name that you'd like to update: ")

        sql = "SELECT * FROM STUDENTS WHERE FIRST_NAMEOne like '%s'" % (NAME,)
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        print("\n")
        i =0

        for row in results:
            i += 1
            print("Student: ", i, " " , row)

        if i > 0 :
            
            NAMEUPDATE = input("Enter a First name to update: ")
            UPDATELASTNAME = input("Enter a lastename to update: ")
            UPDATE_AGE = input("Enter age to update: ")
            UPDATE_GEND = input("Enter gender to update: ")
            UPDATE_DEGREE = input("Enter degree to update: ")

            query = "UPDATE STUDENTS SET FIRST_NAMEOne='%s', LAST_NAME='%s', Age='%s', GENDER='%s', DEGREE='%s' WHERE FIRST_NAMEONE LIKE '%s'" % (NAMEUPDATE,UPDATELASTNAME,UPDATE_AGE,UPDATE_GEND,UPDATE_DEGREE,NAME)

            #TRY AND CATCH 
            try:
                cursor.execute(query)
                db.commit()
            except:
                db.rollback() 
        else:
            print("Not in database")          
    else:
        print("\nYOU HAVE EXITED!!!")

    print("\nPRESS 1 TO ADD A NEW STUDENTS")
    print("PRESS 2 TO SELECT * FROM STUDENTS")
    print("PRESS 3 TO DELETE A STUDENT FROM DATABASE")
    print("PRESS 4 TO UPDATE A STUDENTS")
    print("PRESS 5 TO EXIT")
    var = int(input("\nENTER A NUMBER: "))
#end of while loop    
db.close()