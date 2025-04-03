from django.db import models
from django.contrib.auth.models import User



class Scholar(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="scholars/", blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)  # Store social media links
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Scholars"  # Plural form


    def __str__(self):
        return self.name

class Category(models.Model):
    CATEGORY_CHOICES = (
        ("Tafsiri", "Tafsiri"),
        ("Fiqhu", "Fiqhu"),
        ("Aqida", "Aqida"),
        ("Tarihi", "Tarihi"),
        ("Hadisi", "Hadisi"),
        ("Sira", "Sira"),
        ("Kyawawan Halaye", "Kyawawan Halaye"),
        ("Karatun Alƙur'ani", "Karatun Alƙur'ani"),
        ("Fiqhun Shari'a", "Fiqhun Shari'a"),
        ("Ruhaniya", "Ruhaniya"),
    )

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100, unique=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name



class Waazi(models.Model):
    title = models.CharField(max_length=255)
    scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    audio_file = models.FileField(upload_to="waazi_audio/")
    duration = models.DurationField(blank=True, null=True)  # Store length of audio
    description = models.TextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Waazis"

    def __str__(self):
        return self.title


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waazi = models.ForeignKey(Waazi, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "User Favorites"


class ListeningHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waazi = models.ForeignKey(Waazi, on_delete=models.CASCADE)
    listened_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Listening Histories"