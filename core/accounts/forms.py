from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Profile , UserDocument 

User = get_user_model()


class LoginForm(forms.Form):
    
    username = forms.CharField(
        label = _("نام کاربری"),
        widget=forms.TextInput
    )
    password = forms.CharField(
        label=_("رمز عبور"),
        widget=forms.PasswordInput
    )
    

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("رمز عبور"),
        widget=forms.PasswordInput(attrs={'placeholder': _('رمز عبور خود را وارد کنید')})
    )
    password2 = forms.CharField(
        label=_("تکرار رمز عبور"),
        widget=forms.PasswordInput(attrs={'placeholder': _('رمز عبور را دوباره وارد کنید')})
    )

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': _('example@domain.com')})
        }
        labels = {
            'email': _('ایمیل')
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("این ایمیل قبلاً ثبت شده است."))
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("رمز عبور یکسان نیست."))
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # مهم: username = email
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user






class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'national_id',
            'father_name',
            'father_national_id',
            'city',
            'address',
            'passport_number',
            'telegram_phone',
            'whatsapp_phone',
        ]
        widgets = {
            'national_id': forms.TextInput(attrs={'placeholder': _('مثال: 0012345678')}),
            'father_name': forms.TextInput(attrs={'placeholder': _('مثال: محمد')}),
            'father_national_id': forms.TextInput(attrs={'placeholder': _('مثال: 0087654321')}),
            'city': forms.TextInput(attrs={'placeholder': _('مثال: تهران')}),
            'address': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': _('آدرس کامل محل سکونت خود را وارد کنید')
            }),
            'passport_number': forms.TextInput(attrs={'placeholder': _('مثال: A12345678')}),
            'telegram_phone': forms.TextInput(attrs={'placeholder': _('مثال: +989123456789')}),
            'whatsapp_phone': forms.TextInput(attrs={'placeholder': _('مثال: +989123456789')}),
        }
        labels = {
            'national_id': _('کد ملی / الرقم الوطني'),
            'father_name': _('نام پدر / اسم الأب'),
            'father_national_id': _('کد ملی پدر / الرقم الوطني للأب'),
            'city': _('شهر محل سکونت / المدينة'),
            'address': _('آدرس دقیق / العنوان التفصيلي'),
            'passport_number': _('شماره پاسپورت / رقم جواز السفر'),
            'telegram_phone': _('شماره تلگرام / رقم تيليجرام'),
            'whatsapp_phone': _('شماره واتساپ / رقم واتساب'),
        }





class UserDocumentForm(forms.ModelForm):
    class Meta:
        model = UserDocument
        fields = [
            'personal_photo',
            'id_card_front',
            'id_card_back',
            'last_education_certificate',
            'school_permission_certificate',
            'document_request_register',
            'document_contract_finance',
        ]
        widgets = {
            'personal_photo': forms.FileInput(attrs={'accept': 'image/*'}),
            'id_card_front': forms.FileInput(attrs={'accept': 'image/*,application/pdf'}),
            'id_card_back': forms.FileInput(attrs={'accept': 'image/*,application/pdf'}),
            'last_education_certificate': forms.FileInput(attrs={'accept': 'image/*,application/pdf'}),
            'school_permission_certificate': forms.FileInput(attrs={'accept': 'image/*,application/pdf'}),
            'document_request_register': forms.FileInput(attrs={'accept': 'image/*,application/pdf'}),
            'document_contract_finance': forms.FileInput(attrs={'accept': 'image/*,application/pdf'}),
        }
        labels = {
            'personal_photo': _('عکس پرسنلی دانش‌آموز / الصورة الشخصية للطالب'),
            'id_card_front': _('تصویر روی مدرک هویتی / صورة الوجه الأمامي للهوية'),
            'id_card_back': _('تصویر پشت مدرک هویتی / صورة الوجه الخلفي للهوية'),
            'last_education_certificate': _('آخرین مدرک تحصیلی / آخر شهادة دراسية'),
            'school_permission_certificate': _('مجوز معتبر مدرسه / تصريح المدرسة المعتمد'),
            'document_request_register': _('درخواست ثبت‌نام / طلب التسجيل'),
            'document_contract_finance': _('قرارداد مالی / العقد المالي'),
        }