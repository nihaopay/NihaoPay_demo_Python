# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
import requests
from .models import SECUREPAY
import os
import io
import string
import urllib

# Create your views here.
def index(request):
    url = 'https://apitest.nihaopay.com/v1.2/transactions/securepay'
    template =loader.get_template('main.html')
    context = {
        "term": "invalid POST"
    }
    if request.POST:
        term =request.POST.get('term')
        # change your reference per your test, reference String have to be unique during the process.
        # See the document detail in https://docs.nihaopay.com/api/v1.2/en/#create-a-standard-securepay
        data = '{"amount":"'+term+'", "currency":"USD","vendor":"unionpay","reference":"helloworldreferencenum","ipn_url":"https://demo.nihaopay.com/ipn","callback_url":"http://YourCallback_URL"}'
        response = requests.post(url, data=data, headers={"Content-Type": "application/json",
                                                          "authorization": "Bearer YourTokenNumber"})
        return HttpResponse(response)

    return HttpResponse(template.render(context,request))
#  Success Response
# Array
# (
#     [id] => YourtransactionID
#     [amount] => 500
#     [currency] => USD
#     [reference] => YourreferenceNumber
#     [status] => success
#     [time] => 2017-10-30T17:11:05Z
#     [note] => null
#     [verify_sign] => de289acc324ca654007151b314205ea6
# )
#


# To verify your transaction on the callback_url:
# <?php
# header('Content-type: text/plain');
# ksort($_REQUEST);
# $result="";
# foreach($_REQUEST as $x => $x_value){
#         if($x_value!="null"&&$x_value!=null&&$x!="verify_sign"){
#                 $result.=$x."=".$x_value."&";
#         }
# }
# $token =YourtokenNumber;
# $check =md5($result.md5($token));
# if($check===$_REQUEST["verify_sign"]){
#         echo "\n*********************\nsuccess\n************************\n";
# }
# ?>
#

def generateQRcode(request):
    url = 'https://apitest.nihaopay.com/v1.2/transactions/qrcode'
    template = loader.get_template('main.html')
    context = {
        "term": "invalid POST"
    }
    if request.POST:
        term = request.POST.get('term')
        print(term)
        b = []
        reference = 55
        # See the document detail in https://docs.nihaopay.com/api/v1.2/en/#generate-a-wechat-qrcode
        data = '{"amount":"' + term + '", "currency":"USD","reference":"helloworld' + str(reference) + '","ipn_url":"https://demo.nihaopay.com/ipn"}'
        response = requests.post(url, data=data, headers={"Content-Type": "application/json",
                                                          "authorization": "Bearer YourTokenNumber"})
        return HttpResponse(response)
    return HttpResponse(template.render(context, request))


#  Success Response
# {"amount":500,
    # "id":"20171030172724017870",
    # "time":"2017-10-30T17:27:24Z",
    # "code_url":"weixin://wxpay/bizpayurl?pr=v8h3Zbq",
    # "reference":"helloworld51",
    # "timeout":120,
    # "currency":"USD"
# }

# code_url is the generated QRcode