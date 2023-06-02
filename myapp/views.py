from django.shortcuts import render
from django.conf import settings
from matplotlib.pyplot import figimage
from myapp.models import contactus
from myapp.models import stockguide
from myapp.models import cryptoguide
from myapp.models import expert
from myapp.models import expertquestions
from myapp.models import register as rgstr
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
import matplotlib.pyplot as plt
from matplotlib import pylab
import matplotlib
from io import BytesIO
import io
import base64
from PIL import Image, ImageDraw
import PIL, PIL.Image
import pandas as pd
import pylab as plt
import numpy as np
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Create your views here.
def home(request):
    return render(request,'homepage.html',{})
def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('mail')
        phone= request.POST.get('phone')
        Message = request.POST.get('message')
        Selected_Course = request.POST.get('selected')
        cont=contactus()
        cont.First_Name=first_name
        cont.last_name=last_name
        cont.emailid=email
        cont.Phone=phone
        cont.Message=Message
        cont.Selected_Course=Selected_Course
        cont.save()
    return render(request,'contact_us.html',{})
def register(request):
    if request.method == 'POST':
        FullName = request.POST.get('fullname')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Confirm = request.POST.get('confirm')


           
        us = rgstr.objects.filter(Email = Email) 
        k=len(us)
        if k>0:
            
            return render(request,'register.html',{})
        else:
            if (Password==Confirm):
                reg=rgstr()

                reg.FullName=FullName
                reg.Email=Email
                reg.Password=Password
                reg.save()

    return render(request,'register_login.html',{})
def login(request):
    my_dict={'my_text':"this is index page"}
    if request.method=='POST':
        email=request.POST.get('username')
        pw=request.POST.get('pwd')
        
        us= rgstr.objects.filter(Email = email , Password = pw)  
        k=len(us)
        if k>0:
            print("valid credentials ")
            request.session['email'] = email

            return render(request,'index7.html',{}) 
        else:
            print("Invalid credentials")
            return render(request,'register_login.html',{})   
    

    return render(request,'register_login.html',{})
def forgotpass(request):
    if (request.method=='POST'):
        em=request.POST.get('email')
        user=rgstr.objects.filter(Email=em)
        
        if (len(user)>0):
            pw=user[0].Password
            subject="Password"
            message="Welcome . your Password is " + pw
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em,]
            send_mail(subject,message,email_from,recipient_list)
            rest="your password is sent to your repective email account. Please check"
            return render(request,'forgot_pass.html',{'rest':rest})
        else:
            res="This email id is not registered"
            return render(request,'forgot_pass.html',{'res':res})
    else:
        return render(request,'forgot_pass.html')
   
def widgets(request):
    return render(request,'widgets.html',{})
def header(request):
    return render(request,'base.html',{})
def dashboard(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'index7.html',{})
def chat(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'contact_app_chat.html',{})
def mail(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'mailbox.html',{})
def reports_stats(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'reports_crypto_stats.html',{})
def reports_capital(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'reports_market_capitalizations.html',{})
def top_charts(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    from nsetools import Nse
    nse=Nse()
    all_stock_codes = nse.get_stock_codes()
    print(all_stock_codes)

    top_gainers = nse.get_top_gainers()
    print(top_gainers)

    top_losers = nse.get_top_losers()
    print(top_losers)
    return render(request,'reports_top_gainers_losers.html',{'tg':top_gainers,'tl':top_losers})
def transactions(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'reports_transactions.html',{})
def currency_exchange(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'currency_exchange.html',{})
def ticker(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'tickers_live_pricing.html',{})
def tickers(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'tickers1.html',{})
def logout(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    del request.session['email']
    return redirect('/login')
def edit(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    userdetail=rgstr.objects.get(Email=request.session['email'])
    if request.method == 'POST':
        detail = rgstr.objects.get(Email=request.session['email'])
        detail.FullName = request.POST.get('Username')
        detail.Email = request.POST.get('Email')
        detail.city= request.POST.get('City')
        detail.Address = request.POST.get('Address')
        detail.mobile = request.POST.get('mobile')
        detail.save()
        data=rgstr.objects.get(Email=request.session['email'])
        return render(request,'index7.html',{'user':data})
    else:
        return render(request,'edit_profile.html',{'user':userdetail})
def profile(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    userdetail=rgstr.objects.get(Email=request.session['email'])
    return render(request,'myprofile.html',{'user':userdetail})
def Resetpassword(request):
    if request.method=='POST':
        reg=rgstr.objects.get(Email=request.session['email'])
        password=request.POST.get('Password')
        newpwd=request.POST.get('newpass')
        confirmpwd=request.POST.get('confirmpass')
        if(newpwd==confirmpwd):
            p=reg.Password
         
            if(password==p):
                reg.Password=newpwd
                reg.save()
                rest="Password Changed"
                return render(request,'change_password.html',{'rest':rest})
            else:
                res="Invalid Current Password"
                return render(request,'change_password.html',{'res':res})
        else:
            res="Confirm password and new password don't match"
            return render(request,'change_password.html',{'res':res})
    
    else:
        return render(request,'change_password.html')
def viewexpert(request):
    ex=expert.objects.all()
    return render(request,'viewexperts.html',{'data':ex})

def expertdetail(request,id):
    ex=expert.objects.get(id=id)
    return render(request,'expertdetail.html',{'data':ex})
def questions(request):
    que=expertquestions.objects.all()
    return render(request,'questions.html',{'data':que})
def Stockguide(request):
    guide=stockguide.objects.all()
    return render(request,'stockguide.html',{'data':guide})
def Cryptoguide(request):
    guide=cryptoguide.objects.all()
    return render(request,'cryptoguide.html',{'data':guide})
def stock1(request):
    return render(request,'stockyearvisual.html',{})
def stock2(request):
    return render(request,'twomonths.html',{})
def stock3(request):
    return render(request,'onemonth.html',{})
def stock4(request):
    return render(request,'allopen.html',{})
def stock5(request):
    return render(request,'timeseries.html',{})
#Visualisations........................................................................................
def user_login(request):
    
    if request.method=='POST':
        s=request.POST.get('stocks')
        year1=request.POST.get('year1')
        year2=request.POST.get('year2')
        a=int(year1)
        b=int(year2)
        if b < a:
            msg="SELECT APPROPRIATE YEARS!!!"
            return render(request,'stockyearvisual.html',{'msg':msg})
        # import 
        fig=plt.figure(figsize=(10, 8), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        # plot code
        #s=input("enter the name of the stock")
        df = pd.read_csv(s+".csv",)
        df=df.dropna()
        df['Date']=pd.to_datetime(df['Date'],format="%Y.%m.%d")
        df['month']=df['Date'].dt.month
        df['Year']=df['Date'].dt.year
        df=df.set_index('Year')
        #a=input("ENTER STARTING YEAR")
        #b=input("ENTER ENDING YEAR")
        df1=df.loc[a:b,:]
        df1=df1.reset_index()

        df1.dtypes
        convert={'month':str}
        df1=df1.astype(convert)
        convert={'Year':str}
        df1=df1.astype(convert)
        def month(x):
                if x=='1':
                    return "Jan"
                elif x=='2':
                    return "Feb"
                elif x=='3':
                    return "Mar"
                elif x=='4':
                    return "Apr"
                elif x=='5':
                    return "May"
                elif x=='6':
                    return "Jun"
                elif x=='7':
                    return "Jul"
                elif x=='8':
                    return "Aug"
                elif x=='9':
                    return "Sep"
                elif x=='10':
                    return "Oct"
                elif x=='11':
                    return "Nov"
                elif x=='12':
                    return "Dec"
        df1['month']=df1['month'].apply(month)
        sns.lineplot(data=df1, x="Year", y="Open", hue="month", style="month")
        # saving an image 
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        fig.savefig('abc.png')
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "This text is drawn on image")
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
    else:
        return render(request,'stockyearvisual.html',{})

def user_login2(request):
    
    if request.method=='POST':
        s=request.POST.get('stocks')
        year1=request.POST.get('year1')
        year2=request.POST.get('year2')
        month1=request.POST.get('month1')
        month2=request.POST.get('month2')
        a=int(year1)
        b=int(year2)
        c=int(month1)
        d=int(month2)
        if b < a:
            msg="select appropriate years"
            return render(request,'stockyearvisual.html',{'msg':msg})
        elif c<d:
            msg="select appropriate years"
            return render(request,'stockyearvisual.html',{'msg':msg})
        print("input",a,b,c,d)
        # import 
        #s=input("enter the name of the stock")
        fig=plt.figure(figsize=(10, 8), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        #plot code
        df = pd.read_csv(s+".csv",)
        df=df.dropna()
        #sns.lineplot(data=df,x="Period",y="Revenue")

        df['Date']=pd.to_datetime(df['Date'],format="%Y.%m.%d")
        df['month']=df['Date'].dt.month
        df['year']=df['Date'].dt.year
        df=df.set_index('year')
        #a=input("ENTER STARTING YEAR")
        #b=input("ENTER ENDING YEAR")
        #c=int(input("enter the month in digits"))
        #d=int(input("enter the 2nd month in digits"))
        df1=df.loc[a:b,:]
        df1=df1.reset_index()
        #dfnew=df[df['Date'].dt.month==2]
        df1.head()

        df1=df1[(df1['month']==c) | (df1['month']==d) ]

        #sns.lineplot(data=df, x="Period", y="Revenue")
        df1.dtypes
        convert={'month':str}
        df1=df1.astype(convert)
        convert={'year':str}
        df1=df1.astype(convert)
        def month(x):
                if x=='1':
                    return "Jan"
                elif x=='2':
                    return "Feb"
                elif x=='3':
                    return "Mar"
                elif x=='4':
                    return "Apr"
                elif x=='5':
                    return "May"
                elif x=='6':
                    return "Jun"
                elif x=='7':
                    return "Jul"
                elif x=='8':
                    return "Aug"
                elif x=='9':
                    return "Sep"
                elif x=='10':
                    return "Oct"
                elif x=='11':
                    return "Nov"
                elif x=='12':
                    return "Dec"
        df1['month']=df1['month'].apply(month)

        #sns.barplot(data=df1,x="year",y="Open")
        sns.lineplot(data=df1, x="year", y="Open", hue="month", style="month")
        # saving an image 
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        fig.savefig('abc2.png')
        plt.close(fig)
        image = Image.open("abc2.png")
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "This text is drawn on image")
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
    else:
        return render(request,'twomonths.html',{})

def user_login3(request):
    
    if request.method=='POST':
        s=request.POST.get('stocks')
        year1=request.POST.get('year1')
        year2=request.POST.get('year2')
        month=request.POST.get('month')
        a=int(year1)
        b=int(year2)
        c=int(month)
        if b < a:
            msg="select appropriate years"
            return render(request,'stockyearvisual.html',{'msg':msg})
        # import 
        #s=input("enter the name of the stock")
        fig=plt.figure(figsize=(10, 8), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        #plot code
        #s=input("enter the name of the stock")

        df = pd.read_csv(s+".csv",)
        df=df.dropna()
        #sns.lineplot(data=df,x="Period",y="Revenue")

        df['Date']=pd.to_datetime(df['Date'],format="%Y.%m.%d")
        df['month']=df['Date'].dt.month
        df['year']=df['Date'].dt.year
        df=df.set_index('year')
        #a=input("ENTER STARTING YEAR")
        #b=input("ENTER ENDING YEAR")
        #c=int(input("enter the month in digits"))
        df1=df.loc[a:b,:]
        df1=df1.reset_index()
        #dfnew=df[df['Date'].dt.month==2]
        df1.head()
        df1=df1[df1['month']==c]

        #sns.lineplot(data=df, x="Period", y="Revenue")
        df1.dtypes
        convert={'month':str}
        df1=df1.astype(convert)
        convert={'year':str}
        df1=df1.astype(convert)
        def month(x):
                if x=='1':
                    return "Jan"
                elif x=='2':
                    return "Feb"
                elif x=='3':
                    return "Mar"
                elif x=='4':
                    return "Apr"
                elif x=='5':
                    return "May"
                elif x=='6':
                    return "Jun"
                elif x=='7':
                    return "Jul"
                elif x=='8':
                    return "Aug"
                elif x=='9':
                    return "Sep"
                elif x=='10':
                    return "Oct"
                elif x=='11':
                    return "Nov"
                elif x=='12':
                    return "Dec"
        df1['month']=df1['month'].apply(month)

        #sns.barplot(data=df1,x="year",y="Open")
        sns.lineplot(data=df1, x="year", y="Open", hue="month", style="month")
        # saving an image 
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        fig.savefig('abc3.png')
        plt.close(fig)
        image = Image.open("abc3.png")
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "This text is drawn on image")
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
    else:
        return render(request,'onemonth.html',{})
def user_login4(request):

     if request.method=='POST':
        s=request.POST.get('stocks')
       
        # import 
        #s=input("enter the name of the stock")
        fig=plt.figure(figsize=(12, 9), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        #plot code
        #s=input("enter the name of the stock")
        df = pd.read_csv(s+".csv",)
        df=df.dropna()
        df= df.set_index('Date')
        ax=df.iloc[:,3].plot.line(title="Bitcoin \n Open" , rot=90,grid=True)
        ax.set_ylabel("Dollars")
        # saving an image 
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        fig.savefig('abc3.png')
        plt.close(fig)
        image = Image.open("abc3.png")
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "This text is drawn on image")
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
        return render(request,'twomonths.html',{})
def user_login4(request):

     if request.method=='POST':
        s=request.POST.get('stocks')
       
        # import 
        #s=input("enter the name of the stock")
        fig=plt.figure(figsize=(12, 9), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        #plot code
        #s=input("enter the name of the stock")
        df = pd.read_csv(s+".csv",)
        df=df.dropna()
        df= df.set_index('Date')
        ax=df.iloc[:,3].plot.line(title="Bitcoin \n Open" , rot=90,grid=True)
        ax.set_ylabel("Dollars")
        # saving an image 
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        fig.savefig('abc3.png')
        plt.close(fig)
        image = Image.open("abc3.png")
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "This text is drawn on image")
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
        return render(request,'twomonths.html',{})

def user_login5(request):

     if request.method=='POST':
        s=request.POST.get('stocks')
        predyears=request.POST.get('yearss')
        e=int(predyears)
        f=e*12
        import matplotlib.pyplot as plt
        import warnings
        import itertools
        import numpy as np
        import matplotlib.pyplot as plt
        import pandas as pd
        import statsmodels.api as sm
        import matplotlib
        fig=plt.figure(figsize=(20, 20), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams.update({'font.size': 20, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
        # df['month']=pd.to_datetime(df['month'])
        
        warnings.filterwarnings("ignore")
        plt.style.use('fivethirtyeight')
        
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 12
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        #s=input("enter the name of the stock")

        df = pd.read_csv(s+".csv", parse_dates=['Date'])
        cols = ['Symbol', 'Series', 'Prev Close','High', 'Low', 'Last', 'Close', 'VWAP', 'Volume', 'Turnover', 'Trades', 'Deliverable Volume', '%Deliverble']
        df.drop(cols, axis=1, inplace=True)
        df = df.sort_values('Date')
        df.isnull().sum()


        furniture = df.groupby('Date')['Open'].sum().reset_index()
        furniture = furniture.set_index('Date')
        furniture.index
        y = furniture['Open'].resample('MS').mean()
        y['2017':]
        #y.plot(figsize=(15, 6))
       # plt.show()
        #We can also visualize our data using a method called time-series decomposition 
        #that allows us to decompose our time series into three distinct components: trend, seasonality, and noise.
        from pylab import rcParams
        rcParams['figure.figsize'] = 18, 8
        decomposition = sm.tsa.seasonal_decompose(y, model='additive')
        #fig = decomposition.plot()
        #plt.show()
        # Time series forecasting with ARIMA 
        #finding all possible combination for p,d,q
        #ARIMA models are denoted with the notation ARIMA(p, d, q). 
        #These three parameters account for seasonality, trend, and noise in data:
        p = d = q = range(0, 2)
        pdq = list(itertools.product(p, d, q))
        seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
        print('Examples of parameter combinations for Seasonal ARIMA...')
        print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
        print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
        print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
        print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

        min=999999999
        for param in pdq:
            for param_seasonal in seasonal_pdq:
                try:
                    mod = sm.tsa.statespace.SARIMAX(y,
                                                    order=param,
                                                    seasonal_order=param_seasonal,
                                                    enforce_stationarity=False,
                                                    enforce_invertibility=False)
                    results = mod.fit()
                    if results.aic<min:
                        min=results.aic
                        k=[param,param_seasonal,results.aic]
                    print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                except:
                    continue
        print(k)
        print(k[0][0])
        # 12 is the interval for 12 months 
        mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(k[0][0], k[0][1], k[0][2]),
                                        seasonal_order=(k[1][0], k[1][1], k[1][2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
        results = mod.fit()
        print(results.summary().tables[1])

        #results.plot_diagnostics(figsize=(16, 8))
        #plt.show()
        #validating forecast
        pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
        pred_ci = pred.conf_int()
        ax = y['2014':].plot(label='observed')
        pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
        ax.fill_between(pred_ci.index,
                        pred_ci.iloc[:, 0],
                        pred_ci.iloc[:, 1], color='k', alpha=.2)
        ax.set_xlabel('Date')
        ax.set_ylabel('Furniture Sales')
        #plt.legend()
        #plt.show()
        #visualizing the forecast 
        pred_uc = results.get_forecast(steps=f)
        pred_ci = pred_uc.conf_int()
        ax = y['2019':].plot(label='observed', figsize=(14, 7))
        pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
        ax.fill_between(pred_ci.index,
                        pred_ci.iloc[:, 0],
                        pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.set_xlabel('Date')
        ax.set_ylabel('Open Predicitons')
        plt.legend()
        #plt.show()
        ###
        # saving an image 
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        fig.savefig('abc4.png')
        plt.close(fig)
        image = Image.open("abc4.png")
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "This text is drawn on image")
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
            #response = HttpResponse(buf.getvalue(), content_type='image/png')
            #return response
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
     else:
        return render(request,'timeseries.html',{})
def user_login6(request):
     if request.method=='POST':
        import yfinance as yf
        msft = yf.Ticker("MSFT")

                    # get stock info
        msft.info

        hist = msft.history(period="max")
        msft.actions




                    #msft.history(..., proxy="PROXY_SERVER")

        #s=input("enter the name of the stock")
        s=request.POST.get('ticker')

        data = yf.download(  # or pdr.get_data_yahoo(...
                # tickers list or string as well
                #tickers = "TCS",
                tickers =s,
                # use "period" instead of start/end
                # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                # (optional, default is '1mo')
                period = "1d",

                # fetch data by interval (including intraday if period < 60 days)
                # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                # (optional, default is '1d')
                interval = "15m",

                # group by ticker (to access via data['SPY'])
                # (optional, default is 'column')
                group_by = 'ticker',

                # adjust all OHLC automatically
                # (optional, default is False)
                auto_adjust = True,

                # download pre/post regular market hours data
                # (optional, default is False)
                prepost = True,

                # use threads for mass downloading? (True/False/Integer)
                # (optional, default is True)
                threads = True,

                # proxy URL scheme use use when downloading?
                # (optional, default is None)
                proxy = None
            )
        data
        data=data.reset_index()
        data.dtypes
        data['date'] = data['Datetime'].dt.date
        data['time'] = data['Datetime'].dt.time

        s=data.values.tolist()
        print(s)
        return render(request,'ticker2.html',{'s':s})
     else:
        return render(request,'ticker1.html',{})
