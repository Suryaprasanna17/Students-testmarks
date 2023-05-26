from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy student data (replace with your actual data loading logic)
students = [
    {"id": 1, "name": "John", "total_marks": 85},
    {"id": 2, "name": "Jane", "total_marks": 92},
    # Add more student data...
]

@app.route('/students', methods=['GET'])
def get_students():
    # Pagination logic (same as before)...
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    # Filtering logic
    filtered_students = filter_students(request.args)

    # Apply pagination to filtered results
    paginated_students = filtered_students[start_index:end_index]

    return jsonify(paginated_students)

def filter_students(filter_criteria):
    # Implement your filtering logic based on the filter_criteria
    filtered_students = students

    # Example filter criteria: filtering by minimum total marks
    min_marks = filter_criteria.get('min_marks')
    if min_marks:
        filtered_students = [student for student in filtered_students if student['total_marks'] >= int(min_marks)]

    # Add more filtering criteria as needed

    return filtered_students

if __name__ == '__main__':
    app.run()