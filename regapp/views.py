from django.shortcuts import render
from regapp.models import registration,admin,facultyreg,atta,marks,facultyleave,studentleavez
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
def fun2(request):  
    if request.method=='POST':
        name = request.POST.get('name')
        stdid = request.POST.get('stdid')
        year = request.POST.get('year')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        branch = request.POST.get('branch')
        a=registration(name=name,stdid=stdid,year=year,address=address,mobile=mobile,email=email,password=password,branch=branch)
        a.save()
    return render(request,'dropdown.html')
def attand(request):
    if request.method=='POST':
        name = request.POST.get('name')
        stdid = request.POST.get('stdid') 
        firstp = request.POST.get('firstp')
        secondp = request.POST.get('secondp')
        thirdp = request.POST.get('thirdp')
        fourthp = request.POST.get('fourthp') 
        s=atta(name=name,stdid=stdid,firstp=firstp,secondp=secondp,thirdp=thirdp,fourthp=fourthp)
        s.save()
        return render(request,'sattendance.html')
def markstu(request):
    if request.method=='POST':
        name = request.POST.get('name')
        stdid = request.POST.get('stdid') 
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        s=marks(name=name,stdid=stdid,mark1=mark1,mark2=mark2,mark3=mark3)
        s.save()
        return render(request,'mark.html')            
def authetication(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        name=str(name)
        password=str(password)
        u=registration.objects.filter(password=password,name=name)
        if u.count()==1:
            request.session['name']=name
            return render(request,'sdrop.html')
        else:
            z=facultyreg.objects.filter(password=password,name=name)
            if z.count()==1:
                request.session['name']=name
                return render(request,'fdrop.html') 
            else:
                return HttpResponse('login failed.')
def ad(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        name=str(name)
        password=str(password)
        u=admin.objects.filter(password=password,name=name)
        if u.count()==1:
            return render(request,'dropdown.html')
        else:
            return HttpResponse('login failed')

def fac(request):  
    if request.method=='POST':
        name = request.POST.get('name')
        fid = request.POST.get('fid')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        b=facultyreg(name=name,fid=fid,address=address,mobile=mobile,email=email,password=password)
        b.save()
    return render(request,'dropdown.html') 
def facleave(request):
    if request.method=='POST':
        name = request.POST.get('name')
        stdid = request.POST.get('stdid') 
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        status = request.POST.get('status')
        reason = request.POST.get('reason')
        v=facultyleave(name=name,stdid=stdid,fromdate=fromdate,todate=todate,status=status,reason=reason)
        v.save()
        return render(request,'fdrop.html')   
def stuzleave(request):
    if request.method=='POST':
        name = request.POST.get('name')
        stdid = request.POST.get('stdid') 
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        status = request.POST.get('status')
        reason = request.POST.get('reason')
        v=studentleavez(name=name,stdid=stdid,fromdate=fromdate,todate=todate,status=status,reason=reason)
        v.save()
        return render(request,'sdrop.html')               
def spers(request):
    queryset=registration.objects.all().filter()
    return render(request,'spersonal.html',{'authors':queryset})    
    # Create your views here.
def fpers(request):
    queryset=facultyreg.objects.all().filter()
    return render(request,'fdetails.html',{'authors':queryset})    

def slog(request):
    queryset=registration.objects.all().filter(name=request.session['name'])
    return render(request,'stdetails.html',{'authors':queryset})
def flog(request):
    queryset=facultyreg.objects.all().filter(name=request.session['name'])
    return render(request,'f1details.html',{'authors':queryset})
def viewstu(request):
    queryset=atta.objects.all().filter()
    return render(request,'viewattend.html',{'authors':queryset})  
def singleatt(request):
    queryset=atta.objects.all().filter(name=request.session['name'])
    return render(request,'stuviewatt.html',{'authors':queryset})   
def viewmarkz(request):
    queryset=marks.objects.all().filter()
    return render(request,'viewmark.html',{'authors':queryset})   
def fleaveaproval(request):
    queryset=facultyleave.objects.all().filter()
    return render(request,'fleaveapro.html',{'authors':queryset})
def sleaveaproval(request):
    queryset=studentleavez.objects.all().filter()
    return render(request,'sleaveapro.html',{'authors':queryset})    
def approvefaculty(request):
    if request.method=='POST':
        name=request.POST.get('name')
        facultyleave.objects.filter(name=name).update(status='Approved')
def approveS(request):
    if request.method=='POST':
        name=request.POST.get('name')
        studentleavez.objects.filter(name=name).update(status='Approved')        
    return render (request,'sleaveapro.html')
def statuz(request):
    queryset=facultyleave.objects.all().filter(name=request.session['name'])
    return render(request,'fleavestatus.html',{'authors':queryset})  
def statuzz(request):
    queryset=studentleavez.objects.all().filter(name=request.session['name'])
    return render(request,'sleavestatus.html',{'authors':queryset})        
def sviewmark(request):
    queryset=marks.objects.all().filter(name=request.session['name'])
    return render(request,'stuviewmark.html',{'authors':queryset})  
def logoutz(request):
    logout(request)
    return redirect('index')          
def editdetails(request):
    queryset=facultyreg.objects.all().filter(name=request.session['name'])    
    return render(request,'f2details.html',{'authors':queryset})


def facdetailsedit(request):  
    if request.method=='POST':
        name=request.POST.get('name')
        fid=request.POST.get('fid')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        facultyreg.objects.all().filter(name=request.session['name']).update(fid=fid,address=address,mobile=mobile,email=email,password=password)
    return redirect('f2details') 