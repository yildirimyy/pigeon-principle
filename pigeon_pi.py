import math

# bos dictionary olustur
dizi = dict()
max = 1001
pi = math.pi
# n carpi pi
n_pi = 0
# m carpi pi
m_pi = 0
m = 0
n = 0
for n in range(0, max):
    n_pi = n * pi

    # 146,487.. * 1000 = 146487,.. % 1000 -> 487,...
    uc_eleman = (n_pi * 1000) % 1000
    # 487,... -> 487
    uc_eleman = int(math.floor(uc_eleman))

    # dizinin icinde ilk uc eleman yoksa diziye ata carpmaya devam et
    if not uc_eleman in dizi:
        dizi[uc_eleman] = n
    else:
        # dizinin icinde varsa eski carpimdaki n(m sayisini) bul
        m = dizi[uc_eleman]
        # for dongusunden cik
        break

m_pi = m * math.pi
# n ve m sayilarini cikar yuvarla
pay = round(n_pi - m_pi)
pay = int(pay)
payda = n - m
sonuc = pay / payda

print('')
print('{} (m: {}, n : {})'.format(pay, m, n))
print('--- : {}'.format(sonuc))
print('{}'.format(payda))
print('')
print(' yaklasik : {}'.format(sonuc))
print(' pi : {}'.format(pi))
print('')
