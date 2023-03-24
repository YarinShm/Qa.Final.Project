

import requests
#res = requests.get('https://fruityvice.com/api/fruit/banana')


def send_http_request(url):
    res = requests.get(url)
    return res

def code_site(url):
    code = send_http_request(url).status_code
    return code

def Check_status_code(code):
    if 199 < code < 400:
        return True
    else:
        return False


def Does_it_contain_number(url, inside, dictionary):
    valeus = send_http_request(url).json()
    if inside == valeus[dictionary]:
        return True
    else:
        return False

def Does_it_contain_value(url, inside, dictionary):
    valeus = send_http_request(url).json()
    if inside in valeus[dictionary]:
        return True
    else:
        return False


def Check_how_many_Jsons(url):
    group = send_http_request(url).json()
    print(f'\n {len(group)} ')
    return len(group)


def How_many_nut_values(url,locatin):
    valeus = send_http_request(url).json()
    nut =valeus['nutritions']
    print(nut[locatin])
    return nut[locatin]




