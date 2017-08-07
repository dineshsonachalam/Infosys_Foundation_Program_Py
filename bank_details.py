import cx_Oracle
con = cx_Oracle.connect("system/dinesh@localhost/xe")
cur = con.cursor()

cur.execute(
            """
                    CREATE TABLE Bank
                    (

                        AccountNo INT PRIMARY KEY ,
                        Password VARCHAR2(30),
                        First_Name VARCHAR2(20) ,
                        Last_name VARCHAR2(30),
                        Address VARCHAR2(30),
                        Balance INT  NOT NULL,
                        Admin INT  NOT NULL

                    )

            """
)

con.commit() #saves changes to the database
con.close()
