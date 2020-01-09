from django.urls import path
from regapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
    path('sign',TemplateView.as_view(template_name='sign.html'),name='sign'),
    path('student/',TemplateView.as_view(template_name='sdrop.html'),name='sdrop'),  
    path('faculty/',TemplateView.as_view(template_name='faculty.html'),name='faculty'),
    path('adminz/',TemplateView.as_view(template_name='adminz.html'),name='adminz'),
    path('dropdown1/',TemplateView.as_view(template_name='dropdown.html'),name='dropdown'),
    path('stuviewattendance/',TemplateView.as_view(template_name='stuviewatt.html'),name='stuviewatt'),
    path('facultydetails/',TemplateView.as_view(template_name='fdetails.html'),name='fdetails'),
    path('leave/',TemplateView.as_view(template_name='leave.html'),name='leave'),
    path('studentdetails/',TemplateView.as_view(template_name='stdetails.html'),name='stdetails'),
    path('studentpersonal',TemplateView.as_view(template_name='spersonal.html'),name='spersonal'),
    path('studentattendance/',TemplateView.as_view(template_name='sattendance.html'),name='sattendance'),
    path('facultyattendance/',TemplateView.as_view(template_name='fattendance.html'),name='fattendance'),
    path('fattendance/',TemplateView.as_view(template_name='mark.html'),name='mark'),
    path('fdrop/',TemplateView.as_view(template_name='fdrop.html'),name='fdrop'),
    path('sdrop/',TemplateView.as_view(template_name='sdrop.html'),name='sdrop'),
    path('f1details/',TemplateView.as_view(template_name='f1details.html'),name='f1details'),
    path('viewattendance/',TemplateView.as_view(template_name='viewattend.html'),name='viewattend'),
    path('viewmark/',TemplateView.as_view(template_name='viewmark.html'),name='viewmark'),
    path('studentleave/',TemplateView.as_view(template_name='stuleave.html'),name='stuleave'),
    path('leavemanagements/',TemplateView.as_view(template_name='leavemanagement.html'),name='leavemanagement'),
    path('sleaveapro/',TemplateView.as_view(template_name='sleaveapro.html'),name='sleaveapro'),
    path('fleaveapro/',TemplateView.as_view(template_name='fleaveapro.html'),name='fleaveapro'), 
    path('studentmark_view/',TemplateView.as_view(template_name='stuviewmark.html'),name='stuviewmark'), 
    path('status/',TemplateView.as_view(template_name='sleavestatus.html'),name='sleavestatus'), 
    path('f2details/',TemplateView.as_view(template_name='f2details.html'),name='f2details'),
    path('submit/',views.fun2,name='submit'),
    path('logins/',views.authetication,name='loginss'),
    path('adm/',views.ad,name='adm'),
    path('facl/',views.fac,name='facl'),
    path('spersonal/',views.spers,name='spersonal'),
    path('fdetailss/',views.fpers,name='fdetails'),
    path('sdetailss/',views.slog,name='stdetails'),
    path('f1detailss/',views.flog,name='f1details'),
    path('attandance/',views.attand,name='att'),
    path('viewattendans/',views.viewstu,name='viewattend'),
    path('singleatts/',views.singleatt,name='stuviewatt'),
    path('markz/',views.markstu,name='markz'),
    path('viewmarkzz/',views.viewmarkz,name='viewmark'),
    path('facultylev/',views.facleave,name='facleav'),
    path('facultyl/',views.fleaveaproval,name='fleaveapro'),
    path('Student/',views.sleaveaproval,name='sleaveapro'), 
    path('facultyl1/',views.approvefaculty,name='faculty1'), 
    path('studentz1/',views.approveS,name='student1'), 
    path('facultystatus/',views.statuz,name='fleavestatus'),     
    path('sstatus/',views.statuzz,name='sleavestatus'),  
    path('studentmarkview/',views.sviewmark,name='stuviewmark'),  
    path('studentleavs/',views.stuzleave,name='s'),   
    path('logoutss/',views.logoutz,name='logout1'),
    path('edits/',views.editdetails,name='logo'), 
    path('facultyedits/',views.facdetailsedit,name='logoo'),   
      
    
    # path('submit',views.fun3,name='submit'),
]



     