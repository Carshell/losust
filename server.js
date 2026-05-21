const http = require('http');

// Налаштування хоста та порту
const hostname = '0.0.0.0'; // 0.0.0.0 дозволяє підключатися з будь-якого IP
const port = 3000;          // Ти можеш змінити порт на будь-який інший (наприклад, 80)

// HTML-код сторінки з мінімалістичним дизайном (CSS)
const htmlContent = `
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Панель керування Locust</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            display: flex;
            gap: 30px;
        }
        .card {
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            text-align: center;
            width: 250px;
        }
        h2 {
            margin-top: 0;
            color: #333;
            text-transform: capitalize;
        }
        .btn {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 24px;
            background-color: #28a745;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        .btn:hover {
            background-color: #218838;
        }
        .btn-blue {
            background-color: #007bff;
        }
        .btn-blue:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h2>Authorize</h2>
            <p>Навантажувальний тест авторизації</p>
            <a href="http://57.129.100.77:8089/" class="btn" target="_blank">Перейти до Locust</a>
        </div>

        <div class="card">
            <h2>Specialists</h2>
            <p>Навантажувальний тест спеціалістів</p>
            <a href="http://57.129.100.77:8090/" class="btn btn-blue" target="_blank">Перейти до Locust</a>
        </div>
    </div>
</body>
</html>
`;

// Створення сервера
const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.end(htmlContent);
});

// Запуск сервера
server.listen(port, hostname, () => {
    console.log(`Сервер запущено. Відкрий у браузері: http://твій_айпі:${port}/`);
});