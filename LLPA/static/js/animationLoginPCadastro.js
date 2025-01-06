    document.addEventListener("DOMContentLoaded", function() {
        var btnSignin = document.querySelector("#signin"); // Sempre que houve um evento click em cadastrar ou logar
        var btnSignup = document.querySelector("#signup"); // Vai acionar a animação que enconde os elementos
        var body = document.querySelector("body");

        btnSignin.addEventListener("click", function () {
            body.className = "sign-in-js";
        });

        btnSignup.addEventListener("click", function () {
            body.className = "sign-up-js";
        });
    });

// Alertas de Cadastro e Login
    document.addEventListener('DOMContentLoaded', function () {
        // Temporizador para remover a mensagem após 3 segundos (3000 milissegundos)
        setTimeout(function(){
            // Seleciona a lista de mensagens e a remove
            var messages = document.querySelector('.messages');
            messages.parentNode.removeChild(messages);
        }, 3000); // Tempo em milissegundos
    });