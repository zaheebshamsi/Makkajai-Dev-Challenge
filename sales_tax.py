# Copyright (c) 07-Mar-2021, Zaheeb Shamsi. All other marks are the property of their respective owners.

__author__ = 'Zaheeb Shamsi'

import sys


def sales_tax(product_list, product_type):
    """

    :param product_list: a list of products entered by the user. Checks for 4 scenarios :
                        1. exempted product and imported - 5%
                        2. exempted product and non imported - 0%
                        3. non exempted product and imported - 15%
                        4. non exempted product and non imported - 10%
    :param product_type: a dictionary to tell the code about exempted products.
    :return/output: Total cost including tax.

    """
    try:
        sales_tax_total = 0
        total_amount = 0
        total_amount_prod = 0
        sales_tax_final = 0
        for j in range(len(product_list)):
            temp = False
            product = product_list[j].split(' at')
            product_name_quantity = product[0]
            product_cost = product[-1]

            check_prod_dict = product_name_quantity.split(' ')
            for k in check_prod_dict:
                res = dict(filter(lambda item: k in item[0], product_type.items()))
                # print(res)
                if res:
                    temp = True

            if temp and "imported" in product_name_quantity:
                sales_tax_prod = 0
                total_amount = 0
                sales_tax_prod = sales_tax_prod + (5 * float(product_cost)) / 100
                sales_tax_total = sales_tax_total + sales_tax_prod
                total_amount_prod = total_amount_prod + float(product_cost)
                total_amount = sales_tax_total + total_amount_prod
                x = (float(product_cost) + sales_tax_prod)
                print(product_name_quantity + ": " + str(round(x, 2)))
            elif temp and "imported" not in product_name_quantity:
                sales_tax_total = 0
                total_amount = 0
                total_amount_prod = total_amount_prod + float(product_cost)
                total_amount = sales_tax_total + total_amount_prod
                x = (float(product_cost) + sales_tax_total)
                print(product_name_quantity + ": " + str(round(x, 2)))

            elif not temp and "imported" in product_name_quantity:
                sales_tax_prod = 0
                total_amount = 0
                sales_tax_prod = sales_tax_prod + (15 * float(product_cost)) / 100
                sales_tax_total = sales_tax_total + sales_tax_prod
                total_amount_prod = total_amount_prod + float(product_cost)
                total_amount = sales_tax_total + total_amount_prod
                x = (float(product_cost) + sales_tax_prod)
                print(product_name_quantity + ": " + str(round(x, 2)))

            elif not temp and "imported" not in product_name_quantity:
                sales_tax_prod = 0
                total_amount = 0
                sales_tax_prod = sales_tax_prod + (10 * float(product_cost)) / 100
                sales_tax_total = sales_tax_total + sales_tax_prod
                total_amount_prod = total_amount_prod + float(product_cost)
                total_amount = sales_tax_total + total_amount_prod
                x = (float(product_cost) + sales_tax_total)
                print(product_name_quantity + ": " + str(round(x, 2)))
            sales_tax_final = sales_tax_final + sales_tax_total

        print("---------------------")
        print("Sales Taxes: " + str(round(sales_tax_final, 2)))
        print("Total: " + str(round(total_amount, 2)))

    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)
        print(e)
        print(type(e))
        raise


if __name__ == '__main__':
    product_l = list()

    # The exempted dictionary.
    product_dict = {
        "book": "book",
        "books": "book",
        "chocolate": "food",
        "chocolates": "food",
        "pills": "medical"

    }
    try:
        n = int(input("No of products: "))
    except ValueError:
        print("Please use an integer value!!!!")
        raise
    for i in range(n):
        product_l.append(input("Enter product and price: "))
    sales_tax(product_l, product_dict)

"""
# Driver Code

sales_tax(['1 imported bottle of perfume at 32.19', '1 bottle of perfume at 20.89', 
            '1 packet of headache pills at 9.75', '1 imported box of chocolates at 11.85'], {
    "book": "book",
    "books": "book",
    "chocolate": "food",
    "chocolates": "food",
    "pills": "medical"

}

"""

# ['1 book at 12.49', '1 music CD at 14.99', '1 chocolate bar at 0.85'] ['1 imported box of chocolates at 10.00',
# '1 imported bottle of perfume at 47.50'] ['1 imported bottle of perfume at 32.19', '1 bottle of perfume at 20.89',
# '1 packet of headache pills at 9.75', '1 imported box of chocolates at 11.85']
