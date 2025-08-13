<?php

session_start();
if (isset($_GET['logout'])) {
    // Limpa todas as variáveis da sessão
    $_SESSION = array();
    session_destroy();
    header('Location: login.php');
    exit;
}
if (isset($_SESSION['username'])) {
    header('Location: main.php');
    exit;
}

?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Login - Projeto Oráculo</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="login-container">
        <h2>Login</h2>
        <form action="valida_login.php" method="POST">
            <label for="username">Usuário</label>
            <input type="text" id="username" name="username" required>

            <label for="password">Senha</label>
            <input type="password" id="password" name="password" required>

            <button type="submit">Entrar</button>
        </form>
    </div>
</body>

</html>