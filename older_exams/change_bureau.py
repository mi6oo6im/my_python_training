bitcoin_bgn = 1168.0
yoan_usd = 0.15
usd_bgn = 1.76
euro_bgn = 1.95

bitcoin = int(input())
yoan = float(input())
commission_percent = float(input())

bitcoin_euro = bitcoin * bitcoin_bgn / euro_bgn
yoan_euro = yoan * yoan_usd * usd_bgn / euro_bgn

total_euro = bitcoin_euro + yoan_euro
commission_euro = total_euro * commission_percent / 100
final_euro = total_euro - commission_euro

print(f"{final_euro:.2f}")
