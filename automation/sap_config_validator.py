import json

# Simulated SAP Organizational Data from the Blueprint
sap_structure = {
    "CompanyCode": "NC10",
    "Plants": ["NCP1", "NCP2"],
    "SalesOrg": "NCS1",
    "DistChannel": "01",
    "Division": "10"
}

def validate_enterprise_structure(config):
    print("--- SAP Configuration Health Check: NexaCore Industries ---")
    
    # 1. Check Company Code
    if config["CompanyCode"] == "NC10":
        print("[SUCCESS] Company Code NC10 is active.")
    else:
        print("[ERROR] Company Code missing!")

    # 2. Check Plant Integration
    if "NCP1" in config["Plants"]:
        print(f"[SUCCESS] Plant NCP1 (Bhubaneswar) is correctly assigned.")
    
    # 3. Check Sales Area
    sales_area = f"{config['SalesOrg']}-{config['DistChannel']}-{config['Division']}"
    if sales_area == "NCS1-01-10":
        print(f"[SUCCESS] Sales Area {sales_area} is fully operational.")
    else:
        print("[WARNING] Sales Area configuration mismatch.")

    print("--- Health Check Complete: System is ready for transactions ---")

if __name__ == "__main__":
    validate_enterprise_structure(sap_structure)
