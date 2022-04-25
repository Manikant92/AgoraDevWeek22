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
def homepage(request):

    appID = "fdcda8c61fa54dfea8b5b5d1a1f58514"
    appCertificate = "e7dc87249c9f4a68ab90f543b8678e20"
    channelName = "test"
    uid = 2882341273
    publishKey = "pub-c-abc530cc-7203-41e7-ae7d-9358a65bcecd"
    subscribeKey = "sub-c-bb7b6ce0-c3b0-11ec-b74b-82b465a2b170"
    userAccount = "2882341273"
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Attendee, privilegeExpiredTs)
    print("Token with int uid: {}".format(token))

    return render(request, 'projectApp/index-ht.html', {'appID': appID, 'channelName': channelName, 'uid': uid, 'token': token, 'publishKey': publishKey, 'subscribeKey': subscribeKey})