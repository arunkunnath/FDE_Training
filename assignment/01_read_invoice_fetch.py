import csv

# File name
csv_file = "data/homework_invoices.csv"
output_file = "data/high_value_invoices.csv"

# Summary counters
total_homework_invoices = 0
greater_than = 0
invalid_amount = 0

# Read CSV file
# Read input CSV and create output CSV
with open(csv_file, mode="r", newline="", encoding="utf-8-sig") as file, \
     open(output_file, mode="w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(file)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    # Read each invoice record
    for invoice in reader:

        total_homework_invoices += 1
        invoice_id = invoice["invoice_id"]
        vendor = invoice["vendor"]
        amount = invoice["amount"]
        status = invoice["status"]

        print(f"invoice_id: {invoice_id}, Vendor: {vendor}, Amount: {amount}, Status: {status}")

        # Check amount
        try:
            # Check for missing amount
            if amount is None or amount.strip() == "":
                raise ValueError("Missing amount")

            amount = float(amount)

            # Check amount greater than 100000
            if amount > 100000:
                greater_than += 1
                print("  -> Amount is greater than 100000")
                                # Write matching record to output CSV
                writer.writerow(invoice)
                print(f"Matched: {invoice_id}, {vendor}, {amount}, {status}")

        except (ValueError, TypeError):
            invalid_amount += 1
            print("  -> Invalid or missing amount")


# Print summary
print("\n===== Summary =====")
print(f"Total homework_invoices read: {total_homework_invoices}")
print(f"Invoices with amount > 100000: {greater_than}")
print(f"Invoices with missing/invalid amount: {invalid_amount}")
print(f"Output file: {output_file}")