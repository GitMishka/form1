from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_schedule', methods=['POST'])
def submit_schedule():
    with open('schedules.txt', 'a') as file:
        file.write(f"{request.form.get('fname', 'N/A')} {request.form.get('lname', 'N/A')}")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            start_time = f"{request.form.get(f'start-{day}', 'N/A')} {request.form.get(f'ampm-start-{day}', '')}"
            end_time = f"{request.form.get(f'end-{day}', 'N/A')} {request.form.get(f'ampm-end-{day}', '')}"
            start_time = start_time.strip() if start_time.strip() != 'AM' and start_time.strip() != 'PM' else 'N/A'
            end_time = end_time.strip() if end_time.strip() != 'AM' and end_time.strip() != 'PM' else 'N/A'
            file.write(f" - {day}: {start_time} to {end_time}")
        file.write("\n")
    return 'Schedule submitted successfully!'

if __name__ == "__main__":
    app.run(debug=True)
