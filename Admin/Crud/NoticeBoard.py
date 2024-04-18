from Admin.Crud.DbConnection import ExecuteQuery, GetDataSet, GetSingleData, MyCon, isExist

def NoticeBoardInsertUpdate(request):
    if request.method == "POST":
        ID = int(request.POST['hidId'])
        user_id =0
        notice_type = request.POST['notice_type']
        notice_board_title = request.POST['notice_board_title']
        notice_board_meesge = request.POST['notice_board_meesge']
        status = request.POST['status']
        if(isExist("notice_board_tbl","notice_type",notice_type,"notice_board_id",ID) > 0):
            ctx = {
                'msg': 'This Notice Board '+notice_type+ ' is Already Exist.',
                'status':'Exist'
            }
            return (ctx)
        con = MyCon()
        cur = con.cursor()
        if(ID != 0):
            SQLQuery ="update notice_board_tbl set user_id={}, notice_type='{}', notice_board_title='{}', notice_board_meesge='{}', status='{}' Where notice_board_id={}".format(user_id,notice_type,notice_board_title,notice_board_meesge,status,ID)
        else:
            SQLQuery ="Insert into notice_board_tbl values(NULL,{},'{}' ,'{}' ,'{}','{}' ,NOW())".format(user_id,notice_type,notice_board_title,notice_board_meesge,status)
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

def NoticeBoardEditCrud(id):
    Query= "Select * from notice_board_tbl Where notice_board_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)

def NoticeBoardDeleteCrud(id):
   Query = "Delete from notice_board_tbl Where notice_board_id={}".format(id)
   ExecuteQuery(Query)
   ctx = {
       'msg':'Successfully Delete Data'
   }
   return(ctx)

def NoticeBoardListCrud():
    Query = "Select * from notice_board_tbl"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx