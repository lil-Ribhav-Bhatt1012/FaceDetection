# Face Detection Project

This project focuses on image processing and computer programming, implementing face detection using Haar cascades and OpenCV. Additionally, the project involves drawing geometric shapes using OpenCV and a warehouse parcel management system.

## Features

1. **Face Detection**:
   - Uses OpenCV and Haar cascades for detecting faces in images.

2. **Drawing Geometric Shapes**:
   - Utilizes OpenCV to draw basic geometric shapes such as:
     - Lines <br>
     - Rectangles <br>
     - Ellipses <br>
     - Circles

3. **Warehouse Parcel Management**:
   - A Python class representation for managing basic warehouse parcel details. <br>
   - Features include:
     - Storing parcel number, weight, and category. <br>
     - Saving and displaying parcel details in a tabular format and storing them in a CSV file. <br>

## Directory Structure

- `data`: Contains sample images and CSV files. <br>
- `utils`: Houses utility scripts including initial setup and shape drawing functions. <br>
- `face_detection.py`: Main script for the face detection feature. <br>
- `warehouse.py`: Script for the warehouse parcel management system.

## Setup and Usage

**Prerequisites**:
Sure, here's a concise version in bullet points:

- **Install Python**:
  - Windows: Download from [python.org](https://www.python.org/downloads/windows/). <br>
  - macOS: `brew install python` or use pre-installed version. <br>
  - Linux: `sudo apt-get install python3`
  
- **Set Up Virtual Environment**:
  - `pip install virtualenv` <br>
  - `python -m venv env` <br>
  - Activate: Windows (`.\env\Scripts\activate`) | macOS/Linux (`source env/bin/activate`)
  
- **Install OpenCV**:
  - `pip install opencv-python` <br>
  - For extra features: `pip install opencv-python-contrib`

- **Update Libraries**: `pip install --upgrade library-name`
  
**Running the Scripts**:
1. Navigate to the project directory.
2. For face detection, run `python face_detection.py`.
3. For drawing shapes, execute `python shape_drawing.py`.
4. To manage parcels in the warehouse system, use `python warehouse.py`.
