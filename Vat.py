def vatcalculator(totalprice,vatrate):
    result = totalprice+(totalprice*vatrate/100)
    return result

pricein=int(input("Price(THB): "))
Vatrate=int(input("Vat rate(%): "))
print(vatcalculator(pricein,Vatrate))



