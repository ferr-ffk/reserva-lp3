CREATE DATABASE IF NOT EXISTS `teste_python` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `teste_python`;

CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int(11) primary key NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL,
  `senha` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `admin` boolean NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `sala` (
  `codigo_sala` int(11) primary key NOT NULL auto_increment,
  `capacidade` int(11) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `ativa` boolean NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `reserva` (
  `codigo_reserva` int(11) primary key NOT NULL auto_increment,
  `data_hora_inicio` datetime NOT NULL,
  `data_hora_fim` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `reserva`
ADD COLUMN `id_usuario` int(11) not null,
ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuario`(`id_usuario`);

ALTER TABLE `reserva`
ADD COLUMN `codigo_sala` int(11) not null,
ADD FOREIGN KEY (`codigo_sala`) REFERENCES `sala`(`codigo_sala`);
