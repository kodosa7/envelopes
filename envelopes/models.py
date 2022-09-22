from django.db import models
from django.utils import timezone
from django_countries.data import COUNTRIES


# Create your models here.
class Main(models.Model):
    TITLE = [('', ''), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Vážený pan', 'Vážený pan'), ('Vážená paní', 'Vážená paní'), ('Vážená slečna', 'Vážená slečna')]

    senderTitle = models.CharField(max_length=15, verbose_name=('Sender Title'), choices=TITLE)
    senderName = models.CharField(max_length=40, verbose_name=('Sender Full Name'))
    senderAddress = models.CharField(max_length=50, verbose_name=('Sender Address'))
    senderCity = models.CharField(max_length=40, verbose_name=('Sender City'))
    senderProvince = models.CharField(max_length=40, verbose_name=('Sender Province'))
    senderZip = models.CharField(max_length=40, verbose_name=('Sender ZIP/postal code'))
    senderCountry = models.CharField(max_length=60, verbose_name=('Sender Country'), choices=sorted(COUNTRIES.items()))

    receiverTitle = models.CharField(max_length=15, verbose_name=('Receiver Title'), choices=TITLE)
    receiverName = models.CharField(max_length=40, verbose_name=('Receiver Full Name'))
    receiverAddress = models.CharField(max_length=50, verbose_name=('Receiver Address'))
    receiverCity = models.CharField(max_length=40, verbose_name=('Receiver City'))
    receiverProvince = models.CharField(max_length=40, verbose_name=('Receiver Province'))
    receiverZip = models.CharField(max_length=40, verbose_name=('Receiver ZIP/postal code'))
    receiverCountry = models.CharField(max_length=60, verbose_name=('Receiver Country'), choices=sorted(COUNTRIES.items()))

    # this doesn't need to be here - maybe?:
    def __str__(self):
        return self.senderTitle, self.senderName, self.senderAddress, self.senderCity, self.senderProvince, self.senderCountry, self.senderZip, self.receiverTitle, self.receiverName, self.receiverAddress, self.receiverCity, self.receiverProvince, self.receiverCountry, self.receiverZip

    def submit(self):
        self_submitted_date = timezone.now()
        self.save()
