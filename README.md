# Restaurant Reservation System - 演算法期中專案

## Introduction
This project is a **restaurant reservation system** built using **Flask** for the backend and **HTML/CSS/JavaScript** for the frontend. The system implements basic algorithmic functions to enable users to:
- Add reservations
- Search for reservations (by name or phone)
- List all reservations

The project demonstrates simple algorithm applications in data management and retrieval.

---

## Features
### 1. Add Reservations  
Users can input customer names and phone numbers to save reservation data.

### 2. Search Reservations  
- **Search by Name**: Users can search reservations by the customer's name.  
- **Search by Phone**: Users can search reservations by the customer's phone number.

### 3. List All Reservations  
Displays all reservations stored in the system.

---

## System Architecture

### Backend
- **Framework**: Flask
- **API Endpoints**:
  - `/add_reservation`: Adds a new reservation.
  - `/search_reservation`: Searches reservations by name.
  - `/search_by_phone`: Searches reservations by phone number.
  - `/list_reservations`: Lists all reservations.

### Frontend
- **HTML**: Structures the page content.
- **CSS**: Provides styling with custom styles and **Bootstrap** for responsive design.
- **JavaScript**: Uses **Fetch API** to interact with the backend.

### Algorithms
- **Linear Search**: Used for searching reservations by name or phone.
- **Data Management**: Implements basic Python data structures (e.g., lists or dictionaries) for storing reservations.

---

## Usage Instructions

### 1. Environment Setup
Install the required packages by running:
```bash
pip install -r requirements.txt
```
(Currently, only Flask is required.)

### 2. Start the Server
Run the following command to start the server:
```bash
python app.py
```
The server will be hosted at:

```arduino
http://127.0.0.1:5000
```
### 3. Access the Frontend
Open `index.html` in your browser to interact with the system.

---

## File Structure

- **app.py**: Flask backend application that handles API requests.
- **reservation_system.py**: Core Python script containing reservation logic.
- **requirements.txt**: File listing Python dependencies required for the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.

### Directories:
- **static**: Contains static assets for the frontend.
  - **script.js**: JavaScript file handling user actions and API calls.
  - **style.css**: Custom styles for the frontend design.
- **templates**: Contains HTML templates for the frontend.
  - **index.html**: Main user interface for the reservation system.

---

## Interface Preview

Below is a preview of the system interface:

![image](https://github.com/user-attachments/assets/b7b544cd-6c3f-479f-965a-508cb41995ed)

---


## Contributors

- **Name**: 蔣哿樂 (CHIANG, KE-LE)  
- **Student ID**: 111113201  
- **Project Title**: 餐廳訂位系統 (Restaurant Reservation System)





