CREATE DATABASE IF NOT EXISTS app;
use app;

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL
);

INSERT INTO `users` (`id`, `username`, `password`) VALUES (1, 'admin', 'admin'), (2, 'user', 'user');

ALTER TABLE `users` ADD PRIMARY KEY (`id`);