document.addEventListener('DOMContentLoaded', function() {
    // Função para formatar a entrada de moeda
    function formatCurrency(input) {
        let value = input.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
        let formattedValue = (parseFloat(value) / 100).toFixed(2) // Converte para float e formata com 2 casas decimais
                            .replace('.', ',') // Substitui ponto por vírgula
                            .replace(/\B(?=(\d{3})+(?!\d))/g, '.'); // Adiciona pontos como separadores de milhar

        input.value = formattedValue;
    }

    let selectors = '#emprestimoTot, #comissaoCorretor, #comissaoLLPromotora, #idprecoSER, #idprecoSERATU, #idprecoDES, #idprecoDESATU, #emprestimoTotATU, #comissaoCorretorATU, #comissaoLLPromotoraATU';

    // Aplica a formatação ao digitar
    document.querySelectorAll(selectors).forEach(input => {
        input.addEventListener('input', function(event) {
            formatCurrency(event.target);
        });

        // Verifica o foco no campo para garantir que ele não fique vazio
        input.addEventListener('focus', function(event) {
            if (event.target.value === "") {
                event.target.value = "0,00";
            }
        });
    });

    function calcularComissoesCORR() {
        // Pega os valores dos inputs e converte para o formato numérico
        let emprestimoTot = parseFloat(document.getElementById('emprestimoTot').value.replace(/\./g, '').replace(',', '.')) || 0;
        let comissaoCorretor = parseFloat(document.getElementById('comissaoCorretor').value.replace(/\./g, '').replace(',', '.')) || 0;

        let comissaoC;
        // Verifica se a comissão do corretor é uma porcentagem
        if (comissaoCorretor >= 0 && comissaoCorretor <= 1) {
            comissaoC = emprestimoTot * comissaoCorretor;
        }
        // Verifica se o número tem um zero antes do decimal e está entre 0 e 100
        else if (/^0\.\d+$/.test(comissaoCorretor) || (comissaoCorretor >= 0 && comissaoCorretor <= 100)) {
            comissaoC = emprestimoTot * (comissaoCorretor / 100);
        } else {
            console.log("Valor de comissão inválido.");
            return;
        }

        // Formata o valor da comissão no padrão brasileiro
        document.getElementById('comissaoCorretor').value = comissaoC.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }

    // Torna a função acessível globalmente
    window.calcularComissoesCORR = calcularComissoesCORR;


    function calcularComissoesCORRATU() {
        // Pega os valores dos inputs e converte para o formato numérico
        let emprestimoTotATU = parseFloat(document.getElementById('emprestimoTotATU').value.replace(/\./g, '').replace(',', '.')) || 0;
        let comissaoCorretorATU = parseFloat(document.getElementById('comissaoCorretorATU').value.replace(/\./g, '').replace(',', '.')) || 0;

        let comissaoCATU;
        // Verifica se a comissão do corretor é uma porcentagem
        if (comissaoCorretorATU >= 0 && comissaoCorretorATU <= 1) {
            comissaoCATU = emprestimoTotATU * comissaoCorretorATU;
        }
        // Verifica se o número tem um zero antes do decimal e está entre 0 e 100
        else if (/^0\.\d+$/.test(comissaoCorretorATU) || (comissaoCorretorATU >= 0 && comissaoCorretorATU <= 100)) {
            comissaoCATU = emprestimoTotATU * (comissaoCorretorATU / 100);
        } else {
            console.log("Valor de comissão inválido.");
            return;
        }

        // Formata o valor da comissão no padrão brasileiro
        document.getElementById('comissaoCorretorATU').value = comissaoCATU.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }

    // Torna a função acessível globalmente
    window.calcularComissoesCORRATU = calcularComissoesCORRATU;


    function calcularComissoesLLPRO() {
        // Pega os valores dos inputs e converte para o formato numérico
        let emprestimoTot = parseFloat(document.getElementById('emprestimoTot').value.replace(/\./g, '').replace(',', '.')) || 0;
        let comissaoLLPromotora = parseFloat(document.getElementById('comissaoLLPromotora').value.replace(/\./g, '').replace(',', '.')) || 0;

        let comissaoLLP;
        // Verifica se a comissão da promotora de empréstimo é uma porcentagem
        if (comissaoLLPromotora >= 0 && comissaoLLPromotora <= 1) {
            comissaoLLP = emprestimoTot * comissaoLLPromotora;
        }
        // Verifica se o número tem um zero antes do decimal e está entre 0 e 100
        else if (/^0\.\d+$/.test(comissaoLLPromotora) || (comissaoLLPromotora >= 0 && comissaoLLPromotora <= 100)) {
            comissaoLLP = emprestimoTot * (comissaoLLPromotora / 100);
        } else {
            console.log("Valor de comissão inválido.");
            return;
        }

        // Formata o valor da comissão no padrão brasileiro
        document.getElementById('comissaoLLPromotora').value = comissaoLLP.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }

    // Torna a função acessível globalmente
    window.calcularComissoesLLPRO = calcularComissoesLLPRO;

    function calcularComissoesLLPROATU() {
        // Pega os valores dos inputs e converte para o formato numérico
        let emprestimoTotATU = parseFloat(document.getElementById('emprestimoTotATU').value.replace(/\./g, '').replace(',', '.')) || 0;
        let comissaoLLPromotoraATU = parseFloat(document.getElementById('comissaoLLPromotoraATU').value.replace(/\./g, '').replace(',', '.')) || 0;

        let comissaoLLPATU;
        // Verifica se a comissão da promotora de empréstimo é uma porcentagem
        if (comissaoLLPromotoraATU >= 0 && comissaoLLPromotoraATU <= 1) {
            comissaoLLPATU = emprestimoTotATU * comissaoLLPromotoraATU;
        }
        // Verifica se o número tem um zero antes do decimal e está entre 0 e 100
        else if (/^0\.\d+$/.test(comissaoLLPromotoraATU) || (comissaoLLPromotoraATU >= 0 && comissaoLLPromotoraATU <= 100)) {
            comissaoLLPATU = emprestimoTotATU * (comissaoLLPromotoraATU / 100);
        } else {
            console.log("Valor de comissão inválido.");
            return;
        }

        // Formata o valor da comissão no padrão brasileiro
        document.getElementById('comissaoLLPromotoraATU').value = comissaoLLPATU.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }

    // Torna a função acessível globalmente
    window.calcularComissoesLLPROATU = calcularComissoesLLPROATU;
});