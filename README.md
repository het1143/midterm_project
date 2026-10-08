# Midterm Project — Dosa Restaurant Order Processor

## What It Does

This project processes a JSON file of orders from a Dosa restaurant. It reads
the raw order data and produces two summary files:

- **customers.json** — A mapping of customer phone numbers to their names.
- **items.json** — A mapping of menu item names to their price and total number
  of times they were ordered.

## Design

The script is organized into small, focused functions:

| Function           | Purpose                                          |
|--------------------|--------------------------------------------------|
| `load_orders`      | Reads and parses the JSON orders file             |
| `build_customers`  | Extracts unique phone → name pairs from orders    |
| `build_items`      | Tallies item order counts and records prices      |
| `save_json`        | Writes a Python dict to a JSON file               |
| `main`             | Ties everything together with `argparse`          |

The input filename is passed as a **positional command-line argument** using
Python's `argparse` module, making the script flexible for any orders file.

## How to Use It

```bash
python process_orders.py <orders_file>
```

### Example

```bash
python process_orders.py example_orders.json
```

This will create (or overwrite) two files in the current directory:

- `customers.json`
- `items.json`

## Requirements

- Python 3.6+
- No external dependencies (uses only the standard library)
