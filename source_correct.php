<?php

if (isset($_GET['Submit'])) {
    // Получаем входные данные
    $id = $_GET['id'];

    // Подготовка SQL-запроса
    $stmt = $conn->prepare("SELECT first_name, last_name FROM users WHERE user_id = ?");
    
    // Привязываем параметры
    $stmt->bind_param("i", $id); // Предполагаем, что user_id - это целое число

    // Выполняем запрос
    $stmt->execute();

    // Получаем результаты
    $result = $stmt->get_result();
    $num = $result->num_rows;

    if ($num > 0) {
        // Обратная связь для конечного пользователя
        echo '<pre>User ID exists in the database.</pre>';
    } else {
        // Пользователь не найден, поэтому страница не найдена
        header($_SERVER['SERVER_PROTOCOL'] . ' 404 Not Found');

        // Обратная связь для конечного пользователя
        echo '<pre>User ID is MISSING from the database.</pre>';
    }

}

?>

