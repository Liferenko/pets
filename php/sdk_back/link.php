<?php
include_once 'header.php';

header('Content-type: text/json');
$json_res = [];
foreach ($_REQUEST['link'] as $link) {
    if ($stmt = $mysqli->prepare("INSERT INTO links (entity, entity_id, quantity, product_id) VALUES (?, ?, ?, ?) ON DUPLICATE KEY UPDATE quantity = ?")) {
        /* связываем параметры со значениями */
        // @see http://php.net/manual/ru/mysqli-stmt.bind-param.php
        $stmt->bind_param('siiii', $link['from'], $link['from_id'], $link['quantity'], $link['to_id'], $link['quantity']);

        /* запускаем запрос */
        $stmt->execute();

        $json_res['query'][] = $link['from'] . '|' . $link['from_id'] . '|' . $link['quantity'] . '|' . $link['to_id'];

        /* закрываем запрос */
        $stmt->close();
    }
}

foreach ($_REQUEST['unlink'] as $link) {
    if ($stmt = $mysqli->prepare("DELETE FROM links WHERE entity = ? AND entity_id = ? AND product_id = ?")) {
        /* связываем параметры со значениями */
        // @see http://php.net/manual/ru/mysqli-stmt.bind-param.php
        $stmt->bind_param('sii', $link['from'], $link['from_id'], $link['to_id']);

        /* запускаем запрос */
        $stmt->execute();

        $json_res['query'][] = $link['from'] . '|' . $link['from_id'] . '|' . $link['to_id'];

        /* закрываем запрос */
        $stmt->close();
    }
}

echo json_encode($json_res);
