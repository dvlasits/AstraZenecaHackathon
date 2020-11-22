from Person import Person
import SSH

SSH.OnlineInterface().putData(
    [Person("Daniel", "123", {"Bike": 100, "Cups": 20, "Heating": 40, "Trees":0}),
     Person("Hari", "456", {"Bike": 20, "Cups": 0, "Heating": 10, "Trees":0}),
     Person("Kirpal", "190", {"Bike": 50, "Cups": 17, "Heating": 60,"Trees":0}),
     Person("Tommy", "45", {"Bike": 3, "Cups": 5, "Heating": 0, "Trees":0},True)])