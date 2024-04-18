from Admin.Crud.DbConnection import ExecuteQuery, GetDataSet, GetSingleData, MyCon, isExist

def IncomeExpanseTypeInsertUpdate(request):
    if request.method == "POST":
        ID = int(request.POST['hidId'])
        income_expance_type = request.POST['income_expance_type']
        status = request.POST['status']
        if(isExist("income_expance_type_tbl","income_expance_type",income_expance_type,"income_expance_type_id",ID) > 0):
            ctx = {
                'msg': 'This Income Expanse Type '+income_expance_type+ ' is Already Exist.',
                'status':'Exist'
            }
            return (ctx)
        con = MyCon()
        cur = con.cursor()
        if(ID != 0):
            SQLQuery ="update income_expance_type_tbl set income_expance_type='{}' , status='{}' Where income_expance_type_id={}".format(income_expance_type,status,ID)
        else:
            SQLQuery ="Insert into income_expance_type_tbl values(NULL,'{}','{}')".format(income_expance_type,status)
        cur.execute(SQLQuery)
        con.commit()
        if(ID != 0):
            ctx = {
                'msg':'Successfully Update a Data.',
                'status':"Success"
            }
        else:
            ctx = {
                'msg':'Successfully Insert a Data.',
                'status':"Success"
            }
        return (ctx)

############# Edit Member ############

################# Delete #############

def IncomeExpanseTypeDeleteCrud(id):
   Query = "Delete from income_expance_type_tbl Where income_expance_type_id={}".format(id)
   ExecuteQuery(Query)
   ctx = {
       'msg':'Successfully Delete Data'
   }
   return(ctx)
################# List ###########

def IncomeExpanseTypeListCrud():
    Query = "Select * from income_expance_type_tbl"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx