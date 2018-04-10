<?php

include_once 'header.php';

if ($_REQUEST['install'] == 'Y') {
    $queries = ['CREATE TABLE `links` (
  `entity` varchar(20) NOT NULL,
  `entity_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  UNIQUE KEY `really_unique_key` (`entity`,`entity_id`,`product_id`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;',
'CREATE TABLE IF NOT EXISTS `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sku` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `price` bigint(20) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;',
"INSERT INTO `products` (`id`, `sku`, `name`, `price`) VALUES
(1, '1-01', 'Product 1', 124),
(2, '1-02', 'Product 2', 2256),
(3, '2-01', 'Product 3', 346),
(4, '3-01', 'Product 4', 21544);",];

    foreach ($queries as $query) {
        $mysqli->query($query);
    }

    echo 'Done';
}
