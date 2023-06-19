import dns
def check_mx_records(domain: str)-> bool:
    import dns.resolver
    mx = []
    try:
        responses = dns.resolver.query(domain, 'MX')    
        mx = [str(r.exchange)[:-1] for r in responses]
        print(mx)
        return True
    except dns.resolver.NoAnswer:
        return False
check_mx_records("gmail.com")
check_mx_records("kfifoifzoifoiz.com")

def check_server_mail(domain: str) -> bool:
    import smtplib
    try:
        with smtplib.SMTP(domain) as smtp:
            print("Status:Done")
            return True
    except(smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected):
        print('Status:not done ')
        return False
check_server_mail("gmail.com")
check_server_mail('kfifoifzoifoiz.com')