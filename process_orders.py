"""
process_orders.py

Reads a JSON file of restaurant orders and produces two output files:
  - customers.json: maps phone numbers to customer names
  - items.json: maps item names to their price and total order count
"""

import argparse
import json


def load_orders(filepath):
    """Load and return the list of orders from a JSON file."""
    with open(filepath, "r") as f:
        orders = json.load(f)
    return orders


def build_customers(orders):
    """Build a dictionary mapping phone numbers to customer names.

    Args:
        orders: A list of order dictionaries, each containing 'phone' and
                'name' keys.

    Returns:
        A dict with phone numbers (str) as keys and customer names (str) as
        values.
    """
    customers = {}
    for order in orders:
        phone = order["phone"]
        name = order["name"]
        customers[phone] = name
    return customers


def build_items(orders):
    """Build a dictionary mapping item names to price and order count.

    Args:
        orders: A list of order dictionaries, each containing an 'items' key
                whose value is a list of dicts with 'name' and 'price' keys.

    Returns:
        A dict with item names (str) as keys and dicts containing 'price'
        (float) and 'orders' (int) as values.
    """
    items = {}
    for order in orders:
        for item in order["items"]:
            item_name = item["name"]
            item_price = item["price"]
            if item_name in items:
                items[item_name]["orders"] += 1
            else:
                items[item_name] = {"price": item_price, "orders": 1}
    return items


def save_json(data, filepath):
    """Write a Python object to a JSON file with readable formatting."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def main():
    """Parse command-line arguments and process the orders file."""
    parser = argparse.ArgumentParser(
        description="Process restaurant orders and generate customer and item reports."
    )
    parser.add_argument(
        "orders_file",
        help="Path to the JSON file containing orders"
    )
    args = parser.parse_args()

    # Load orders from the input file
    orders = load_orders(args.orders_file)

    # Build and save customers.json
    customers = build_customers(orders)
    save_json(customers, "customers.json")
    print(f"Created customers.json with {len(customers)} customers.")

    # Build and save items.json
    items = build_items(orders)
    save_json(items, "items.json")
    print(f"Created items.json with {len(items)} items.")


if __name__ == "__main__":
    main()
