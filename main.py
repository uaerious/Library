from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

seats = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
timeslots = ['9:00', '11:00', '13:00', '15:00']

# Dictionary to store bookings
bookings = {}

@app.route('/')
def index():
	return render_template('index.html', seats=seats, timeslots=timeslots)

@app.route('/book', methods=['POST'])
def book_seat():
	name = request.form['name']
	email = request.form['email']
	seat = request.form['seat']
	date = request.form['date']
	timeslot = request.form['timeslot']

	# Check if seat is available for the chosen date and timeslot
	if bookings.get(date) and bookings[date].get(timeslot) and seat in bookings[date][timeslot]:
		message = f'Seat {seat} is already booked for the selected date and timeslot. Please choose another seat or select a different date/timeslot.'
		return render_template('error.html', message=message)

	# Add booking to dictionary
	if date not in bookings:
		bookings[date] = {}
	if timeslot not in bookings[date]:
		bookings[date][timeslot] = []
	bookings[date][timeslot].append(seat)

	# Store the booking information in a session variable
	session['booking'] = {'name': name, 'email': email, 'seat': seat, 'date': date, 'timeslot': timeslot}

	return redirect('/confirmation')

@app.route('/confirmation')
def confirmation():
	# Retrieve the booking information from the session variable
	booking = session.get('booking')

	if booking:
		return render_template('confirmation.html', booking=booking)
	else:
		return render_template('error.html')

app.run(host='0.0.0.0', port=81)