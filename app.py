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

# Run home page
@app.route('/')
def home():
    return redirect(url_for('length'))

# Define route for the length page
@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        # Convert input to meters first
        value_in_meters = value * length_units[from_unit]
        # Then convert meters to target unit
        result = value_in_meters / length_units[to_unit]

    return render_template('length.html', result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)