import datetime
from Admin.Crud.DbConnection import ExecuteQuery, GetDataSet, GetSingleData, MyCon, isExist

def SocietyRuleInsertUpdate(request):
    if request.method == "POST":
        ID = int(request.POST['hidId'])
        rule_title =request.POST['rule_title']
        rule_discription = request.POST['rule_discription']
        apply_on = request.POST['apply_on']
        dismiss_on = request.POST['dismiss_on']
        status = request.POST['status']
        if(isExist("society_rule_tbl","rule_title",rule_title,"society_rule_id",ID) > 0):
            message = {
                'msg': 'This Rule Type '+rule_title+ ' is Already Exist.',
                'status':'Exist'
            }
            return (message)
        con = MyCon()
        cur = con.cursor()
        if(ID != 0):
            SQLQuery ="update society_rule_tbl set rule_title='{}', rule_discription='{}', apply_on='{}', dismiss_on='{}', status='{}' Where society_rule_id={}".format(rule_title,rule_discription,apply_on,dismiss_on,status,ID)
        else:
            SQLQuery ="Insert into society_rule_tbl values(NULL,'{}','{}' ,'{}' ,'{}','{}',NOW())".format(rule_title,rule_discription,apply_on,dismiss_on,status)
        cur.execute(SQLQuery)
        con.commit()
        if(ID != 0):
            ctx = {
                'msg':'Successfully Update a House Type.',
                'status':"Success"
            }
        else:
            ctx = {
                'msg':'Successfully Insert a House Type.',
                'status':"Success"
            }
        return ctx
def SocietyRuleSingleData(id):
    Query = "Select * from society_rule_tbl Where society_rule_id={}".format(id)
    list = GetSingleData(Query)
    print(list)
    ctx = {
        'Data' : list
    }
    return ctx

def SocietyRulesDeleteCrud(id):
    Query = "Delete from society_rule_tbl Where society_rule_id={}".format(id)
    ExecuteQuery(Query)
    ctx = {
        'msg':'Successfully Delete Data'
    }    
    return ctx

def SocietyRuleListCrud():
    Query = "Select * from society_rule_tbl"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx