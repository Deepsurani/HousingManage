from Admin.Crud.DbConnection import *
from Admin.Crud.user import CreateUser

def MemberInsertUpdate(request):
    if request.method == "POST":
        ID = int(request.POST['hidId'])
        user_id = int(request.POST['user_id'])
        member_name = request.POST['member_name']
        gender = request.POST['gender']
        house_id =request.POST['house_id']
        in_house_member = request.POST['in_house_member']
        children_count = request.POST['children_count']
        adult_count = request.POST['adult_count']
        business_or_job = request.POST['business_or_job']
        business_job_title = request.POST['business_job_title']
        business_job_address = request.POST['business_job_address']
        status = request.POST['status']

        if(ID == 0):
            email = request.POST['email']
            password = request.POST['password']
            mobile = request.POST['mobile']
            UserModel = {
                'user_id': 0,
                'user_role':  'Member',
                'username':  member_name,
                'email':  email,
                'password': password,
                'mobile':  mobile,
                'status':  status
            }
            user_id = CreateUser(UserModel)
        if(user_id > 0):
            Query = "Select * from member_tbl Where user_id={} and house_id={} and member_id != {}".format(user_id, house_id, ID)
            if(isExistByQuery(Query) > 0):
                message = {
                    'msg': 'This House Member is Already Exist.',
                    'status':'Exist'
                }
                return (message)
            if(ID != 0):
                SQLQuery ="update member_tbl set user_id={} , member_name='{}' , gender='{}' , house_id={} , in_house_member={} , children_count={} , adult_count={} , business_or_job='{}' , business_job_title='{}' , business_job_address='{}' , status='{}' Where member_id={}".format(user_id,member_name,gender,house_id,in_house_member,children_count,adult_count,business_or_job,business_job_title,business_job_address,status,ID)
            else:
                SQLQuery ="Insert into member_tbl values(NULL,{},'{}','{}',{},{},{},{},'{}','{}','{}', NOW(),'{}')".format(user_id,member_name,gender,house_id,in_house_member,children_count,adult_count,business_or_job,business_job_title,business_job_address,status)
            ExecuteQuery(SQLQuery)
            if(ID != 0):
                ctx = {
                    'msg':'Successfully Update a Member.',
                    'status':"Success"
                }
            else:
                ctx = {
                    'msg':'Successfully Insert a Member.',
                    'status':"Success"
                }
        else:
            ctx = {
                'msg':'This Email or Mobile No is Already Exist.',
                'status': 'Exist'
            }

        return ctx

############# Edit Member ############

def MemberEditCrud(id):
    Query = "Select * from member_view Where member_id={}".format(id)
    list = GetSingleData(Query)
    ctx = {
        'Data' : list
    }
    return(ctx)
################# Delete #############

def MemberDeleteCrud(id):
    Query = "Delete From user_tbl Where user_id In (Select user_id From member_tbl Where member_id={})".format(id)
    ExecuteQuery(Query)
    Query = "Delete from member_tbl Where member_id={}".format(id)
    ExecuteQuery(Query)
    ctx = {
        'msg':'Successfully Delete Data'
    }
    return(ctx)
################# Delete #############


################# List ###########

def MemberListCrud():
    Query = "Select * from member_view"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx

##########################-------Report Start-------#######################

# Delete Start
def HousingChangeStatusCrud(request):
    if request.method == "POST":
        ID = int(request.POST['hidId'])
        status = request.POST['status']
        Query = "Update member_tbl SET status='{}' Where member_id={}".format(status, ID)
        ExecuteQuery(Query)
        ctx = {
            'msg' : 'Successfully Update Status.',
            'status':1
        }
        return ctx
# Edit End


# List Start
def HousingDateWiseCrud(StartDate,EndDate):
    Query = "Select * from member_view Where date(entry_Date) BETWEEN date('{}') and date('{}')".format(StartDate, EndDate)
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx
# List End



# List Start
def HousingSingleDateWiseCrud(StartDate):
    Query = "Select * from member_view Where date(entry_Date) = date('{}')".format(StartDate)
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx
# List End
# Select * from ride_booking_view Where date(Enter_date) BETWEEN date('2023-05-01') and date('2023-05-30')