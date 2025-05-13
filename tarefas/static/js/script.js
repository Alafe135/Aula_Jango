//Função que pergunta ao usuario se ele quer mesmo excluir a tarefa

document.querySelectorAll(".delete-btn").forEach(
    btn => {
        btn.addEventListener("click", function(e){
            e.preventDefault();

            const delLink = this.getAttribute("href");

            if(delLink && confirm("quer deletar esta tarefa?")){
                window.location.href = delLink;
            }
        });
    }
);