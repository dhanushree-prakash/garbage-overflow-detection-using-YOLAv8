import cv2
from ultralytics import YOLO
from flask import Flask, Response, render_template, request, redirect, url_for
import tempfile
import os

# Flask APPLICATION
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

# Load the YOLOv8 model
model = YOLO('last.pt')

# Flag to indicate if the script should terminate
terminate_flag = False

# Define a generator function to stream video frames to the web page
def generate(file_path):
    global terminate_flag
    if file_path == "camera":
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(file_path)

    while cap.isOpened():
        # Break immediately if stop is requested
        if terminate_flag:
            break

        success, frame = cap.read()
        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Encode the frame as JPEG
            ret, jpeg = cv2.imencode('.jpg', annotated_frame)

            # Yield the JPEG data to Flask
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        else:
            break

    cap.release()

# Define a route to serve the video stream
@app.route('/video_feed')
def video_feed():
    file_path = request.args.get('file')
    return Response(generate(file_path),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Define a route to serve the HTML page with the file upload form
@app.route('/', methods=['GET', 'POST'])
def index():
    global terminate_flag
    if request.method == 'POST':
        if request.form.get("camera") == "true":
            file_path = "camera"
        elif 'file' in request.files:
            file = request.files['file']
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
        else:
            file_path = None
        return render_template('index.html', file_path=file_path)
    else:
        terminate_flag = False
        return render_template('index.html')

@app.route('/stop', methods=['POST'])
def stop():
    global terminate_flag
    terminate_flag = True
    print("Camera stopped")
    return redirect(url_for('index'))  # Redirect back to home

@app.route('/stop_page')
def stop_page():
    global terminate_flag
    terminate_flag = True  # Stop the video feed
    return render_template('stop.html')  # Show stop.html

if __name__ == '__main__':
    app.run(debug=True)
