# SAFE PLUS – Women Safety Emergency Alert Web App

Safe Plus is a women’s safety web application that allows a user to quickly send an SOS alert with her **live location** to trusted emergency contacts.  
The app is built with Django and integrates browser geolocation and Twilio to send SMS alerts (and optional calls) in real time.

![image alt](https://github.com/Devadharshani13/Safe-Plus-App/blob/main/Screenshots/main%20page.jpg?raw=true)

---

## Key Features

- **Secure Authentication**
  - User **signup, login, and logout**.
  - Only authenticated users can access the SOS dashboard.

- **One-Tap SOS Button**
  - A large, clearly visible emergency button on the home page.
  - When pressed, it captures the user’s **current GPS location** (with browser permission).

- **Real-Time Location Sharing**
  - Generates a **Google Maps link** from the captured latitude and longitude.
  - Sends an alert message like:  
    `Alert! I am in danger, help me. My location is <Google Maps URL>`  

- **SMS & Call Integration (Twilio)**
  - Uses **Twilio API** to send SMS alerts to predefined emergency contacts.
  - Can optionally trigger a **phone call** to a saved emergency number.

- **User Feedback**
  - After sending the alert, the app shows a success notification:  
    `✅ Emergency alert sent successfully!`

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript (Bootstrap/custom CSS)
- **APIs & Services:**  
  - HTML5 Geolocation API  
  - Twilio Programmable SMS / Voice  
  - Google Maps (for location link)
- **Database:** SQLite (Django default, can be changed)
- **Version Control:** Git & GitHub
---

## 🧭 How It Works (User Flow)

1. **Signup / Login**

   * User creates an account or logs in to the app.

2. **Grant Location Permission**

   * Browser prompts: *“127.0.0.1 wants to know your location”* → User clicks **Allow**.

3. **Press SOS Button**

   * On pressing the SOS / shield button, JavaScript fetches the current latitude & longitude.

4. **Backend Processing**

   * Coordinates are sent to the Django backend.
   * Backend forms a **Google Maps URL**.
   * Twilio API sends an **SMS** (and optional **call**) to the registered emergency contacts.

5. **Confirmation**

   * User sees a success toast / alert:
     `Emergency alert sent successfully!`

---

## Security & Privacy

* Location is only accessed **when the user presses the SOS button** and grants permission.
* Sensitive data such as Twilio credentials should **never be committed** to Git.

  * Use environment variables / `.env` file.
* For production, configure:

  * HTTPS
  * Secure session and CSRF settings
  * Strong password policies

---

##  Future Enhancements

* Mobile app version (Android / iOS) synced with the web app
* Allow user to manage multiple emergency contacts from UI
* Live location tracking and periodic location updates
* Integration with email alerts / WhatsApp messages
* Panic gesture detection (shake phone, press power button x times, etc.)
---

> **Safe Plus** – A small step towards making the world safer for women, with the power of technology.



