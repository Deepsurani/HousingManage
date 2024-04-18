from Admin.Crud.DbConnection import *

def SponsorInsertUpdate(request):
    if request.method == "POST":
        Id = int(request.POST['hidId'])
        event_id =request.POST['event_id']
        sponser_name = request.POST['sponser_name']
        business_name = request.POST['business_name']
        contat_no = request.POST['contat_no']
        business_address = request.POST['business_address']
        sponser_amount = request.POST['sponser_amount']
        
        ExistQuery = "Select * from sponser_tbl Where sponser_name='{}' and event_id={} and sponser_id != {}".format(sponser_name, event_id, Id)
        if(isExistByQuery(ExistQuery) > 0):
            message = {
                'msg': 'This Sponser  '+sponser_name+ ' is Already Exist for Selected Event.',
                'status':'Exist'
            }
            return (message)



        con = MyCon()
        cur = con.cursor()
        if(Id != 0):
            SQLQuery ="update sponser_tbl set event_id={} , sponser_name='{}' , business_name='{}' , contat_no='{}' ,  business_address='{}'  , sponser_amount={} Where sponser_id={}".format(event_id,sponser_name,business_name,contat_no,business_address,sponser_amount,Id)
        else:
            SQLQuery ="Insert into sponser_tbl values(NULL,{} ,'{}' ,'{}','{}','{}',{},NOW())".format(event_id,sponser_name,business_name,contat_no,business_address,sponser_amount)
        cur.execute(SQLQuery)
        con.commit()
        if(Id != 0):
            ctx = {
                'msg':'Successfully Update a Sponsor.',
                'status':"Success"
            }
        else:
            ctx = {
                'msg':'Successfully Insert a Sponsor.',
                'status':"Success"
            }
        return ctx

def SponsorEditCrud(id):
    Query = "Select * from sponser_tbl Where sponser_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)

def SponsorDeleteCrud(id):
    Query = "Delete from sponser_tbl Where sponser_id={}".format(id)
    ExecuteQuery(Query)
    ctx = {
        'msg':'Successfully Delete Data'
    }
    return(ctx)

def SponsorListCrud():
    Query = "Select * from sponsor_view"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx