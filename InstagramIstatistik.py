import instaloader
from collections import Counter
from tabulate import tabulate
import time

print("**************************************")
print("██████████████████████████████████████████████████")
print("█───█─██─█───█───█────█───█────█───█─██─█───█────█")
print("██─██──█─█─████─██─██─█─███─██─██─██─██─█─███─██─█")
print("██─██─█──█───██─██────█───█────██─██────█───█────█")
print("██─██─██─███─██─██─██─█─███─██─██─██─██─█─███─█─██")
print("█───█─██─█───██─██─██─█─███─██─██─██─██─█───█─█─██")
print("██████████████████████████████████████████████████")
print("Author : A.Vahap Doğan\n")

print("**************************************")
print("Bu program, Instagram açık hesapların istatistiklerini hazırlayan bir programdır.")
print("Program, girilen kullanıcı adına ait istatistikleri toplar ve tablo halinde kullanıcıya sunar.")
print("Programı kullanabilmek için internet bağlantısının olması gerekmektedir.")
print("NOT: Programın kullanılabilir olması için sahip olması gereken kütüphaneler: instaloader, collections, time ve tabulate.")
print("**************************************")


def fetch_statistics(username):
    print("Veriler alınıyor. Lütfen bekleyin...\n")

    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        time.sleep(2)

        follower_count = profile.followers
        posts_count = profile.mediacount
        likes_count = sum([post.likes for post in profile.get_posts()])
        comments_count = sum([post.comments for post in profile.get_posts()])
        total_views = sum([post.video_view_count for post in profile.get_posts() if post.is_video])

        interaction_count = likes_count + comments_count
        engagement_rate = (interaction_count / follower_count) * 100 if follower_count > 0 else 0

        most_liked_video_likes = max([post.likes for post in profile.get_posts() if post.is_video], default=0)
        most_viewed_video_views = max([post.video_view_count for post in profile.get_posts() if post.is_video], default=0)

        average_views_per_post = total_views / posts_count if posts_count > 0 else 0
        average_likes_per_post = likes_count / posts_count if posts_count > 0 else 0
        average_comments_per_post = comments_count / posts_count if posts_count > 0 else 0

        age_distribution = Counter()
        gender_distribution = Counter()
        active_hours = Counter()
        used_tags = Counter()

        for post in profile.get_posts():
            if post.owner_profile is not None and post.owner_profile.external_url is not None:
                age_gender_info = post.owner_profile.external_url
                age_gender_info_split = age_gender_info.split("/")
                if len(age_gender_info_split) == 2:
                    age, gender = age_gender_info_split
                    age_distribution[age] += 1
                    gender_distribution[gender] += 1

            if post.likes is not None and post.comments is not None:
                active_hours[post.date_local.hour] += post.likes + post.comments

            used_tags.update(post.caption_hashtags)

        content_type = set([post.typename for post in profile.get_posts()])

        data = [
            ["Takipçi Sayısı", follower_count],
            ["Gönderi Sayısı", posts_count],
            ["Beğeni Sayısı", likes_count],
            ["Yorum Sayısı", comments_count],
            ["Hesap Katılım Oranı (%)", f"{engagement_rate:.2f}%"],
            ["Toplam İzlenme Sayısı", total_views],
            ["En Çok Beğenilen Video Beğeni Sayısı", most_liked_video_likes],
            ["En Çok İzlenen Video İzlenme Sayısı", most_viewed_video_views],
            ["Gönderi Başına Ortalama Görüntüleme Sayısı", f"{average_views_per_post:.2f}"],
            ["Gönderi Başına Ortalama Beğeni Sayısı", f"{average_likes_per_post:.2f}"],
            ["Gönderi Başına Ortalama Yorum Sayısı", f"{average_comments_per_post:.2f}"],
        ]

        print(tabulate(data, headers=["Bilgi", "Değer"], tablefmt="fancy_grid"))

        print("\nYaş Dağılımı:")
        print(tabulate(age_distribution.items(), headers=["Yaş", "Sayı"], tablefmt="fancy_grid"))

        print("\nCinsiyet Dağılımı:")
        print(tabulate(gender_distribution.items(), headers=["Cinsiyet", "Sayı"], tablefmt="fancy_grid"))

        print("\nEtkileşimin En Aktif Olduğu Saatler:")
        print(tabulate(active_hours.items(), headers=["Saat", "Etkileşim Sayısı"], tablefmt="fancy_grid"))

        print("\nEn Çok Kullanılan Etiketler:")
        print(tabulate(used_tags.items(), headers=["Etiket", "Sayı"], tablefmt="fancy_grid"))

        print("\nİçerik Türü:")
        print(tabulate([[content] for content in content_type], headers=["İçerik Türü"], tablefmt="fancy_grid"))

    except instaloader.exceptions.ProfileNotExistsException:
        print("Kullanıcı bulunamadı.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print("Profil gizli, istatistikler alınamadı.")
    except Exception as e:
        print("Bir hata oluştu:", e)

if __name__ == "__main__":
    print("\nInstagram hesabının istatistiklerini görmek için kullanılabilir.\n")
    print("Lütfen bir Instagram kullanıcı adı girin:")
    username = input("Instagram Kullanıcı Adı: ")
    fetch_statistics(username)
