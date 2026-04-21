import pandas as pd

# Mock dataset representing materials in your SAP Plants (NCP1 & NCP2)
# In a real scenario, this data would come from SAP via an OData or RFC connection.
data = {
    'Plant': ['NCP1', 'NCP1', 'NCP2', 'NCP2'],
    'Material_ID': ['MAT-101', 'MAT-102', 'MAT-201', 'MAT-202'],
    'Current_Stock': [500, 150, 800, 50],
    'Daily_Usage': [50, 20, 60, 15],
    'Lead_Time_Days': [5, 10, 4, 12]
}

def calculate_safety_stock(df):
    """
    Calculates Safety Stock and Reorder Points for the Enterprise Structure.
    Formula: (Max Daily Usage * Max Lead Time) - (Avg Daily Usage * Avg Lead Time)
    Simplified for this simulation: (Daily Usage * Lead Time) * 1.5
    """
    print("--- NexaCore Inventory Analytics Report ---")
    
    # Calculate Reorder Point (ROP)
    df['Reorder_Point'] = df['Daily_Usage'] * df['Lead_Time_Days']
    df['Safety_Stock'] = (df['Reorder_Point'] * 0.5).astype(int)
    
    # Identify items that need restocking
    df['Status'] = df.apply(lambda x: 'REORDER' if x['Current_Stock'] <= x['Reorder_Point'] else 'OK', axis=1)
    
    return df

if __name__ == "__main__":
    inventory_df = pd.DataFrame(data)
    results = calculate_safety_stock(inventory_df)
    
    # Display the results
    print(results[['Plant', 'Material_ID', 'Current_Stock', 'Reorder_Point', 'Status']])
    
    # Summary per plant
    print("\n--- Summary by Plant ---")
    print(results.groupby('Plant')['Current_Stock'].sum())
