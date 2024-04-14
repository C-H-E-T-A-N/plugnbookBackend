from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings

@api_view(['POST'])
@csrf_exempt
def userRegister(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if email and password:  # Ensure email and password are provided
            if not User.objects.filter(email=email).exists():  # Check if email already exists
                user = User.objects.create_user(username=username, password=password, email=email)
                return JsonResponse({'message': 'User created successfully', 'success':True}, status=201)
            else:
                return JsonResponse({'error': 'Email already exists','success':False}, status=400)
        else:
            return JsonResponse({'error': 'Email and password are required','success':False}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method allowed','success':False}, status=405)

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['POST'])
@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
        print(request.body)
        email = request.data.get('email')
        password = request.data.get('password')
        # email = request.POST.email
        # password = request.POST.password
        print(request.data.get('email'))
        print(email)
        # Check if a user with the provided email exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'}, status=400)
        
        # Authenticate the user using email and password
        user = authenticate(request, username=user.username, password=password)
        
        if user is not None:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful','token':token})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid email or password'}, status=400)
    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)

from unicodedata import name
from django.shortcuts import render
import razorpay

razorpay_client = razorpay.Client(auth=("rzp_test_uimqIRUwRnutpf", "hAic5Kp0zOpCkMUWLqpE8etL"))

@csrf_exempt
@api_view(['POST'])
def Token_Fee(request):
    if request.method == "POST":

        print("", request.POST['price'])
        amount = int(request.POST['price'])
        product_name = request.POST['product_name']

        new_order_response = razorpay_client.order.create({
                        "amount": amount*100,
                        "currency": "INR",
                        "payment_capture": "1"
                      })

        response_data = {
                "callback_url": "http://127.0.0.1:8000/app/callback",
                "razorpay_key": "rzp_test_uimqIRUwRnutpf",
                "order": new_order_response,
                "product_name": product_name
        }

        print(response_data)
        return JsonResponse(response_data)    

    
@csrf_exempt
@api_view(['POST'])
def order_callback(request):
    if request.method == "POST":
        print(request.data)
        print(request.data.get('razorpay_signature'))
        params_dict = {
        'razorpay_order_id': request.data.get('razorpay_order_id'),
        'razorpay_payment_id': request.data.get('razorpay_payment_id'),
        'razorpay_signature': request.data.get('razorpay_signature')
        }
        if "razorpay_signature" in request.data:
            payment_verification = razorpay_client.utility.verify_payment_signature(params_dict)
            if payment_verification:
                return JsonResponse({"res":"success", "success":True})
                # Logic to perform is payment is successful
            else:
                return JsonResponse({"res":"failed1"})
                # Logic to perform is payment is unsuccessful
        else:
            return JsonResponse({"res":"failed2"})
