import cx_Oracle
con = cx_Oracle.connect("system/dinesh@localhost/xe")
cur = con.cursor()

cur.execute(
            """
                    drop table Bank

            """
)

con.commit() #saves changes to the database
con.close()
