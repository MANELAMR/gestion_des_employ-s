from functools import total_ordering
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login as auth_login 
from .models import Employer , Administrateur
from .forms import AjouterEmployer
from xhtml2pdf import pisa 
from django.http import HttpResponse
from django.views.generic import View
from io import BytesIO 
from django.template.loader import get_template
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from .utils import render_to_pdf
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from django.core.mail import send_mail



# Create your views here.
def home1(request):
    emp = Employer.objects.all()
    total_emp = emp.count()

    empF = Employer.objects.all().filter(sex='F')
    total_empF = empF.count()

    empP1 = Employer.objects.all().filter(postes='technicien_-supérieure')
    d1=empP1.count()

    empP2 = Employer.objects.all().filter(postes='comptable')
    d2=empP2.count()

    empP3 = Employer.objects.all().filter(postes='administrateur')
    d3=empP3.count()

    empP4 = Employer.objects.all().filter(postes='secrrtaire')
    d4=empP4.count()

    empP5 = Employer.objects.all().filter(postes='responsable de traitement')
    d5=empP5.count()

    empP6 = Employer.objects.all().filter(postes='agent de securite')
    d6=empP6.count()

    empP7 = Employer.objects.all().filter(postes='enseignant')
    d7=empP7.count()

    empP8 = Employer.objects.all().filter(postes='responsable de laboratoire')
    d8=empP8.count()

    empP9 = Employer.objects.all().filter(postes='responsable de traitement bancaire')
    d9=empP9.count()

    empP10 = Employer.objects.all().filter(postes='bibliothécaire')
    d10=empP10.count()
    empP11 = Employer.objects.all().filter(postes='informaticien')
    d11=empP11.count()





    empH = Employer.objects.all().filter(sex='H')
    total_empH = empH.count()
    context = {'total_emp': total_emp ,'total_empF':total_empF , 'total_empH':total_empH , 'emp':emp , 'd1':d1,'d2':d2 , 'd3':d3,'d4':d4,'d5':d5,'d6':d6,'d7':d7,'d8':d8,'d9':d9,'d10':d10,'d11':d11 }
    return render(request, 'home1.html',context )

def emp(request, pk_test):
    post = Employer.objects.get(id=pk_test)
    
    return render(request, 'emp.html',{'post':post})  

def att(request, pk_test):
    post = Employer.objects.get(id=pk_test)
    
    return render(request, 'att.html',{'post':post})
def M(request):
    
    return render(request, 'M.html')
def info(request):
    
    return render(request, 'info.html')         

def index(request):
    
    if request.method =='POST':
        nom=request.POST['email']
        pas=request.POST['pas']
        return redirect('home1')
    return render(request,'index.html')


def generatePDF(request,id):
    enseignant = Employer.objects.get(pk=id)
    template = get_template('pdf/pdf_att.html')
    context = {
        "post":enseignant 
    }
    html = template.render(context)
    pdf = render_to_pdf('pdf/pdf_att.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


def generatePDF2(request,id):
    enseignant = Employer.objects.get(pk=id)
    template = get_template('pdf/pdf_template.html')
    context = {
        "post":enseignant 
    }
    html = template.render(context)
    pdf = render_to_pdf('pdf/pdf_template.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")    

def ajouter(request):
    if request.method =='POST':
        
        form=AjouterEmployer(request.POST)
        if form.is_valid():
            print('success')
            form.save()
        else:
            print(form.errors)
            return render(request, 'ajouter.html',{'form':form})
        return redirect('consult')
        Employer=Employer.objects.create(
            Nom=Nom,
            Prenom=Prenom,
            dateN=dateN,
            nbr_femmes=nbr_femmes,
            num_inférentiek_inf=num_inférentiek_inf,
            situation_familiale=situation_familiale,
            categorie=categorie,
            rang=rang,
            nbr_enfants=nbr_enfants,
            num_telephon=num_telephon,
            email=email,
            sex=sex,
            Nommarital=Nommarital,
            Date_de_recrutement=Date_de_recrutement
            

        )

        
        


    return render(request, 'ajouter.html',{'form':AjouterEmployer()})
def modifier(request,pk):
    post=Employer.objects.get(id=pk)
    form=AjouterEmployer(instance=post)

    if request.method=='POST':
        form=AjouterEmployer(request.POST,instance=post) 
        if form.is_valid():
            form.save()
        else:
             return render(request, 'ajouter.html',{'form':form})
        return redirect('consult')
    context={'form':form}   
    return render(request, 'ajouter.html',context)


   
def modifier2(request,pk):
    post=Employer.objects.get(id=pk)
    form=AjouterEmployer(instance=post)

    if request.method=='POST':
        form=AjouterEmployer(request.POST,instance=post) 
        if form.is_valid():
            form.save()
        else:
             return render(request, 'ajouter.html',{'form':form})
        return redirect('modetsupp')
    context={'form':form}   
    return render(request, 'ajouter.html',context)   

 

def modetsupp(request):
    post=Employer.objects.all().order_by('Nom')
    return render(request, 'modetsupp.html',{'post':post})



def login(request):
    
    if request.method =='POST':
        Nom=request.POST['name']
        Prenom=request.POST['prenom']
        sex=request.POST['sex']
        date=request.POST['date']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        mot_passe=request.POST['mot_passe']

        Administrateurss=Administrateur.objects.create(
            name=Nom,
            prenom=Prenom,
            email=email,
            sex=sex,
            mot_passe=mot_passe,
            date=date,
            phone_number=phone_number

            


            
        )


        return redirect('home1')
    return render(request, 'login.html')
       
       
          
       
def consult(request):
    post=Employer.objects.all().order_by('Nom')
    return render(request, 'consult.html',{'post':post})



def attestation(request):
    post=Employer.objects.all().order_by('Nom')
    return render(request, 'attestation.html',{'post':post})    

def att(request, pk_test):
    post = Employer.objects.get(id=pk_test)
    
    return render(request, 'att.html',{'post':post})      

def searchbar (request):
    if request.method=='GET':
        search=request.GET.get('search')
        post=Employer.objects.all().filter(Nom=search)
        return render(request,'searchbar.html',{'post':post})

def searchbar2 (request):
    if request.method=='GET':
        search=request.GET.get('search')
        post=Employer.objects.all().filter(Prenom=search)
        return render(request,'searchbar2.html',{'post':post})

def searchbar3 (request):
    if request.method=='GET':
        search=request.GET.get('search')
        post=Employer.objects.all().filter(postes=search)
        return render(request,'searchbar3.html',{'post':post})


#hana bdit nzid 

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None
    

data = {
     
	
	
	}

class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('../template/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


class ViewPDF2(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('../template/pdf_att.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('../template/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response


class DownloadPDF2(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('../template/pdf_att.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def index2(request):
	context = {}
	return render(request, 'index2.html', context)

    
def index3(request, id):
    post = Employer.objects.get(pk=id)
    
    return render(request, 'index3.html',{'post':post}) 

def pdf_template(request, pk_test):
    post = Employer.objects.get(id=pk_test)
    
    return render(request, 'pdf_template.html',{'post':post})    

def pdf_att(request, pk_test):
    post = Employer.objects.get(id=pk_test)
    
    return render(request, 'pdf_att.html',{'post':post})    

	 
def deleteOrder(request, pk):
	order = Employer.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('modetsupp')

	context = {'item':order}
	return render(request, 'delete.html', context)

def delete(request):
    
    return render(request, 'delete.html')

def email(request):
    
    return render(request, 'email.html')    




def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home1')

    return render(request,'signup.html',{'form':form})

###########
def contact(request):
    if request.method=="POST":
        message_name=request.POST['message_name']
        
        message=request.POST['file']
        to=request.POST['emailE']
        

        send_mail(
               message_name,
               message,
               settings.EMAIL_HOST_USER,
               to 
               
        )
        return render(request, 'email.html')    
    