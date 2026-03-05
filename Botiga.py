"""
This module manages product price calculations in a shop,
applying specific discounts and surcharges based on product type and customer age.
"""

# Constants to replace "Magic Numbers"
DISCOUNT_CLOTHING = 0.90      # 10% discount for clothing items
SURCHARGE_ELECTRONICS = 1.15  # 15% surcharge for electronic items
YOUTH_VOUCHER_VALUE = 5       # 5 euro discount for customers under 18
MINIMUM_PRICE = 0             # Price cannot be negative

def apply_discounts_and_surcharges(price, product_type):
    """
    Calculates the adjusted price based on the category of the product.

    Electronics carry a surcharge due to higher handling and recycling costs,
    while clothing is discounted to encourage seasonal sales.
    """
    if product_type == "ROBA":
        return price * DISCOUNT_CLOTHING
    elif product_type == "ELECTRONICA":
        return price * SURCHARGE_ELECTRONICS
    return price

def calculate_final_total(base_price, product_type, customer_age):
    """
    Calculates the final amount a customer has to pay.

    This includes product-specific adjustments and a youth voucher
    deduction for customers under the age of 18.
    """
    # 1. Apply category logic
    total = apply_discounts_and_surcharges(base_price, product_type)

    # 2. Apply youth voucher if applicable
    if customer_age < 18:
        total -= YOUTH_VOUCHER_VALUE

    # 3. Ensure total is never negative
    if total < MINIMUM_PRICE:
        total = MINIMUM_PRICE

    print(f"The total for the {product_type} item is: {total:.2f}€")

# Main execution calls
if __name__ == "__main__":
    calculate_final_total(100, "ROBA", 15)
    calculate_final_total(200, "ELECTRONICA", 40)
