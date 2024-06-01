This project shows a solution to the traveling salesman problem. 
Using the example of a university parcel service, the objective is to find an efficient way to use 3 trucks and 2 drivers to deliver 40 packages with a network of 27 locations.
The solution must deliver all packages and keep mileage under 140 miles and consider all package constraints.
The program uses a modification of the nearest neighbor algorithm to determine the best route to deliver packages, given different package constraints.
Package constraints include different package delivery time deadlines and updating dropoff locations at different times. 
The program keeps track of the package status at all points in time to ensure proper tracking (ie heading to depot, loaded, in route, delivered).
Application uses a simple menu to allow user to view the status of any package at any time and truck delivery details.
