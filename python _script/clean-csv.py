import pandas as pd

def clean_population_data(file_path, output_path):
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Ensure the "Year" column is numeric
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    
    # Filter for rows where Year is between 1990 and 2022
    df_cleaned = df[(df["Year"] >= 1990) & (df["Year"] <= 2022)]
    
    # Remove rows where "Code" is missing
    df_cleaned = df_cleaned.dropna(subset=["Code"])
    
    # Save the cleaned data
    df_cleaned.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

# Example usage
input_file = r"C:\Users\prema\Desktop\Final Project-Carbon Emission\csv dataset\before clean datasets\annual-co-emissions-by-region.csv"
output_file = "annual-co-emissions-by-region-new.csv"
clean_population_data(input_file, output_file)
