from Admin.Crud.DbConnection import *
#--------------------- IncomeReport Start -------------------#
def IncomeReportCrud():
    Query = "select iet.*, iett.income_expance_type from income_expance_tbl as iet left join income_expance_type_tbl as iett on iet.income_expance_type_id=iett.income_expance_type_id Where iet.type='CREDIT'"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx
#--------------------- IncomeReport End -------------------#

#--------------------- ExpenseReport Start -------------------#
def ExpenseReportCrud():
    Query = "select iet.*, iett.income_expance_type from income_expance_tbl as iet left join income_expance_type_tbl as iett on iet.income_expance_type_id=iett.income_expance_type_id Where iet.type='DEBIT'"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx
#--------------------- ExpenseReport End -------------------#


# TotalExpance
def TotalExpanceCrud():
    Query = "select sum(income_expance_amount) as totalExpance from income_expance_tbl Where type='Debit'"
    list = GetDataSet(Query)
    ctx = {
        'List' : list[0]
    }
    return ctx

###--------------------Total Income------------------------###

def TotalIncomeCrud():
    Query = "select sum(income_expance_amount) from income_expance_tbl Where type='credit'"
    list = GetDataSet(Query)
    ctx = {
        'List' : list[0]
    }
    return ctx
