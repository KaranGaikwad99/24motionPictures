import datetime
AWS_ACCESS_KEY_ID = "AKIAIAI7F24VJB42D4ZA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'src.MotionPictures.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'src.MotionPictures.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'motionpicture-static'
S3DIRECT_REGION = 'ap-south-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}