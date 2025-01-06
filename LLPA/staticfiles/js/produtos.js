let names = [
  "Novo",
  "Refinanciamento",
  "Cartão",
  "Saque Complementar",
  "Portabilidade",
  "Saque FGTS"
];

document.addEventListener("DOMContentLoaded", (event) => {

  //Ordena os nomes em ordem crescente
  let sortedNames = names.sort();

  // referência
  let input = document.getElementById("inputproduct");
  if (input) {
    // Executar função no evento keyup
    input.addEventListener("keyup", (e) => {
      // loop através do array acima
      // Inicialmente remover todos os elementos (assim, se o usuário apagar uma letra ou adicionar uma nova letra, limpar saídas anteriores)
      removeElements();
      let count = 0; // Contador para limitar as sugestões
      for (let i of sortedNames) {
        // converter entrada para minúsculas e comparar com cada string
        if (
          i.toLowerCase().startsWith(input.value.toLowerCase()) &&
          input.value != ""
        ) {
          // criar elemento li
          let listItem = document.createElement("li");
          // Um nome de classe comum
          listItem.classList.add("list-items");
          listItem.style.cursor = "pointer";
          listItem.setAttribute("onclick", "displayNames('" + i + "')");
          // Exibir a parte correspondente em negrito
          let word = "<b>" + i.substr(0, input.value.length) + "</b>";
          word += i.substr(input.value.length);
          // exibir o valor no array
          listItem.innerHTML = word;
          document.querySelector(".list").appendChild(listItem);

          count++;
          if (count >= 3) {
            break; // Limitar a 3 sugestões
          }
        }
      }
    });
  }
});

function displayNames(value) {
  let input = document.getElementById("input");
  if (input) {
    input.value = value;
    removeElements();
  }
}

function removeElements() {
  // limpar todos os itens
  let items = document.querySelectorAll(".list-items");
  items.forEach((item) => {
    item.remove();
  });
}
