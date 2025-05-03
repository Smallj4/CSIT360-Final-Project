import pandas as pd
import statsmodels.api as sm

def main():
    
    # Reload the uploaded CSV file
    df = pd.read_csv("data/soccerdata.csv")


    # Select features and target variable
    features = ['Age', 'Height', 'Weight', 'Speed', 'Finishing']
    target = 'Rating'

    # Drop rows with missing values in the selected columns
    df_model = df[features + [target]].dropna()

    # Define independent variables (X) and add a constant term
    X = df_model[features]
    X = sm.add_constant(X)

    # Define dependent variable (y)
    y = df_model[target]

    # Fit the OLS model
    ols_model = sm.OLS(y, X).fit()

    # Display the summary of the model
    print(ols_model.summary())


main()
