from main import convert_cm_to_m, bmi_formula, bmi_category_health_risk
from fixtures import correct_data

def test_convert_cm_to_m():
    """Validate a correct conversion to meters"""
    height_cm = 171
    assert convert_cm_to_m(height_cm) == 1.71

def test_zero_convert_cm_to_m():
    """Validate an incorrect value of height (height = 0)"""
    height_cm = 0
    assert convert_cm_to_m(height_cm) == "The height has to be >0"

def test_none_convert_cm_to_m():
    """Validate an incorrect value of height (height = none)"""
    height_cm = None
    assert convert_cm_to_m(height_cm) == "The height is none"

def test_bmi_formula():
    "Validate a correct computation of BMI"
    height_cm = 175
    mass = 75
    assert bmi_formula(mass, height_cm) == 24.49

def test_zero_mass_bmi_formula():
    "Validate a correct computation of BMI"
    height_cm = 175
    mass = 0
    assert bmi_formula(mass, height_cm) == None

def test_bmi_category_health_risk():
    "Validate a correct computation of BMI"
    height_cm = 175
    mass = 75
    assert bmi_category_health_risk(mass, height_cm) == {'bmi category': 'Normal weight', 'bmi range': 24.49,
                                                         'health_risk':'Low risk'}

