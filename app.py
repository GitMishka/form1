from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <title>Weekly Schedule Entry</title>
</head>
<body>
    <h2>Enter Weekly Schedule</h2>
    <form action="/submit_schedule" method="post">
        <label for="fname">First Name:</label><br>
        <input type="text" id="fname" name="fname" required><br>
        <label for="lname">Last Name:</label><br>
        <input type="text" id="lname" name="lname" required><br>
        <label for="schedule">Schedule:</label><br>
        <textarea id="schedule" name="schedule" rows="4" required></textarea><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit_schedule', methods=['POST'])
def submit_schedule():
    with open('schedules.txt', 'a') as file:
        file.write(f"{request.form['fname']} {request.form['lname']} - {request.form['schedule']} - {datetime.datetime.now()}\n")
    return 'Schedule submitted successfully!'

# Reset the file every 7 days
@app.cli.command("reset-schedules")
def reset_schedules():
    with open('schedules.txt', 'w') as file:
        file.truncate(0)  # Clear the content

if __name__ == "__main__":
    app.run(debug=True)
