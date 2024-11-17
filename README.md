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
