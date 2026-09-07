#Define a function called apply_coupon that takes an order total and an optional coupon code argument (default is None). If the coupon code is 'SAVE10', apply a 10% discount; otherwise, return the original total.
def apply_coupon(order_total, coupon_code=None):
    if coupon_code == "SAVE10":
        return order_total - (order_total * 10 / 100)
    else:
        return order_total


print("With coupon:", apply_coupon(1000, "SAVE10"))
print("Without coupon:", apply_coupon(1000))