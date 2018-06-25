from django.shortcuts import render
from .models import code_model as Code_Model
import string
import os
import subprocess
import random
from django.http import JsonResponse,HttpResponse
# Create your views here.


def editor(request):
	z = subprocess.call("dir",shell=True)
	if(z):
		print("working")
	else:
		print("not working")
	default_temp = "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>\n\t\t</title>\n\t</head>\n<body>\n\n</body>\n</html>"
	if request.method == 'POST':
		custom_key = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for _ in range(8))
		while(Code_Model.objects.filter(custom_Key = custom_key).exists()):
			custom_key = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for _ in range(8))
		code_model = Code_Model()
		default_temp = request.POST['code']
		temp_key = request.POST['key']
		if temp_key:
			if 	Code_Model.objects.filter(custom_Key = temp_key).exists():
				response = JsonResponse({"error":"Keyword already exists. Try another Keyword!"})
				response.status_code = 403
				return response
			custom_key = request.POST['key']
		default_temp = default_temp.replace( '\n', '<br>')
		code_model.custom_Key = custom_key
		code_model.HTML_code = default_temp
		code_model.save()
		response = JsonResponse({'key':custom_key})
		response.status_code = 200
		return response
	default_temp = default_temp.replace( '\n', '<br>')
	print(default_temp)
	return render(request,'editor.html',{'default':default_temp})

def get_code(request,pk):
	if Code_Model.objects.filter(custom_Key = pk).exists():
		Code = Code_Model.objects.get(custom_Key = pk)
		return render(request,'editor.html',{'default':Code.HTML_code})
	#print(Code)
	else:
		return HttpResponse('<center><h1>No saved data on this URL.<br><a href="/">Go to Home</a><h1><center>')
		#return render(request,'error.html',{'default':Code.HTML_code})

def does_not_exist(request):
	return HttpResponse('<center><h1>No saved data on this URL.<br><a href="/">Go to Home</a><h1><center>')
