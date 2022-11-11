'''
Studi Kasus

Pak Fatih memiliki Toko Buah Faishal dengan urutan buah ["Durian", "Semangka", "Pepaya", "Alpukat", "Tomat", "Mangga", "Melon", "Nanas", "Apel", "Pisang"].

Perintah --> Urutkan buah tersebut menurut abjad, Namun sayangnya Pak Fatih tidak suka mengurutkan dengan otomatis, Selesaikan dengan perulangan.
 '''
 
import string
 
 # deklarasi listBuah
listBuah = ["Durian", "Semangka", "Pepaya", "Alpukat",
"Tomat", "Mangga", "Melon", "Nanas", "Apel", "Pisang"]
 
 # membuat listHuruf untuk membandingkan urutan huruf
listHuruf = []
 
 # memasukkan huruf ke dalam list
for huruf in string.ascii_uppercase:
    listHuruf.append(huruf)
    
    
# melakukan print sebelum diurutkan untuk perbandingan
print(f'Sebelum diurutkan: \n{listBuah}\n')
     
# melakukan sorting dengan membandingkan urutan index huruf pertama
for count in range(len(listBuah)):
    for compareOne in listBuah:
        for compareTwo in listBuah:
            # mendeteksi urutan buah di dalam listBuah
            if (listHuruf.index(compareOne[0]) < listHuruf.index(compareTwo[0])):
                # menampilkan hasil debug
                '''
                print(listBuah)
                print('Membandingkan antara', listBuah[listBuah.index(compareOne)], 'dan', listBuah[listBuah.index(compareTwo)])
                print('lebih dulu', compareOne); print('\n')
                '''
                
                # penyimpanan sementara
                pivot = listBuah[listBuah.index(compareOne)]
                
                # melakukan penukaran
                listBuah[listBuah.index(compareOne)] = listBuah[listBuah.index(compareTwo)]
                
                # mengambil dari penyimpanan sementara
                listBuah[listBuah.index(compareTwo)] = pivot
            
            
# melakukan print setelah diurutkan untuk perbandingan
print(f'Setelah diurutkan: \n{listBuah}')
