import paramiko
import smtplib
from email.mime.text import MIMEText
import sqlite3
import requests
from bs4 import BeautifulSoup
import concurrent.futures

# Email Alerts
class EmailAlerts:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to_email

        server = smtplib.SMTP_SSL(self.smtp_server, self.port)
        server.login(self.username, self.password)
        server.sendmail(self.username, to_email, msg.as_string())
        server.quit()

# Patient Management
class Patient:
    def __init__(self, patient_id, name, email, age, medical_history=None):
        self.patient_id = patient_id
        self.name = name
        self.email = email
        self.age = age
        self.medical_history = medical_history if medical_history else []

    def update_medical_history(self, record):
        self.medical_history.append(record)
        print(f"Updated medical history for {self.name}.")

    def send_email_alert(self, subject, body):
        if self.email:
            email_alerts = EmailAlerts("smtp.gmail.com", 465, "ishaghule@gmail.com", "kaqe akej rpvx ihjy")
            email_alerts.send_email(self.email, subject, body)

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print("Medical History:")
        for record in self.medical_history:
            print(record)

class PatientManagementSystem:
    def __init__(self):
        self.patients = {}

    def register_patient(self, patient_id, name, email, age):
        if patient_id in self.patients:
            print("Patient already exists.")
        else:
            self.patients[patient_id] = Patient(patient_id, name, email, age)
            print(f"Patient {name} registered with ID {patient_id}.")

    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

# Network Communication
class NetworkDevice:
    def __init__(self, ip_address, device_type):
        self.ip_address = ip_address
        self.device_type = device_type

    def communicate(self):
        print(f"Communicating with {self.device_type} at {self.ip_address}")

    def send_data(self, data):
        print(f"Sending data to {self.device_type}: {data}")

    def receive_data(self):
        print(f"Receiving data from {self.device_type}")

def main():
    # Patient Management
    pms = PatientManagementSystem()

    # Register patients
    pms.register_patient("001", "Isha Ghule", "ishaghule@gmail.com", 30)
    pms.register_patient("002", "Girish Chaudhari", "girishchaudhari251@gmail.com", 25)

    # Accessing patient information
    patient = pms.get_patient("001")
    if patient:
        patient.update_medical_history("Diagnosed with hypertension.")
        patient.send_email_alert("Medical Alert", "Your recent test results are available.")
        patient.display_info()

    patient2 = pms.get_patient("002")
    if patient2:
        patient2.update_medical_history("Annual check-up completed.")
        patient2.display_info()

    # Network Communication
    router = NetworkDevice("192.168.1.1", "Router")
    router.communicate()
    router.send_data("Hello, Router!")
    router.receive_data()

if __name__ == "__main__":
    main()
