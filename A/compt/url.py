from django.urls import path , include 
from . import views
from django.contrib.auth  import views as auth_views

urlpatterns = [
   path('index/',views.index ,name='index'),
   path('ajouter/',views.ajouter ,name='ajouter'),
   path('login/',views.login ,name='login'), 
   path('logout/',auth_views.LogoutView.as_view() ,name='logout'), 
   path('consult/',views.consult ,name='consult'), 
   path('searchbar/',views.searchbar ,name='searchbar'),
   path('home1/',views.home1 ,name='home1'),
   path('', views.index),
   path('ViewPDF/', views.ViewPDF.as_view(), name="ViewPDF"),
   path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
   path('index2/',views.index2 ,name='index2'),
   path('pdf_template/<str:pk_test>/',views.pdf_template ,name='pdf_template'),
   path('emp/<str:pk_test>/',views.emp ,name='emp'),
   path('modifier/<str:pk>/',views.modifier ,name='modifier'),
   path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
   path('delete/',views.delete ,name='delete'),
   path('searchbar2/',views.searchbar2 ,name='searchbar2'),
   path('searchbar3/',views.searchbar3 ,name='searchbar3'),
   path('signup/',views.signup ,name='signup'),
   path('modifier2/<str:pk>/',views.modifier2 ,name='modifier2'),
   path('modetsupp/',views.modetsupp ,name='modetsupp'), 
   path('attestation/',views.attestation ,name='attestation'),
   path('att/<str:pk_test>/',views.att ,name='att'),
   path('index3/',views.index3 ,name='index3'),
   path('ViewPDF2/', views.ViewPDF2.as_view(), name="ViewPDF2"),
   path('pdf_download2/', views.DownloadPDF2.as_view(), name="pdf_download2"),
   path('pdf_att/<str:pk_test>/',views.pdf_att ,name='pdf_att'),
   path('email/',views.email ,name='email'),
   path('contact/',views.contact ,name='contact'),
   path('generatepdf/<int:id>/',views.generatePDF,name='generatepdf'),
   path('generatePDF2/<int:id>/',views.generatePDF2,name='generatePDF2'),
   path('info/',views.info ,name='info'),




 

 
   

   


   

   
   
   
   
   
   ]