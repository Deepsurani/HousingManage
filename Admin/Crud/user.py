from Admin.Crud.DbConnection import *


def CreateUser(UserModel):
    user_id = UserModel.get("user_id")
    user_role = UserModel.get("user_role")
    username = UserModel.get("username")
    email = UserModel.get("email")
    password = UserModel.get("password")
    mobile = UserModel.get("mobile")
    status = UserModel.get("status")
    Query = "Select * from user_tbl Where email='{}' or mobile = '{}'".format(
        username, mobile)
    if (isExistByQuery(Query) > 0):
        return 0
    SQLQuery = "Insert into user_tbl values(NULL,'{}','{}','{}','{}','{}','{}',NOW())".format(
        user_role, username, email, password, mobile, status)
    ExecuteQuery(SQLQuery)
    return GetMaxVal('user_tbl', 'user_id')


def UserInsert(request):
    if request.method == "POST":
        user_id = int(request.POST['hidId'])
        user_role = request.POST['user_role']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        status = request.POST['status']
        UserModel = {
            'user_id': user_id,
            'user_role':  user_role,
            'username':  username,
            'email':  email,
            'password': password,
            'mobile':  mobile,
            'status':  status
        }
        user_id = CreateUser(UserModel)
        if(user_id > 0):
            ctx = {
                'msg':'Successfully Create User',
                'user_id': user_id
            }
        else:
            ctx = {
                'msg':'This User is Already Exist.',
                'user_id': user_id
            }
        return ctx

# edit DAta


def UserEdit(id):
    con = MyCon()
    cur = con.cursor()
    cur.execute("Select * from user_tbl Where user_id={}".format(id))
    data = cur.fetchone()
    return (data)


def UserDelete(id):
    con = MyCon()
    cur = con.cursor()
    cur.execute("Delete from user_tbl Where user_id={}".format(id))
    con.commit()
    con.close()
    cur.close()
    message = {
        'msg': 'Successfully Save Data.'}
    return (message)


def UserType_List():
    con = MyCon()
    cur = con.cursor()
    cur.execute("Select * from user_tbl")
    data = cur.fetchall()
    con.close()
    cur.close()
    return data


def LoginCrud(request):
    if request.method == "POST":
        Password = request.POST['password']
        email = request.POST['email']
        Query = "Select * from user_tbl Where email='{}' and password = '{}'".format(email, Password)
        if (isExistByQuery(Query) > 0):
            Data = GetSingleData(Query)
            ctx = {
                'msg': 'SuccessFully Login To Your Account',
                'status':1,
                'UserId':Data[0],
                'UserName':Data[2],
                'UserRole':Data[1],
            }
            return ctx
        else:
            ctx = {
                    'msg': 'Your Email or Password is Wrong.',
                    'status':0,
                    'UserId':0,
                    'UserName':'',
                    'UserRole':''
                }
    return ctx