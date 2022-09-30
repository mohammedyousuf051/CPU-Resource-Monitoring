# CPU_Usage_Monitoring
a simple front-end (web app) that can monitor the ram and CPU usage at a server. The front-end communicates with backend about the resource consumption through a web API.

python3 manage.py celeryd -v 2 -B -s celery -E -l INFO

Steps to run the web app:
1) First activate the environment using the command 

`source venv/bin/activate`

2) Enter your source email id and password in settings.py file in relative path `CPUMonitoring/CPUMonitoring/settings.py` in the fields

`EMAIL_HOST_USER = 'emailid@mail.com'
EMAIL_HOST_PASSWORD = 'password'
`

 Also change the to email address in the function  `check_usage()` in relative path  
 'CPUMonitoring/Monitor/views.py'   
 
 change the to email id in the below line
 
 `send_mail('Ram over utilisation', 'RAM stayed for 50% for over 10 seconds.', '**toemail@email.com**', ['receiver1@email.com','receiver2@email.com'...], fail_silently=False)`
  
  and add receivers email id as a list or array in the following argument
 
3) Run the project by changing to the directory with manage.py file

4) Run the project using the command
 
 `python manage.py runserver` 
 
 
 5) Open another terminal and run the below command on the same directory as manage.py file
 
 `python manage.py celeryd -v 2 -B -s celery -E -l INFO`
 
 6) Open the index.html file available in relative path `CPU_UTILISATION_UI/index.html` to view the output in the form of a graph
 
  