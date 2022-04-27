from django.shortcuts import render
import sys
import os
import time
from random import randint
from django.contrib.auth.decorators import login_required
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .src.RtcTokenBuilder import RtcTokenBuilder,Role_Attendee


# Create your views here.
@login_required(login_url='/login')
def joinmeet(request):

    appID = "<appID>" # From Agora console
    appCertificate = "<appCert>" # From Agora Console
    channelName = "test"
    uid = 2882341273
    publishKey = "<pubKey>" # From PubNub console
    subscribeKey = "subKey" # From PubNub console
    userAccount = "2882341273"
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

    # Token builder
    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Attendee, privilegeExpiredTs)
    print("Token with int uid: {}".format(token))

    return render(request, 'projectApp/index-ht.html', {'appID': appID, 'channelName': channelName, 'uid': uid, 'token': token, 'publishKey': publishKey, 'subscribeKey': subscribeKey})


@login_required(login_url='/login')
def homepage(request):
    return render(request, 'projectApp/homepage.html')



@login_required(login_url='/login')
def coursePage(request):
    return render(request, 'projectApp/coursePage.html')