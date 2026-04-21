# SAP-Enterprise-Structure-NexaCore
SAP S/4HANA Enterprise Structure Blueprint for FI, MM, and SD modules.
# SAP Enterprise Structure: NexaCore Industries Global
**Student Name:** Hardik_Chaturvedi  
**Roll Number:** 2305452  
**Institution:** KIIT (3rd Year CSE)

## 1. Project Overview
This repository contains the technical blueprint and implementation logic for a centralized ERP system using SAP S/4HANA. The project focuses on the integration of Financial Accounting (FI), Materials Management (MM), and Sales and Distribution (SD) modules for a fictitious global entity, NexaCore Industries.

## 2. Organizational Structure
The system is designed with a hierarchical structure to ensure real-time data consistency across departments:

- **Financial Accounting (FI):**
  - Company Code: `NC10` (NexaCore India Ltd.)
- **Materials Management (MM):**
  - Plants: `NCP1` (Bhubaneswar), `NCP2` (Kolkata)
  - Storage Locations: `RM01` (Raw Materials), `FG01` (Finished Goods)
- **Sales & Distribution (SD):**
  - Sales Org: `NCS1` (India Domestic)
  - Distribution Channel: `01` (Wholesale)
  - Division: `10` (Electronics)

## 3. Tech Stack
- **ERP:** SAP S/4HANA
- **Database:** SAP HANA (SQL-based verification)
- **Programming:** ABAP (Custom reporting logic)

## 4. Repository Contents
- `/scripts`: Contains ABAP and SQL scripts for system verification.
- `/config`: Technical logs of the SPRO implementation paths.
- `/docs`: Final Capstone Project Report (PDF).
