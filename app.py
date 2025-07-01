from flask import Flask, render_template, request, redirect, url_for

# Create a Flask web app
app = Flask(__name__)

# Conversion factors to meters
length_units = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
}
# Conversion factors to grams
weight_units = {
    "milligram": 0.001,
    "gram": 1,
    "kilogram": 1000,
    "ounce": 28.3495,
    "pound": 453.592
}

# Run home page
@app.route('/')
def home():
    return redirect(url_for('length'))

def get_form_data():
    try:
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        return value, from_unit, to_unit, None  # No error
    except (ValueError, KeyError) as e:
        return None, None, None, "Invalid input: " + str(e)

# Define route for the length page
@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    error = None

    if request.method == 'POST':
        value, from_unit, to_unit, error = get_form_data()

        if error is None:
            # Convert input to meters first
            value_in_meters = value * length_units[from_unit]
            # Convert meters to target unit
            result = round(value_in_meters / length_units[to_unit], 4)

    return render_template('length.html', result=result, error=error, active='length')

# Define route for the weight page
@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    error = None

    if request.method == 'POST':
        value, from_unit, to_unit, error = get_form_data()

        if error is None:
            # Convert input to grams first
            value_in_grams = value * weight_units[from_unit]
            # Convert grams to target unit
            result = round(value_in_grams / weight_units[to_unit], 4)

    return render_template('weight.html', result=result, error=error, active='weight')

# Define route for the temperature page
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        value = value - 273.15

    # Convert from Celsius to target
    if to_unit == "Fahrenheit":
        return round((value * 9 / 5) + 32, 4)
    elif to_unit == "Kelvin":
        return round(value + 273.15, 4)
    else:  # to_unit == "Celsius"
        return round(value, 4)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    result = None
    error = None

    if request.method == 'POST':
        value, from_unit, to_unit, error = get_form_data()

        if error is None:
            result = convert_temperature(value, from_unit, to_unit)
    return render_template('temperature.html', result=result, error=error, active='temperature')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)