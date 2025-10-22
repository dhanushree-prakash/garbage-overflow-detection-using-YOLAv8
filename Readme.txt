Project Title: YOLOv8 Garbage Overflow Detection with Flask Web App 🗑️🤖

Description:
This project detects overflowing garbage bins in real-time using YOLOv8 object detection. 
It provides a web interface built with Flask where users can view live detection results 
and get notifications for full bins. 🌐📸

Folder Structure:
1. source_code/        -> Contains all source code files 💻
2. Executable/         -> Compiled executable files (if any) ⚙️
3. Project_Report/     -> Project report in Word format 📄
4. PPT/                -> Final viva presentation 📊
5. Video/              -> Demonstration video 🎥
6. Journal_Paper/      -> Journal paper in Word format 📑
7. Abstract/           -> One-page abstract ✏️
8. Readme.txt          -> Instructions to run the project 📝

## Project Documents

- [Project Report](Project_Report/Project_Report.docx)
- [Journal Paper](Journal_Paper/Journal_Paper.docx)
- [Abstract](Abstract/Abstract.docx)


Requirements:
- Python 3.10 or higher 🐍
- pip (Python package installer) 📦
- Recommended IDE: VS Code, PyCharm, or any code editor 💻
- Webcam or video feed for live detection 🎥

Python Libraries:
- ultralytics 🤖
- opencv-python 🖼️
- Flask 🌐
- numpy 🔢
- matplotlib 📊 (optional)
- torch 🔥

Installation Steps:
1. Navigate to the source_code folder:
   cd source_code

2. Create a virtual environment (optional but recommended):
   python -m venv venv
   # Activate environment:
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt
   # If requirements.txt is not available, install manually:
   pip install ultralytics opencv-python Flask numpy matplotlib torch

Execution Steps:
1. To run the Flask web application:
   python app.py 🚀

2. Open a web browser and go to:
   http://127.0.0.1:5000/ 🌐

3. Upload an image or start live detection to see overflowing bins highlighted 🗑️✅

Notes:
- Ensure that yolov8n.pt (YOLOv8 model) is present in the source_code folder 📦
- You can retrain the YOLOv8 model using your custom dataset if required 🔄
- For any issues with video feed, make sure your webcam is connected and not used by other applications 📷❌

Contact:
For any queries or help, contact:
Name: Dhanushree S. P. ✨
Email: dhanushreesp13@gmail.com 📧
Phone: 8667631044 📞
