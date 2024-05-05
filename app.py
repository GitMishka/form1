from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_schedule', methods=['POST'])
def submit_schedule():
    with open('schedules.txt', 'a') as file:
        file.write(f"{request.form.get('fname', 'Not scheduled')} {request.form.get('lname', 'Not scheduled')}")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            start = request.form.get(f'start-{day}', 'N/A')
            end = request.form.get(f'end-{day}', 'N/A')
            if start != 'N/A' and ':' not in start:
                start += ':00'
            if end != 'N/A' and ':' not in end:
                end += ':00'
            file.write(f" - {day}: {start} to {end}")
        file.write("\n")
    return 'Schedule submitted successfully!'

if __name__ == "__main__":
    app.run(debug=True)
