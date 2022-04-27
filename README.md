# DeveloperWeek2022 - Agora Submission

### Setup:
1. Download the Code Repo
2. Python version - 3.7.9
3. Set up virtualEnv: py -m venv DevWeek -> DevWeek\Scripts\activate.bat
4. Install the modules present in requirements.txt to install the necessary components
5. Go to AgoraSign/settings.py and provide email and password for your application's email
6. Create an account at https://www.agora.io/en/ and copy paste the appId and appCertificate into the method: joinMeet() of projectApp/views.py
7. Create an account at https://www.pubnub.com/ and copy paste the publisherKey and subscriberKey into the method: joinMeet() of projectApp/views.py
8. Go to AgoraSign/projectApp and run "python manage.py runserver"
9. Navigate to localhost:8000/homepage to get started

### Project Submission: 
https://devpost.com/software/lessontutor
