import string
import random

def check_server_mail(list_domain: list) -> bool:
    import smtplib
    list_domains_available = []
    try:
        for i in range(len(list_domain)):
            with smtplib.SMTP(list_domain[i]) as smtp:
                list_domains_available.append(list_domain[i])
        print(len(list_domain))
        print(len(list_domains_available))
        if len(list_domain) == len(list_domains_available):
            return True
        else:
            return True #ça veut dire que les serveurs mail existent mais la connexion est possible mais refus de leur part. (donc fonctionnels) Cependant cela ne veut pas dire qu'ils ne sont pas fonctionnels. On a quand meme réussi à avoir une réponse.
    except(smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected):
        return False #non fonctionnels problèmes de connexion.


def check_server_mail_(list_domain: list) -> bool:
    import smtplib
    list_domains_available = []
    try:
        for i in range(len(list_domain)):
            with smtplib.SMTP(list_domain[i]) as smtp:
                list_domains_available.append(list_domain[i])
        print(len(list_domain))
        print(len(list_domains_available))
        print(list_domain)
        print(list_domains_available)
        if len(list_domain) == len(list_domains_available):
            return True, len(list_domain), list_domains_available
        else:
            return False,len(list_domain), len(list_domains_available),list_domain, list_domains_available
    except(smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected):
        return False, len(list_domain), len(list_domains_available), list_domain, list_domains_available


def services(database_name, payload: dict):
    database_name.save(payload)

def attempt(mx: list)->bool:
    list_ = []
    try:
        for i in range(len(mx)):
            server = smtplib.SMTP(mx[i])
            print(f"test réussi {mx}")
            server.quit()
            list_.append(mx[i])
        if len(mx) == len(list_):
            return True, list_
        else:
            return False, list_ 
    except:
        print(f"test non réussi")
        return False 


def choose_country()->str:
    import random 
    import pycountry
    from pycountry import countries
    final_list_of_countries_imported_uwu = []
    for i in range(len(pycountry.countries)):
        final_list_of_countries_imported_uwu.append(list(pycountry.countries)[i].name.upper())
    return final_list_of_countries_imported_uwu[random.randint(0, len(final_list_of_countries_imported_uwu))]

def list_country()->list:
    import random 
    import pycountry
    from pycountry import countries
    final_list_of_countries_imported_uwu = []
    for i in range(len(pycountry.countries)):
        final_list_of_countries_imported_uwu.append(list(pycountry.countries)[i].name.upper())
    return final_list_of_countries_imported_uwu

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
def check_mx_records(domain: str)->bool:
    import dns.resolver
    mx = []
    try:
        responses = dns.resolver.resolve(domain, 'MX')
        mx = [str(r.exchange)[:-1] for r in responses]
        return mx
    except dns.resolver.NoAnswer:
        return False

def _list_countries()->list:
    import random 
    import pycountry
    from pycountry import countries
    final_list_of_countries_imported_uwu = []
    for i in range(len(pycountry.countries)):
        final_list_of_countries_imported_uwu.append(list(pycountry.countries)[i].name.upper())
    return final_list_of_countries_imported_uwu

def generate_email()->str:
    debut = []
    domain = []
    endings = []
    characters = string.digits + string.punctuation + string.ascii_lowercase + string.ascii_lowercase.upper() 
    for i in range(random.randint(4, 15)):
        debut.append(characters[random.randint(0, len(characters) - 1)])
    username_email = "".join(debut)
    for i in range(random.randint(5, 10)):
            domain.append(characters[random.randint(0, len(characters) - 1)])
    domain_email = "".join(domain)
    for i in range(len(string.ascii_lowercase)):
        for j in range(26):
            if j <= 26:
                endings.append(string.ascii_lowercase[i] + string.ascii_lowercase[j])
    final_email = f"{username_email}@{domain_email}.{endings[random.randint(0, len(endings) - 1)]}"
    print(endings)
    print(domain)
    print(debut)
    return final_email


test_fonction_check_server_mail = check_server_mail(check_mx_records("ent.auvergnerhonealpes.fr"))
test_fonction_attempt = attempt(check_mx_records("ent.auvergnerhonealpes.fr"))
print(f"Ceci est le test avec la fonction check_server_mail {test_fonction_check_server_mail}")
print(f"Ceci est le test avec la fonction attempt {test_fonction_attempt}")
check =check_mx_records("ent.auvergnerhonealpes.fr")
print(f"le check des mx est celui ci {check}")
try:
    import smtplib
    with smtplib.SMTP(str(check[0])) as smtp:
        smtp.connect("ayoub.semsar@ent.auvergnerhonealpes.fr","kolea21342")
except:
    print("Not done")

