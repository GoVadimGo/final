# Интернет магазин занимается продажей различных сувениров и безделушек. Каждый сувенир весит 75г , а безделушка
# 112г . Написать программу , запрашивающую  у пользователя количество тех и других покупок, после чего
# выведите на экран общий вес посылки.

suv = int(input('Enter quantity of gifts: '))
bagatelle = int(input('Enter quantity of bagatelles: '))

SUV = suv * 75

BAG = bagatelle * 112

SUM = (SUV + BAG)/1000

print(f'In summary you have {SUM:.1f} kg of parcel weight. ')