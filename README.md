This project shows a solution to the traveling salesman problem. 
Using the example of a university parcel service, the objective is to find an efficient way to use 3 trucks and 2 drivers to deliver 40 packages with a network of 27 locations.
The solution must deliver all packages and keep mileage under 140 miles and consider all package constraints.
The program uses a modification of the nearest neighbor algorithm to determine the best route to deliver packages, given different package constraints.
Package constraints include different package delivery time deadlines and updating dropoff locations at different times. 
The program keeps track of the package status at all points in time to ensure proper tracking (ie heading to depot, loaded, in route, delivered).
Application uses a simple menu to allow user to view the status of any package at any time and truck delivery details.



Title: Customer Appointment System

Purpose: This is an application that allows a user to add, edit, and delete appointments and customers. The application accepts login credentials and displays appointments scheduled by week or month. Additionally, the application has three reports: appointments by type, contact schedule, and total customers.

Author: Michael Lee
Contact Information: m.brady.lee@gmail.com
Student Application Version: V1
Date: 3/12/24

IDE: Intellij IDEA 2023.3.3 (Community Edition). JDK-11.0.22  JavaFX-SDK-21.0.2

Directions: To run the program, you must first log in. There is a log in screen which accepts and correct username and password combo. Once logged in, the application will alert you of any upcoming appointments starting in the next 15 minutes, including the appointment ID and start date/time. If no appointment is upcoming, it will also alert you of this fact. 

After clicking past this alert, the user is taken to the appointment details view, which shows all of the appointments filtered by week, by month, or the user can view all of the appointments. The Appointment Details view displays the following information for each appointment in a table view: Appointment ID, Title, Description, Location, Contact ID, Type, Start Date/Time, End Date/Time, Customer ID, and User ID. A user can add, edit or delete any appointments. The application allows the user to add and edit appointments using the local time zone and will automatically convert it to ET to make sure the appointment is scheduled during business hours (8am - 10pm ET).

The Add and Edit Appointment views capture the following information: 
Appointment ID (autopopulated), Title, Description, Location, Contact, Type, Start Date, Start Time (in military time), End Date, End Time (in military time), Customer, and User. Any of this information can be modified, except for the appointment ID. There are checks in place to ensure that appointments cannot overlap eachother.

From the Appointment Details view, the user can access both the Customer Details view or the Reports View by clicking on the respective button in the bottom righthand side of the Appointment Details view. 

The Customer Details view displays the following information for each customer in a table view: Customer ID, Name, Address, Postal Code, Phone, Division ID. A user can add, edit, or delete any customers from this view, however, the user must first delete all associated appointments before they are allowed to delete a customer, due to the customer ID foreign key constraints of the database. 

From the Customer Details view, the user can access both the Appointment Details view or the Reports View by clicking on the respective button in the bottom righthand side of the Customer Details view. 

The Add and Edit Customer views capture the following information: Customer ID (autopopulated), Name, Country, Address, Province/State, Postal Code, and Phone Number. Any of this information can be modified, except for the customer ID.

The Reports view allows the user to access three distinct reports: Total Appointments By Type, Contact Schedule, and Total Customers. The Total Appointments By Type report shows how many appointments are in the database based on the four appointment types: Announcement, Brainstorm Session, Customer Engagement, and Review. The Contact Schedule report allows the user to see the following information after selecting a contact from the combo box: Appointment ID, Title, Type, Description, Start Date/Time, End Date/Time, and Customer ID. The Total Customers report shows the total number of customers in the database at that moment.

From the Reports view, the user can access both the Appointment Details view or the Customer Details View by clicking on the respective button in the bottom righthand side of the Reports view. 

Description of Additional Report: The additional report I ran will show the total customers that are in the database at this moment.

MySQL Connector Driver Version Number: mysql-connector-java-8.0.28
