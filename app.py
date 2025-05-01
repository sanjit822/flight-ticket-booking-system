from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Mock database of available flights
flights_db = [
    {"from": "New York", "to": "Los Angeles", "date": "2025-06-01", "class": "Economy"},
    {"from": "Chicago", "to": "Miami", "date": "2025-06-05", "class": "Business"},
    {"from": "San Francisco", "to": "Chicago", "date": "2025-07-10", "class": "First"},
    {"from": "London", "to": "Paris", "date": "2025-08-15", "class": "Economy"},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search_flights():
    if request.method == 'POST':
        from_city = request.form['from']
        to_city = request.form['to']
        date = request.form['date']
        travel_class = request.form['class']

        # Filtering flights from mock database
        available_flights = [flight for flight in flights_db if
                             (flight["from"].lower() == from_city.lower()) and
                             (flight["to"].lower() == to_city.lower()) and
                             (flight["date"] == date) and
                             (flight["class"].lower() == travel_class.lower())]

        return render_template('search_flights.html', flights=available_flights)

    return render_template('search_flights.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/confirm_booking', methods=['POST'])
def confirm_booking():
    if request.method == 'POST':
        # Get booking details (in a real app, this should save to a database)
        name = request.form['name']
        email = request.form['email']
        flight_from = request.form['from']
        flight_to = request.form['to']
        date = request.form['date']
        travel_class = request.form['class']

        # Here you can implement payment and booking confirmation logic
        confirmation_message = f"Booking confirmed for {name}, {email}. Flight details: {flight_from} to {flight_to} on {date} in {travel_class} class."

        return render_template('booking_confirmation.html', confirmation_message=confirmation_message)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
