*&---------------------------------------------------------------------*
*& Report Z_NEXACORE_STRUCTURE
*& Purpose: Verify Enterprise Structure Assignments for Capstone Project
*&---------------------------------------------------------------------*
REPORT z_nexacore_structure.

TABLES: t001, t001w, tvko.

SELECT-OPTIONS: s_bukrs FOR t001-bukrs DEFAULT 'NC10'.

START-OF-SELECTION.
  WRITE: / '--- NexaCore Industries: Enterprise Structure Assignment ---'.
  ULINE.

  " Verify Plant to Company Code Assignment
  SELECT bukrs, werks FROM t001k INTO TABLE @DATA(lt_plants)
    WHERE bukrs IN @s_bukrs.

  LOOP AT lt_plants INTO DATA(ls_plant).
    WRITE: / 'Company Code:', ls_plant-bukrs, 'Linked Plant:', ls_plant-werks.
  ENDLOOP.

  " Verify Sales Org to Company Code Assignment
  SELECT vkorg, bukrs FROM tvko INTO TABLE @DATA(lt_sales)
    WHERE bukrs IN @s_bukrs.

  LOOP AT lt_sales INTO DATA(ls_sales).
    WRITE: / 'Sales Org:', ls_sales-vkorg, 'Assigned to FI Code:', ls_sales-bukrs.
  ENDLOOP.
