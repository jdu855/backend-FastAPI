-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla api.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `marca` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `modelo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `color` varchar(50) NOT NULL,
  `fecha_de_compra` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla api.users: ~3 rows (aproximadamente)
DELETE FROM `users`;
INSERT INTO `users` (`id`, `marca`, `modelo`, `color`, `fecha_de_compra`) VALUES
	(20, 'toyota', 'hilux', 'plata', '2023/10/12'),
	(21, 'Toyota', 'Corolla', 'Rojo', '2023-05-15'),
	(22, 'Ford', 'Mustang', 'Negro', '2023-06-20'),
	(23, 'Chevrolet', 'Camaro', 'Azul', '2023-07-25'),
	(24, 'Honda', 'Civic', 'Blanco', '2023-08-30'),
	(25, 'Nissan', 'Altima', 'Gris', '2023-09-10'),
	(26, 'Hyundai', 'Elantra', 'Verde', '2023-03-12'),
	(27, 'Kia', 'Sportage', 'Azul', '2023-04-17'),
	(28, 'Mazda', 'CX-5', 'Naranja', '2023-01-22'),
	(29, 'Subaru', 'Outback', 'Amarillo', '2023-02-28'),
	(30, 'Volkswagen', 'Golf', 'Negro', '2023-07-05'),
	(31, 'BMW', 'Serie 3', 'Blanco', '2023-08-12'),
	(32, 'Audi', 'A4', 'Plata', '2023-06-15'),
	(33, 'Mercedes-Benz', 'C-Class', 'Rojo', '2023-05-01'),
	(34, 'Porsche', '911', 'Gris', '2023-04-25'),
	(35, 'Land Rover', 'Range Rover', 'Verde', '2023-03-10'),
	(36, 'Lexus', 'RX', 'Negro', '2023-02-14'),
	(37, 'Fiat', '500', 'Rojo', '2023-01-30'),
	(38, 'Chrysler', '300', 'Blanco', '2023-07-18'),
	(39, 'Dodge', 'Challenger', 'Azul', '2023-08-09'),
	(40, 'Jeep', 'Wrangler', 'Naranja', '2023-09-22');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
