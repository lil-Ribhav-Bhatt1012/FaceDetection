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
Certainly! For your project, you will primarily require the `OpenCV` library. Here's a breakdown of what to install and the steps to do so:

### Installations:

1. **Python**:
   - You'll need Python installed on your system. If you don't have it installed, you can download it from [Python's official website](https://www.python.org/downloads/). <br>

2. **OpenCV**:
   - A powerful library primarily aimed at real-time computer vision. <br>

3. **csv (module in Python's standard library)**:
   - For reading and writing CSV files.

### Steps to Install:

1. **Install Python**:
   - Download the appropriate version for your system from [Python's official website](https://www.python.org/downloads/). <br>
   - Install it by following the on-screen instructions. Make sure to add Python to PATH during installation.

2. **Setup a Virtual Environment (Optional but Recommended)**:
   - It's a good practice to use a virtual environment for your projects to avoid version conflicts between packages. <br>
   ```bash
   python -m venv project_env
   ```
   - Activate the virtual environment:
     - On Windows:
     ```bash
     .\project_env\Scripts\activate
     ```
     - On macOS and Linux:
     ```bash
     source project_env/bin/activate
     ```

3. **Install OpenCV**:
   - Once you have Python and (optionally) a virtual environment setup, you can install OpenCV using `pip`:
   ```bash
   pip install opencv-python
   ```

### Project Setup:

1. **Setup the File Structure**:
   - Create the directories and files as mentioned in the previously provided file structure. <br>

2. **Initialize CSV**:
   - Run the `initialize_csv.py` script once to set up your `parcels.csv` file with the appropriate headers. <br>

3. **Place Images**:
   - If you have any images you want to process using the face detection script, place them in the `images/` directory. <br>

4. **Run the Scripts**:
   - You can now run the individual scripts (`face_detection.py`, `shape_drawing.py`, `warehouse.py`) as needed for your project.

Remember to always activate your virtual environment (if you've set one up) before running the scripts or installing additional packages. This ensures that all dependencies remain within the scope of the current project.
  
**Running the Scripts**:
1. Navigate to the project directory.
2. For face detection, run `python face_detection.py`.
3. For drawing shapes, execute `python shape_drawing.py`.
4. To manage parcels in the warehouse system, use `python warehouse.py`.
