from Admin.Crud.DbConnection import GetDataSet, GetSingleData, MyCon, isExist
import mysql.connector as dbCon

# HouseType Insert-Update Start
def HouseTypeInsert(request):
    if request.method == 'POST':
        try:
            Type = request.POST['txtHouseType']
            Status = request.POST['dropStatus']
            ID = int(request.POST['hidId'])
            if(isExist("house_type_tbl","house_type",Type,"house_type_id",ID) > 0):
                message = {
                    'msg': 'This House Type '+Type+ ' is Already Exist.',
                    'status':'Exist'
                }
                return (message)
            con = MyCon()
            if(ID != 0):
                SQLQuery ="update house_type_tbl set House_type='{}' , Status='{}' Where house_type_id={}".format(Type,Status,ID)
            else:
                SQLQuery ="Insert into house_type_tbl values(NULL,'{}','{}')".format(Type,Status)
        
            # SqlQuery = "Insert into house_type_tbl values(NULL,%s, %s)"
            # Params = (Type,Status)
            # cur.execute(SqlQuery, Params)

            cur = con.cursor(prepared=True)
            cur.execute(SQLQuery)
            con.commit()
            if con.is_connected():
                con.close()
            cur.close()
            if(ID != 0):
                ctx = {
                    'msg':'Successfully Update a House Type.',
                    'status':"Success"
                }
            else:
                ctx = {
                    'msg':'Successfully Insert a House Type.',
                    'status':"Success"
                }
            return ctx
        except dbCon.Error as error:
            print("Parameterized Query Failed {}".format(error))
# HouseType Insert-Update End

#HouseType Single Data
def HouseEditRegistration(id):
    Query = "Select * from house_type_tbl Where house_type_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)

def HouseTypeDelete(id):
    con = MyCon()
    cur = con.cursor()
    cur.execute("Delete from house_type_tbl Where house_type_id={}".format(id))
    con.commit()
    con.close()
    cur.close()
    message = {
        'msg':'Successfully Save Data.'
    }
    return(message)

def HouseType_List():
    Query = "Select * from house_type_tbl"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx