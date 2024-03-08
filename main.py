import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Your Cloudflare details
cf_api_token = os.getenv('cf_api_token')
cf_zone_id = os.getenv('cf_zone_id')
cf_aaa_record_id = os.getenv('cf_aaa_record_id')
cf_a_record_id = os.getenv('cf_a_record_id')


def get_public_ipv6():
    return requests.get('https://api6.ipify.org?format=json').json()['ip']

def get_public_ipv4():
    return requests.get('https://api4.ipify.org?format=json').json()['ip']

def update_ipv4_dns(ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{cf_zone_id}/dns_records/0f101e476e17c76002b7670e63614ef6"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cf_api_token}"
    }

    data = {
        "content": ip,
        "name": "neilclack.com",
        "proxied": False,
        "type": "A",
        "comment": "Updated via PyDDNS",
        "ttl": 120
    }

    response = requests.patch(url, headers=headers, json=data)

    return response.json()

def update_ipv6_dns(ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{cf_zone_id}/dns_records/87ee691c74c3e0a567cf7d7ce7f41b96"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cf_api_token}"
    }

    data = {
        "content": ip,
        "name": "neilclack.com",
        "proxied": False,
        "type": "AAA",
        "comment": "Updated via PyDDNS",
        "ttl": 120
    }

    response = requests.patch(url, headers=headers, json=data)

    return response.json()


if __name__ == '__main__':
    while True:
        # try:
        #     public_ip = get_public_ipv6()
        #     update_ipv6_dns(public_ip)
        #     print(f'DDNS AAA updated successfully. New IP: {public_ip}')
        # except Exception as e:
        #     print(f'Error updating DDNS: {e}')
        
        try:
            public_ip = get_public_ipv4()
            update_ipv4_dns(public_ip)
            print(f'DDNS A updated successfully. New IP: {public_ip}')
        except Exception as e:
            print(f'Error updating DDNS: {e}')

        time.sleep(1800)  # Sleep for 30 minutes before checking and updating again

