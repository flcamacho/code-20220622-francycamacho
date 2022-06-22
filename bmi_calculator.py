import json
import pandas as pd

def convert_cm_to_m(height_cm):
    """Convert centimeters to meters"""
    height_m = "The height is none"
    if height_cm == None:
        return height_m
    elif height_cm <= 0:
        return "The height has to be >0"
    else:
        height_m = height_cm/100
    return height_m

def bmi_formula(mass, height):
    """Compute the bmi index : mass/(height)2"""
    bmi = None
    height_m = convert_cm_to_m(height)
    if mass != None and type(height_m) != str:
        if mass > 0:
            bmi = round((mass / (height_m * height_m)), 2)
            return bmi
        else:
            return bmi
    else:
        return bmi

def bmi_category_health_risk(mass, height):
    """Compute the category and health risk according to BMI"""
    category = None
    health_risk = None
    bmi = bmi_formula(mass, height)
    if bmi is None:
        return {'bmi category': category, 'bmi range': bmi,  'health_risk': health_risk}
    elif bmi>=0 and bmi<=18.4:
        category = "Underweight"
        health_risk = "Malnutrition risk"
    elif bmi>18.4 and bmi<=24.9:
        category = "Normal weight"
        health_risk = "Low risk"
    elif bmi>24.9 and bmi<=29.9:
        category = "Overweight"
        health_risk = "Enhanced risk"
    elif bmi>29.9 and bmi<=34.9:
        category = "Moderately obese"
        health_risk = "Medium risk"
    elif bmi>35 and bmi<=39.9:
        category = "Severely obese"
        health_risk = "High risk"
    elif bmi>40:
        category = "Very severely obese"
        health_risk = "Very high risk"
    else:
        return {bmi, "BMI incorrect", "BMI incorrect"}
    return {'bmi category': category, 'bmi range': bmi,  'health_risk': health_risk}

def main():
    data = json.load(open('bmi.json'))
    print("The data is loaded")
    df_data = pd.DataFrame(data)
    df_data[['bmi category', 'bmi range', 'health_risk']] = df_data.apply(lambda x: bmi_category_health_risk(x['WeightKg'], x['HeightCm']), axis=1,
                                               result_type='expand')
    json_string = df_data.to_json(orient='records')
    with open('bmi_with_features.json', 'w') as outfile:
        json.dump(json_string, outfile)
    print("The data is saved in bmi_with_features.json")
    print('Number of overweight people', df_data[df_data['bmi category']=='Overweight'].shape[0])