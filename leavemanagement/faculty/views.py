from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Faculty
from student.models import Application, Student
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import smtplib

# Faculty Dashboard
@login_required(login_url='facultyLogin')
def FacultyHome(request):
    return render(request, 'faculty/home.html')


# Show Pending Application for Faculty
@login_required(login_url='facultyLogin')
def PendingApplications(request):
    user = request.user
    faculty = Faculty.objects.all().filter(user=user).first()
    applications = Application.objects.all().filter(faculty=faculty, is_pending=True)
    context = {
        'applications': applications,
    }
    return render(request, 'faculty/pending.html', context)


# Accept Pending Application 
@login_required(login_url='facultyLogin')
def AcceptApplication(request, app_id):
    application = Application.objects.all().filter(id=app_id).first()
    faculty = application.faculty
    
    if faculty.department == 'Dean':
        application.accepted = True
        application.is_pending = False
        application.save()
        print('\nSending mail...!\n') 

        # Enter the Senders email address and Password below
        gmailAddress = 'alphakillerrr@gmail.com'      # The default Id-password are working
        gmailPassword = 'qwerty@123'
        msg = "Application accepted!"
        mailTo = [application.author.user.email]
        # Below is code to send mail to the Client using SMTPLIB 
        try:
            Sub='Response for your queries '
            Message='Subject:{}\n\n{}'.format(Sub,msg)
            mailServer = smtplib.SMTP('smtp.gmail.com', 587)
            mailServer.starttls()
            mailServer.login(gmailAddress, gmailPassword)
            mailServer.sendmail(gmailAddress, mailTo, Message)
            print(" \nMail has been sent to your email!\n")
            mailServer.quit()
        except:
            return redirect('FacultyPendingApplications')
    else:
        if faculty.level == settings.MAX_LEVEL-1:
            department = faculty.department
            nextFaculty = Faculty.objects.all().filter(department='Dean', level=faculty.level+1).first()
            application.faculty = nextFaculty
            application.save()
        else:
            department = faculty.department
            nextFaculty = Faculty.objects.all().filter(department=department, level=faculty.level+1).first()
            application.faculty = nextFaculty
            application.save()
    return redirect("FacultyPendingApplications")


# Reject Pending Application
@login_required(login_url='facultyLogin')
def RejectApplication(request, app_id):
    application = Application.objects.all().filter(id=app_id).first()
    faculty = application.faculty
    application.rejected = True
    application.is_pending = False
    application.save()
    
    print('\nSending mail...!\n') 

    # Enter the Senders email address and Password below
    gmailAddress = 'alphakillerrr@gmail.com'      # The default Id-password are working
    gmailPassword = 'qwerty@123'
    msg = "Application Rejected!"
    mailTo = [application.author.user.email]
    # Below is code to send mail to the Client using SMTPLIB 
    try:
        Sub='Response for your queries '
        Message='Subject:{}\n\n{}'.format(Sub,msg)
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(gmailAddress, gmailPassword)
        mailServer.sendmail(gmailAddress, mailTo, Message)
        print(" \nMail has been sent to your email!\n")
        mailServer.quit()

    except:
        return redirect('FacultyPendingApplications')
    return redirect("FacultyPendingApplications")
