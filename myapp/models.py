from django.db import models

# Create your models here.
class contactus(models.Model):
    First_Name= models.CharField(max_length = 30)
    last_name= models.CharField(max_length=30)
    emailid = models.EmailField()
    Phone = models.IntegerField()
    Message=models.TextField()
    Selected_Course = models.CharField(
        max_length = 20,
        choices = [('Stocks', 'Stocks'), ('Cryptocurrency','Cryptocurrency')],
        default = 'Stocks'
    )
    def __str__(self):
        return self.First_Name
class register(models.Model):
    FullName= models.CharField(max_length = 30)
    Email = models.EmailField()
    Password = models.CharField(max_length = 30)
    city=models.CharField(max_length=15,null=True , blank=True)
    mobile=models.CharField(max_length=10,null=True , blank=True)
    Address=models.TextField(null=True , blank=True)
    def __str__(self):
        return self.FullName
class expert(models.Model):
    expert_email=models.EmailField(null=True , blank=True)
    FullName= models.CharField(max_length = 30)
    phone =models.CharField(max_length = 30,null=True , blank=True)
    address =models.TextField(null=True , blank=True)
    jobTitle =models.CharField(max_length = 30)
    description =models.TextField()
    profile_pic =models.ImageField(upload_to="data",blank=True)
    def __str__(self):
        return self.FullName
class expertquestions(models.Model):
    question =models.CharField(max_length = 200)
    answer =models.TextField(null=True , blank=True)
    def __str__(self):
        return self.question
class post(models.Model):
    title=models.CharField(max_length =40) 
    description =models.TextField(null=True, blank=True)
    content =models.TextField(null=True,blank=True)
    expert_email=models.EmailField() 
    def __str__(self):
        return self.Name 
class watchStock(models.Model):
    user_email=models.EmailField() 
    stock =models.CharField(max_length=50)
class stockguide(models.Model):
    questions =models.CharField(max_length = 200)
    answers =models.TextField(null=True , blank=True)
    def __str__(self):
        return self.questions
class cryptoguide(models.Model):
    questions =models.CharField(max_length = 200)
    answers =models.TextField(null=True , blank=True)
    picture =models.ImageField(upload_to="data",blank=True)
    pdf=models.FileField(upload_to="data",blank=True)
    def __str__(self):
        return self.questions