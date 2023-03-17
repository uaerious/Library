from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Available seats
SEATS = ['Seat 1', 'Seat 2', 'Seat 3', 'Seat 4', 'Seat 5']

# Bookings dictionary
bookings = {}

@app.route('/')
def index():
    return render_template('index.html', seats=SEATS)

@app.route('/book', methods=['POST'])
def book():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    seat = request.form['seat']

    # Check if seat is available
    if seat in bookings:
        message = f'Seat {seat} is already booked. Please choose another seat.'
        return render_template('error.html', message=message)
    else:
        # Add booking to dictionary
        bookings[seat] = {'name': name, 'email': email}
        return redirect('/confirm')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html', bookings=bookings)

app.run(host='0.0.0.0', port=81)