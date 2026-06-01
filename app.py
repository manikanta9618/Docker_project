from flask import Flask, render_template, jsonify

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Rahul",
        "department": "CSE",
        "joining_date": "2026-01-10",
        "exam_fee": "Paid"
    },
    {
        "id": 2,
        "name": "Priya",
        "department": "ECE",
        "joining_date": "2026-02-15",
        "exam_fee": "Pending"
    },
    {
        "id": 3,
        "name": "Kiran",
        "department": "EEE",
        "joining_date": "2026-03-05",
        "exam_fee": "Paid"
    }
]

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/students')
def student_list():
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
