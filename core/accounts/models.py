from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name=_("کاربر / المستخدم")
    )

    national_id = models.CharField(
        max_length=20,
        verbose_name=_("کد ملی / الرقم الوطني"),
        null=True,
        blank=True
    )

    father_name = models.CharField(
        max_length=100,
        verbose_name=_("نام پدر / اسم الأب"),
        null  = True , 
        blank = True 
    )

    father_national_id = models.CharField(
        max_length=20,
        verbose_name=_("کد ملی پدر / الرقم الوطني للأب"),
        null=True,
        blank=True
    )

    city = models.CharField(
        max_length=50,
        verbose_name=_("شهر محل سکونت / المدينة"),
        null  = True , 
        blank = True 
    )

    address = models.CharField(
        max_length=255,
        verbose_name=_("آدرس دقیق / العنوان التفصيلي"),
        null  = True , 
        blank = True 
    )

    passport_number = models.CharField(
        max_length=50,
        verbose_name=_("شماره پاسپورت / رقم جواز السفر"),
        null=True,
        blank=True
    )

    telegram_phone = models.CharField(
        max_length=20,
        verbose_name=_("شماره تلگرام / رقم تيليجرام"),
        null=True,
        blank=True
    )

    whatsapp_phone = models.CharField(
        max_length=20,
        verbose_name=_("شماره واتساپ / رقم واتساب"),
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email if hasattr(self.user, 'email') else str(self.user)

    class Meta:
        db_table = "profiles"
        verbose_name = _("پروفایل کاربر")
        verbose_name_plural = _("پروفایل کاربران")



def user_document_path(instance, filename):
    return f'documents/user_{instance.user.id}/{filename}'


class UserDocument(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name=_("کاربر / المستخدم")
    )

    personal_photo = models.ImageField(
        upload_to=user_document_path,
        verbose_name=_("عکس پرسنلی دانش‌آموز / الصورة الشخصية للطالب")
    )

    id_card_front = models.FileField(
        upload_to=user_document_path,
        verbose_name=_("تصویر روی مدرک هویتی / صورة الوجه الأمامي للهوية")
    )

    id_card_back = models.FileField(
        upload_to=user_document_path,
        verbose_name=_("تصویر پشت مدرک هویتی / صورة الوجه الخلفي للهوية")
    )

    last_education_certificate = models.FileField(
        upload_to=user_document_path,
        verbose_name=_("آخرین مدرک تحصیلی / آخر شهادة دراسية")
    )

    school_permission_certificate = models.FileField(
        upload_to=user_document_path,
        verbose_name=_("مجوز معتبر مدرسه / تصريح المدرسة المعتمد")
    )
    
    
    document_request_register = models.FileField(
        upload_to=user_document_path,
        verbose_name=_("درخواست ثبت‌نام / طلب التسجيل")
    )

    document_contract_finance = models.FileField(
        upload_to=user_document_path,
        verbose_name=_("قرارداد مالی / العقد المالي")
    )
    

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("زمان بارگذاری / وقت الرفع")
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("آخرین بروزرسانی / آخر تحديث")
    )

    def __str__(self):
        return f"{_('مدارک')} - {self.user}"

    class Meta:
        db_table = "user_documents"
        verbose_name = _("مدارک کاربر")
        verbose_name_plural = _("مدارک کاربران")
        
        
        
class Mostanadat(models.Model):
    name_document = models.CharField(verbose_name="نام سند" , max_length=20 ) 
    file_document = models.FileField()
    
    
    def __str__(self):
        return f'{self.name_document}'
    
    
    class Meta:
        db_table = "Mostanadat"
        verbose_name_plural = "اسناد برای پرکردن دانش آموزان"
    
    
    