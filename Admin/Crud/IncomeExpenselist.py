from Admin.Crud.DbConnection import *
#--------------------- IncomeList Start -------------------#
def IncomeListCrud():
    Query = "select iet.*, iett.income_expance_type from income_expance_tbl as iet left join income_expance_type_tbl as iett on iet.income_expance_type_id=iett.income_expance_type_id Where iet.type='CREDIT'"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx
#--------------------- IncomeList End -------------------#

#--------------------- ExpenseList Start -------------------#
def ExpenseListCrud():
    Query = "select iet.*, iett.income_expance_type from income_expance_tbl as iet left join income_expance_type_tbl as iett on iet.income_expance_type_id=iett.income_expance_type_id Where iet.type='DEBIT'"
    list = GetDataSet(Query)
    ctx = {
        'List' : list
    }
    return ctx
#--------------------- ExpenseList End -------------------#