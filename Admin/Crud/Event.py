from Admin.Crud.DbConnection import *

def EventInsertUpdate(request):
    if request.method == "POST":
        Id = int(request.POST['hidId'])
        title = request.POST['title']
        # thumbnil = request.POST['thumbnil']
        event_date = request.POST['event_date']
        discription = request.POST['discription']
        any_theme = request.POST['any_theme']
        contribution = request.POST['contribution']
        status = request.POST['status']

        thumbnil = handle_uploaded_file(request.FILES['thumbnil'])

        if(isExist("events_tbl","title",title,"events_id",Id) > 0):
            message = {
                'msg': 'This Event '+title+ ' is Already Exist.',
                'status':'Exist'
            }
            return (message)
        con = MyCon()
        cur = con.cursor()
        if(Id != 0):
            SQLQuery ="update events_tbl set title='{}' , thumbnil='{}' , event_date='{}' , discription='{}' , any_theme='{}' , contribution={} , status='{}' Where events_id={}".format(title,thumbnil,event_date,discription,any_theme,contribution,status,Id)
        else:
            SQLQuery ="Insert into events_tbl values(NULL,'{}','{}','{}','{}','{}',{},'{}',NOW())".format(title,thumbnil,event_date,discription,any_theme,contribution,status)
        cur.execute(SQLQuery)
        con.commit()
        if(Id != 0):
            ctx = {
                'msg':'Successfully Update a Event.',
                'status':"Success"
            }
        else:
            ctx = {
                'msg':'Successfully Insert a Event.',
                'status':"Success"
            }
        return ctx

############# Edit Event ############

def EventEditCrud(id):
    Query = "Select * from events_tbl Where events_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)

################# Delete Event #############

def EventDeleteCrud(id):
    Query = "Delete from events_tbl Where events_id={}".format(id)
    ExecuteQuery(Query)
    ctx = {
        'msg':'Successfully Delete Data'
    }
    return(ctx)

################# List ###########
def EventListCrud():
    Query = "Select * from events_tbl"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx