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

class SaveData(APIView):
    def get(self, request):
        var = None
        return render_to_response("sendmessage.html", var)

    def post(self, request):
        name = "Gaurav"
        customer_name = request.DATA.get('customer_name')
        customer_mail_id = request.DATA.get('customer_mail_id')
        customer_message = request.DATA.get('customer_message')
        customer_phone = request.DATA.get('customer_phone')
        try:
            subject = 'Customer Query'
            to_user_list = ["grv6262@gmail.com", "grv.deserves09@gmail.com",  "dataf3sto@gmail.com"]
            mail_html = loader.get_template('user_message.html')
            data = Context({"name": name, "customer_name": customer_name, "customer_mail_id": customer_mail_id, "customer_phone": customer_phone, "customer_message": customer_message})
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

