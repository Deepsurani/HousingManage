from django.urls import path
from .import views
urlpatterns = [
    path('',views.Home,name="Home" ),
    path('Home',views.Home,name="Home"),
    path('AboutUS',views.AboutUS,name="AboutUS"),
    path('Contact',views.Contact,name="Contact"),
    path('Events',views.Events,name="Events"),
    path('Notice',views.Notice,name="Notice"),
    path('SocietyRules',views.SocietyRules,name="SocietyRules"),
    path('Maintenancelist',views.Maintenancelist,name="Maintenancelist"),
    path('Meeting',views.Meeting,name="Meeting"),
    path('Societyfunds',views.Societyfunds,name="Societyfunds"),
    path('Societyexpense',views.Societyexpense,name="Societyexpense"),
    path('Complaintbox/Add',views.ComplaintboxAdd,name="ComplaintboxAdd"),
    path('Complaintbox',views.Complaintbox,name="Complaintbox"),
    path('login',views.login,name="login"),   
    path('Logout',views.Logout,name="Logout"),
    path('Login/CheckLogin',views.CheckLogin,name="CheckLogin"),
    path('PaymentBilAmount',views.PaymentBilAmount,name="PaymentBilAmount")
]