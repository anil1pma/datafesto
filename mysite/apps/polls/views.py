from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from rest_framework.views import APIView
import json
from polls.models import SendMessage
import time
import calendar
from django.utils.dateparse import parse_date

class SaveData(APIView):
    def get(self, request):
        var = None
        return render_to_response("sendmessage.html", var)

    def post(self, request):
        info = json.loads(request.body)
        mob_no = info['mobnumber']
        msg = info['message']
        mail_id = info['emailaddress']
        msg_through = info['message_through']
        msg_time = info['message_time']
        SendMessage.objects.create(user_mob_no=mob_no, user_message=msg, user_mail_id=mail_id, user_message_through= msg_through, user_msg_date_time=msg_time)
        return HttpResponse("success")
