CREATE TABLE Drivers (
  DriverID NUMBER PRIMARY KEY,
  DriverName VARCHAR2(50) NOT NULL,
  LicenseNumber VARCHAR2(50) NOT NULL,
  HireDate DATE,
  ContactPhone VARCHAR2(15),
  Email VARCHAR2(100)
);

CREATE TABLE Taxis (
  TaxiID NUMBER PRIMARY KEY,
  LicensePlate VARCHAR2(20) NOT NULL,
  Model VARCHAR2(50),
  Capacity NUMBER,
  Availability VARCHAR2(10) NOT NULL CHECK (Availability IN ('Available', 'Unavailable'))
);

CREATE TABLE Rides (
  RideID NUMBER PRIMARY KEY,
  DriverID NUMBER,
  TaxiID NUMBER,
  PassengerID NUMBER,
  PickupLocation VARCHAR2(100),
  DropoffLocation VARCHAR2(100),
  PickupTime TIMESTAMP,
  DropoffTime TIMESTAMP,
  Fare NUMBER,
  CONSTRAINT fk_ride_driver FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID),
  CONSTRAINT fk_ride_taxi FOREIGN KEY (TaxiID) REFERENCES Taxis(TaxiID),
  CONSTRAINT fk_ride_passenger FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID)
);

CREATE TABLE Passengers (
  PassengerID NUMBER PRIMARY KEY,
  PassengerName VARCHAR2(50) NOT NULL,
  Email VARCHAR2(100),
  ContactPhone VARCHAR2(15),
  Country VARCHAR2(50)
);

CREATE TABLE Driver_Schedules (
  ScheduleID NUMBER PRIMARY KEY,
  DriverID NUMBER,
  ShiftStartTime TIMESTAMP,
  ShiftEndTime TIMESTAMP,
  CONSTRAINT fk_schedule_driver FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Payments (
  PaymentID NUMBER PRIMARY KEY,
  RideID NUMBER,
  Amount NUMBER NOT NULL,
  PaymentTime TIMESTAMP,
  PaymentMethod VARCHAR2(20) CHECK (PaymentMethod IN ('Cash', 'Card', 'Online')),
  CONSTRAINT fk_payment_ride FOREIGN KEY (RideID) REFERENCES Rides(RideID)
);


-- Insert sample data
INSERT INTO Drivers (DriverID, DriverName, LicenseNumber, HireDate, ContactPhone, Email)
VALUES (1, 'Feller Smith', 'ABC12345', TO_DATE('2021-06-15', 'YYYY-MM-DD'), '+994-55-555-5555', 'johndoe@google.com');

INSERT INTO Taxis (TaxiID, LicensePlate, Model, Capacity, Availability)
VALUES (1, 'XYZ-1234', 'Toyota Prius', 4, 'Available');

INSERT INTO Passengers (PassengerID, PassengerName, Email, ContactPhone, Country)
VALUES (1, 'Alexksandr Bach', 'janesmith@gmail.com', '+994-50-555-1234', 'USA');

INSERT INTO Rides (RideID, DriverID, TaxiID, PassengerID, PickupLocation, DropoffLocation, PickupTime, DropoffTime, Fare)
VALUES (1, 1, 1, 1, '123 Main St', '456 Elm St', TIMESTAMP '2023-05-01 08:30:00', TIMESTAMP '2023-05-01 08:50:00', 25.00);

INSERT INTO Driver_Schedules (ScheduleID, DriverID, ShiftStartTime, ShiftEndTime)
VALUES (1, 1, TIMESTAMP '2023-05-01 08:00:00', TIMESTAMP '2023-05-01 16:00:00');

INSERT INTO Payments (PaymentID, RideID, Amount, PaymentTime, PaymentMethod)
VALUES (1, 1, 25.00, TIMESTAMP '2023-05-01 08:55:00', 'Card');

-- Select data to verify
SELECT * FROM Drivers;
SELECT * FROM Taxis;
SELECT * FROM Passengers;
SELECT * FROM Rides;
SELECT * FROM Driver_Schedules;
SELECT * FROM Payments;
