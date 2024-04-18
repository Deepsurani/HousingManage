from django.shortcuts import redirect, render

from Admin.Crud.NoticeBoard import *
from Admin.Crud.Event import *
from Admin.Crud.IncomeExpenseReport import *
from Admin.Crud.Meeting import *
from Admin.Crud.SocietyRule import *
from Admin.Crud.SuggestionBox import *
from Admin.Crud.user import *
from Admin.views import *
from Admin.views import DashBoard 


# Create your views here.
def Home(request):
    Data = EventListCrud()
    return render(request,'Client/home.html',Data)

#AboutUS
def AboutUS(request):
    return render(request,'client/AboutUS.html')

#Contact
def Contact(request):
    return render(request,'client/Contact.html')

#Events
def Events(request):
    Data = EventListCrud()
    return render(request,'client/Events.html',Data)
  
#Notices
def Notice(request):
    Data = NoticeBoardListCrud()
    return render(request,'client/Notice.html',Data)
  
#Society Rules
def SocietyRules(request):
    Data = SocietyRuleListCrud()
    return render(request,'client/SocietyRules.html',Data)

#Maintenance List
def Maintenancelist(request):
    Data = ExpenseReportCrud()
    return render(request,'client/Maintenancelist.html',Data)

#Meeting
def Meeting(request):
    Data = MeetingTypeListCrud()
    return render(request,'client/Meeting.html',Data)

#Society Funds
def Societyfunds(request):
    ExpanceCount = TotalExpanceCrud()
    IncomeCount = TotalIncomeCrud()
    TotalExpance = int(ExpanceCount.get('List')[0])
    TotalIncome = int(IncomeCount.get('List')[0])
    Funds = TotalIncome - TotalExpance
    
    ctx ={
        'ExpanceCount':TotalExpance,
        'IncomeCount':TotalIncome,
        'Funds':Funds
    }
    print(ctx)
    return render(request,'client/Societyfunds.html',ctx)

#Society Expense
def Societyexpense(request):
    Data = ExpenseListCrud()
    return render(request,'client/Societyexpense.html',Data)

#Complaint Box
def Complaintbox(request):
    return render(request,'client/Complaintbox.html')

def ComplaintboxAdd(request):
    Data = SuggestionBoxInsertUpdate(request)
    return render(request,'client/Complaintbox.html',Data)

#Login
def login(request):
    return render(request,'client/login.html')



def CheckLogin(request):
    Data = LoginCrud(request)
    Status = Data.get('status')
    if(Status == 1):
        UserId = Data.get('UserId')
        UserName = Data.get('UserName')
        UserRole = Data.get('UserRole')
        request.session["User"] = UserId
        request.session["UserName"] = UserName
        if(UserRole == "Admin"):
            return redirect(DashBoard)
        else:
            return redirect(Home)
    elif(Status == 0):
        return render(request,"client/Login.html",Data)   

def Logout(request):
    del request.session['User']
    del request.session['UserName']
    request.session.modified = True
    return redirect(Home)  

#------------------- PaymentBilAmount ---------------#
def PaymentBilAmount(request):
    Data = ExpenseReportCrud()
    return render(request,"client/PaymentBilAmount.html",Data)