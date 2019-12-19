from django.shortcuts import render
import pandas as pd 
from task_app.models import UserInfo
import re 
from django.http import JsonResponse
from django.db.models import Q
import json
from django.core import serializers

regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

def check_email(email):  
	if(re.search(regex,email)):
		return True
	else:
		return False

def check_mobile_no(mobile_no):
	# 1) Begins with 0 or 91 
    # 2) Then contains 7 or 8 or 9. 
    # 3) Then contains 9 digits
	Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
	return Pattern.match(str(mobile_no))


# Create your views here.

def search(request):
	fieldlist = UserInfo._meta.get_fields()
	tag_list = []
	for field in fieldlist:
		tag_list.append(field.name)
	data = {
		'tag_list':tag_list
	}
	return render(request,"task_app/search.html",context=data)


def upload(request):
	if request.method == "POST":
		excel_file = request.FILES["excel_file"]
		df = pd.read_excel(excel_file) 
		for index, row in df.iterrows():
			if check_email(row['Email']) and check_mobile_no(row['Phone Number']):
				model = UserInfo()
				model.name = row['Name']
				model.email = row['Email']
				model.phone_number = row['Phone Number']
				model.date_of_birth = row['Date of Birth']
				model.save()
			else:
				continue
		return render(request,"task_app/search.html")
	return render(request,"task_app/upload.html")



def requested_search(request):
	input_value = request.GET.get('inputValue', None)
	selected_search_field = request.GET.get('selectedSearchField', None)
	list_of_data = Q()
	search_type = 'startswith'
	key_filter = selected_search_field + '__' + search_type
	list_of_data = Q(**{key_filter:input_value})
	search_result_obj = UserInfo.objects.filter(list_of_data)
	filtered_search_list_val = list(search_result_obj.values_list('name','email','phone_number','date_of_birth'))
	response_data={
    	'output_data':filtered_search_list_val
    }
	return JsonResponse(json.dumps(response_data), safe=False)

