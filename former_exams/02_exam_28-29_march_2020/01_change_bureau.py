number_bitcoins = int(input())
number_chineese_yuana = float(input())
commission = float(input())

btc_in_bgn = number_bitcoins * 1168
cya_in_bgn = number_chineese_yuana * 0.15 * 1.76
total_leva = btc_in_bgn + cya_in_bgn
total_eur = total_leva / 1.95
commission_total = total_eur * commission / 100
total = total_eur - commission_total
print(f"{total:.2f}")
