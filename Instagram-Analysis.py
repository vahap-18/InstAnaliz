import instaloader
import webbrowser
from rich.console import Console
from rich.table import Table
from tqdm import tqdm
import time


# Örnek kullanıcı adı   : useranalysis
# Örnek parola          : User.1453/1*8.
# Kullanılan bu örnek hesaın kapanma ihtimali olduğundan dolayı kendi hesabınızı veya fake bir hesap kullanmanız 
# gerekebilir. Kullanılacak hesapta çift doğrulama sistemi bulunması projenin çalışmasına engel olabilir. 

class InstagramAnalyzer:
    def __init__(self, target_username, username, password):
        self.target_username = target_username
        self.username = username
        self.password = password
        self.loader = instaloader.Instaloader()
        self.console = Console()
        self.start_time = time.time()

    def login(self):
        try:
            self.console.print("[yellow]Instagram'a giriş yapılıyor...[/yellow]")
            self.loader.login(self.username, self.password)
            self.console.print("[green]Giriş başarılı! Analiz başlatılıyor...[/green]")
        except instaloader.exceptions.LoginException as e:
            self.console.print(f"[red]Giriş sırasında hata oluştu: {e}[/red]")
            self.console.print("[yellow]Lütfen kullanıcı adı ve şifreyi kontrol edin veya tarayıcıdan giriş yapmayı deneyin.[/yellow]")
            return self.handle_login_required()

    def handle_login_required(self):
        self.console.print("[yellow]Hesap gizli, tarayıcıdan giriş yapılması gerekiyor.[/yellow]")
        self.console.print("[yellow]Giriş için tarayıcıya yönlendiriliyorsunuz...[/yellow]")
        webbrowser.open('https://www.instagram.com/accounts/login/')
        self.console.print("[yellow]Lütfen tarayıcıda giriş işlemini tamamlayın ve ardından Enter tuşuna basın.[/yellow]")
        input()  # Kullanıcıdan Enter'a basmasını bekliyoruz
        self.console.print("[green]Giriş işlemi tamamlandı. Analiz başlatılıyor...[/green]")
        self.login()  # Yeniden giriş yapmayı dener

    def fetch_profile_data(self):
        try:
            self.console.print("[yellow]Profil bilgileri alınıyor... Lütfen bekleyin...[/yellow]")

            for _ in tqdm(range(100), desc="Profil Bilgileri Alınıyor"):
                time.sleep(0.1)

            profile = instaloader.Profile.from_username(self.loader.context, self.target_username)
            self.console.print(f"[blue]Profil bilgileri alındı: {profile.username}[/blue]")
            self.display_basic_info(profile)

            # Gönderi istatistikleri
            self.console.print("[yellow]Gönderi istatistikleri alınıyor... Lütfen bekleyin...[/yellow]")
            for _ in tqdm(range(100), desc="Gönderi İstatistikleri Alınıyor"):
                time.sleep(0.1)
            self.display_post_stats(profile)

            # Video istatistikleri
            self.console.print("[yellow]Video istatistikleri alınıyor... Lütfen bekleyin...[/yellow]")
            for _ in tqdm(range(100), desc="Video İstatistikleri Alınıyor"):
                time.sleep(0.1)
            self.display_video_stats(profile)

            # Hedef kitle verileri
            self.console.print("[yellow]Hedef kitle verileri alınıyor... Lütfen bekleyin...[/yellow]")
            for _ in tqdm(range(100), desc="Hedef Kitle Verileri Alınıyor"):
                time.sleep(0.1)
            self.display_audience_data(profile)

            # Etkileşim oranları
            self.console.print("[yellow]Etkileşim oranları alınıyor... Lütfen bekleyin...[/yellow]")
            for _ in tqdm(range(100), desc="Etkileşim Oranları Alınıyor"):
                time.sleep(0.1)
            self.display_engagement_rates(profile)

            # Hikaye istatistikleri
            self.console.print("[yellow]Hikaye istatistikleri alınıyor... Lütfen bekleyin...[/yellow]")
            for _ in tqdm(range(100), desc="Hikaye İstatistikleri Alınıyor"):
                time.sleep(0.1)
            self.display_story_stats(profile)

            # Zamanlama ve performans analizi
            self.console.print("[yellow]Zamanlama ve performans analizi yapılıyor... Lütfen bekleyin...[/yellow]")
            for _ in tqdm(range(100), desc="Zamanlama ve Performans Analizi Yapılıyor"):
                time.sleep(0.1)
            self.display_timing_performance_analysis(profile)

            # Rekabet analizi
            self.console.print("[yellow]Rekabet analizi yapılıyor... Lütfen bekleyin...[/yellow]")
            for _ in tqdm(range(100), desc="Rekabet Analizi Yapılıyor"):
                time.sleep(0.1)
            self.display_competition_analysis(profile)

        except instaloader.exceptions.ProfileNotExistsException:
            self.console.print("[red]Profil mevcut değil veya gizli. Lütfen kontrol edin.[/red]")

        except instaloader.exceptions.LoginRequiredException:
            self.console.print("[red]Giriş yapılması gerekiyor. Giriş bilgilerinizi kontrol edin.[/red]")
            return self.handle_login_required()

        except instaloader.exceptions.QueryReturnedBadRequestException as e:
            self.console.print(f"[red]Bir hata oluştu: Bu profil için erişim sağlanamadı. Hata mesajı: {e}[/red]")

        except instaloader.exceptions.AbortDownloadException:
            self.console.print("[red]Oturum kapatıldı. Lütfen giriş bilgilerinizi kontrol edin ve tekrar deneyin.[/red]")

        except Exception as e:
            self.console.print(f"[red]Beklenmeyen bir hata oluştu: {e}[/red]")

    def display_basic_info(self, profile):
        table = Table(title="Temel Profil Bilgileri")
        table.add_column("Açıklama")
        table.add_column("Değer")

        table.add_row("Kullanıcı Adı", profile.username)
        table.add_row("---------", "---------")

        table.add_row("Profil Resmi", str(profile.profile_pic_url))
        table.add_row("---------", "---------")

        table.add_row("Biyografi", profile.biography)
        table.add_row("---------", "---------")

        table.add_row("Web Sitesi", profile.external_url or "Yok")
        table.add_row("---------", "---------")

        table.add_row("Takipçi Sayısı", str(profile.followers))
        table.add_row("---------", "---------")

        table.add_row("Takip Edilen Sayısı", str(profile.followees))
        table.add_row("---------", "---------")

        table.add_row("Gönderi Sayısı", str(profile.mediacount))

        self.console.print(table)
        time.sleep(5)  # 5 saniye bekle

    def display_post_stats(self, profile):
        table = Table(title="Gönderi İstatistikleri")
        table.add_column("Gönderi Türü")
        table.add_column("Beğeni Sayısı")
        table.add_column("Yorum Sayısı")
        table.add_column("Gönderi Zamanı")
        table.add_column("Hashtag Kullanımı")

        for post in profile.get_posts():
            hashtags = [hashtag for hashtag in post.caption_hashtags]
            post_type = "Video" if post.is_video else "Fotoğraf veya Carousel"

            table.add_row(
                post_type,
                str(post.likes),
                str(post.comments),
                post.date_utc.strftime('%Y-%m-%d %H:%M:%S'),
                ", ".join(hashtags) if hashtags else "Yok"
            )
            table.add_row("---------", "---------", "---------", "---------", "---------")
            if post == list(profile.get_posts())[4]:  # İlk 5 gönderi için
                break

        self.console.print(table)
        time.sleep(5)  # 5 saniye bekle

    def display_video_stats(self, profile):
        table = Table(title="Video İstatistikleri")
        table.add_column("Açıklama")
        table.add_column("Değer")

        total_views = 0
        view_count_first_3s = 0  # Bu bilgiye erişim sınırlı
        for post in profile.get_posts():
            if post.is_video:
                total_views += post.video_view_count
                view_count_first_3s += 0  # Gerçek bilgi yok, dolayısıyla sıfır

        table.add_row("Toplam Video Görüntüleme Sayısı", str(total_views))
        table.add_row("---------", "---------")

        table.add_row("İlk 3 Saniye İzlenme Oranı", str(view_count_first_3s))
        table.add_row("---------", "---------")

        table.add_row("Tam İzleme Oranı", "Veri alınamadı")

        self.console.print(table)
        time.sleep(5)  # 5 saniye bekle

    def display_audience_data(self, profile):
        table = Table(title="Hedef Kitle Verileri")
        table.add_column("Açıklama")
        table.add_column("Değer")

        table.add_row("Kullanıcıların Yaşı", "Veri alınamadı")
        table.add_row("---------", "---------")

        table.add_row("Cinsiyet Dağılımı", "Veri alınamadı")
        table.add_row("---------", "---------")

        table.add_row("Konum Bilgisi", "Veri alınamadı")
        table.add_row("---------", "---------")

        table.add_row("Aktif Saatler", "Veri alınamadı")

        self.console.print(table)
        time.sleep(5)  # 5 saniye bekle

    def display_engagement_rates(self, profile):
        table = Table(title="Etkileşim Oranları")
        table.add_column("Açıklama")
        table.add_column("Değer")

        total_engagements = sum(post.likes + post.comments for post in profile.get_posts())
        engagement_rate = (total_engagements / profile.followers * 100) if profile.followers else 0
        activity_rate = total_engagements  # Daha fazla bilgi yok

        table.add_row("Katılım Oranı", f"{engagement_rate:.2f}%")
        table.add_row("---------", "---------")

        table.add_row("Etkinlik Oranı", str(activity_rate))

        self.console.print(table)
        time.sleep(5)  # 5 saniye bekle

    def display_story_stats(self, profile):
        table = Table(title="Hikaye İstatistikleri")
        table.add_column("Açıklama")
        table.add_column("Değer")

        table.add_row("Görüntüleme Sayısı", "Veri alınamadı")
        table.add_row("---------", "---------")

        table.add_row("Yanıt Sayısı", "Veri alınamadı")
        table.add_row("---------", "---------")

        table.add_row("Çıkış Oranı", "Veri alınamadı")

        self.console.print(table)
        time.sleep(5)  # 5 saniye bekle

    def display_timing_performance_analysis(self, profile):
        table = Table(title="Zamanlama ve Performans Analizi")
        table.add_column("Açıklama")
        table.add_column("Değer")

        table.add_row("Gönderi Zamanlaması", "Veri alınamadı")
        table.add_row("---------", "---------")

        table.add_row("Başarılı Gönderiler", "Veri alınamadı")
        table.add_row("---------", "---------")

        table.add_row("Zaman İçindeki Değişim", "Veri alınamadı")

        self.console.print(table)
        time.sleep(5)  # 5 saniye bekle

    def display_competition_analysis(self, profile):
        table = Table(title="Rekabet Analizi")
        table.add_column("Açıklama")
        table.add_column("Değer")

        table.add_row("Rakip Hesapların Performansı", "Veri alınamadı")
        table.add_row("---------", "---------")

        table.add_row("Farklı Gönderi Türlerinin Başarısı", "Veri alınamadı")

        self.console.print(table)
        time.sleep(5)  # 5 saniye bekle

    def analyze(self):
        self.login()
        self.fetch_profile_data()
        self.console.print(f"[yellow]Analiz süresi: {time.time() - self.start_time:.2f} saniye.[/yellow]")

if __name__ == "__main__":
    target_username = input("Analiz edilecek Instagram kullanıcı adını girin: ")
    username = input("Instagram kullanıcı adınızı girin: ")
    password = input("Instagram şifrenizi girin: ")

    analyzer = InstagramAnalyzer(target_username, username, password)
    analyzer.analyze()
