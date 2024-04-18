from Admin.Crud.DbConnection import *

def IncomeExpenseInsertUpdate(request):
    if request.method == "POST":
        ID = int(request.POST['hidId'])
        type = request.POST['type']
        income_expance_type_id = request.POST['income_expance_type_id']
        income_expance_from = request.POST['income_expance_from']
        income_expance_amount =request.POST['income_expance_amount']
        payment_type = request.POST['payment_type']
        remarks = request.POST['remarks']
        con = MyCon()
        cur = con.cursor()
        # if(isExist("income_expance_tbl","income_expance_type_id",income_expance_type_id,"income_expance_from",ID) > 0):
        #     ctx = {
        #         'msg': 'This Income Expense ' +income_expance_type_id+ ' is Already Exist.',
        #         'status':'Exist'
        #     }
        #     return (ctx)
        con = MyCon()
        cur = con.cursor()
        if(ID != 0):
            SQLQuery ="update income_expance_tbl set type='{}', income_expance_type_id={} , income_expance_from='{}', income_expance_amount='{}' ,  payment_type='{}' , remarks='{}' Where income_expance_id={}".format(type,income_expance_type_id,income_expance_from,income_expance_amount,payment_type,remarks,ID)
        else:
            SQLQuery ="Insert into income_expance_tbl values(NULL,'{}',{},'{}',{},'{}','{}',NOW())".format(type,income_expance_type_id,income_expance_from,income_expance_amount,payment_type,remarks)
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
    
def IncomeExpenseEditCrud(id):
    Query= "Select * from income_expance_tbl Where income_expance_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)

def IncomeExpenseDeleteCrud(id):
   Query = "Delete from income_expance_tbl Where income_expance_id={}".format(id)
   ExecuteQuery(Query)
   ctx = {
       'msg':'Successfully Delete Data'
   }
   return(ctx)


def IncomeExpenseListCrud():
    Query = "select iet.*, iett.income_expance_type from income_expance_tbl as iet left join income_expance_type_tbl as iett on iet.income_expance_type_id=iett.income_expance_type_id"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx


################################################################################################### Reports

# def IncomeExpanseTypeSingleData(id):
#     Query = "Select * from income_expance_type_tbl Where income_expance_type_id={}".format(id)
#     list = GetSingleData(Query)
#     ctx = {
#         'Data' : list
#     }
#     return(ctx)

# def IncomeSingleDateWiseCrud(StartDate):
#     Query = "Select * from income_expance_tbl Where date(entry_Date) = date('{}')".format(StartDate)
#     list = GetDataSet(Query)
#     ctx = {
#         'List' : list
#     }
#     return ctx
# List End
# Select * from ride_booking_view Where date(Enter_date) BETWEEN date('2023-05-01') and date('2023-05-30')

def IncomeExpanseDateWiseCrud(StartDate,EndDate):
    Query = "Select * from  incomexpance_tbl Where date(entry_date) BETWEEN date('{}') and date('{}')".format(StartDate, EndDate)
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx
# List End



# List Start
def IncomeExpanseSingleDateWiseCrud(StartDate):
    Query = "Select * from  incomexpance_tbl Where date(entry_date) = date('{}')".format(StartDate)
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx