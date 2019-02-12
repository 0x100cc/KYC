from django import forms


class UserForm(forms.Form):
    useremail = forms.EmailField(label="邮箱",widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'input'}))

class RegisterForm(forms.Form):
    Name = forms.CharField(label="FULL NAME",max_length=128, widget=forms.TextInput(attrs={'class': 'name_input'}))
    Nationality = forms.CharField(label="NATIONALITY",max_length=128,widget=forms.TextInput(attrs={'class': 'nationality_input'}))
    Email = forms.EmailField(label="EMAIL",widget=forms.TextInput(attrs={'class': 'email_input'}))
    Wallet = forms.CharField(label="VSYS COIN WALLET ADDRESS",max_length=256,widget=forms.TextInput(attrs={'class': 'wallet_input'}))
    # KYC_CERTIFICATION = models.ImageField()
    password1 = forms.CharField(label="PASSWORD", max_length=256, widget=forms.PasswordInput(attrs={'class': 'password1_input'}))
    password2 = forms.CharField(label="CONFIRM PASSWORD", max_length=256, widget=forms.PasswordInput(attrs={'class': 'password2_input'}))
