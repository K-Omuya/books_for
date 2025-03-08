import requests
import base64
import datetime
from django.conf import settings

def get_mpesa_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    headers = {
        "Authorization": "Basic " + base64.b64encode(
            f"{settings.MPESA_CONSUMER_KEY}:{settings.MPESA_CONSUMER_SECRET}".encode()
        ).decode()
    }
    response = requests.get(url, headers=headers)
    return response.json().get("access_token")

def initiate_payment(phone_number, amount=20):
    access_token = get_mpesa_access_token()
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode(f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()).decode()

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "BookUpload",
        "TransactionDesc": "Payment for book upload"
    }

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
