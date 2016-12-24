from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import loader, Context
from rest_framework.response import Response
from django.shortcuts import redirect
import json

class SaveData(APIView):
    def get(self, request):
        var = None
        return render_to_response("sendmessage.html", var)

    def post(self, request):
        parameters = json.loads(request.body.decode(encoding='UTF-8'))
        customer_name = parameters['customer_name']
        customer_mail_id = parameters['customer_mail_id']
        customer_message = parameters['customer_message']
        customer_phone = parameters['customer_phone']
        try:
            subject = 'Customer Query'
            to_user_list = ["grv6262@gmail.com", "anil.bhu2009@gmail.com", "grv.deserves09@gmail.com",  "dataf3sto@gmail.com"]
            mail_html = loader.get_template('user_message.html')
            data = Context({"name": "Gaurav", "customer_name": customer_name, "customer_mail_id": customer_mail_id, "customer_phone": customer_phone, "customer_message": customer_message})
            content = mail_html.render(data)
            msg = EmailMessage(subject, content, settings.EMAIL_HOST_USER, to_user_list)
            msg.content_subtype = "html"
            msg.send()
        except:
            pass
        context = {"message": "SUCCESS", "error": "error"}
        return Response(context)

class HomePage(APIView):
    def get(self, request):
        var = None
        return redirect('/')

