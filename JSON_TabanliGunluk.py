import json
import os
from datetime import datetime

class GunlukUygulamasi:
       def __init__(self, dosya_adi="gunlukler.json"):
              self.dosya_adi = dosya_adi
              self.gunlukler = self.verileri_yukle()

       def verileri_yukle(self):
              if os.path.exists(self.dosya_adi):
                     with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
                            return json.load(dosya)
              return []
       
       def verileri_kaydet(self):
              with open(self.dosya_adi, "w", encoding="utf-8") as dosya:
                     json.dump(self.gunlukler, dosya, indent=4, ensure_ascii=False)

       def yeni_gunluk_ekle(self, baslik, icerik, tarih=None):
              tarih = tarih or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
              yeni_gunluk ={
                     "baslik" : baslik,
                     "icerik" : icerik,
                     "tarih" : tarih
              }
              self.gunlukler.append(yeni_gunluk)
              self.verileri_kaydet()
              print("Günlük başarı ile yüklendi!\n")
       
       def gunlukleri_listele(self):
              if not self.gunlukler:
                     print("Henüz bir günlük yüklenmemiş!\n")
                     return
              print("\nMevcut Günlükler:\n")
              for i, gunluk in enumerate(self.gunlukler, start=1):
                     print(f"{i}. {gunluk['baslik']} - {gunluk['tarih']}")
              print()

       def gunlugu_duzenle(self, indeks, yeni_baslik=None, yeni_icerik=None):
              if 0 <= indeks < len(self.gunlukler):
                     if yeni_baslik:
                            self.gunlukler[indeks]["baslik"] = yeni_baslik
                     if yeni_icerik:
                            self.gunlukler[indeks]["icerik"] = yeni_icerik
                     self.verileri_kaydet()
                     print("Günlük başarı ile güncellendié\n")
              else:
                     print("Geçersiz günlük seçimi!\n")

       def gunlugu_sil(self, indeks):
              if 0 <= indeks < len(self.gunlukler):
                     silinen = self.gunlukler.pop(indeks)
                     self.verileri_kaydet()
                     print(f"'{silinen['baslik']}' başlıklı günlük silindi!\n")
              else:
                     print("Geçersiz günlük seçimi!\n")
              
       def calistir(self):
              while True:
                     print("\n--- Günlük Uygulaması ---")
                     print("1. Yeni Günlük Ekle")
                     print("2. Günlükleri Listele")
                     print("3. Günlüğü Düzenle")
                     print("4. Günlüğü Sil")
                     print("5. Çıkış")

                     secim = input("Yapmak istediğiniz işlemi seçiniz: ")

                     if secim == "1":
                            baslik = input("Günlük Başlığı: ")
                            icerik = input("Günlük İçeriği: ")
                            self.yeni_gunluk_ekle(baslik, icerik)
                     
                     elif secim == "2":
                            self.gunlukleri_listele()

                     elif secim == "3":
                            self.gunlukleri_listele()
                            try:
                                   indeks = int(input("Düzenlemek istediğiniz günlük numarası: ")) - 1
                                   yeni_baslik = input("Yeni başlık (Dilerseniz boş bırakabilirsiniz): ")
                                   yeni_icerik = input("Yeni içerik (Dilerseniz boş bırakabilirsiniz): ")
                                   self.gunlugu_duzenle(indeks, yeni_baslik, yeni_icerik)
                            except ValueError:
                                   print("Geçersiz giriş!\n")
                            
                     elif secim == "4":
                            self.gunlukleri_listele()
                            try:
                                   indeks = int(input("Silmek istediğiniz günlük numarası: ")) - 1
                                   self.gunlugu_sil(indeks)
                            except ValueError:
                                   print("Geçersiz Giriş!\n")

                     elif secim == "5":
                            print("Günlük uygulamasından çıkış yapılıyor...")
                            print("Görüşmek üzere!\n")
                            break

                     else:
                            print("Geçersiz seçim! Lütfen tekrar deneyiniz\n")
                     
uygulama = GunlukUygulamasi()
uygulama.calistir()