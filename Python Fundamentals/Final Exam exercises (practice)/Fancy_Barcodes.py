import re


def parse_barcodes(barcode_data):
    pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

    for barcode in barcode_data:
        match = re.findall(pattern, barcode)
        if match:
            product_group = ''.join(re.findall(r'\d', barcode))
            if product_group:
                print(f"Product group: {product_group}")
            else:
                print(f'Product group: 00')
        else:
            print('Invalid barcode')


n = int(input())
barcodes = [input() for _ in range(n)]
parse_barcodes(barcodes)