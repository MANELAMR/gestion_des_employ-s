from django.shortcuts import render , redirect
from django.http import response 




# Create your views here.








def supprimer(request):
   
    return render(request, 'supprimer.html') 





def emp(request):
    return render(request,'emp.html')    

           
