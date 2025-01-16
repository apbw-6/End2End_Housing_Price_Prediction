# End2End_Housing_Price_Prediction

This project takes a basic linear regression model regarding the problem of predicting house prices in California, to produce an end-to-end data science project. The prediction can be accessed on [pythonanywhere](https://apb.pythonanywhere.com/) temporarily.

### Creating a virtual environment:
1. Open new terminal on VSCode.
2. Check base Python version (here 3.11.7)
3. conda create -p venv python==3.11.7 -y
4. To activate it: conda activate venv/

### Requirements (UNSYNCED):
1. The libraries that need to be installed are kept in requirements.txt.
2. To install, in the terminal, type pip install -r requirements.txt

### Requirements (SYNCED):
1. Type requirements into requirements.in and then run pip-compile in terminal (ensure you're in venv).
2. To sync with venv, pip-sync into terminal.
3. Read more here: https://suyojtamrakar.medium.com/managing-your-requirements-txt-with-pip-tools-in-python-8d07d9dfa464

### Running the application:
1. In the terminal, python3 app.py
2. Go to the webpage.

### Input from Client's end from Postman:
1. Go to Postman, create a new post request.
2. Link is: http://127.0.0.1:5000/predict_api (check the link the terminal displays)
3. Fill in raw data (also in temp.ipynb): (This looks like a dictionary but the syntax is different!)
   {
    "data": {
        "longitude": -122.21,
        "latitude": 36.88,
        "housing_median_age": 32,
        "total_rooms": 860,
        "total_bedrooms": 119,
        "population": 302,
        "households": 116,
        "median_income": 8.3252,
        "ocean_proximity": "NEAR BAY"
    }
}
4. Send the request and the output is the predicted price.

### Input from Client's end from homepage (https://apb.pythonanywhere.com/):
1. Enter values against the relevant boxes in the homepage.
2. Press the Predict button.