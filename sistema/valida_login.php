<?php

session_start();
// Lê o arquivo dados.json
$dados = json_decode(file_get_contents('dados.json'), true);

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

$login_valido = false;

// Verifica se existe usuário e senha correspondentes
foreach ($dados['users'] as $usuario) {
    if ($usuario['username'] === $username && $usuario['password'] === $password) {
        $login_valido = true;
        $_SESSION['username'] = $username;
        break;
    }
}

if ($login_valido) {
    // Login bem-sucedido
    header('Location: main.php');
    exit;
} else {
    // Login falhou
    //echo $usuario['username'].'<br>'.$usuario['password'];
    echo "<script>alert('Usuário ou senha inválidos!'); window.location.href='login.php';</script>";
    exit;
}
