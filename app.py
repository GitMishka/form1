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
            start = request.form.get(f'start-{day}', '').strip()
            end = request.form.get(f'end-{day}', '').strip()
            
            # Check if start or end is completely empty or not provided
            if not start and not end:
                schedule = 'N/A'
            else:
                # Append ':00' if hour is provided without minutes
                if start and ':' not in start:
                    start += ':00'
                elif not start:  # If start time is empty
                    start = 'N/A'
                
                if end and ':' not in end:
                    end += ':00'
                elif not end:  # If end time is empty
                    end = 'N/A'
                
                schedule = f"{start} to {end}"
            
            file.write(f" - {day}: {schedule}")
        file.write("\n")
    return render_template('confirmation.html')

@app.route('/finalize')
def finalize_schedule():
    # Handle finalization logic here
    return render_template('finalize.html', message="Your schedule has been confirmed.")
if __name__ == "__main__":
    app.run(debug=True)
