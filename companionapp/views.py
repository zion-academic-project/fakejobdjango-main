from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer


def index(request):
    return render(request, "general/index.html")

def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_customer:
            login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'user/user_login.html')


def user_home(request):
    return render(request, 'user/user_home.html')


def user_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'user/user_register.html')
        else:
            user = User.objects.create_user(
                username=uname,
                password=passw,
                is_customer=True,
            )
            # Add a success message
            messages.success(request, 'Registration successful. You can now log in.')

            return redirect('user_login')
    else:
        return render(request, "user/user_register.html")


def user_profile(request):
    return render(request, 'user/user_profile.html')



from django.shortcuts import render, redirect, get_object_or_404
from .models import User

def user_profile(request, pk):
    get_profile = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        new_name = request.POST['name']
        new_mob = request.POST['mob']
        new_profile_picture = request.FILES.get('profile_picture')
        new_aboutme = request.POST['aboutme']
        new_resume_file = request.FILES.get('resume_file')

        if new_profile_picture:
            get_profile.profile_picture = new_profile_picture

        get_profile.name = new_name
        get_profile.mobile_number = new_mob
        get_profile.aboutme = new_aboutme

        if new_resume_file:
            get_profile.resume_file = new_resume_file

        get_profile.save()
        return redirect('user_home')

    context = {'get_profile': get_profile}
    return render(request, 'user/user_profile.html', context)

def view_jobposting(request):
    jobpostings = Job_posting.objects.all()
    context = {'jobpostings':jobpostings}
    return render(request, 'user/view_jobposting.html', context)


def view_posting_single(request, pk):
    jobposting = get_object_or_404(Job_posting, pk=pk)
    context = {'jobposting': jobposting}  # Use 'jobposting' instead of 'jobpostings'
    return render(request, 'user/view_posting_single.html', context)


def view_company_profile(request, companyid):
    company = get_object_or_404(User, pk=companyid)
    context = {'company': company} 
    return render(request, 'user/view_company_profile.html', context)


def apply(request, pk):
    user = request.user
    company = get_object_or_404(Job_posting, pk=pk)
    postingid = company.pk
    companyid=company.companyid
    userid = user.pk

    job_title = company.job_title
    location_job = company.location_job
    department = company.department
    company_profile = company.company_profile
    job_description = company.job_description
    job_requirements = company.job_requirements
    job_benefits = company.job_benefits
    employment_type = company.employment_type
    required_experience = company.required_experience
    required_education = company.required_education
    industry = company.industry
    job_function = company.job_function

    Applications.objects.create(
        postingid = postingid,
        userid = userid,
        companyid = companyid,
        job_title = job_title,
        location_job = location_job,
        department = department, 
        company_profile = company_profile,
        job_description = job_description,
        job_requirements = job_requirements,
        job_benefits = job_benefits,
        employment_type = employment_type,
        required_experience= required_experience,
        required_education = required_education,
        industry = industry, 
        job_function = job_function

    )

    return redirect('user_home')


def my_applications(request):
    user = request.user
    userid = user.pk
    applications = Applications.objects.filter(userid=userid)
    context = {'postings': applications} 
    return render(request, 'user/my_applications.html', context)

def SignOut(request):
     logout(request)
     return redirect('user_login')



def company_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_company:
            login(request, user)
            return redirect('company_home')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'company/company_login.html')


def company_home(request):
    return render(request, 'company/company_home.html')


def view_my_job_postings(request):
    user = request.user
    userid = user.pk

    postings = Job_posting.objects.filter(companyid=userid)

    context = {'postings':postings}
    return render(request, 'company/view_my_job_postings.html', context)


def add_job_vacancy(request):

    user = request.user
    userid = user.pk

    if request.method == "POST":
        job_title = request.POST.get('job_title')
        location_job = request.POST.get('location_job')
        department = request.POST.get('department')
        company_profile = request.POST.get('company_profile')
        job_description = request.POST.get('job_description')
        job_requirements = request.POST.get('job_requirements')
        job_benefits = request.POST.get('job_benefits')
        employment_type = request.POST.get('employment_type')
        required_experience = request.POST.get('required_experience')
        required_education = request.POST.get('required_education')
        industry = request.POST.get('industry')
        job_function = request.POST.get('job_function')

        job_posting = Job_posting.objects.create(
            job_title=job_title,
            location_job=location_job,
            department=department,
            company_profile=company_profile,
            job_description=job_description,
            job_requirements=job_requirements,
            job_benefits=job_benefits,
            employment_type=employment_type,
            required_experience=required_experience,
            required_education=required_education,
            industry=industry,
            job_function=job_function,
            companyid= userid,
        )

        return redirect('company_home') 

    return render(request, 'company/add_job_vacancy.html')



def company_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'company/company_register.html')
        else:
            user = User.objects.create_user(
                username=uname,
                password=passw,
                is_company=True,
            )
            # Add a success message
            messages.success(request, 'Registration successful. You can now log in.')

            return redirect('company_login')
    else:
        return render(request, "company/company_register.html")
    
 
from django.contrib.auth.decorators import login_required

@login_required
def company_profile(request, pk):
    get_profile = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        new_name = request.POST.get('name')
        new_mob = request.POST.get('mobile_number')
        new_profile_picture = request.FILES.get('profile_picture')
        new_aboutme = request.POST.get('aboutme')

        if new_profile_picture:
            get_profile.profile_picture = new_profile_picture

        get_profile.name = new_name
        get_profile.mobile_number = new_mob
        get_profile.aboutme = new_aboutme

        get_profile.save()
        return redirect('company_home')

    context = {'get_profile': get_profile}
    return render(request, 'company/company_profile.html', context)



def applications(request):
    user = request.user
    userid = user.pk
    application = Applications.objects.filter(companyid=userid)
    context={'posting':application}
    return render(request, 'company/applications.html', context)


def view_applicant(request,pk):
    get_applicant = get_object_or_404(User, pk=pk)

    context = {'get_applicant': get_applicant}
    return render(request, 'company/view_applicant.html', context)


def update_application(request,pk):
    get_application = get_object_or_404(Applications, pk=pk)

    if request.method=="POST":
        application_message=request.POST.get('application_messsage')

        get_application.application_messsage = application_message
        get_application.save()
        return redirect('applications')
    
    context = {'get_application': get_application}
    return render(request, 'company/update_application.html', context)
    
    
def accept_application(request,pk):
    get_application = get_object_or_404(Applications, pk=pk)

    get_application.application_status = True
    get_application.save()
    return redirect('applications')

def reject_application(request,pk):
    get_application = get_object_or_404(Applications, pk=pk)

    get_application.application_status = False
    get_application.save()
    return redirect('applications')


def SignOut2(request):
     logout(request)
     return redirect('company_login')





def admin_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'admin123/admin_register.html')
        else:
            user = User.objects.create_user(
                username=uname,
                password=passw,
                is_admin=True,
            )
            # Add a success message
            messages.success(request, 'Registration successful. You can now log in.')

            return redirect('mainlogin')
    else:
        return render(request, "admin123/admin_register.html")
    
model = load('./savedModels/model2.joblib')
vect = load('./savedModels/Vector.joblib')
def mainlogin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_admin:
            login(request, user)
            return redirect('mainhome')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'admin123/mainlogin.html')

def mainhome(request):
    return render(request, 'admin123/mainhome.html')

def SignOut3(request):
     logout(request)
     return redirect('mainlogin')

def job_providers(request):
    jobs = User.objects.filter(is_company=True)
    context= {'jobs':jobs}
    return render(request, 'admin123/job_providers.html', context)


def job_seekers(request):
    jobs = User.objects.filter(is_customer=True)
    context= {'jobs':jobs}
    return render(request, 'admin123/job_seekers.html', context)

def job_postings(request):
    jobs = Job_posting.objects.all()
    context= {'jobs':jobs}
    return render(request, 'admin123/job_postings.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Job_posting

def posting_prediction(request, pk):
    posting = get_object_or_404(Job_posting, pk=pk)

    job_title = posting.job_title
    location_job = posting.location_job
    department = posting.department
    company_profile = posting.company_profile
    job_description = posting.job_description
    job_requirements = posting.job_requirements
    job_benefits = posting.job_benefits
    employment_type = posting.employment_type
    required_experience = posting.required_experience
    required_education = posting.required_education
    industry = posting.industry
    job_function = posting.job_function

    input_text = f"{job_title}, {location_job}, {department}, {company_profile}, {job_description}, {job_requirements}, {job_benefits}, {employment_type}, {required_experience}, {required_education}, {industry}, {job_function}"

    input_data_features = vect.transform([input_text])

    y_pred = model.predict(input_data_features)

    if y_pred[0] == 1:
        posting.verified = False
    else:
        posting.verified = True

    posting.save()

    return redirect('job_postings')


def remove_company(request,pk):
    get_job = get_object_or_404(User, pk=pk)
    get_job.delete()
    return redirect('job_providers')