def check_server_mail(domain: str) -> bool:
    import smtplib
    try:
        with smtplib.SMTP(domain) as smtp:
            print(f"There is a server mail behind {domain}")
            return True
    except(smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected):
        print(f"There is not a server mail behind this domain {domain}")
        return False


def services(database_name, payload: dict):
    database_name.save(payload)


def choose_country()->str:
    import random 
    import pycountry
    from pycountry import countries
    final_list_of_countries_imported_uwu = []
    for i in range(len(pycountry.countries)):
        final_list_of_countries_imported_uwu.append(list(pycountry.countries)[i].name.upper())
    return final_list_of_countries_imported_uwu[random.randint(0, len(final_list_of_countries_imported_uwu))]


def generate_password():
    import string
    import random 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(random.randint(0,8)))
    return password


def generate_random_ip()->str:
    import random
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip


def valid_ip(ip)->bool:
    import ipaddress
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
def check_mx_records(domain: str)-> list or bool:
    import dns.resolver
    mx = []
    try:
        responses = dns.resolver.resolve(domain, 'MX')
        mx = [str(r.exchange)[:-1] for r in responses]
        return mx
    except dns.resolver.NoAnswer:
        return False
print(check_mx_records("gmail.com"))
print(check_server_mail(str(check_mx_records("gmail.com")[0])))
print(valid_ip("127.0.0.1"))
def _list_countries()->list:
    import random 
    import pycountry
    from pycountry import countries
    final_list_of_countries_imported_uwu = []
    for i in range(len(pycountry.countries)):
        final_list_of_countries_imported_uwu.append(list(pycountry.countries)[i].name.upper())
    return final_list_of_countries_imported_uwu
print(_list_countries())
print('algeria'.upper() in _list_countries())
print('france'.upper() in _list_countries())

