from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_schedule', methods=['POST'])
def submit_schedule():
    with open('schedules.txt', 'a') as file:
        file.write(f"{request.form['fname']} {request.form['lname']}")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            file.write(f" - {day}: {request.form[f'schedule-{day}']} {request.form[f'ampm-{day}']}")
        file.write("\n")
    return 'Schedule submitted successfully!'

if __name__ == "__main__":
    app.run(debug=True)
