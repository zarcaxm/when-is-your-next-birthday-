__author__ = 'Andre cirilo'
import datetime

bday = input("When is your next birthday? (dd/mm/yyyy)")
bday2 = datetime.datetime.strptime(bday,"%d/%m/%Y").date()

today = datetime.date.today()
today.strftime("%d/%m/%Y")

number_days= bday2 - today

print("U have to wait",number_days," :)")