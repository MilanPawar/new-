

# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def calculate_sum():
#     if request.method == 'POST':
#         try:
#             num1 = float(request.form['num1'])
#             num2 = float(request.form['num2'])
#             result = num1 + num2
#             return render_template('result.html', result=result)
#         except ValueError:
#             return "Invalid input. Please enter valid numbers."
#     return render_template('input_form.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template,request
import cv2
import numpy as np
import os
from  skimage.metrics import structural_similarity as ssim

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
        if 'dataset_1' in request.form:
            result = run_helper_anomaly()
        elif 'dataset_2' in request.form:
            result = run_helper_safe()
        else:
            result = "Unknown button clicked"
        return render_template('result.html', result=result)
   return render_template('index.html')
def compare_images(img1_path, img2_path):
    # Construct the full paths to the images
    directory = '/home/codespace/zany-palm-tree/'
    img1_full_path = os.path.join(directory, img1_path)
    img2_full_path = os.path.join(directory, img2_path)
    

# Read the grayscale image (gray2 in your case)
# Assuming you already have 'gray2' loaded

# Specify the output path
    output_path4 = '/home/codespace/zany-palm-tree/static/image4.jpg'
    output_path3 = '/home/codespace/zany-palm-tree/static/image3.jpg'
    output_path2 = '/home/codespace/zany-palm-tree/static/image2.jpg'
    output_path1 = '/home/codespace/zany-palm-tree/static/image1.jpg'
# Save the image
   # cv2.imwrite(output_path4, gray2)

    # Load images
    img1 = cv2.imread(img1_full_path)
    img2 = cv2.imread(img2_full_path)
    cv2.imwrite(output_path1, img1)
    cv2.imwrite(output_path2, img2)
    
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path3, gray1)
    cv2.imwrite(output_path4, gray2)

    
    # Compute Structural Similarity Index (SSIM)
    ssim_index = ssim(gray1, gray2)
    
    # Define a threshold for SSIM to determine if images are similar
    threshold = 0.95
    
    # Compare SSIM with threshold
    if ssim_index > threshold:
        return "Normal Behaviour"
    else:
        return "Suspecious Activity"
def run_helper_anomaly():
 img1_path = "Screenshot (917).png"
 img2_path = "Screenshot (916).png"
 result = compare_images(img1_path, img2_path)
 print(result)
 return result
    # Implement the logic from helperAnomaly.py
    # Example: return "Anomaly detected!"

def run_helper_safe():
 img1_path = "Screenshot (916).png"
 img2_path = "Screenshot (916).png"
 result = compare_images(img1_path, img2_path)
 print(result)
 return result
    # Implement the logic from helperSafe.py
    # Example: return "Safe data!"



if __name__ == '__main__':
    app.run(debug=True)
