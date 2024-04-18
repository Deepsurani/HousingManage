import mysql.connector as dbCon
#database connect
def MyCon():
    con = dbCon.connect(host='localhost',user='root',passwd='',database='housing_society')
    return con

def isExist(TableName, ColumCompare, ColValue, PrimaryKey, KeyValue):
    con = MyCon()
    cur = con.cursor(buffered=True)
    cur.execute("Select * from {} Where {} = '{}' and {} != {}".format(TableName,ColumCompare,ColValue,PrimaryKey, KeyValue))
    # data = cur.fetchone()
    RowCount = cur.rowcount

    # if(data == None and cur.rowcount > 0):
    #     RowCount = cur.rowcount
    # else:
    #     RowCount = 0
    con.disconnect()
    con.close()
    cur.close()
    return RowCount


def isExistByQuery(SQLQuery):
    con = MyCon()
    cur = con.cursor(buffered=True)
    cur.execute(SQLQuery)
    # data = cur.fetchone()
    RowCount = cur.rowcount

    # if(data == None and cur.rowcount > 0):
    #     RowCount = cur.rowcount
    # else:
    #     RowCount = 0
    con.disconnect()
    con.close()
    cur.close()
    return RowCount

def GetSingleData(SQLQuery):
    try:
        con = MyCon()
        cur = con.cursor()
        cur.execute(SQLQuery)
        data = cur.fetchone()
        return(data)
    except dbCon.Error as error:
        print("Parameterized Query Failed {}".format(error))
    finally:
        if con.is_connected():
            cur.close()
            con.close()

def GetDataSet(SQLQuery):
    try:
        con = MyCon()
        cur = con.cursor()
        cur.execute(SQLQuery)
        data = cur.fetchall()
        return(data)
    except dbCon.Error as error:
        print("Parameterized Query Failed {}".format(error))
    finally:
        if con.is_connected():
            cur.close()
            con.close()
# Execute For Insert, Update 
def ExecuteQuery(SqlQuery):
    con = MyCon()
    cur = con.cursor()
    cur.execute(SqlQuery)
    con.commit()
    con.close()
    cur.close()

# GetMaxValue
def GetMaxVal(Table, PrimaryKey):
    con = MyCon()
    cur = con.cursor(buffered=True)
    cur.execute("Select Max({}) from {} order By {} DESC".format(PrimaryKey,Table,PrimaryKey))
    data = cur.fetchone()
    con.disconnect()
    con.close()
    cur.close()
    return data[0]


def handle_uploaded_file(f):
    with open('static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)
    return 'static/upload/'+f.name