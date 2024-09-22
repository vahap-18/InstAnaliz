import instaloader
import logging
import re
import json
from datetime import datetime
import sys
import time
from tabulate import tabulate

# Türkçe karakter destekli logging yapılandırması
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

class InstagramScraper:
    def __init__(self, username):
        self.username = username
        self.loader = instaloader.Instaloader()

    def get_profile_data(self):
        try:
            logging.info(f"'{self.username}' profili için veriler alınıyor.")
            print("Profil verileri alınıyor...")
            start_time = time.time()
            profile = instaloader.Profile.from_username(self.loader.context, self.username)

            elapsed_time = time.time() - start_time
            self.display_time_bar(1, 6, elapsed_time)

            data = {
                "Temel Profil Bilgileri": {
                    "Kullanıcı Adı": profile.username,
                    "Profil Resmi": profile.profile_pic_url,
                    "Tam Ad": profile.full_name,
                    "Biyografi": profile.biography,
                    "Web Sitesi": profile.external_url,
                    "Takipçi Sayısı": profile.followers,
                    "Takip Edilen Sayısı": profile.followees,
                    "Gönderi Sayısı": profile.mediacount
                }
            }

            is_private = profile.is_private
            account_status = "Hesap gizli" if is_private else "Hesap açık"
            print(f"Hesap durumu: {account_status}")
            logging.info(f"Hesap durumu: {account_status}")

            if is_private:
                logging.info(f"'{self.username}' hesabı gizli. Sadece temel bilgiler gösterilecek.")
                print("Hesap gizli olduğu için sadece sınırlı bilgilere erişilebiliyor.")
                return data  # Gizli hesapta analiz burada sonlanır

            # Gönderi İstatistikleri
            media_edges = list(profile.get_posts())
            post_stats = {
                "Gönderi Türü": {
                    "Toplam Beğeni Sayısı": sum(post.likes for post in media_edges),
                    "Toplam Yorum Sayısı": sum(post.comments for post in media_edges),
                    "Gönderi Sayısı": len(media_edges)
                }
            }
            data["Gönderi İstatistikleri"] = post_stats

            self.display_time_bar(2, 6)

            # Etkileşim Oranı
            engagement_rate = (sum(post.likes + post.comments for post in media_edges) / profile.followers) * 100 if profile.followers else 0
            data["Etkileşim Oranı"] = f"% {engagement_rate:.2f}"

            logging.info("Profil analizi tamamlandı.")
            return data

        except Exception as e:
            logging.error(f"Veri çekilirken hata oluştu: {str(e)}")
            return None

    def display_time_bar(self, current_step, total_steps, elapsed_time=None):
        """ İlerleme çubuğu ve süre bilgisi gösterimi. """
        progress = (current_step / total_steps) * 100
        time_info = f"{elapsed_time:.1f}s" if elapsed_time else "N/A"
        sys.stdout.write(
            f"\r{progress:.1f}% [{('=' * int(progress // 5)).ljust(20)}] {current_step}/{total_steps} Adım, Süre: {time_info}")
        sys.stdout.flush()

def display_terminal_data(data):
    if data:
        print("\n" + "="*50)
        print("         Temel Profil Bilgileri         ")
        print("="*50)
        profile_info = []
        for key, value in data["Temel Profil Bilgileri"].items():
            profile_info.append([key, value])
        print(tabulate(profile_info, headers=["Bilgi Türü", "Değer"], tablefmt="fancy_grid"))

        if "Gönderi İstatistikleri" in data:
            print("\n" + "="*50)
            print("         Gönderi İstatistikleri         ")
            print("="*50)
            post_stats = []
            for key, value in data["Gönderi İstatistikleri"].items():
                post_stats.append([key, value])
            print(tabulate(post_stats, headers=["Bilgi Türü", "Değer"], tablefmt="fancy_grid"))

        print("\n" + "="*50)
        print("               Etkileşim Oranı           ")
        print("="*50)
        print(f"{data.get('Etkileşim Oranı', 'Veri yok.'): <25}")
        print("="*50)

if __name__ == "__main__":
    username = input("Analiz edilecek Instagram kullanıcı adını girin: ")
    scraper = InstagramScraper(username)
    results = scraper.get_profile_data()
    display_terminal_data(results)
