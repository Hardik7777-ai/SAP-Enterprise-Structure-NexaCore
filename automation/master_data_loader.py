import csv
import os

# Define the Master Data for NexaCore Industries
vendors = [
    {"ID": "VEND_001", "Name": "Steel Corp India", "City": "Bhubaneswar", "Org": "NCP0"},
    {"ID": "VEND_002", "Name": "TechLogistics Ltd", "City": "Kolkata", "Org": "NCP0"}
]

customers = [
    {"ID": "CUST_501", "Name": "Global Retailers", "Channel": "01", "Div": "10"},
    {"ID": "CUST_502", "Name": "Odisha Electronics", "Channel": "02", "Div": "10"}
]

def generate_sap_upload_file(data, filename):
    """Simulates generating a flat file for SAP Legacy System Migration Workbench (LSMW)"""
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"[SUCCESS] Generated {filename} for SAP Master Data Upload.")

if __name__ == "__main__":
    # Create the data files
    generate_sap_upload_file(vendors, 'vendor_master_nc10.csv')
    generate_sap_upload_file(customers, 'customer_master_nc10.csv')
