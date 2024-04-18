from django.urls import path
from .import views
urlpatterns=[
    path('',views.DashBoard, name="AdminDashboard"),
    path('dashboard',views.DashBoard, name="AdminDashboard"),

    # ----------------- HOUSE TYPE START ----------------------#
    path('HouseType/List/',views.HouseTypeList, name="HouseTypeList"),
    path("HouseType/Form/",views.HouseTypeForm,name="HouseTypeForm"),
    path("HouseType/Add/",views.HouseTypeAdd,name="HouseTypeAdd"),
    path("HouseType/Edit/<int:id>",views.HouseTypeFormEdit,name="HouseTypeFormEdit"),
    path("HouseType/Delete/<int:id>",views.HouseTypeDeleteView,name="HouseTypeFormDelete"),
    # ----------------- HOUSE TYPE END ----------------------#


    # ----------- INCOME EXPANSE TYPE START ----------------#
    path("IncomeExpanseType/List/",views.IncomeExpanseTypeList,name="IncomeExpanseTypeList"),
    path("IncomeExpanseType/Form/",views.IncomeExpanseTypeForm, name="IncomeExpanseTypeForm"),
    path("IncomeExpanseType/Add/",views.IncomeExpanseTypeAdd, name="IncomeExpanseTypeAdd"),
    path("IncomeExpanseTypeEdit/Edit/<int:id>",views.IncomeExpanseTypeEdit, name="IncomeExpanseTypeEdit"),
    path("IncomeExpanseTypeDelete/Delete/<int:id>",views.IncomeExpanseTypeDelete, name="IncomeExpanseTypeDelete"),
    # ----------- INCOME EXPANSE TYPE END ----------------#


    # ----------- INCOME EXPANSE START ----------------#
    path("IncomeExpanse/List/",views.IncomeExpanseList,name="IncomeExpanseList"),
    path("IncomeExpanse/Form/",views.IncomeExpanseForm, name="IncomeExpanseForm"),
    path("IncomeExpanse/Add/",views.IncomeExpanseAdd, name="IncomeExpanseAdd"),
    path("IncomeExpanse/Edit/<int:id>",views.IncomeExpanseEdit, name="IncomeExpanseEdit"),
    path("IncomeExpanseDelete/Delete/<int:id>",views.IncomeExpanseDelete, name="IncomeExpanseDelete"),
    # ----------- INCOME EXPANSE END ----------------#


    # ----------- INCOME List Start ----------------#
    path("Income/List/",views.IncomeList,name="IncomeList"),
    # ----------- INCOME List END ----------------#

    # ----------- Expense List Start ----------------#
    path("Expense/List/",views.ExpenseList,name="ExpenseList"),
    # ----------- Expense List END ----------------#

    

    # ----------- Society Rule Start ----------------#
    path("SocietyRule/List/",views.SocietyRuleList,name="SocietyRuleList"),
    path("SocietyRule/Form/",views.SocietyRuleForm,name="SocietyRuleForm"),
    path("SocietyRule/Add/",views.SocietyRuleAdd,name="SocietyRuleAdd"),
    path("SocietyRule/Edit/<int:id>",views.SocietyRuleEdit,name="SocietyRuleEdit"),
    path("SocietyRule/Delete/<int:id>",views.SocietyRuleDelete,name="SocietyRuleDelete"),
    # ----------- Society Rule End ----------------#


    # ----------- Society Noticeboard Start ----------------#
    path("Noticeboard/List/",views.NoticeboardList,name="NoticeboardList"),
    path("Noticeboard/Form/",views.NoticeboardForm,name="NoticeboardForm"),
    path("Noticeboard/Add/",views.NoticeboardAdd,name="NoticeboardAdd"),
    path("Noticeboard/Edit/<int:id>",views.NoticeboardEdit,name="NoticeboardEdit"),
    path("Noticeboard/Delete/<int:id>",views.NoticeboardDelete,name="NoticeboardDelete"),
    # ----------- Society Noticeboard End ----------------#


    # ----------------- HOUSE  START ----------------------#
    path('House/List/',views.HouseList, name="HouseList"),
    path("House/Form/",views.HouseForm,name="HouseForm"),
    path("House/Add/",views.HouseAdd,name="HouseAdd"),
    path("House/Edit/<int:id>",views.HouseFormEdit,name="HouseFormEdit"),
    path("House/Delete/<int:id>",views.HouseDeleteView,name="HouseFormDelete"),
    # ----------------- HOUSE  END ----------------------#


    # ----------------- MEETING  START ----------------------#
    path("Meeting/List/",views.MeetingList,name="MeetingList"),
    path("Meeting/Form/",views.MeetingForm,name="MeetingForm"),
    path("Meeting/Add/",views.MeetingAdd,name="MeetingAdd"),
    path("Meeting/Edit/<int:id>",views.MeetingEdit,name="MeetingEdit"),
    path("Meeting/Delete/<int:id>",views.MeetingDelete,name="MeetingEdit"),
    # ----------------- MEETING  END ----------------------#


    # ----------------- Suggestion  START ----------------------#
    path("Suggestion/List/",views.SuggestionList,name="SuggestionList"),
    path("Suggestion/Form/",views.SuggestionForm,name="SuggestionForm"),
    path("Suggestion/Add/",views.SuggestionAdd,name="SuggestionAdd"),
    path("Suggestion/Edit/<int:id>",views.SuggestionEdit,name="SuggestionEdit"),
    path("Suggestion/Delete/<int:id>",views.SuggestionDelete,name="SuggestionDelete"),
    # ----------------- Suggestion  END ----------------------#


    # ----------------- Event  START ----------------------#
    path("Event/List/",views.EventList,name="EventList"),
    path("Event/Form/",views.EventForm,name="EventForm"),
    path("Event/Add/",views.EventAdd,name="EventAdd"),
    path("Event/Edit/<int:id>",views.EventEdit,name="EventEdit"),
    path("Event/Delete/<int:id>",views.EventDelete,name="EventDelete"),
    # ----------------- Event  END ----------------------#


    # ----------------- Event Photo Gallery START ----------------------#
    path("EventPhotoGallery/List/",views.EventPhotoGalleryList,name="EventPhotoGalleryList"),
    path("EventPhotoGallery/Form/",views.EventPhotoGalleryForm,name="EventPhotoGalleryForm"),
    path("EventPhotoGallery/Add/",views.EventPhotoGalleryAdd,name="EventPhotoGalleryAdd"),
    path("EventPhotoGallery/Edit/<int:id>",views.EventPhotoGalleryEdit,name="EventPhotoGalleryEdit"),
    path("EventPhotoGallery/Delete/<int:id>",views.EventPhotoGalleryDelete,name="EventPhotoGalleryDelete"),
    # ----------------- Event Photo Gallery End ----------------------#


    # ----------------- Sponsor START ----------------------#
    path("Sponsor/List/",views.SponsorList,name="SponsorList"),
    path("Sponsor/Form/",views.SponsorForm,name="SponsorForm"),
    path("Sponsor/Add/",views.SponsorAdd,name="SponsorAdd"),
    path("Sponsor/Edit/<int:id>",views.SponsorEdit,name="SponsorEdit"),
    path("Sponsor/Delete/<int:id>",views.SponsorDelete,name="SponsorDelete"),
    # ----------------- Sponsor START ----------------------#


    # ----------------- Member START ----------------------#
    path("Member/List/",views.MemberList,name="MemberList"),
    path("Member/Form/",views.MemberForm,name="MemberForm"),
    path("Member/Add/",views.MemberAdd,name="SponsorAdd"),
    path("Member/Edit/<int:id>",views.MemberFormEdit,name="SponsorEdit"),
    path("Member/Delete/<int:id>",views.MemberDelete,name="SponsorDelete"),
    # ----------------- Member START ----------------------#


    #------------------Report Form Start-------------------------#
    path('Report/List', views.ReportList, name="ReportList"),
    path('Report/List/DateWise/', views.ReportTwoDateWiseList, name="ReportTwoDateWiseList"),
    path('Report/Date/List/', views.ReportByDateList, name="ReportByDateList"),
    path('Report/Date/List/Single', views.ReportDateWiseList, name="ReportDateWiseList"),
    #-------------------Report Form End---------------------------#

    #-------------------Income Report List End---------------------------#
    path('Income/Report/List', views.IncomeReportList, name="IncomeReportList"),
    #-------------------Income Report List End---------------------------#

    #-------------------Expense Report List End---------------------------#
    path('Expense/Report/List', views.ExpenseReportList, name="ExpenseReportList"),
    #-------------------Expense Report List End---------------------------#
    
    #-------------------Login---------------------------#
    path('Login', views.Login, name="Login")
    #-------------------Login End---------------------------#
]