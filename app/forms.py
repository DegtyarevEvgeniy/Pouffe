from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import Account


from django.forms import ModelForm, TextInput, Textarea, Select, CharField


from .models import *

COUNTRY_CHOICE = [
    ('Афганистан', 'Афганистан'),
    ('Аландские острова', 'Аландские острова'),
    ('Албания', 'Албания'),
    ('Алжир', 'Алжир'),
    ('американское Самоа', 'американское Самоа'),
    ('Андорра', 'Андорра'),
    ('Ангола', 'Ангола'),
    ('Ангилья', 'Ангилья'),
    ('Антарктида', 'Антарктида'),
    ('Антигуа и Барбуда', 'Антигуа и Барбуда'),
    ('Аргентина', 'Аргентина'),
    ('Армения', 'Армения'),
    ('Аруба', 'Аруба'),
    ('Австралия', 'Австралия'),
    ('Австрия', 'Австрия'),
    ('Азербайджан', 'Азербайджан'),
    ('Багамы', 'Багамы'),
    ('Бахрейн', 'Бахрейн'),
    ('Бангладеш', 'Бангладеш'),
    ('Барбадос', 'Барбадос'),
    ('Беларусь', 'Беларусь'),
    ('Бельгия', 'Бельгия'),
    ('Белиз', 'Белиз'),
    ('Бенин', 'Бенин'),
    ('Бермуды', 'Бермуды'),
    ('Бутан', 'Бутан'),
    ('Боливия', 'Боливия'),
    ('Босния и Герцеговина', 'Босния и Герцеговина'),
    ('Ботсвана', 'Ботсвана'),
    ('Остров Буве', 'Остров Буве'),
    ('Бразилия', 'Бразилия'),
    ('Британская территория Индийского океана', 'Британская территория Индийского океана'),
    ('Бруней-Даруссалам', 'Бруней-Даруссалам'),
    ('Болгария', 'Болгария'),
    ('Буркина-Фасо', 'Буркина-Фасо'),
    ('Бурунди', 'Бурунди'),
    ('Камбоджа', 'Камбоджа'),
    ('Камерун', 'Камерун'),
    ('Канада', 'Канада'),
    ('Кабо-Верде', 'Кабо-Верде'),
    ('Каймановы острова', 'Каймановы острова'),
    ('Центрально-Африканская Республика', 'Центрально-Африканская Республика'),
    ('Чад', 'Чад'),
    ('Чили', 'Чили'),
    ('Китай', 'Китай'),
    ('Остров Рождества', 'Остров Рождества'),
    ('Кокосовые (Килинг) острова', 'Кокосовые (Килинг) острова'),
    ('Колумбия', 'Колумбия'),
    ('Коморы', 'Коморы'),
    ('Конго', 'Конго'),
    ('Демократическая Республика Острова Кука', 'Демократическая Республика Острова Кука'),
    ('Коста-Рика', 'Коста-Рика'),
    ("Cote D'ivoire", "Cote D'ivoire"),
    ('Хорватия', 'Хорватия'),
    ('Куба', 'Куба'),
    ('Кипр', 'Кипр'),
    ('Чешская Республика', 'Чешская Республика'),
    ('Дания', 'Дания'),
    ('Джибути', 'Джибути'),
    ('Доминика', 'Доминика'),
    ('Доминиканская Респблика', 'Доминиканская Респблика'),
    ('Эквадор', 'Эквадор'),
    ('Египет', 'Египет'),
    ('Эль Сальвадор', 'Эль Сальвадор'),
    ('Экваториальная Гвинея', 'Экваториальная Гвинея'),
    ('Эритрея', 'Эритрея'),
    ('Эстония', 'Эстония'),
    ('Эфиопия', 'Эфиопия'),
    ('Фолклендские (Мальвинские) острова', 'Фолклендские (Мальвинские) острова'),
    ('Фарерские острова', 'Фарерские острова'),
    ('Фиджи', 'Фиджи'),
    ('Финляндия', 'Финляндия'),
    ('Франция', 'Франция'),
    ('Французская Гвиана', 'Французская Гвиана'),
    ('Французская Полинезия', 'Французская Полинезия'),
    ('Южные Французские Территории', 'Южные Французские Территории'),
    ('Габон', 'Габон'),
    ('Гамбия', 'Гамбия'),
    ('Грузия', 'Грузия'),
    ('Германия', 'Германия'),
    ('Гана', 'Гана'),
    ('Гибралтар', 'Гибралтар'),
    ('Греция', 'Греция'),
    ('Гренландия', 'Гренландия'),
    ('Гренада', 'Гренада'),
    ('Гваделупа', 'Гваделупа'),
    ('Гуам', 'Гуам'),
    ('Гватемала', 'Гватемала'),
    ('Гернси', 'Гернси'),
    ('Гвинея', 'Гвинея'),
    ('Гвинея-бисау', 'Гвинея-бисау'),
    ('Гайана', 'Гайана'),
    ('Гаити', 'Гаити'),
    ('Остров Херд и острова Макдональдс', 'Остров Херд и острова Макдональдс'),
    ('Святой Престол (город-государство Ватикан)', 'Святой Престол (город-государство Ватикан)'),
    ('Гондурас', 'Гондурас'),
    ('Гонконг', 'Гонконг'),
    ('Венгрия', 'Венгрия'),
    ('Исландия', 'Исландия'),
    ('Индия', 'Индия'),
    ('Индонезия', 'Индонезия'),
    ('Иран', 'Иран'),
    ('Исламская Республика', 'Исламская Республика'),
    ('Ирак', 'Ирак'),
    ('Ирландия', 'Ирландия'),
    ('Остров Мэн', 'Остров Мэн'),
    ('Израиль', 'Израиль'),
    ('Италия', 'Италия'),
    ('Ямайка', 'Ямайка'),
    ('Япония', 'Япония'),
    ('Джерси', 'Джерси'),
    ('Иордания', 'Иордания'),
    ('Казахстан', 'Казахстан'),
    ('Кения', 'Кения'),
    ('Кирибати', 'Кирибати'),
    ("Korea", "Korea"),
    ("Democratic People's Republic of Korea", "Democratic People's Republic of Korea"),
    ('Республика Кувейт', 'Республика Кувейт'),
    ('Кыргызстан', 'Кыргызстан'),
    ("Lao People's Democratic Republic", "Lao People's Democratic Republic"),
    ('Латвия', 'Латвия'),
    ('Ливан', 'Ливан'),
    ('Лесото', 'Лесото'),
    ('Либерия', 'Либерия'),
    ('Ливийская арабская джамахирия', 'Ливийская арабская джамахирия'),
    ('Лихтенштейн', 'Лихтенштейн'),
    ('Литва', 'Литва'),
    ('Люксембург', 'Люксембург'),
    ('Макао', 'Макао'),
    ('Македония, бывшая', 'Македония, бывшая'),
    ('Югославская Республика Мадагаскар', 'Югославская Республика Мадагаскар'),
    ('Малави', 'Малави'),
    ('Малайзия', 'Малайзия'),
    ('Мальдивы', 'Мальдивы'),
    ('Мали', 'Мали'),
    ('Мальта', 'Мальта'),
    ('Маршалловы острова', 'Маршалловы острова'),
    ('Мартиника', 'Мартиника'),
    ('Мавритания', 'Мавритания'),
    ('Маврикий', 'Маврикий'),
    ('Майотта', 'Майотта'),
    ('Мексика', 'Мексика'),
    ('Микронезия, Федеративные Штаты Молдовы', 'Микронезия, Федеративные Штаты Молдовы'),
    (' Республика Монако', ' Республика Монако'),
    ('Монголия', 'Монголия'),
    ('Черногория', 'Черногория'),
    ('Монтсеррат', 'Монтсеррат'),
    ('Марокко', 'Марокко'),
    ('Мозамбик', 'Мозамбик'),
    ('Мьянма', 'Мьянма'),
    ('Намибия', 'Намибия'),
    ('Науру', 'Науру'),
    ('Непал', 'Непал'),
    ('Нидерланды', 'Нидерланды'),
    ('Нидерландские Антильские острова', 'Нидерландские Антильские острова'),
    ('Новая Каледония', 'Новая Каледония'),
    ('Новая Зеландия', 'Новая Зеландия'),
    ('Никарагуа', 'Никарагуа'),
    ('Нигер', 'Нигер'),
    ('Нигерия', 'Нигерия'),
    ('Ниуэ', 'Ниуэ'),
    ('Остров Норфолк', 'Остров Норфолк'),
    ('Северные Марианские острова', 'Северные Марианские острова'),
    ('Норвегия', 'Норвегия'),
    ('Оман', 'Оман'),
    ('Пакистан', 'Пакистан'),
    ('Палау', 'Палау'),
    ('Палестинская территория, оккупированная', 'Палестинская территория, оккупированная'),
    ('Панама', 'Панама'),
    ('Папуа - Новая Гвинея', 'Папуа - Новая Гвинея'),
    ('Парагвай', 'Парагвай'),
    ('Перу', 'Перу'),
    ('Филиппины', 'Филиппины'),
    ('Питкэрн', 'Питкэрн'),
    ('Польша', 'Польша'),
    ('Португалия', 'Португалия'),
    ('Пуэрто-Рико', 'Пуэрто-Рико'),
    ('Катар', 'Катар'),
    ('Воссоединение', 'Воссоединение'),
    ('Румыния', 'Румыния'),
    ('Российская Федерация', 'Российская Федерация'),
    ('Руанда', 'Руанда'),
    ('Святая Елена', 'Святая Елена'),
    ('Сент-Китс и Невис', 'Сент-Китс и Невис'),
    ('Сент-Люсия', 'Сент-Люсия'),
    ('Сен-Пьер и Микелон', 'Сен-Пьер и Микелон'),
    ('Святой Винсент и Гренадины', 'Святой Винсент и Гренадины'),
    ('Самоа', 'Самоа'),
    ('Сан-Марино', 'Сан-Марино'),
    ('Сан-Томе и Принсипи', 'Сан-Томе и Принсипи'),
    ('Саудовская Аравия', 'Саудовская Аравия'),
    ('Сенегал', 'Сенегал'),
    ('Сербия', 'Сербия'),
    ('Сейшелы', 'Сейшелы'),
    ('Сьерра-Леоне', 'Сьерра-Леоне'),
    ('Сингапур', 'Сингапур'),
    ('Словакия', 'Словакия'),
    ('Словения', 'Словения'),
    ('Соломоновы острова', 'Соломоновы острова'),
    ('Сомали', 'Сомали'),
    ('Южная Африка', 'Южная Африка'),
    ('Южная Георгия и Южные Сандвичевы острова', 'Южная Георгия и Южные Сандвичевы острова'),
    ('Испания', 'Испания'),
    ('Шри-Ланка', 'Шри-Ланка'),
    ('Судан', 'Судан'),
    ('Суринам', 'Суринам'),
    ('Шпицберген и Ян-Майен', 'Шпицберген и Ян-Майен'),
    ('Свазиленд', 'Свазиленд'),
    ('Швеция', 'Швеция'),
    ('Швейцария', 'Швейцария'),
    ('Сирийская Арабская Республика', 'Сирийская Арабская Республика'),
    ('Тайвань', 'Тайвань'),
    ('Таджикистан', 'Таджикистан'),
    ('Танзания, Объединенная Республика Таиланд', 'Танзания, Объединенная Республика Таиланд'),
    ('Тимор-Лешти', 'Тимор-Лешти'),
    ('Идти', 'Идти'),
    ('Токелау', 'Токелау'),
    ('Тонга', 'Тонга'),
    ('Тринидад и Тобаго', 'Тринидад и Тобаго'),
    ('Тунис', 'Тунис'),
    ('Турция', 'Турция'),
    ('Туркменистан', 'Туркменистан'),
    ('острова Теркс и Кайкос', 'острова Теркс и Кайкос'),
    ('Тувалу', 'Тувалу'),
    ('Уганда', 'Уганда'),
    ('Украина', 'Украина'),
    ('Объединенные Арабские Эмираты', 'Объединенные Арабские Эмираты'),
    ('Соединенное Королевство', 'Соединенное Королевство'),
    ('Соединенные Штаты', 'Соединенные Штаты'),
    ('Малые окраины США', 'Малые окраины США'),
    ('острова', 'острова'),
    ('Уругвай', 'Уругвай'),
    ('Узбекистан', 'Узбекистан'),
    ('Вануату', 'Вануату'),
    ('Венесуэла', 'Венесуэла'),
    ('Вьетнам', 'Вьетнам'),
    ('Виргинские острова, Британские', 'Виргинские острова, Британские'),
    ('Виргинские острова, США', 'Виргинские острова, США'),
    ('Уоллис и Футуна', 'Уоллис и Футуна'),
    ('Западная Сахара', 'Западная Сахара'),
    ('Йемен', 'Йемен'),
    ('Замбия', 'Замбия'),
    ('Зимбабве', 'Зимбабве'),
]
CATEGORY_CHOICE = [
    ('Одежда', 'Одежда'),
    ('Обувь', 'Обувь'),
    ('Сумки', 'Сумки'),
    ('Интерьер', 'Интерьер'),
    ('Аксессуары', 'Аксессуары'),
]

DURATION_CHOICE = [
    ('1 - 2 дня', '1 - 2 дня'),
    ('2 - 5 дней', '2 - 5 дней'),
    ('5 - 7 дней', '5 - 7 дней'), 
    ('1 - 2 недели', '1 - 2 недели'),
    ('2 недели - месяц', '2 недели - месяц'),
    ('1 - 3 месяца', '1 - 3 месяца'),
    ('3 - 6 месяцев', '3 - 6 месяцев'),
    ('6 - 12 месяцев', '6 - 12 месяцев'),
    ('1 - 2 года', '1 - 2 года'),
    ('более 3-х лет', 'более 3-х лет'),
]

SEX_CHOICE = [
    ('женское', 'женский'),
    ('мужское', 'мужской'),
    ('унисекс', 'унисекс'),
]
User = get_user_model()

# Class with all the fields of the form for Signup
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded',
            'required': '',
            'name': 'name',
            'id': 'name',
            'type': 'text',
            'placeholder': '',
            'minlength': '1'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': '',
            'minlength': '8'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded pswdChecker',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': '',
            'minlength': '8'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded pswdChecker',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': '',
            'minlength': '8'
        })

    first_name = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')

# Class with all the fields of the form for Product editing
class ProductEditForm(ModelForm):
    class Meta:
        model = Product_creator
        fields = '__all__'
        widgets = {
            'product_name': TextInput(attrs={
                'class': 'uk-form uk-input',
                'placeholder': "Введите название товара",
                'id': 'product_name',
                'max_length': '100',
                'oninput': 'PassChecker(1)',
            }),
            'country': Select(attrs={
                'class': 'uk-form uk-select',
            }, choices=COUNTRY_CHOICE),
            'brand': TextInput(attrs={
                'class': 'uk-form uk-input',
                'id': 'brand',
                'placeholder': 'Введите бренд товара',
                'max_length': '100',
                'oninput': 'PassChecker(1)',
            }),
            'description': Textarea(attrs={
                'class': 'uk-form uk-textarea',
                'id': 'description',
                'placeholder': 'Введите описание товара',
                'oninput': 'PassChecker(1)',
            }),
            'category': Select(attrs={
                'class': 'uk-form uk-select',
            }, choices=CATEGORY_CHOICE),
            'duration': Select(attrs={
                'class': 'uk-form uk-select',
            }, choices=DURATION_CHOICE),
            'sex': Select(attrs={
                'class': 'uk-form uk-select',
            }, choices=SEX_CHOICE),
            'price': TextInput(attrs={
                'class': 'uk-form uk-input uk-width-4-5',
                'type': 'number',
                'id': 'priceInput',
                'oninput': 'recalc(this)',
                'placeholder': 'Введите стоимость товара'
            }),
            'width_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'height_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'length_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'width_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'height_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'length_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),

        }

# Class with all the fields of the form to create product
class ProductCreateForm(ModelForm):
    class Meta:
        model = Product_creator
        fields = '__all__'
        widgets = {
            'product_name': TextInput(attrs={
                'class': 'uk-form uk-input',
                'placeholder': "Введите название товара",
                'id': 'product_name',
                'max_length': '100',
                'oninput': 'PassChecker(1)',
            }),
            'country': Select(attrs={
                'class': 'uk-form uk-select',
            }, choices=COUNTRY_CHOICE),
            'brand': TextInput(attrs={
                'class': 'uk-form uk-input',
                'id': 'brand',
                'placeholder': 'Введите бренд товара',
                'max_length': '100',
                'oninput': 'PassChecker(1)',
            }),
            'description': Textarea(attrs={
                'class': 'uk-form uk-textarea',
                'id': 'description',
                'placeholder': 'Введите описание товара',
                'oninput': 'PassChecker(1)',
            }),
            'category': Select(attrs={
                'class': 'uk-form uk-select',
            }, choices=CATEGORY_CHOICE),
            'duration': Select(attrs={
                'class': 'uk-form uk-select',
            }, choices=DURATION_CHOICE),
            'sex': Select(attrs={
                'class': 'uk-form uk-select',
            }, choices=SEX_CHOICE),
            'price': TextInput(attrs={
                'class': 'uk-form uk-input uk-width-4-5',
                'type': 'number',
                'id': 'priceInput',
                'oninput': 'recalc(this)',
                'placeholder': 'Введите стоимость товара'
            }),
            'width_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'height_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'length_product': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'width_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'height_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),
            'length_packaging': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
            }),

        }

    # product_name = forms.CharField(required=True)
    # cost = forms.CharField(required=True)
    # availability = forms.ChoiceField()
    # description = forms.CharField()
    # picture = forms.ImageField()


class Resume(forms.Form):
    description = forms.CharField(label='Расскажите о себе', required=True, widget=forms.Textarea(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
    }))
    is_company = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'onchange': "isCompany()",
        'id': "isCompanyTrigger",
    }))
    company_name = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': "Название компании",

    }))
    email = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
    }))
    first_name = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'value': "TROLOLO"
    }))
    cover = forms.ImageField(required=False)
    telegram = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': "@tag",
    }))
    vk = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': "https://vk.com/yourid",
    }))
    whatsapp = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': "+71234567890",
    }))
    instagram = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
        'placeholder': " https://instagram.com/tag",
    }))
    tag = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "uk-input uk-width-1-3",
        'value': "",
    }))
    published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'value': "1",
    }))


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = Account
        fields = ('email', 'city', 'first_name', 'last_name', 'email',
        'ogrn', 'inn', 'kpp', 'street', 'fiz_adress', 'index', 'checking_account', 'bik', 
        'korr_check','name_small','nameFull', 'payment_account', 'reg_form')
