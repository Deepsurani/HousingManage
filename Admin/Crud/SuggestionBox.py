from Admin.Crud.DbConnection import ExecuteQuery, GetDataSet, GetSingleData, MyCon

def SuggestionBoxInsertUpdate(request):
    if request.method == "POST":
        Id = int(request.POST['hidId'])
        user_id = request.session["User"]
        suggestion_type = request.POST['suggestion_type']
        suggestion_description = request.POST['suggestion_description']
        remarks = request.POST['remarks']
        status = request.POST['status']

        con = MyCon()
        cur = con.cursor()
        if(Id != 0):
            SQLQuery ="update suggestion_box_tbl set user_id={}, suggestion_type='{}', suggestion_description='{}', remarks='{}', status='{}' Where suggestion_box_id={}".format(user_id,suggestion_type,suggestion_description,remarks,status,Id)
        else:
            SQLQuery ="Insert into suggestion_box_tbl values(NULL,{},'{}','{}','{}','{}',NOW())".format(user_id,suggestion_type,suggestion_description,remarks,status)
        cur.execute(SQLQuery)
        con.commit()
        
        if(Id != 0):
            ctx = {
                'msg':'Successfully Update a Data.',
                'status':"Success"
            }
        else:
            ctx = {
                'msg':'Your Complain is Successfully Submit.',
                'status':"Success"
            }
        return (ctx)

def SuggestionBoxEditCrud(id):
    Query = "Select * from suggestion_box_tbl Where suggestion_box_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)

def SuggestionBoxDeleteCrud(id):
    Query = "Delete from suggestion_box_tbl Where suggestion_box_id={}".format(id)
    ExecuteQuery(Query)
    ctx = {
        'msg':'Successfully Delete Data'
    }
    return(ctx)

def SuggestionBoxListCrud():
    Query = "Select * from suggestion_box_view"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx