let names = [
  "Agiplan",
  "Arbi",
  "Amazônia",
  "Brasil",
  "Nordeste",
  "Banestes",
  "Bradesco",
  "Banrisul",
  "Caixa Econômica Federal",
  "Itaú Consignado",
  "Paraná",
  "Santander",
  "Safra",
  "Votorantim",
  "Mercantil do Brasil",
  "Industrial do Brasil",
  "Pan",
  "C6 Bank",
  "Daycoval",
  "Cetelem",
  "Semear",
  "Cooperativo Sicredi",
  "Cooperativo do Brasil",
  "CCB Brasil",
  "Intermedium",
  "Financeira Alfa",
  "Parati",
  "Santinvest",
  "Barigui",
  "Socicred",
  "Crediare",
  "BRB",
  "Caruana",
  "Gazincred",
  "Facta Financeira",
  "Sicoob Coopernapi",
  "CBSS",
  "Olé Bonsucesso Consignado",
  "Via Certa Financiadora"
];

document.addEventListener("DOMContentLoaded", (event) => {
// Ordena os nomes em ordem crescente
let sortedNames = names.sort();

// Array de IDs dos campos de entrada e listas correspondentes
let inputDetails = [
  { inputId: "input", listId: "listB1" },
  { inputId: "input2", listId: "listB2" }
];

inputDetails.forEach(({ inputId, listId }) => {
  let input = document.getElementById(inputId);
  let list = document.getElementById(listId);
  if (input) {
    // Executar função no evento keyup
    input.addEventListener("keyup", (e) => {
      // Remover todos os elementos anteriores
      removeElements(listId);
      let count = 0; // Contador para limitar as sugestões
      for (let i of sortedNames) {
        // Converter entrada para minúsculas e comparar com cada string
        if (
          i.toLowerCase().startsWith(input.value.toLowerCase()) &&
          input.value != ""
        ) {
          // Criar elemento li
          let listItem = document.createElement("li");
          // Nome de classe comum
          listItem.classList.add("list-items");
          listItem.style.cursor = "pointer";
          listItem.setAttribute("onclick", `displayNames('${i}', '${inputId}')`);
          // Exibir a parte correspondente em negrito
          let word = "<b>" + i.substr(0, input.value.length) + "</b>";
          word += i.substr(input.value.length);
          // Exibir o valor no array
          listItem.innerHTML = word;
          list.appendChild(listItem);

          count++;
          if (count >= 3) {
            break; // Limitar a 3 sugestões
          }
        }
      }
    });
  }
});
});

function displayNames(value, inputId) {
let input = document.getElementById(inputId);
if (input) {
  input.value = value;
  removeElements(inputId === "input" ? "listB1" : "listB2");
}
}

function removeElements(listId) {
// Limpar todos os itens
let items = document.querySelectorAll(`#${listId} .list-items`);
items.forEach((item) => {
  item.remove();
});
}