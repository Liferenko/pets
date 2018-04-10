<?php
include_once 'header.php';

if (isset($_GET['new_product']) && $_GET['new_product']) {
    // @see http://php.net/manual/ru/mysqli.prepare.php
    /* создаем подготавливаемый запрос */
    if ($stmt = $mysqli->prepare("INSERT INTO products (`sku`, `name`, `price`) VALUES (?, ?, ?)")) {

        /* связываем параметры со значениями */
        // @see http://php.net/manual/ru/mysqli-stmt.bind-param.php
        $stmt->bind_param('ssi', $_GET['sku'], $_GET['name'], $_GET['price']);

        /* запускаем запрос */
        $stmt->execute();

        /* связываем переменные с результатами запроса */
        $stmt->bind_result($result);

        /* получаем значения */
        $stmt->fetch();

        echo 'Затронуто строк в БД:'.$mysqli->affected_rows;

        /* закрываем запрос */
        $stmt->close();
    }
}

include_once 'footer.php';
