-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2024 at 02:30 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `seedstory`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `CustomerID` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`CustomerID`, `Name`, `Email`, `Phone`) VALUES
(1, 'John Doe', 'johndoe1@gmail.com', '1234567890'),
(2, 'Jane Smith', 'janesmith2@yahoo.com', '2345678901'),
(3, 'Carlos Reyes', 'carlos.reyes3@gmail.com', '3456789012'),
(4, 'Mia Lee', 'mialee4@yahoo.com', '4567890123'),
(5, 'Sakura Tanaka', 'sakura.tanaka5@gmail.com', '5678901234'),
(6, 'Liam Johnson', 'liam.johnson6@yahoo.com', '6789012345'),
(7, 'Emma Wilson', 'emma.wilson7@gmail.com', '7890123456'),
(8, 'Noah Martinez', 'noah.martinez8@yahoo.com', '8901234567'),
(9, 'Olivia Brown', 'olivia.brown9@gmail.com', '9012345678'),
(10, 'Ethan Garcia', 'ethan.garcia10@yahoo.com', '1230987654'),
(11, 'Sophia Miller', 'sophia.miller11@gmail.com', '2341098765'),
(12, 'James Davis', 'james.davis12@yahoo.com', '3452109876'),
(13, 'Isabella Rodriguez', 'isabella.rodriguez13@gmail.com', '4563210987'),
(14, 'Benjamin Hernandez', 'benjamin.hernandez14@yahoo.com', '5674321098'),
(15, 'Charlotte Lee', 'charlotte.lee15@gmail.com', '6785432109'),
(16, 'Lucas Perez', 'lucas.perez16@yahoo.com', '7896543210'),
(17, 'Amelia Young', 'amelia.young17@gmail.com', '8907654321'),
(18, 'Henry Walker', 'henry.walker18@yahoo.com', '9018765432'),
(19, 'Ava King', 'ava.king19@gmail.com', '1239876543'),
(20, 'Jack Scott', 'jack.scott20@yahoo.com', '2340987654'),
(21, 'Mason Adams', 'mason.adams21@gmail.com', '3451098765'),
(22, 'Lily Green', 'lily.green22@yahoo.com', '4562109876'),
(23, 'Alexander Hall', 'alexander.hall23@gmail.com', '5673210987'),
(24, 'Grace Allen', 'grace.allen24@yahoo.com', '6784321098'),
(25, 'Sebastian Young', 'sebastian.young25@gmail.com', '7895432109'),
(26, 'Ella White', 'ella.white26@yahoo.com', '8906543210'),
(27, 'Samuel Harris', 'samuel.harris27@gmail.com', '9017654321'),
(28, 'Archer Clark', 'archer.clark28@yahoo.com', '1238765432'),
(29, 'Hazel Lewis', 'hazel.lewis29@gmail.com', '2349876543'),
(30, 'Zoe Nelson', 'zoe.nelson30@yahoo.com', '3450987654');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `OrderID` int(11) NOT NULL,
  `SeedID` int(11) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  `Subtotal` int(11) DEFAULT NULL,
  `Discount` int(11) DEFAULT NULL,
  `FinalTotal` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`OrderID`, `SeedID`, `Quantity`, `Total`, `Subtotal`, `Discount`, `FinalTotal`) VALUES
(1, NULL, 3, 1500, 1450, 50, 1400),
(2, NULL, 5, 2000, 1900, 100, 1800),
(3, NULL, 2, 1200, 1100, 100, 1000),
(4, NULL, 10, 3000, 2900, 100, 2800),
(5, NULL, 1, 500, 450, 50, 400),
(6, NULL, 7, 2100, 2000, 100, 1900),
(7, NULL, 4, 1800, 1700, 100, 1600),
(8, NULL, 8, 2400, 2300, 100, 2200),
(9, NULL, 6, 1800, 1700, 100, 1600),
(10, NULL, 3, 1500, 1450, 50, 1400),
(11, NULL, 5, 2500, 2400, 100, 2300),
(12, NULL, 2, 800, 750, 50, 700),
(13, NULL, 4, 1200, 1150, 50, 1100),
(14, NULL, 9, 2700, 2600, 100, 2500),
(15, NULL, 3, 900, 850, 50, 800),
(16, NULL, 7, 2100, 2000, 100, 1900),
(17, NULL, 6, 1800, 1700, 100, 1600),
(18, NULL, 2, 1000, 950, 50, 900),
(19, NULL, 10, 3000, 2900, 100, 2800),
(20, NULL, 4, 1200, 1150, 50, 1100),
(21, NULL, 5, 1500, 1450, 50, 1400),
(22, NULL, 1, 500, 450, 50, 400),
(23, NULL, 3, 1200, 1150, 50, 1100),
(24, NULL, 6, 1800, 1700, 100, 1600),
(25, NULL, 8, 2400, 2300, 100, 2200),
(26, NULL, 2, 1000, 950, 50, 900),
(27, NULL, 4, 1600, 1550, 50, 1500),
(28, NULL, 7, 2100, 2000, 100, 1900),
(29, NULL, 9, 2700, 2600, 100, 2500),
(30, NULL, 5, 1500, 1450, 50, 1400);

-- --------------------------------------------------------

--
-- Table structure for table `seedbreeders`
--

CREATE TABLE `seedbreeders` (
  `BreederName` varchar(50) NOT NULL,
  `Country` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `seedbreeders`
--

INSERT INTO `seedbreeders` (`BreederName`, `Country`) VALUES
('American Meadows', 'United States'),
('Blossom Hill', 'Canada'),
('Bonnie Plants', 'United States'),
('Bulb Company', 'Netherlands'),
('Burpee', 'United States'),
('David Austin', 'United Kingdom'),
('Eden Brothers', 'United States'),
('Ferry-Morse', 'United States'),
('Florida Nursery', 'India'),
('Gurney', 'China'),
('Gurneys', 'Japan'),
('Home Depot', 'South Korea'),
('Jackson & Perkins', 'Philippines'),
('Lowes', 'Indonesia'),
('Monrovia', 'Vietnam'),
('Park Seed', 'Thailand'),
('Seedsman', 'United Kingdom');

-- --------------------------------------------------------

--
-- Table structure for table `seeds`
--

CREATE TABLE `seeds` (
  `SeedID` int(11) NOT NULL,
  `SeedName` varchar(50) NOT NULL,
  `Weeks` int(11) DEFAULT NULL,
  `SeedBreeder` varchar(50) DEFAULT NULL,
  `NetWt` int(11) DEFAULT NULL,
  `Sales` int(11) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL,
  `InStock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`CustomerID`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `Phone` (`Phone`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `SeedID` (`SeedID`);

--
-- Indexes for table `seeds`
--
ALTER TABLE `seeds`
  ADD PRIMARY KEY (`SeedID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `seeds`
--
ALTER TABLE `seeds`
  MODIFY `SeedID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5644;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`SeedID`) REFERENCES `seeds` (`SeedID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
