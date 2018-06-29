-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Час створення: Чрв 29 2018 р., 14:22
-- Версія сервера: 5.7.16
-- Версія PHP: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База даних: `decision_support`
--

-- --------------------------------------------------------

--
-- Структура таблиці `Position`
--

CREATE TABLE `Position` (
  `idPosition` int(11) NOT NULL,
  `rank` int(11) NOT NULL,
  `title` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп даних таблиці `Position`
--

INSERT INTO `Position` (`idPosition`, `rank`, `title`) VALUES
(1, 1, 'Boss'),
(2, 2, 'Manager'),
(3, 3, 'Programmer');

-- --------------------------------------------------------

--
-- Структура таблиці `Score`
--

CREATE TABLE `Score` (
  `idScore` int(11) NOT NULL,
  `co` int(3) NOT NULL,
  `tw` int(3) NOT NULL,
  `ri` int(3) NOT NULL,
  `imp` int(3) NOT NULL,
  `pl` int(3) NOT NULL,
  `me` int(3) NOT NULL,
  `cf` int(3) NOT NULL,
  `sh` int(3) NOT NULL,
  `sp` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп даних таблиці `Score`
--

INSERT INTO `Score` (`idScore`, `co`, `tw`, `ri`, `imp`, `pl`, `me`, `cf`, `sh`, `sp`) VALUES
(1, 100, 40, 80, 80, 0, 40, 0, 50, 0),
(2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(3, 80, 100, 50, 30, 60, 20, 30, 40, 0),
(4, 30, 70, 100, 50, 90, 20, 20, 60, 0),
(5, 10, 20, 30, 100, 0, 60, 80, 0, 100),
(6, 10, 20, 80, 60, 100, 80, 40, 40, 80),
(7, 20, 40, 50, 30, 0, 100, 0, 20, 60),
(8, 30, 90, 20, 70, 0, 40, 100, 0, 40),
(9, 30, 20, 40, 40, 0, 60, 70, 100, 50),
(10, 10, 50, 40, 80, 50, 40, 70, 20, 100),
(11, 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Структура таблиці `Users`
--

CREATE TABLE `Users` (
  `idUser` int(11) NOT NULL,
  `login` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `surname` varchar(20) NOT NULL,
  `idPosition` int(11) NOT NULL,
  `idScore` int(11) NOT NULL,
  `isAdmin` int(3) NOT NULL,
  `alreadyInTeam` int(3) NOT NULL,
  `email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп даних таблиці `Users`
--

INSERT INTO `Users` (`idUser`, `login`, `password`, `name`, `surname`, `idPosition`, `idScore`, `isAdmin`, `alreadyInTeam`, `email`) VALUES
(1, 'dima', 'dima', 'Vitalik', 'Volok', 1, 1, 1, 0, ''),
(2, 'vova', 'vova', 'Ivan', 'Demkin', 3, 3, 0, 0, 'dspuzin@ukr.net'),
(3, 'misha', 'misha', 'Andrey', 'Zabrodin', 3, 4, 0, 0, 'misha@mail.ru'),
(4, 'masha', 'masha', 'Natasha', 'Klimchuk', 3, 5, 0, 0, 'masha@ukr.net'),
(5, 'Egor', 'egor', 'Maxim', 'Menshev', 3, 6, 0, 0, 'egor@ukr.net'),
(6, 'valera', 'valera', 'Fedor', 'Molchanov', 3, 7, 0, 0, 'valera@ukr.net'),
(7, 'max', 'max', 'Olga', 'Titova', 3, 8, 0, 0, 'max@uke.nwt'),
(8, 'zina', 'zina', 'Julia', 'Mirza', 2, 9, 0, 0, 'zina@ukr.net'),
(9, 'serg', 'serg', 'Vitalik', 'Birukov', 2, 10, 0, 0, 'serg@ukr.net'),
(10, 'borya', 'borya', 'Ð‘Ð¾Ñ€Ð¸Ñ', 'Ð“Ð»Ð°Ð´ÐºÐ¸Ñ…', 3, 11, 0, 0, 'borya@ukr.net');

--
-- Індекси збережених таблиць
--

--
-- Індекси таблиці `Position`
--
ALTER TABLE `Position`
  ADD PRIMARY KEY (`idPosition`);

--
-- Індекси таблиці `Score`
--
ALTER TABLE `Score`
  ADD PRIMARY KEY (`idScore`);

--
-- Індекси таблиці `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`idUser`),
  ADD UNIQUE KEY `idUser` (`idUser`);

--
-- AUTO_INCREMENT для збережених таблиць
--

--
-- AUTO_INCREMENT для таблиці `Position`
--
ALTER TABLE `Position`
  MODIFY `idPosition` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT для таблиці `Score`
--
ALTER TABLE `Score`
  MODIFY `idScore` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT для таблиці `Users`
--
ALTER TABLE `Users`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
