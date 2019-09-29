
"""
----------------------------------------------------------------
                   *Imports section*
----------------------------------------------------------------
"""
import pyodbc as odbc
import array as arr
from datetime import datetime
"""
----------------------------------------------------------------
"""

"""
----------------------------------------------------------------
           *Declaration of user defined functions*
----------------------------------------------------------------
"""
#This function returns the time in a specific format for the log.
def fn_formattime (time):
    return time.strftime("%d/%m/%Y %H:%M:%S.%f")
"""
----------------------------------------------------------------
"""


"""
----------------------------------------------------------------
               *Declaration of the variables*
----------------------------------------------------------------
"""
arYears = arr.array('i',[])
Now = datetime.now()
strServerName = "."
strDatabaseName = "ResellerSales"
strUserName = "sa"
strPassword = "sql"
strGetYears = """
                        SELECT DISTINCT
                            YEAR(OrderDate) [Order_Year]
                        FROM [ResellerSales].[dbo].[SalesOrderHeader]
                        ORDER BY YEAR(OrderDate)
                """
"""
----------------------------------------------------------------
"""


"""
----------------------------------------------------------------
                    *Section of logic*
----------------------------------------------------------------
"""
#Getting a connection to the local host
print("--> Establish the connection with the database.")
cnSQLServer = odbc.connect('DRIVER={SQL Server};SERVER='+strServerName+';DATABASE='+strDatabaseName+';UID='+strUserName+';PWD='+ strPassword)
print("--> Connection was established ok!")
print("-->")
print("-->")
print("-->")
print("-->")
#Trying get info of the connection :/
#print("-[ACCESS MODE]: " + odbc.sqlget + "-")
#print("-[DATABASE NAME]: " + odbc.SQL_DATABASE_NAME + "-")

cnCursor = cnSQLServer.cursor()
#Started querying to the database
cnCursor.execute(strGetYears)

print("--> The first query was obtain the following values:")
print("--> [arYears]:")
for cnRow in cnCursor:
    arYears.append(cnRow.Order_Year)
    print("--> [arYears.value()]: " + str(cnRow.Order_Year))

cnSQLServer.commit()
print("-->")
print("-->")
print("-->")
print("-->")

print("--> These values was use for create tables in the database and insert the data.")

print("-->")
print("-->")
print("-->")
print("-->")

for intYear in arYears:
    print("--> Creating table for specific year")

    strTableName = 'Temp_' + str(intYear)
    print("--> The table to create is: " + strTableName)
    print("--> The process for the table " + strTableName + " start at the " + fn_formattime(datetime.now()))

    strCreateTable = """
                            IF EXISTS (
                                SELECT *
                                    FROM sys.tables
                                    JOIN sys.schemas
                                        ON sys.tables.schema_id = sys.schemas.schema_id
                                WHERE sys.schemas.name = N'dbo'
                                    AND sys.tables.name = N'""" + strTableName + """'
                            )
                                DROP TABLE dbo.""" + strTableName + """

                            IF OBJECT_ID('dbo.""" + strTableName + """', 'U') IS NOT NULL
                            DROP TABLE dbo.""" + strTableName + """
                            
                            CREATE TABLE dbo.""" + strTableName + """
                            (
                                ID INT NOT NULL PRIMARY KEY IDENTITY (1,100),
                                SalesOrderNumber [NVARCHAR](40) NOT NULL,
                                ResellerKey [INT]  NOT NULL,
                                EmployeeID [INT]  NULL,
                                OrderDate [DATETIME] NULL,
                                ShipDate [DATETIME] NULL,
                                PaymentType [INT] NULL
                            );
                        """
    cnCursor.execute(strCreateTable)
    print("--> Creation its done !" )
    ##cnSQLServer.commit()
    
    print("--> Start with the population of the table: " + strTableName)
    #In the following section of code, i inserted the data in the temporal table.
    strGetDataByYear = """INSERT INTO dbo.""" + strTableName + """ (SalesOrderNumber,ResellerKey,EmployeeID,OrderDate,ShipDate,PaymentType)"""
    strGetDataByYear += """
                                SELECT
                                    SalesOrderNumber
                                    ,ResellerKey
                                    ,EmployeeID
                                    ,OrderDate
                                    ,ShipDate
                                    ,PaymentType
                                FROM [ResellerSales].[dbo].[SalesOrderHeader]
                                WHERE YEAR(OrderDate) = ?
                                ORDER BY OrderDate
                        """
    cnCursor.execute(strGetDataByYear,intYear)
    print("--> It's done!. The population for the table " + strTableName + " finished at the " + fn_formattime(datetime.now()))
    print("-->")
    print("-->")
    print("-->")
    print("-->")

print("--> The query its done!")
cnSQLServer.commit()
"""
----------------------------------------------------------------
"""