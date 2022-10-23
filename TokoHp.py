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
            print(listMenu[i])
            
        choose1 = int(input("\nSilahkan pilih menu yang tersedia (INPUT HARUS BERUPA ANGKA) : "))
        choose1 != 1 or 2 or 3
