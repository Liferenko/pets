<?php
include_once 'header.php';

header('Content-type: text/json');
$json_res = [];
if (isset($_GET['products']) && $_GET['products']) {
    // @see http://php.net/manual/ru/mysqli.prepare.php
    /* создаем подготавливаемый запрос */
    if ($stmt = $mysqli->prepare("SELECT id, name, price, sku, quantity FROM products INNER JOIN links ON products.id = links.product_id WHERE links.entity_id = ? AND links.entity = ?")) {
        /* связываем параметры со значениями */
        // @see http://php.net/manual/ru/mysqli-stmt.bind-param.php
        $stmt->bind_param('is', $_GET['entity_id'], $_GET['type']);

        /* запускаем запрос */
        $stmt->execute();

        $stmt->bind_result($id, $name, $price, $sku, $quantity);

        while ($stmt->fetch())
        {
            $json_res[] = [
                'id' => (int)$id,
                'name' => $name,
                'price' => (int)$price,
                'sku' => $sku,
                'quantity' => (int)$quantity
            ];
        }

        /* закрываем запрос */
        $stmt->close();
    }

} else {
    $res = $mysqli->query("SELECT * FROM products LIMIT 50");
    while ($result = $res->fetch_array(MYSQLI_ASSOC)) {
        $json_res[] = $result;
    }
}
echo json_encode($json_res);

include_once 'footer.php';
