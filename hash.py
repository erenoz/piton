import csv
def hash(csv_dosyasi):
    hash_listesi = dict()
    top = 0
    i = 1
    for row in csv.reader(open(csv_dosyasi)):
        for col in row:
            tmp=col[0].split(';')
            tmp2=col[1].split(';')
            top += ord(tmp[0])**2 + ord(tmp2[0])**(0.5)
            
        hash_listesi[i] = top % 64
        i = i + 1
    return hash_listesi
#hash('ogrenci_Listesi.csv')
