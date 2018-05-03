"""Bill"""
def main():
    """Calculate money from Bill"""
    price = int(input())
    service = price*0.1
    if service < 50:
        vat = (price + 50) * 0.07
        print("%.2f" %(price + 50 + vat))
    elif service >= 1000:
        vat = (price + 1000) * 0.07
        print("%.2f" %(price + 1000 + vat))
    else:
        vat = (price + service) * 0.07
        print("%.2f" %(price + service + vat))
main()
