from Admin.Crud.DbConnection import ExecuteQuery, GetDataSet, GetSingleData, MyCon, isExist


def MeetingTypeInsertUpdate(request):
    if request.method == "POST":
        ID = int(request.POST['hidId'])
        meeting_agenda = request.POST['meeting_agenda']
        meeting_description = request.POST['meeting_description']
        meeting_type = request.POST['meeting_type']
        meeting_date = request.POST['meeting_date']
        meeting_time = request.POST['meeting_time']
        remarks = request.POST['remarks']
        status = request.POST['status']
        
        if(isExist("meeting_tbl","meeting_agenda",meeting_agenda,"meeting_id",ID) > 0):
            ctx = {
                'msg': 'This Meeting Agenda '+meeting_agenda+ ' is Already Exist.',
                'status':'Exist'
            }
            return (ctx)
        con = MyCon()
        cur = con.cursor()
        if(ID != 0):
            SQLQuery ="update meeting_tbl set meeting_agenda='{}' , meeting_description='{}' , meeting_type='{}' , meeting_date='{}' , meeting_time='{}' , remarks='{}' , status='{}' Where meeting_id={}".format(meeting_agenda,meeting_description,meeting_type,meeting_date,meeting_time,remarks,status,ID)
        else:
            SQLQuery ="Insert into meeting_tbl values(NULL,'{}','{}','{}','{}','{}','{}','{}',NOW())".format(meeting_agenda,meeting_description,meeting_type,meeting_date,meeting_time,remarks,status)
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

#edit DAta
def MeetingEditCrud(id):
    Query = "Select * from meeting_tbl Where meeting_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)

def MeetingDeleteCrud(id):
    Query = "Delete from meeting_tbl Where meeting_id={}".format(id)
    ExecuteQuery(Query)
    ctx = {
        'msg':'Successfully Delete Data'
    }
    return(ctx)

def MeetingTypeListCrud():
    Query = "Select * from meeting_tbl"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx