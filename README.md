# Ruang Untuk Tantangan dan Permintaan

Repository ini adalah repository yang sengaja saya buat untuk menyelesaikan
tantangan tantangan yang disediakan oleh platform tertentu. Selain itu, saya
juga memberikan script yang diminta oleh rekan rekan sehingga diharapkan
dapat membantu rekan sekalian dalam mempelajari bahasa pemrograman python




# Code Sample - Konsep Tebak Huruf 1

```
import random
import string

# mendeklarasi barang berharga
chance = 10; listHuruf = []
hurufDipilih = ''; totalBenar = 0

# memasukkan huruf kapital ke dalam listHuruf
for char in string.ascii_uppercase:
    listHuruf.append(char)

# menampilkan karakter yang diizinkan
for char in listHuruf:
    print(char,end=' ')
print('')

# melakukan perulangan untuk pengguna menebak
while chance > 0:
    # memberikan keterangan index jawaban yang dimaksud
    indexRandom = random.randrange(0,len(listHuruf))
    
    # memberikan keterangan huruf yang dimaksud
    hurufRandom = listHuruf[indexRandom]
    
    # menentukan index bocoran jawaban yang diinginkan
    sebelumIndex = indexRandom + random.randrange(1, 3) #--> Samping kanan jawaban
    setelahIndex = indexRandom - random.randrange(1, 3) #--> Samping kiri jawaban
    
    # menghindari bug out of range
    if(sebelumIndex > 25): sebelumIndex = 25
    
    # memberikan bocoran jawaban yang diinginkan
    sebelumIndex = listHuruf[sebelumIndex] # mengubah variabel int
    setelahIndex = listHuruf[setelahIndex] # menjadi karakter

    # memberikan hint dan pengguna melakukan input
    print(f'\nHint --> Huruf berada diantara {setelahIndex} dan {sebelumIndex}')
    hurufDipilih = input('Tebakan anda: ')
    
    # memberitahukan ada berapa jawaban yang benar
    if(hurufDipilih == hurufRandom): totalBenar += 1; print('Jawaban Benar')
    else: print('Jawaban Salah')

    # mengurangi chance
    chance -= 1
    
# menampilkan jumlah skor
print('Total benar:', totalBenar)
    
```
