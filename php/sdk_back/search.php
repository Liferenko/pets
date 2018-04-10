<?php
include_once 'header.php';

header('Content-type: text/json');
$json_res = [];

$search = $mysqli->real_escape_string($_REQUEST['query']);

$res = $mysqli->query("SELECT * FROM products WHERE name LIKE '%{$search}%'");
while ($result = $res->fetch_array(MYSQLI_ASSOC)) {
    $json_res[] = $result;
}
echo json_encode($json_res);

include_once 'footer.php';
