# Function to calculate the assessment value (60% of the actual value)
def get_assessment_value(value):
    return value * 0.60

# Function to calculate the property tax (72¢ for each $100 of the assessment value)
def get_tax_assessed(assessment_value):
    return assessment_value * 0.0072

