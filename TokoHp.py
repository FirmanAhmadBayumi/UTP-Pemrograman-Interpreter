def garis(jum):
    print('=' * jum)
    
def min(payment):
    total = print('\nSisa uang anda saat ini Rp.', moneyBuyer - payment)
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

garis(65)
print('\t\tSELAMAT DATANG DI TOKO HP ATSALSUKI')
garis(65)

passw = input('\nSilahkan masukkan nama toko ini untuk melanjutkan transaksi: ')

if passw == 'ATSALSUKI':
    print('Nama toko yang anda masukkan benar!!!\n')

    try :
        garis(55)
        print('\tBerikut daftar menu yang dapat anda pilih')
        garis(55)
        
        for i in range (0, len(listMenu)):
            print(listMenu[i])
            
        choose1 = int(input("\nSilahkan pilih menu yang tersedia (INPUT HARUS BERUPA ANGKA) : "))
        choose1 != 1 or 2 or 3
        
        if choose1 == 1:
            try :
                print('\n')
                garis(65)
                print('\tBerikut daftar Hp Baru yang dapat anda beli!!!')
                garis(65)
                
                for i in range(0,len(listHpBaru)):
                    print(listHpBaru[i])
                    
                choose2 = int(input("\nSilahkan pilih menu yang tersedia (INPUT HARUS BERUPA ANGKA) : "))
                choose2 != 1 or 2
                
                if choose2 == 1:
                    print('\nAnda akan membeli Hp Sumsang dengan harga RP. 500000')
                    print('\nTotal uang yang anda miliki saat ini RP.',moneyBuyer)
                    payment1 = int(input('\nJumlah Hp yang akan dibeli: '))
                    payment1 = payment1 * sumsang
                    print('\nTotal pembayaran sebesar Rp.',payment1)
                    min(payment1)
                       
                elif choose2 == 2:
                    print('\nAnda akan membeli Hp Appa dengan harga Rp. 350000')    
                    print('\nTotal uang yang anda miliki saat ini RP.',moneyBuyer)
                    payment2 = int(input('Jumlah Hp yang akan dibeli: '))
                    payment2 = payment2 * appa
                    print('Total pembayaran sebesar Rp.',payment2)
                    min(payment2)
                
                else:
                    print('Maaf pilihan menu yang anda masukkan tidak tersedia!')               
            except (ValueError, TypeError):
                print('Maaf anda hanya harus memberikan input angka 1 atau 2, dan tidak boleh keduanya!!!')  
      
                elif choose1 == 2:
            try:
                print('\n')
                garis(65)
                print('\tBerikut daftar Hp Seken yang dapat anda beli!!!')
                garis(65)

                for i in range(0,len(listHpSeken)):
                    print(listHpSeken[i])
                    

                    
                    
