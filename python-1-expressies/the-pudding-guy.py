# https://dodona.ugent.be/nl/courses/399/series/3960/activities/761303597

aantal = int(input('Het aantal gekochte stuks van een bepaald product (integer): '))
prijsPS = float(input('De kostprijs per stuk van het product (float): '))
vereisteBarcodes = int(input('Het aantal barcodes nodig voor een frequent flyer coupon (integer): '))
mijlenPerCoupon = int(input('Het aantal mijlen dat men ontvangt per frequent flyer coupon (integer): '))

print(f'Phillips spendeerde ${aantal*prijsPS} voor {int(aantal/vereisteBarcodes) * mijlenPerCoupon} frequent flyer mijlen.')