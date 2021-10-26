# 23% VAT was paid from the amount of PLN 15.84. Calculate and display VAT. Apply formatting with decimal places. Sample result:

# Amount : 15.84 zł
# VAT 23% : 3.64 zł

total = float(input("Total transaction value: "))

vat = round(total * 0.23, 2)

print(f"Amount : {total} zł\nVAT 23% : {vat} zł")
