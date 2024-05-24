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
VALUES (1, 'Feller Aron', 'ABC12345', TO_DATE('2021-06-15', 'YYYY-MM-DD'), '+994-55-555-5555', 'johndoe@google.com');
VALUES (2, 'Murad Əliyev', 'XYZ67890', TO_DATE('2020-08-23', 'YYYY-MM-DD'), '+994-50-123-4567', 'murad.aliyev@example.com');
VALUES (3, 'Nigar Məmmədova', 'ABC56789', TO_DATE('2019-02-12', 'YYYY-MM-DD'), '+994-51-234-5678', 'nigar.mammadova@example.com');
VALUES (4, 'Rəşad Quliyev', 'DEF34567', TO_DATE('2018-11-05', 'YYYY-MM-DD'), '+994-55-345-6789', 'reshad.guliyev@example.com');
VALUES (5, 'Günay Hüseynova', 'JKL12345', TO_DATE('2022-07-19', 'YYYY-MM-DD'), '+994-77-456-7890', 'gunay.huseynova@example.com');

INSERT INTO Taxis (TaxiID, LicensePlate, Model, Capacity, Availability)
VALUES (1, 'XYZ-1234', 'Toyota Prius', 4, 'Available');
VALUES (2, '10-AA-567', 'Hyundai Elantra', 4, 'Available');
VALUES (3, '99-BB-890', 'Kia Optima', 4, 'Available');
VALUES (4, '90-CC-234', 'Mercedes-Benz E-Class', 4, 'Unavailable');
VALUES (5, '77-DD-456', 'BMW 5 Series', 4, 'Available');

INSERT INTO Passengers (PassengerID, PassengerName, Email, ContactPhone, Country)
VALUES (1, 'Alexksandr Bach', 'janesmith@gmail.com', '+994-50-555-1234', 'USA');
VALUES (2, 'Elvin Qasimov', 'elvin.qasimov@example.com', '+994-50-111-2233', 'Azerbaijan');
VALUES (3, 'Aysel Məmmədova', 'aysel.mammadova@example.com', '+994-51-222-3344', 'Azerbaijan');
VALUES (4, 'Kamran Həsənov', 'kamran.hesenov@example.com', '+994-55-333-4455', 'Azerbaijan');
VALUES (5, 'Ləman Hüseynova', 'leman.huseynova@example.com', '+994-77-444-5566', 'Azerbaijan');

INSERT INTO Rides (RideID, DriverID, TaxiID, PassengerID, PickupLocation, DropoffLocation, PickupTime, DropoffTime, Fare)
VALUES (1, 1, 1, 1, '123 Main St', '456 Elm St', TIMESTAMP '2023-05-01 08:30:00', TIMESTAMP '2023-05-01 08:50:00', 25.00);
VALUES (2, 2, 2, 2, '789 Oak St', '101 Pine St', TIMESTAMP '2023-05-02 09:00:00', TIMESTAMP '2023-05-02 09:25:00', 30.00);
VALUES (3, 3, 3, 3, '234 Maple St', '567 Birch St', TIMESTAMP '2023-05-03 10:15:00', TIMESTAMP '2023-05-03 10:35:00', 20.00);
VALUES (4, 4, 4, 4, '345 Cedar St', '678 Willow St', TIMESTAMP '2023-05-04 11:45:00', TIMESTAMP '2023-05-04 12:10:00', 35.00);
VALUES (5, 5, 5, 5, '456 Walnut St', '789 Spruce St', TIMESTAMP '2023-05-05 07:30:00', TIMESTAMP '2023-05-05 07:50:00', 25.00);

INSERT INTO Driver_Schedules (ScheduleID, DriverID, ShiftStartTime, ShiftEndTime)
VALUES (1, 1, TIMESTAMP '2023-05-01 08:00:00', TIMESTAMP '2023-05-01 16:00:00');
VALUES (2, 2, TIMESTAMP '2023-05-02 07:00:00', TIMESTAMP '2023-05-02 15:00:00');
VALUES (3, 3, TIMESTAMP '2023-05-03 09:00:00', TIMESTAMP '2023-05-03 17:00:00');
VALUES (4, 4, TIMESTAMP '2023-05-04 10:00:00', TIMESTAMP '2023-05-04 18:00:00');
VALUES (5, 5, TIMESTAMP '2023-05-05 06:00:00', TIMESTAMP '2023-05-05 14:00:00');

INSERT INTO Payments (PaymentID, RideID, Amount, PaymentTime, PaymentMethod)
VALUES (1, 1, 25.00, TIMESTAMP '2023-05-01 08:55:00', 'Card');
VALUES (2, 2, 30.00, TIMESTAMP '2023-05-02 09:30:00', 'Cash');
VALUES (3, 3, 20.00, TIMESTAMP '2023-05-03 10:40:00', 'Card');
VALUES (4, 4, 35.00, TIMESTAMP '2023-05-04 12:15:00', 'Card');
VALUES (5, 5, 25.00, TIMESTAMP '2023-05-05 07:55:00', 'Cash');


-- Select data to verify
SELECT * FROM Drivers;
SELECT * FROM Taxis;
SELECT * FROM Passengers;
SELECT * FROM Rides;
SELECT * FROM Driver_Schedules;
SELECT * FROM Payments;
