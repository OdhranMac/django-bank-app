from django.shortcuts import render
from django.http import HttpResponse
import requests

# azure url
logic_app_url = 'https://prod-25.uksouth.logic.azure.com:443/workflows/4a91e276d852499dacc021181da7241d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=YgVS-ISBtp84bRhbttyLVwohh9fxbQPsSdqfxiWPDuc'

# Create your views here.
def display_page(request): 
    return render(request, 'transform.html')

def post_to_azure(request):
    print('request to post to azure recieved')
    # requests.post(logic_app_url, json = {}) # DISABLED UNTIL ALL WORKING
    return render(request, 'run.html') # change to below?
    #display_running()

""" page for 'running' """
def display_running(request):
    return render(request, 'run.html')

# def request_page(request):
#     if(request.GET.get('mybtn')):
#         requests.post(logic_app_url, json = {})
#     return render(request,'run.html')