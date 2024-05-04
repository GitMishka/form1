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
            start_time = f"{request.form[f'start-{day}']} {request.form[f'ampm-start-{day}']}"
            end_time = f"{request.form[f'end-{day}']} {request.form[f'ampm-end-{day}']}"
            file.write(f" - {day}: {start_time} to {end_time}")
        file.write("\n")
    return 'Schedule submitted successfully!'

if __name__ == "__main__":
    app.run(debug=True)
