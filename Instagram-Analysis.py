import instaloader
from collections import Counter
from tabulate import tabulate
import time
from tqdm import tqdm


def fetch_statistics(username):
    print("Veriler alınıyor. Lütfen bekleyin...\n")

    try:
        # Instaloader ile kullanıcı profilini al
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        if profile.is_private:
            print(f"Hesap gizli olduğu için aşağıdaki veriler alınamıyor:\n")
            print("- Beğeni Sayısı")
            print("- Yorum Sayısı")
            print("- Video Görüntüleme Sayısı")
            print("- Gönderi Etkileşimleri\n")
        else:
            print("Hesap gizli değil, veriler toplanıyor...\n")

        time.sleep(1)
        # İlerleme çubuğunu başlat
        steps = 6  # Temel işlemler için 6 adım belirliyoruz
        with tqdm(total=steps, desc="Veriler toplanıyor") as pbar:
            # Temel verileri çekebilme
            follower_count = profile.followers
            posts_count = profile.mediacount
            data = [
                ["Takipçi Sayısı", follower_count],
                ["Gönderi Sayısı", posts_count]
            ]
            pbar.update(1)  # Birinci adım tamamlandı

            # Gizli hesap değilse ekstra veriler çekilecek
            if not profile.is_private:
                likes_count = sum([post.likes for post in profile.get_posts()])
                pbar.update(1)  # İkinci adım tamamlandı
                comments_count = sum([post.comments for post in profile.get_posts()])
                pbar.update(1)  # Üçüncü adım tamamlandı
                total_views = sum([post.video_view_count for post in profile.get_posts() if post.is_video])
                pbar.update(1)  # Dördüncü adım tamamlandı

                interaction_count = likes_count + comments_count
                engagement_rate = (interaction_count / follower_count) * 100 if follower_count > 0 else 0

                most_liked_video_likes = max([post.likes for post in profile.get_posts() if post.is_video], default=0)
                most_viewed_video_views = max([post.video_view_count for post in profile.get_posts() if post.is_video],
                                              default=0)

                average_views_per_post = total_views / posts_count if posts_count > 0 else 0
                average_likes_per_post = likes_count / posts_count if posts_count > 0 else 0
                average_comments_per_post = comments_count / posts_count if posts_count > 0 else 0

                # Eklenen veriler
                data.extend([
                    ["Beğeni Sayısı", likes_count],
                    ["Yorum Sayısı", comments_count],
                    ["Katılım Oranı (%)", f"{engagement_rate:.2f}%"],
                    ["Toplam İzlenme Sayısı", total_views],
                    ["En Çok Beğenilen Video", most_liked_video_likes],
                    ["En Çok İzlenen Video", most_viewed_video_views],
                    ["Ortalama Görüntüleme", f"{average_views_per_post:.2f}"],
                    ["Ortalama Beğeni", f"{average_likes_per_post:.2f}"],
                    ["Ortalama Yorum", f"{average_comments_per_post:.2f}"]
                ])
                pbar.update(1)  # Beşinci adım tamamlandı

            # Tablo ile sonuçları göster
            print(tabulate(data, headers=["Bilgi", "Değer"], tablefmt="fancy_grid"))
            pbar.update(1)  # Altıncı adım tamamlandı

    except instaloader.exceptions.ProfileNotExistsException:
        print("Kullanıcı bulunamadı.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print("Profil gizli, veriler alınamıyor. Hesabı takip etmiyorsunuz.")
    except Exception as e:
        print("Bir hata oluştu:", e)


if __name__ == "__main__":
    print("Instagram hesabının istatistiklerini görmek için bir kullanıcı adı girin:")
    username = input("Instagram Kullanıcı Adı: ")
    fetch_statistics(username)
