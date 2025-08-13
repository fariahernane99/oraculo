<?php
session_start();
?>
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <title>Principal - Projeto Oráculo</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1>Bem-vindo ao Projeto Oráculo!</h1>
    <p>
        <?php
        if (!isset($_SESSION['username'])) {
            header('Location: login.php');
            exit;
        } else {
            echo "Usuário logado: " . htmlspecialchars($_SESSION['username']);
        }
        
        ?>
    </p>
    <p>Estamos felizes em ter você aqui. Explore e aproveite!</p>
    <button id="logoutBtn">Sair</button>
    <script>
        document.getElementById('logoutBtn').onclick = function() {
            // Redireciona para a URL que faz o logout no PHP
            window.location.href = 'login.php?logout=1';
        };
    </script>
</body>

</html>