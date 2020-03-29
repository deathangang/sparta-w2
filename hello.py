
def check_mail(s):
     tst1 = s.split('@')
     if tst1[1] == 'gmail.com':
        return True
     else:
        return False

a = 'spartacodingclub@gmail.com'
print(check_mail(a))

