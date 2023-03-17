from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SEATS = ['Seat 1', 'Seat 2', 'Seat 3', 'Seat 4', 'Seat 5']

# Initialize a dictionary to store seat bookings
bookings = {}

@app.route('/')
def index():
    return render_template('index.html', seats=SEATS)

@app.route('/book', methods=['POST'])
def book_seat():
    if request.method == 'POST':
        # Get form data from request
        name = request.form['name']
        email = request.form['email']
        seat = request.form['seat']
        time = request.form['time']

    if seat in bookings:
        message = f'Seat {seat} is already booked. Please choose another seat.'
        return render_template('error.html', message=message)
    else:
        # Add booking to dictionary
        bookings[seat] = {'name': name, 'email': email, 'time': time}
        return redirect('/confirm')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html', bookings=bookings)

app.run(host='0.0.0.0', port=81)