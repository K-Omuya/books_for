import requests
import datetime
import base64
from django.conf import settings

def format_phone_number(phone_number):
    if phone_number.startswith('0'):
        return '+254' + phone_number[1:]
    elif phone_number.startswith('254'):
        return '+254' + phone_number[3:]
    elif phone_number.startswith('+254'):
        return phone_number
    else:
        raise ValueError("Invalid Safaricom number format. Ensure it starts with 07 or 01.")

def get_mpesa_access_token():
    auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(auth_url, auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET))
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception("Failed to generate access token. Check your credentials.")

def initiate_stk_push(safaricom_number, amount):
    formatted_number = format_phone_number(safaricom_number)
    access_token = get_mpesa_access_token()
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(
        (settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode('utf-8')
    ).decode('utf-8')

    stk_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": formatted_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": formatted_number,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "Book Exchange",
        "TransactionDesc": "Payment for Book Exchange",
    }
    response = requests.post(stk_url, json=payload, headers=headers)
    return response.json()
