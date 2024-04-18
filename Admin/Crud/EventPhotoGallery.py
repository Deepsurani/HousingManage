from Admin.Crud.DbConnection import *

def EventPhotoGalleryInsertUpdate(request):
    if request.method == "POST":
        Id = int(request.POST['hidId'])
        events_id = request.POST['events_id']
        photo_title = request.POST['photo_title']
        # photo = request.POST['photo']
        photo = handle_uploaded_file(request.FILES['photo'])
        discription =request.POST['discription']

        if(isExist("event_photo_gallary_tbl","photo_title",photo_title,"event_photo_gallary_id",Id) > 0):
            message = {
                'msg': 'This Event Photo '+photo_title+ ' is Already Exist.',
                'status':'Exist'
            }
            return (message)
        con = MyCon()
        cur = con.cursor()
        if(Id != 0):
            SQLQuery ="update event_photo_gallary_tbl set events_id={} , photo_title='{}' , photo='{}' , discription='{}' Where event_photo_gallary_id={}".format(events_id,photo_title,photo,discription,Id)
        else:
            SQLQuery ="Insert into event_photo_gallary_tbl values(NULL,{},'{}','{}','{}',NOW())".format(events_id,photo_title,photo,discription)
        cur.execute(SQLQuery)
        con.commit()
        if(Id != 0):
            ctx = {
                'msg':'Successfully Update a Event Photo.',
                'status':"Success"
            }
        else:
            ctx = {
                'msg':'Successfully Insert a Event Photo.',
                'status':"Success"
            }
        return ctx

############# Edit Member ############

def EventPhotoEditCrud(id):
    Query = "Select * from event_photo_gallary_tbl Where event_photo_gallary_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)
################# Delete #############

def EventPhotoDeleteCrud(id):
    Query = "Delete from event_photo_gallary_tbl Where event_photo_gallary_id={}".format(id)
    ExecuteQuery(Query)
    ctx = {
        'msg':'Successfully Delete Data'
    }
    return(ctx)
################# List ###########

def EventPhotoListCrud():
    Query = "Select * from event_photo_gallary_view"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx