from Admin.Crud.DbConnection import ExecuteQuery, GetDataSet, GetSingleData, MyCon, isExist

def HouseInsertUpdate(request):
    if request.method == "POST":
        ID = int(request.POST['hidId'])
        house_no = request.POST['house_no']
        house_type_id = request.POST['house_type_id']
        house_sub_typ = request.POST['house_sub_typ']
        building_no =request.POST['building_no']
        floor =request.POST['floor']
        address =request.POST['address']
        house_facility =request.POST['house_facility']
        status =request.POST['status']

        if(isExist("house_tbl","house_no",house_no,"house_id",ID) > 0):
            message = {
                'msg': 'This House No '+house_no+ ' is Already Exist.',
                'status':'Exist'
            }
            return (message)
        con = MyCon()
        cur = con.cursor()
        if(ID != 0):
            SQLQuery ="update house_tbl set house_no='{}' , house_type_id={} , house_sub_typ='{}' , building_no='{}', floor='{}', address='{}', house_facility='{}', status='{}' Where house_id={}".format(house_no,house_type_id,house_sub_typ,building_no,floor,address,house_facility,status,ID)
        else:
            SQLQuery ="Insert into house_tbl values(NULL,'{}',{},'{}','{}','{}','{}','{}','{}',NOW())".format(house_no,house_type_id,house_sub_typ,building_no,floor,address,house_facility,status)
        cur.execute(SQLQuery)
        con.commit()
        if(ID != 0):
            ctx = {
                'msg':'Successfully Update a House.',
                'status':"Success"
            }
        else:
            ctx = {
                'msg':'Successfully Insert a House.',
                'status':"Success"
            }
        return ctx

############# Edit House ############

def HouseEditCrud(id):
    Query = "Select * from house_tbl Where house_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)
################# Delete House #############

def HouseDeleteCrud(id):
    Query = "Delete from house_tbl Where house_id={}".format(id)
    ExecuteQuery(Query)
    ctx = {
        'msg':'Successfully Delete Data'
    }
    return(ctx)
################# List House ###########

def HouseListCrud():
    Query = "Select * from house_view"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx