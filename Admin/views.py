from django.shortcuts import render, redirect
from django.template.loader import render_to_string


from Admin.Crud.Event import *
from Admin.Crud.EventPhotoGallery import *
from Admin.Crud.House import *
from Admin.Crud.HouseType import *
from Admin.Crud.IncomeExpence import *
from Admin.Crud.IncomeExpenseType import *
from Admin.Crud.Member import *
from Admin.Crud.SocietyRule import *
from Admin.Crud.NoticeBoard import *
from Admin.Crud.Meeting import *
from Admin.Crud.Sponsor import *
from Admin.Crud.SuggestionBox import *
from Admin.Crud.IncomeExpenselist import *
from Admin.Crud.IncomeExpenseReport import *


# Create your views here.
def DashBoard(request):
    return render(request,'admin/Dashboard.html')


#--------------- House Type Function Start   -----------------#

# HouseTypeList Start
def HouseTypeList(request):
    ctx = HouseType_List()
    return render(request,'admin/HouseTypeList.html', ctx)
# HouseTypeList End

# HouseTypeForm Start
def HouseTypeForm(request):
    return render(request,"admin/HouseTypeForm.html")
# HouseTypeFormEnd
# HouseTypeForm Edit Start
def HouseTypeFormEdit(request, id):
    ctx = HouseEditRegistration(id)
    return render(request,"admin/HouseTypeForm.html", ctx)
# HouseTypeForm Edit End

# HouseTypeAdd Start
def HouseTypeAdd(request):
    if request.method == 'POST':
        returnMessage = HouseTypeInsert(request)
        return render(request,'admin/HouseTypeForm.html',returnMessage)
    return redirect(HouseTypeForm)
# HouseTypeAdd End

# HouseTypeDelete Start
def HouseTypeDeleteView(request, id):
    HouseTypeDelete(id)
    return redirect(HouseTypeList)
# HouseTypeDelete End

#--------------- House Type Function END   -----------------#



#--------------- IncomeExpanse Type Function Start   -----------------#

# IncomeExpanse Type List Start
def IncomeExpanseTypeList(request):
    Data = IncomeExpanseTypeListCrud()
    return render(request,"admin/IncomeExpanseTypeList.html",Data)
# IncomeExpanse Type List End


# IncomeExpanse Type Form Start
def IncomeExpanseTypeForm(request):
    return render(request,"admin/IncomeExpanseTypeForm.html")
# IncomeExpanse Type Form End

# IncomeExpanse Type Add Start
def IncomeExpanseTypeAdd(request):
    if request.method == 'POST':
        returnMessage = IncomeExpanseTypeInsertUpdate(request)
        return render(request,'admin/IncomeExpanseTypeForm.html',returnMessage)
    return redirect(HouseTypeForm)
# IncomeExpanse Type Add End

# IncomeExpanse Type Edit Start
def IncomeExpanseTypeEdit(request,id):
    ctx = IncomeExpanseSingleDateWiseCrud(id)
    return render(request,"admin/IncomeExpanseTypeForm.html",ctx)
# IncomeExpanse Type Edit End

# IncomeExpanse Type Delete Start
def IncomeExpanseTypeDelete(request,id):
    ctx = IncomeExpanseTypeDeleteCrud(id)
    return redirect(IncomeExpanseTypeList)
# IncomeExpanse Type Delete End

#--------------- IncomeExpanse Type Function END   -----------------#

#--------------- Income List Start   -----------------#
def IncomeList(request):
    Data = IncomeListCrud()
    return render(request,"admin/IncomeList.html",Data) 
#--------------- Income List END   -----------------#


#--------------- Expense List Start   -----------------#
def ExpenseList(request):
    Data = ExpenseListCrud()
    return render(request,"admin/ExpenseList.html",Data) 
#--------------- Expense List END   -----------------#



#--------------- IncomeExpanse Function Start   -----------------#

# IncomeExpanse List Start
def IncomeExpanseList(request):
    Data = IncomeExpenseListCrud()
    return render(request,"admin/IncomeExpenseList.html",Data)
# IncomeExpanse List End


# IncomeExpanse Form Start
def IncomeExpanseForm(request):
    data = IncomeExpanseTypeListCrud()
    return render(request,"admin/IncomeExpenseForm.html",data)
# IncomeExpanse  Form End

# IncomeExpanse  Add Start
def IncomeExpanseAdd(request):
    if request.method == 'POST':
        returnMessage = IncomeExpenseInsertUpdate(request)
        return render(request,'admin/IncomeExpenseForm.html',returnMessage)
    return redirect(IncomeExpanseForm)
# IncomeExpanse  Add End

# IncomeExpanse  Edit Start
def IncomeExpanseEdit(request,id):
    income = IncomeExpenseEditCrud(id)
    IncomeExpense = IncomeExpanseTypeListCrud()
    ctx = {
        'Data':income.get('Data'),
        'List':IncomeExpense.get('List')
    }
    return render(request,"admin/IncomeExpenseForm.html",ctx)   
# IncomeExpanse  Edit End

# IncomeExpanse  Delete Start
def IncomeExpanseDelete(request,id):
    ctx = IncomeExpenseDeleteCrud(id)
    return redirect(IncomeExpanseList)
# IncomeExpanse  Delete End

#--------------- IncomeExpanse  Function END   -----------------#


#--------------- SocietyRule Function Start   -----------------#

# SocietyRule List Start
def SocietyRuleList(request):
    Data = SocietyRuleListCrud()
    return render(request,"admin/SocietyRuleList.html", Data)
# SocietyRule List End

# SocietyRule Form Start
def SocietyRuleForm(request):
    return render(request,"admin/SocietyRuleForm.html")
# SocietyRule Form End

# SocietyRule Add Start
def SocietyRuleAdd(request):
    if request.method == 'POST':
        returnMessage = SocietyRuleInsertUpdate(request)
        return render(request,'admin/SocietyRuleForm.html',returnMessage)
    return redirect(SocietyRuleForm)
# SocietyRule Add End

# SocietyRule Edit Start
def SocietyRuleEdit(request,id):
    returnMessage = SocietyRuleSingleData(id)
    return render(request,'admin/SocietyRuleForm.html',returnMessage)
# SocietyRule Edit End

# SocietyRule Edit Start
def SocietyRuleDelete(request,id):
    returnMessage = SocietyRulesDeleteCrud(id)
    return redirect(SocietyRuleList)
# SocietyRule Edit End

#--------------- SocietyRule Function END   -----------------#


#--------------- NoticeBoard Function Start   -----------------#

# NoticeBoard List Start
def NoticeboardList(request):
    Data = NoticeBoardListCrud()
    return render(request,"admin/NoticeboardList.html",Data)
# NoticeBoard List End

# NoticeBoard Form Start
def NoticeboardForm(request):
    return render(request,"admin/NoticeboardForm.html")
# NoticeBoard Form End

# NoticeBoard Add Start
def NoticeboardAdd(request):
    if request.method == 'POST':
        returnMessage = NoticeBoardInsertUpdate(request)
        return render(request,'admin/NoticeboardForm.html',returnMessage)
    return redirect(NoticeboardForm)
# NoticeBoard Add End

# NoticeBoard Edit Start
def NoticeboardEdit(request, id):
    Data = NoticeBoardEditCrud(id)
    return render(request,"admin/NoticeboardForm.html", Data)
# NoticeBoard Edit End

# NoticeBoard Delete Start
def NoticeboardDelete(request, id):
    Data = NoticeBoardDeleteCrud(id)
    return redirect(NoticeboardList)
# NoticeBoard Delete End



#--------------- NoticeBoard Function End   -----------------#


#--------------- House  Function Start   -----------------#

# HouseList Start
def HouseList(request):
    ctx = HouseListCrud()
    return render(request,'admin/HouseList.html', ctx)
# HouseList End

# HouseForm Start
def HouseForm(request):
    data = HouseType_List()
    return render(request,"admin/HouseForm.html", data)
# HouseFormEnd
# HouseForm Edit Start
def HouseFormEdit(request, id):
    data = HouseType_List()
    ctx = HouseEditCrud(id)
    context = {
        'Data':ctx.get('Data'),
        'List':data.get('List')
    }
    return render(request,"admin/HouseForm.html", context)
# HouseForm Edit End

# HouseAdd Start
def HouseAdd(request):
    if request.method == 'POST':
        returnMessage = HouseInsertUpdate(request)
        return render(request,'admin/HouseForm.html',returnMessage)
    return redirect(HouseForm)
# HouseAdd End

# HouseDelete Start
def HouseDeleteView(request, id):
    HouseDeleteCrud(id)
    return redirect(HouseList)
# HouseDelete End

#--------------- House  Function END   -----------------#

#--------------- Meeting  Function Start   -----------------#

# MeetingList Start
def MeetingList(request):
    List = MeetingTypeListCrud()
    return render(request,"admin/MeetingList.html",List)
# MeetingList End

# MeetingForm Start
def MeetingForm(request):
    return render(request,"admin/MeetingForm.html")
# MeetingForm End

# MeetingAdd Start
def MeetingAdd(request):
    if request.method == 'POST':
        returnMessage = MeetingTypeInsertUpdate(request)
        return render(request,'admin/MeetingForm.html',returnMessage)
    return redirect(MeetingForm)
# MeetingAdd End

# MeetingEdit Start
def MeetingEdit(request,id):
    returnMessage = MeetingEditCrud(id)
    return render(request,'admin/MeetingForm.html',returnMessage)
# MeetingEdit End

# MeetingDelete Start
def MeetingDelete(request,id):
    returnMessage = MeetingDeleteCrud(id)
    return redirect(MeetingList)
# MeetingDelete End

#--------------- Meeting  Function END   -----------------#

#--------------- Suggestion Function START   -----------------#

# SuggestionList Start
def SuggestionList(request):
    Data = SuggestionBoxListCrud()
    return render(request,"admin/SuggestionList.html",Data)
# SuggestionList End

# SuggestionForm Start
def SuggestionForm(request):
    return render(request,"admin/SuggestionForm.html")
# SuggestionForm End

# SuggestionAdd Start
def SuggestionAdd(request):
    if request.method == 'POST':
        returnMessage = SuggestionBoxInsertUpdate(request)
        return render(request,'admin/SuggestionForm.html',returnMessage)
    return redirect(SuggestionForm)
# SuggestionAdd End


# SuggestionEdit Start
def SuggestionEdit(request,id):
    returnMessage = SuggestionBoxEditCrud(id)
    return render(request,'admin/SuggestionForm.html',returnMessage)
# SuggestionEdit End

# SuggestionDelete Start
def SuggestionDelete(request,id):
    returnMessage = SuggestionBoxDeleteCrud(id)
    return redirect(SuggestionList)
# SuggestionDelete End

#--------------- Suggestion Function END   -----------------#


#--------------- Event Function Start   -----------------#

# EventList Start
def EventList(request):
    data = EventListCrud()
    return render(request,"admin/EventList.html",data)
# EventList End

# EventForm Start
def EventForm(request):
    return render(request,"admin/EventForm.html")
# EventForm End

# EventAdd Start
def EventAdd(request):
    if request.method == 'POST':
        returnMessage = EventInsertUpdate(request)
        return render(request,'admin/EventForm.html',returnMessage)
    return redirect(EventForm)
# EventAdd End

# EventEdit Start
def EventEdit(request,id):
    returnMessage = EventEditCrud(id)
    return render(request,'admin/EventForm.html',returnMessage)
# EventEdit End

# EventDelete Start
def EventDelete(request,id):
    returnMessage = EventDeleteCrud(id)
    return redirect(EventList)
# EventDelete End

#--------------- Event Function END   -----------------#


#--------------- Event Photo Gallery Function Start   -----------------#


# EventPhotoGalleryList Start
def EventPhotoGalleryList(request):
    Data = EventPhotoListCrud()
    return render(request,"admin/EventPhotoGalleryList.html",Data)
# EventPhotoGalleryList End

# EventPhotoGalleryForm Start
def EventPhotoGalleryForm(request):
    Data = EventListCrud()
    return render(request,"admin/EventPhotoGalleryForm.html",Data)
# EventPhotoGalleryForm End

# EventPhotoGalleryAdd Start
def EventPhotoGalleryAdd(request):
    if request.method == 'POST':
        returnMessage = EventPhotoGalleryInsertUpdate(request)
        return render(request,'admin/EventPhotoGalleryForm.html',returnMessage)
    return redirect(EventPhotoGalleryForm)
# EventPhotoGalleryAdd End



# EventPhotoGalleryEdit Start
def EventPhotoGalleryEdit(request,id):
    data = EventListCrud()
    ctx = EventPhotoEditCrud(id)
    context = {
        'Data':ctx.get('Data'),
        'List':data.get('List')
    }
    # returnMessage = EventPhotoEditCrud(id)
    return render(request,'admin/EventPhotoGalleryForm.html',context)
# EventPhotoGalleryEdit End


# EventPhotoGalleryDelete Start
def EventPhotoGalleryDelete(request,id):
    returnMessage = EventPhotoDeleteCrud(id)
    return redirect(EventPhotoGalleryList)
# EventPhotoGalleryDelete End

#--------------- Event Photo Gallery Function END   -----------------#


#--------------- Sponsor Function Start   -----------------#


# SponsorList Start
def SponsorList(request):
    Data = SponsorListCrud()
    return render(request,"admin/SponsorList.html",Data)
# SponsorList End

# SponsorForm Start
def SponsorForm(request):
    Data = EventListCrud()
    return render(request,"admin/SponsorForm.html", Data)
# SponsorForm End

# SponsorAdd Start
def SponsorAdd(request):
    if request.method == 'POST':
        Data = SponsorInsertUpdate(request)
        return render(request,"admin/SponsorForm.html", Data)
    return redirect(SponsorForm)
# SponsorAdd End


# SponsorEdit Start
def SponsorEdit(request,id):
    Data = EventListCrud()
    SingleData = SponsorEditCrud(id)
    context = {
        'Data':SingleData.get('Data'),
        'List':Data.get('List')
    }
    return render(request,"admin/SponsorForm.html", context)
# SponsorEdit End

# SponsorDelete Start
def SponsorDelete(request,id):
    Data = SponsorDeleteCrud(id)
    return render(request,"admin/SponsorList.html")
# SponsorDelete End


#--------------- Sponsor Function END   -----------------#


#--------------- Member Function START   -----------------#

# House List
def MemberList(request):
    Data = MemberListCrud()
    return render(request,'Admin/MemberList.html',Data)

#  Member Form
def MemberForm(request):
    House = HouseListCrud()
    ctx = {
        'House':House.get('List')
    }
    return render(request,'Admin/MemberForm.html',ctx)

def MemberAdd(request):
    if request.method == 'POST':
        returnMessage = MemberInsertUpdate(request)
        return render(request,'admin/MemberForm.html',returnMessage)
    return redirect(MemberForm)

def MemberFormEdit(request,id):
    House = HouseListCrud()
    Member = MemberEditCrud(id)
    ctx = {
        'House':House.get('List'),
        'Data' : Member.get('Data')
    }
    return render(request,"admin/MemberForm.html", ctx)

def MemberDelete(request,id):
    MemberDeleteCrud(id)
    return redirect(MemberList)
#--------------- Member Function END   -----------------#

#--------------- IncomeReport Start   -----------------#
def IncomeReportList (request):
    Data = IncomeReportCrud()
    return render(request,'admin/IncomeReport.html',Data)
#--------------- IncomeReport End   -----------------#

#--------------- ExpanseReport Start   -----------------#
def ExpenseReportList (request):
    Data = ExpenseReportCrud()
    return render(request,'admin/ExpenseReport.html',Data)
#--------------- ExpanseReport End   -----------------#


#############  9.Report Start ##########

def ReportList(request):
    ctx = IncomeExpenseListCrud()
    return render(request,"Admin/ReportList.html",ctx)

def ReportByDateList(request):
    ctx = IncomeExpenseListCrud()
    return render(request,"Admin/ReportByDateList.html",ctx)



def ReportTwoDateWiseList(request):
    if request.method == 'POST':
        StartDate = request.POST['StartDate']
        EndDate = request.POST['EndDate']
        List = IncomeExpanseDateWiseCrud(StartDate,EndDate)
        ctx = {
            'StartDate':StartDate,
            'EndDate':EndDate,
            'List':List.get('List')
        }
        return render(request,"Admin/ReportList.html",ctx)
    return render(ReportList)


def ReportDateWiseList(request):
    if request.method == 'POST':
        StartDate = request.POST['StartDate']
        # EndDate = request.POST['EndDate']
        List = IncomeExpanseSingleDateWiseCrud(StartDate)
        ctx = {
            'StartDate':StartDate,
            'List':List.get('List')
        }
        return render(request,"Admin/ReportList.html",ctx)
    return render(ReportList)
#############  9.Report End ##########

############# 9 Login ################
def Login (request):
    return render(request,"Admin/Login.html" )
