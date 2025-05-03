import pandas as pd

    

def main():
    
    data = pd.read_csv("data/FullData.csv")
    
    
    clean_data = data.drop(columns = ["Preffered_Foot", "Work_Rate", "Birth_Date", "Club_Joining", "Vision", "Composure", "Acceleration", "Crossing", "Contract_Expiry", "Volleys", "Curve", "Long_Shots", "Long_Pass","Short_Pass", "GK_Kicking", "GK_Handling",
                                      "GK_Reflexes","GK_Positioning", "GK_Diving", "Freekick_Accuracy", "Stamina", "Strength", "Balance", "Agility", "Jumping", "Heading", "Shot_Power",
                                      ])
    print(clean_data.columns)
    # Data wrangling: Clean Height and Weight columns
    clean_data['Height'] = clean_data['Height'].str.replace('cm', '', regex=False).str.strip()
    clean_data['Height'] = pd.to_numeric(clean_data['Height'], errors='coerce')
    
    clean_data['Weight'] = clean_data['Weight'].str.replace('kg', '', regex=False).str.strip()
    clean_data['Weight'] = pd.to_numeric(clean_data['Weight'], errors='coerce')

# Optional: Drop rows with missing or invalid heeight/weight if needed
# df.dropna(subset=['Height', 'Weight'], inplace=True)

    clean_data = clean_data.fillna(0)
    
    
    clean_data["Age"].value_counts()
    top_two = clean_data["Age"].nlargest(2)
    
    print(top_two)
    
    clean_data.to_csv("data/soccerdata.csv")
    
main()
