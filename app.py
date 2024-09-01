# app.py

from flask import Flask, jsonify, render_template
from parking_detection import count_parking_slots

app = Flask(__name__)

# Endpoint to get parking slot information
@app.route('/parking-info', methods=['GET'])
def get_parking_info():
    video_path = 'easy.mp4'  # Replace with your video file path
    total_slots, filled_slots, carCount, freeSpace = count_parking_slots(video_path)
    
    # Wait for the function to complete
    # Show the output
    print("Total Slots:", total_slots)
    print("Filled Slots:", filled_slots.count('red'))
    print("Empty Slots:", filled_slots.count('green'))
    print("Car Count:", carCount)
    print("Free Space:", freeSpace)

    slot_status = [{'status': status} for status in filled_slots]

    result = jsonify({
        'total_slots': total_slots,
        'filled_slots': filled_slots.count('red'),  # Counting filled slots
        'empty_slots': filled_slots.count('green'),  # Counting empty slots
        'slot_status': slot_status
    })
    return render_template('parking.html', slot_status=slot_status, total_slots=total_slots, filled_slots=filled_slots.count('red'), empty_slots=filled_slots.count('green'))

# Endpoint to render HTML page with parking information
@app.route('/', methods=['GET'])
def render_parking_page():
    return render_template('parking.html')

if __name__ == '__main__':
    app.run(debug=True)
