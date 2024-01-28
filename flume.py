from credentials import *
import requests
import json

BASE_URL = 'https://api.flumewater.com'
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
access_token = None
refresh_token = None


def get_oauth_token():
    oauth_url = f'{BASE_URL}/oauth/token?envelope=true'
    oauth_token_payload = { 
        "grant_type": "password", # must be password
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "username": CLIENT_USERNAME,
        "password": CLIENT_PASSWORD   
    }
    response = requests.post(oauth_url, json=oauth_token_payload, headers=headers)
    # print(vars(response))
    return response.text


def read_from_tokens_file():
    global access_token, refresh_token
    try:
        with open('./tokens.json', 'r') as tokens_file:
            contents = tokens_file.read()
            contents = json.loads(contents)
            # print(contents)
            access_token = contents['access_token']
            refresh_token = contents['refresh_token']
            print('loaded tokens from file!')
            return True
    except Exception as e:
        print(f'ERROR READING TOKENS FILE - {type(e).__name__} - {e}')
    return False


def write_to_tokens_file():
    global access_token, refresh_token
    try:
        with open('./tokens.json', "w") as tokens_file:
            contents = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            # print(contents)
            tokens_file.write(json.dumps(contents, indent=2))
            return True
    except Exception as e:
        print(f'ERROR WRITING TOKENS FILE - {type(e).__name__} - {e}')
    return False


def check_token_valid():
    url = f'{BASE_URL}/me'
    bearer = headers.copy()
    bearer['Authorization'] = f'Bearer {access_token}'
    response = requests.get(url, headers=bearer)
    response = json.loads(response.text)
    print(json.dumps(response, indent=2))
    if response['http_code'] == 200:
        print(f'token valid!')
        return True
    else:
        print(f'token invalid!')
        return False
    

def get_devices():
    url = f'{BASE_URL}/me/devices'
    bearer = headers.copy()
    bearer['Authorization'] = f'Bearer {access_token}'
    response = requests.get(url, headers=bearer)
    response = json.loads(response.text)
    return response


if not read_from_tokens_file() or not check_token_valid():
    api_credentials = json.loads(get_oauth_token())
    access_token = api_credentials['data'][0]['access_token']
    refresh_token = api_credentials['data'][0]['refresh_token']
    write_to_tokens_file()
    

# print(f'access_token: {access_token}')
# print(f'refresh_token: {refresh_token}')

print(get_devices())
