from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace 'your_secret_key_here' with a real secret key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_schedule', methods=['POST'])
def submit_schedule():
    # Collect data from the form
    schedule_data = {
        'fname': request.form.get('fname', 'Not provided'),
        'lname': request.form.get('lname', 'Not provided'),
        'schedules': []
    }
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days:
        start = request.form.get(f'start-{day}', 'N/A')
        end = request.form.get(f'end-{day}', 'N/A')
        if start and ':' not in start:
            start += ':00'
        if not start:
            start = 'N/A'
        if end and ':' not in end:
            end += ':00'
        if not end:
            end = 'N/A'
        schedule_data['schedules'].append({
            'day': day,
            'start': start,
            'end': end
        })

    # Store data in session
    session['schedule_data'] = schedule_data
    return render_template('confirmation.html', data=schedule_data)

@app.route('/finalize')
def finalize_schedule():
    # Retrieve data from session
    schedule_data = session.get('schedule_data', None)
    if schedule_data:
        with open('schedules.txt', 'a') as file:
            file.write(f"{schedule_data['fname']} {schedule_data['lname']}\n")
            for schedule in schedule_data['schedules']:
                file.write(f" - {schedule['day']}: {schedule['start']} to {schedule['end']}\n")
            file.write("\n")
        message = "Your schedule has been confirmed."
        # Clear the session data after saving it
        session.pop('schedule_data', None)
    else:
        message = "No schedule data found to save."
    return render_template('finalize.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
