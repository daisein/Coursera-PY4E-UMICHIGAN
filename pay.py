def computepay(h,r):
    h = float(h)
    r = float(r)
    if h <= 40:
        pay = h * r
    elif h > 40:
        fortypay = 40 * r
        extrapay = (h - 40) * r * 1.5
        pay = fortypay + extrapay
    else:
        print('error')
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print("Pay",p)
