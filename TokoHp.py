import os

def garis(jum):
    print('=' * jum)
    
def min(payment):
    total = print('\nSisa uang anda saat ini Rp.', moneyBuyer - payment)
    print('\n')
    garis(60)
    print('Terima kasih sudah melakukan transaksi di toko Atsalsuki!!!')
    garis(60)
    return total

moneyBuyer = 2000000
sumsang = 500000
appa = 350000
linivi = 200000
pecce = 250000
servLinivi = 100000
servPecce = 150000

listMenu = ['1. Beli Hp Baru','2. Beli Hp Seken', '3. Service Hp']
listHpBaru = ['\n1. Sumsang (Harga: RP. 500000)', '2. Appa (Harga: RP. 350000)']
listHpSeken = ['\n1. Linivi (Harga: RP. 200000)', '2. Pecce (Harga: Rp. 250000)']
listServiceHp = ['\n1. Linivi (Harga: Rp. 100000)', '2. Pecce (Harga: Rp. 150000)']


os.system('cls')
garis(65)
print('\t\tSELAMAT DATANG DI TOKO HP ATSALSUKI')
garis(65)

passw = input('\nSilahkan masukkan nama toko ini untuk melanjutkan transaksi: ')

if passw == 'ATSALSUKI':
    print('Nama toko yang anda masukkan benar!!!\n')

    try :
        os.system('cls')
        garis(55)
        print('\tBerikut daftar menu yang dapat anda pilih')
        garis(55)
        
        for i in range (0, len(listMenu)):
            print(listMenu[i])
            
        choose1 = int(input('\nSilahkan pilih menu yang tersedia (INPUT HARUS BERUPA ANGKA) : '))
        choose1 != 1 or 2 or 3
        
        if choose1 == 1:
            try :
                os.system('cls')
                garis(65)
                print('\tBerikut daftar Hp Baru yang dapat anda beli!!!')
                garis(65)
                
                for i in range(0,len(listHpBaru)):
                    print(listHpBaru[i])
                    
                choose2 = int(input('\nSilahkan pilih menu yang tersedia (INPUT HARUS BERUPA ANGKA) : '))
                choose2 != 1 or 2
                
                if choose2 == 1:
                    os.system('cls')
                    print('\nAnda akan membeli Hp Sumsang dengan harga RP. 500000')
                    print('\nTotal uang yang anda miliki saat ini RP.',moneyBuyer)
                    payment1 = int(input('\nJumlah Hp yang akan dibeli: '))
                    payment1 = payment1 * sumsang
                    
                    if payment1 > 2000000:
                        print('\nMaaf uang yang anda miliki saat ini tidak cukup!!!')
                        print('\nSilahkan mengulang program dari awal!!!')
                        exit()
                    
                        
                    print('\nTotal pembayaran sebesar Rp.',payment1)
                    min(payment1)
                       
                elif choose2 == 2:
                    os.system('cls')
                    print('\nAnda akan membeli Hp Appa dengan harga Rp. 350000')    
                    print('\nTotal uang yang anda miliki saat ini RP.',moneyBuyer)
                    payment2 = int(input('Jumlah Hp yang akan dibeli: '))
                    payment2 = payment2 * appa
                    
                    if payment2 > 2000000:
                        print('\nMaaf uang yang anda miliki saat ini tidak cukup!!!')
                        print('\nSilahkan mengulang program dari awal!!!')
                        exit()
                    
                    
                    print('Total pembayaran sebesar Rp.',payment2)
                    min(payment2)
                
                else:
                    print('\nMaaf pilihan menu yang anda masukkan tidak tersedia!')               
            except (ValueError,TypeError):
                print('\nMaaf anda hanya harus memberikan input angka 1 atau 2, dan tidak boleh keduanya!!!')  
      
        elif choose1 == 2:
                    
            try:
                os.system('cls')
                garis(65)
                print('\tBerikut daftar Hp Seken yang dapat anda beli!!!')
                garis(65)

                for i in range(0,len(listHpSeken)):
                    print(listHpSeken[i])
                    
                choose3 = int(input('\nSilahkan pilih menu yang tersedia (INPUT HARUS BERUPA ANGKA) : '))
                choose3 != 1 or 2
                    
                if choose3 == 1:
                    os.system('cls')
                    print('\nAnda akan membeli Hp Linivi dengan harga RP. 200000')
                    print('\nTotal uang yang anda miliki saat ini RP.',moneyBuyer)
                    payment3 = int(input('\nJumlah Hp yang akan dibeli: '))
                    payment3 = payment3 * linivi
                    
                    if payment3 > 2000000:
                        print('\nMaaf uang yang anda miliki saat ini tidak cukup!!!')
                        print('\nSilahkan mengulang program dari awal!!!')
                        exit()
                    
                    print('\nTotal pembayaran sebesar Rp.',payment3)
                    min(payment3)

                    
                elif choose3 == 2:
                    os.system('cls')
                    print('\nAnda akan membeli Hp Seken Pecce dengan harga Rp. 250000')
                    print('\nTotal uang yang anda miliki saat ini RP.',moneyBuyer)
                    payment4 = int(input('\nJumlah Hp yang akan dibeli: '))
                    payment4 = payment4 * pecce
                    
                    if payment4 > 2000000:
                        print('\nMaaf uang yang anda miliki saat ini tidak cukup!!!')
                        print('\nSilahkan mengulang program dari awal!!!')
                        exit()
                    
                    print('\nTotal pembayaran sebesar Rp.',payment4)
                    min(payment4)
                else:
                    print('\nMaaf pilihan menu yang anda masukkan tidak tersedia!')               
            except (ValueError,TypeError):
                print('\nMaaf anda hanya harus memberikan input angka 1 atau 2, dan tidak boleh keduanya!!!')
        
        elif choose1 == 3:
            try:
                os.system('cls')
                garis(65)
                print('\tBerikut daftar merk Hp yang dapat anda service!!!')
                garis(65)
                
                for i in range(0,len(listServiceHp)):
                    print(listServiceHp[i])
                    
                choose4 = int(input('\nSilahkan pilih menu yang tersedia (INPUT HARUS BERUPA ANGKA) : '))
                choose4 != 1 or 2
                
                if choose4 == 1:
                    os.system('cls')
                    print('\nAnda akan menservice Hp Linivi dengan harga Rp. 100000')
                    print('\nTotal uang yang anda miliki saat ini RP.',moneyBuyer)
                    payment5 = int(input('\nJumlah Hp yang akan di service '))
                    payment5 = payment5 * servLinivi
                    
                    if payment5 > 2000000:
                        print('\nMaaf uang yang anda miliki saat ini tidak cukup!!!')
                        print('\nSilahkan mengulang program dari awal!!!')
                        exit()
                    
                    print('\nTotal pembayaran Rp.',payment5)
                    min(payment5)
                    
                elif choose4 == 2:
                    os.system('cls')
                    print('\nAnda akan menservice Hp Pecce dengan harga Rp. 150000')
                    print('\nTotal uang yang anda miliki saat ini RP.',moneyBuyer)
                    payment6 = int(input('\nJumlah Hp yang akan di service '))
                    payment6 = payment6 * servPecce
                    
                    if payment6 > 2000000:
                        print('\nMaaf uang yang anda miliki saat ini tidak cukup!!!')
                        print('\nSilahkan mengulang program dari awal!!!')
                        exit()

                    print('\nTotal pembayaran Rp.',payment6)
                    min(payment6)
                
                else:
                    print('\nMaaf pilihan menu yang anda masukkan tidak tersedia!')   
            except (ValueError,TypeError):
                print('\nMaaf anda hanya harus memberikan input angka 1 atau 2, dan tidak boleh keduanya!!!')   
        else:
            print('\nMaaf pilihan menu yang anda masukkan tidak tersedia!')
    except (ValueError,TypeError):
                print('\nMaaf anda hanya harus memberikan input angka 1 atau 2 atau 3!!!')            
else:
    if passw.islower():
        print('Nama toko yang dimasukkan harus huruf besar semua!!!')
    else:
        print('Nama toko yang anda masukkan salah!!!')
        
