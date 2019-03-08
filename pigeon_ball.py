from random import shuffle

kirmizi = []
mavi = []
beyaz = []
# dizilere renkleri doldur
k = 10
for x in range(k):
    kirmizi.append('K')
    mavi.append('M')
    beyaz.append('B')

print('\nkirmizi : {}'.format(kirmizi))
print('mavi : {}'.format(mavi))
print('beyaz : {}\n'.format(beyaz))

tum_renkler = []
# tum renkler dizisi olustur renkler sirali cekilmeyecegi icin karistir
tum_renkler = kirmizi + mavi + beyaz
shuffle(tum_renkler)

print('tum renkler : {}\n'.format(tum_renkler))

secilen_kirmizi = []
secilen_mavi = []
secilen_beyaz = []
for x in range(k*3):
    secilen_renk = tum_renkler[x]

    if secilen_renk == 'K':
        secilen_kirmizi.append('K')
    elif secilen_renk == 'M':
        secilen_mavi.append('M')
    elif secilen_renk == 'B':
        secilen_beyaz.append('B')

    # tum renklerden en az 4 tane secilmis ise secmeyi birak
    if len(secilen_kirmizi) >= 4 and len(secilen_mavi) >= 4 and len(secilen_beyaz) >= 4:
        print('her renkten en az 4 tane secildi !')
        print('secilen top sayisi : {} (her zaman 10dan buyuk olur)'.format(x))
        print('secilen kirmizi : {} {} tane'.format(secilen_kirmizi, len(secilen_kirmizi)))
        print('secilen mavi : {} {} tane'.format(secilen_mavi, len(secilen_mavi)))
        print('secilen beyaz : {} {} tane\n'.format(secilen_beyaz, len(secilen_beyaz)))
        break
