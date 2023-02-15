# Python-Exercises
Python Exercises

Create a class Vehicle with the following attributes:

make (string)
model (string)
year (integer)
weight (float)
Also, define the following methods in the class:

description: which returns a string in the following format: "{make} {model} ({year}), weight: {weight} kg"
total_weight: which returns the sum of the weight attribute of all Vehicle objects that have been created
Create two subclasses of Vehicle: Car and Truck. The Car class should have an additional attribute num_doors (integer) and the Truck class should have an additional attribute payload_capacity (float).

Override the description method in both subclasses to include information about their respective additional attributes.

Create a list of 5 Vehicle objects, containing at least two objects of each subclass, and call the description method on each object.

Also, demonstrate the use of the total_weight method to print the total weight of all vehicles that have been created.
