"""stockprediciton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('forgot_pass/',views.forgotpass,name="forgot_pass"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('widgets/',views.widgets),
    path('header/',views.header),
    path('dashboard/',views.dashboard,name="board"),
    path('chat/',views.chat,name="chat"),
    path('mail/',views.mail,name="mail"),
    path('reportsstats/',views.reports_stats,name="reportsstats"),
    path('capital/',views.reports_capital,name="capital"),
    path('topcharts/',views.top_charts,name="topcharts"),
    path('transactions/',views.transactions,name="transactions"),
    path('currency/',views.currency_exchange,name="currency"),
    path('ticker/',views.ticker,name="ticker"),
    path('tickers/',views.tickers,name="tickers"),
    path('edit/',views.edit,name= 'edit'),
    path('logout/',views.logout,name='logout'),
    path('Myprofile/',views.profile,name= 'profile'),
    path('Resetpassword/',views.Resetpassword,name= 'changepassword'),
    path('viewexperts/',views.viewexpert,name= 'expert'),
     path('expertdetails/<int:id>',views.expertdetail,name= 'expert1'),
    path('questions/',views.questions,name= 'questions'),
    path('StockGuide/',views.Stockguide,name= 'stkguide'),
    path('CryptoGuide/',views.Cryptoguide,name= 'cryptoguide'),
#visualisations................................................................................
    path('yeartoyearvisual1/',views.stock1,name= 'yeartoyear'),
    path('twomonths/',views.stock2,name= 'twomonths'),
    path('onemonth/',views.stock3,name= 'onemonth'),
    path('allyearopen/',views.stock4,name= 'allopen'),
    path('stock1',views.user_login,name='userlogin'),
    path('stock2',views.user_login2,name='userlogin2'),
    path('stock3',views.user_login3,name='userlogin3'),
    path('stock4',views.user_login4,name='userlogin4'),
    path('timeseries/',views.stock5,name= 'timeseries'),
    path('stock5',views.user_login5,name='userlogin5'),
    path('ticker',views.user_login6,name='userlogin6')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)