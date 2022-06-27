
### Bu uygulama kendi işimi kolaylaştırmak için üstünde uğraştığım bir nevi tradebot. Ancak bu kendi kullandığım satmak istediğim
#uygulama bundan çok daha farklı olarak internet üzerinden satın alınabilecek uygulamadır.

import os
import math
os.system("cls")

def secim_5():
    oz_kaynaklar = (input("Öz kaynakları giriniz :"))
    aktif_toplam = str(input(" Aktif toplam giriniz :"))
    sonuc_5      = oz_kaynaklar/aktif_toplam
    print("""İşlem sonucu {} bu oran işletmenin toplam varlıklar içerisinde ne kadarlık kısmının
     öz kaynaklardan oluştuğunu göstermektedir bankalar kredi verirken bu oranı göz önüne alır""".format(sonuc_5))



def secim_6():
    kisa_vadeli_yabanci_kaynaklar = float(input("Kısa vadeli yabancı kaynakları giriniz :"))
    toplam_kaynaklar              = float(input("Toplam kaynakları giriniz              :"))
    sonuc_6                       = kisa_vadeli_yabanci_kaynaklar/toplam_kaynaklar
    print("""İşlem sonucu {} bu oran işletmenin varlıklarının yüzde kaçının
     yabancı kaynaklarla finanse edildiğini gösterir """.format(sonuc_6))


def secim_7():
    uzun_vadeli_yabanci_kaynaklar = float(input("Uzun Vadeli yabancı kaynakları giriniz :"))
    toplam_kaynaklar = float(input("Toplam kaynakları giriniz              :"))
    sonuc_7 = uzun_vadeli_yabanci_kaynaklar / toplam_kaynaklar
    print("""İşlem sonucu {} bu oran işletmenin toplam kaynaklarının yüzde kaçının 
    uzun vadeli yabancı kaynaklarla finanse edildiğini gösterir""".format(sonuc_7))


def secim_8():
    kar_yedekleri = float(input("Kâr yedeklerini giriniz                                 :"))
    birikmis_zararlar = float(input("Birikmiş zararları giriniz                              :"))
    odenmis_sermaye = float(input("Ödenmiş sermayeyi giriniz                               :"))
    sonuc_8 = (kar_yedekleri - birikmis_zararlar) / odenmis_sermaye
    print("""İşlem sonucu {}
    İşletmeler elde ettikleri kârı ya hissedarlar dağıtırlar ya da işletmenin bümyesinde tutup yeni yatırımlar için kullanırlar
    dağıtılmayan kârın işletmede tutularak ek fon yaratılmasına otofinansman denmektedir.Oranın sonucu ne kadar yüksek olursa o kadar iyidir
    """.format(sonuc_8))


def secim_9():
    duran_varliklar = float(input("Duran varlıkları giriniz :"))
    devamli_sermaye = float(input("Devamlı Sermayeyi(özkaynaklar + uzun vadeli yabancı kaynaklar) giriniz :"))
    sonuc_9 = duran_varliklar / devamli_sermaye
    print("""İşlemin sonucu {} bu oran il işletmenin duran varlıklarını fonlamada hangi kaynağı ne ölçüde kullandığı tespit edilir"
          özellikle duran varlıkların tümünün öz sermaye ile karşılanmadığı işletmelerde bu oranın hesaplanması önemlidir.
          Öz sermaye ile karşılanmayan kısım uzun vadeli yabancı kaynaklarla karşılanmaktadır.""".format(sonuc_9))


def secim_10():
    maddi_duran_varliklar = float(input("Maddi duran varlıkları(net) giriniz :"))
    oz_kaynaklar = float(input("Öz kaynakları giriniz               :"))
    sonuc_10 = maddi_duran_varliklar / oz_kaynaklar
    print("""İşlem sonucu {} bu oran ile işletmenin maddi duran varlıklarının yüzde kaçının öz kaynaklar ile karşılandığı bulunabilir.
    Bu oranın 1'e eşit veya 1'den küçük olması işletmenin maddi varlıklarının tamamının öz kaynaklar ile finanse edildiğini;1'den büyük olması
    ise maddi duran varlıklarını karşılamada öz kaynaklar dışında yabancı bir kaynak kullanıldığını göstermektedir.""".format(
        sonuc_10))


def secim_11():
    satislarin_maliyeti = float(input("Satışların Maliyetini Giriniz  :"))
    ticari_stoklar = float(input("Ticarı Stokları giriniz        :"))
    sonuc_11 = satislarin_maliyeti / ticari_stoklar
    print("""                   İşlem sonucu {} bu oran satın alma ve üretim verimliliğinin iyi bir göstergesi olarak kabul edilir.
                    İşletmenin stokları kaç günde bitirdiği faaliyetinin niteliğine göre,mevsimsel duruma göre değişebilmektedir""".format(
        sonuc_11))


def secim_20():
    net_kar = float(input("Net kârı giriniz             :"))
    oz_kaynak_toplami = float(input(" Öz kaynak toplamını giriniz :"))
    sonuc_20 = net_kar / oz_kaynak_toplami
    print(
        """İşlem sonucu {} bu oran işletmenin temel sermayesi olan öz kaynağın ne kadarının kâra dönüştürülebildiğini gösterir """.format(
            sonuc_20))


def secim_21():
    donem_kari = float(input("Dönem kârını giriniz             :"))
    uzun_vadeli_borc_gideri = float(input("Uzun vadeli borç giderini giriniz:"))
    toplam_kaynaklar = float(input("Toplam kaynakları giriniz        :"))
    sonuc_21 = (donem_kari + uzun_vadeli_borc_gideri) / toplam_kaynaklar
    print("""İşlem sonucu {} bu oran işletmenin kaynaklarının verimli kullanılıp kullanılmadığını gösterir""".format(
        sonuc_21))


def secim_22():
    vergiden_onceki = float(input("Vergiden önceki kârı giriniz     :"))
    faiz_giderleri = float(input("Faiz giderlerini giriniz         :"))
    sonuc_22 = (vergiden_onceki + faiz_giderleri) / faiz_giderleri
    print(
        """İşlem sonucu {} bu oranla işetmenin yabancı kaynak kullandığında ödemek durumunda kaldığı faiz giderlerini karşılama gücü ölçülür""".format(
            sonuc_22))


def secim_23():
    net_kar = float(input("Net kârı giriniz              :"))
    hisse = float(input("Hisse senedi sayısını giriniz :"))

    sonuc_23 = net_kar / hisse
    print("""İşlem sonucu {} bu oran yatırımcıların işletme için gördüğü değerdir !""".format(sonuc_23))


def secim_24():
    oz_sermaye = float(input("Özsermaye değerini giriniz(toplam varlıklar)               :"))
    toplam_piyasa_degeri = float(input("Toplam piyasa değerini giriniz                             :"))
    sonuc_24 = toplam_piyasa_degeri / oz_sermaye
    print("""İşlem sonucu {} bu oran hissenin pahalı mı yoksa ucuz mu sorusuna cevap arar.Bir hisse senedinin piyasa değerinin defter değerinden düşük olması,hissenin piyasa
     değerinin gerçek değerinden düşük olduğunu göstermektedir""".format(sonuc_24))


def secim_25():
    hisse = float(input("Hisse başına nakit temettü tutarını giriniz : "))
    hisse_piyasa = float(input("Hisse senedi piyasa değerini giriniz        : "))
    sonuc_25 = (hisse / hisse_piyasa) * 100
    print(
        """İşlem sonucu {} bu oran yatırımcının bir birim hisse senedinin ne kadarlık kâr payı sağladığını gösterir.""".format(
            sonuc_25))


def secim_33():
    nominal = float(input("Nominal getiriyi(banka faiz oranı) giriniz(yazarken 'nokta' kullanınız (örn:0.24)):"))
    enf = float(input("Beklenen enflasyon oranını giriniz(yazarken 'nokta' kullanınız (örn:0.26))        :"))
    sonuc_33 = (1 + nominal) / (1 + enf) - 1
    print("""İşlem sonucu {}.Reel getiri enflasyondan arındırılmış,gerçek getiri demektir.Yatırımda esas alınması gereken 'reel getiri'dir.

    Not ==> örneğin işlem sonucu 0.042 çıkarsa bu %4,2 olarak alınmalıdır""".format(sonuc_33))



print("""                           Finans Uygulamasına Hoşgeldiniz                              """)
while True:
 os.system("cls")
 choise = input("""
        İşlemler >>>
        >>>LİKİDİTE ORANLARI
        1-)Cari oran
        2-)Asit-Test oranı
        3-)Nakit oran  
        4-)Finansal Kaldıraç oranı 
        5-)Öz  Kaynakların Aktif Toplamına oranı
        6-)Kısa Vadeli Yabancı Kaynakların Toplam Kaynaklara oranı
        7-)Uzun Vadeli Yabancı Kaynakların Toplam Kaynaklara oranı
        8-)Oto Finansman oranı
        9-)Duran Varlıkların Devamlı Sermayeye oranı
        10-)Maddi Duran Varlıkların Öz Kaynaklara oranı(Yatırım Oranı)
        >>>FAALİYET ORANLARI
        11-)Stok Devir Hızı oranı
        
        >>>KARLILIK ORANLARI
        12-)Mali Rantabilite oranı
        13-)Ekonomik Rantabilite oranı
        14-)Fazileri Karşılama oranı
        15-)Fiyat-Kazanç oranı
        16-)Piyasa Değeri-Defter Değeri oranı
        17-)Temettü Verim oranı
        18-)Reel Getiri

Seçiminiz : """)

 if choise == "1":
    toplam_donen_varliklar               = input("Toplam dönen varlıkları giriniz:")
    toplam_kisa_vadeli_yabanci_kaynaklar = input("Toplam kısa vadeli yabancı kaynaklari giriniz :")
    sonuc_1 = toplam_donen_varliklar/toplam_donen_varliklar
    print("İşlem sonucu {} bu oranın 2 olması yeterlidir ancak 3 olan işletmenin durumu çok iyidir".format(sonuc_1))
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "2":
    toplam_donen_varliklar               = float(input("Toplam dönen varlıkları giriniz :"))
    stoklar                              = float(input("Stokları giriniz :"))
    diger_donen_varliklar                = float(input(" Diğer dönen varlıkları giriniz :"))
    toplam_kisa_vadeli_yabanci_kaynaklar = float(input("Toplam kısa vadeli yabancı kaynakları giriniz :"))
    sonuc_2 = (toplam_donen_varliklar - stoklar - diger_donen_varliklar)/toplam_kisa_vadeli_yabanci_kaynaklar
    print("işlem sonucu {} bu oranın 1 çıkması ideal kabul edilir".format(sonuc_2))
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "3":

     hazir_degerler                = float(input("Hazır değerleri(kasa + bankalar +ve nakde eşdeğer varlıklar) giriniz : "))
     kisa_vadeli_yabanci_kaynaklar = float(input("Kısa vadeli yabancı kaynakları giriniz :"))
     sonuc_3 = hazir_degerler/kisa_vadeli_yabanci_kaynaklar
     print("İşlem sonucu {} bu oranın 0,20 olması ideal kabul edilir ".format(sonuc_3))
     input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "4":
    yabanci_kaynaklar_toplami = float(input("Yabancı kaynaklar toplamını giriniz :"))
    aktif_toplam              = float(input("Aktif toplamı giriniz :"))
    sonuc_4 = yabanci_kaynaklar_toplami/aktif_toplam
    print("""İşlem sonucu {} bu oranın yüksek olması işletmenin çok borçlandığını gösterir 
    ancak işletmenin kârlılığı yüksekse bu oranın yüksek olması kabul edilebilir bi durumdur.
    Sermaye yoğun işletmelerde finansal kaldıraç oranı,emek yoğun ve teknolohi yoğun işletmelere göre daha yüksektir""".format(sonuc_4))
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "5":
    secim_5()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "6":
    secim_6()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "7":
    secim_7()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "8":
    secim_8()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "9":
    secim_9()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "10":
    secim_10()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "11":
    secim_11()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "12":
    secim_20()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "13":
    secim_21()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "14":
    secim_22()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "15":
    secim_23()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "16":
    secim_24()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "17":
    secim_25()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")
 elif choise == "18":
    secim_33()
    input("Menüye dönmek için 'ENTER' tuşuna basınız ")

 else:
     print("Yanlış seçim yaptınız lütfen listede belirtilen sayılardan birini girin ")
     input("Menüye dönmek için 'ENTER' tuşuna basın")