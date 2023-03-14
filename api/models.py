from django.db import models
from django.utils import timezone as tz


class HashtagTrends(models.Model):
    import_time = models.CharField(max_length=255, default=str(tz.now())) 
    hashtag = models.CharField(max_length=255, default="twitter")
    url = models.CharField(max_length=300,default="twitter.com")
    tweet_volume = models.CharField(max_length=255, default="0", blank=True, null=True)


class Tweet(models.Model):
    class Meta:
        unique_together = (('created_at', 'user_screen_name'),)

    created_at=models.CharField(max_length=255,default="0", blank=True, null=True)
    text=models.CharField(max_length=255,default="0", blank=True, null=True)
    id_hash=models.CharField(max_length=255,default="0", blank=True, null=True)
    id_str=models.CharField(max_length=255,default="0", blank=True, null=True)
    truncated=models.CharField(max_length=255,default="0", blank=True, null=True)
    ent_hashtags=models.CharField(max_length=255,default="0", blank=True, null=True)
    ent_symbols=models.CharField(max_length=255,default="0", blank=True, null=True)
    ent_urls=models.CharField(max_length=255,default="0", blank=True, null=True)
    ent_media=models.CharField(max_length=500,default="0", blank=True, null=True)
    metadata_iso_language_code=models.CharField(max_length=255,default="0", blank=True, null=True)
    metadata_result_type=models.CharField(max_length=255,default="0", blank=True, null=True)
    source=models.CharField(max_length=255,default="0", blank=True, null=True)
    in_reply_to_status_id=models.CharField(max_length=255,default="0", blank=True, null=True)
    in_reply_to_status_id_str=models.CharField(max_length=255,default="0", blank=True, null=True)
    in_reply_to_user_id=models.CharField(max_length=255,default="0", blank=True, null=True)
    in_reply_to_user_id_str=models.CharField(max_length=255,default="0", blank=True, null=True)
    in_reply_to_screen_name=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_id=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_id_str=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_name=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_screen_name=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_location=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_description=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_url=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_protected=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_followers_count=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_friends_count=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_listed_count=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_created_at=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_favourites_count=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_utc_offset=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_time_zone=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_geo_enabled=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_verified=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_statuses_count=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_lang=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_contributors_enabled=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_is_translator=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_is_translation_enabled=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_background_color=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_background_image_url=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_background_image_url_https=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_background_tile=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_image_url=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_image_url_https=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_link_color=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_sidebar_border_color=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_sidebar_fill_color=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_text_color=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_profile_use_background_image=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_has_extended_profile=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_default_profile=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_default_profile_image=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_following=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_follow_request_sent=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_notifications=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_translator_type=models.CharField(max_length=255,default="0", blank=True, null=True)
    user_withheld_in_countries=models.CharField(max_length=255,default="0", blank=True, null=True)
    geo=models.CharField(max_length=255,default="0", blank=True, null=True)
    coordinates=models.CharField(max_length=255,default="0", blank=True, null=True)
    place=models.CharField(max_length=255,default="0", blank=True, null=True)
    is_quote_status=models.CharField(max_length=255,default="0", blank=True, null=True)
    retweet_count=models.CharField(max_length=255,default="0", blank=True, null=True)
    favorite_count=models.CharField(max_length=255,default="0", blank=True, null=True)
    favorited=models.CharField(max_length=255,default="0", blank=True, null=True)
    retweeted=models.CharField(max_length=255,default="0", blank=True, null=True)
    lang=models.CharField(max_length=255,default="0", blank=True, null=True)
