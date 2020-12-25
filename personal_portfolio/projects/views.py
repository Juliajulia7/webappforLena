from django.shortcuts import render
from django.shortcuts import render
from projects.models import Project
from .forms import UserForm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

# Create your views here.


def love_story(request):

    return render(request, 'love_story.html')


def individual(request):

    return render(request, 'individual.html')


def insta(request):

    return render(request, 'insta.html')


def family(request):

    return render(request, 'family.html')


def about(request):
    return render(request, 'about.html')

def prices(request):
    submitbutton = request.POST.get("submit")

    emailvalue = ''

    form = UserForm(request.POST or None)
    if form.is_valid():
        emailvalue = form.cleaned_data.get("email")
        msg = MIMEMultipart()

        message = "Приглашаю Вас на фотосесию по специальной цене: экспресс фотосъемка - 1500 рублей, а полноценная фотосъмка - 3500!"

        # setup the parameters of the message
        password = "ZG%TmpM@rqU6"
        msg['From'] = "photoelenabocharova@gmail.com"
        msg['To'] = emailvalue
        msg['Subject'] = "Персональная скидка на фотосессию!"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

    context = {'form': form, 'submitbutton': submitbutton,
               'emailvalue': emailvalue}
    return render(request, 'prices.html', context)



