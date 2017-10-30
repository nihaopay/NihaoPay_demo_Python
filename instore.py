# $ curl https://api.nihaopay.com/v1.2/transactions/scanqrcode \
# -H "Authorization: Bearer <TOKEN>" \
# -d amount=100 \
# -d currency="USD" \
# -d vendor="alipay" \
# -d reference="alipay201705030002" \
# -d buyer_identity_code="288463639882104202" \
# -d client_ip="184.167.25.158" \
# -d note="alipay" \
# -d description="Scan AliPay QrCode"
# https://api.nihaopay.com/v1.2/transactions/scanqrcode
import requests
# Scan QRcode
# url ='https://apitest.nihaopay.com/v1.2/transactions/scanqrcode'
# data = '{"amount": 10, "currency":"USD","vendor":"wechatpay","reference":"helloworldinstore3","buyer_identity_code":"134735342449292804","client_ip":"54.153.51.151","note":"alipay"}'
# response = requests.post(url, data=data,headers={"Content-Type": "application/json","Authorization":"Bearer e0cbab0bee37c1206b0d6430c86813531e0419488072cef8f48a49ad0c97f394"})


# Show QRcode
url='https://apitest.nihaopay.com/v1.2/transactions/showqrcode'
data = '{"amount": 1, "currency":"USD","vendor":"wechatpay","reference":"helloworldinstore4","ipn_url":"http://54.153.51.151/nihaopay.php"}'
response = requests.post(url, data=data,headers={"Content-Type": "application/json","Authorization":"Bearer e0cbab0bee37c1206b0d6430c86813531e0419488072cef8f48a49ad0c97f394"})

# Static QRcode
# url='https://apitest.nihaopay.com/v1.2/merchantqrcode'
# data = '{"trade_currency":"USD","vendor":"alipay","seller_name":"helloworldinstore4","store_name":"helloworld","store_no":"B001"}'
# response = requests.post(url, data=data,headers={"Content-Type": "application/json","Authorization":"Bearer e0cbab0bee37c1206b0d6430c86813531e0419488072cef8f48a49ad0c97f394"})



print(response)
print(response.text)
