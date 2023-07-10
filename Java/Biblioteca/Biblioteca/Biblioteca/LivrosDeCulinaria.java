package Biblioteca;

public class LivrosDeCulinaria extends Livro{

    private static final long serialVersionUID = 1L;
    private String tipoDeCulinaria;

    public String getTipoDeCulinaria() {
        return tipoDeCulinaria;
    }

    public LivrosDeCulinaria(String nome, long ISBN, String autor, String resenha, String tipoDeCulinaria) {
        super(nome, ISBN, autor, resenha);
        this.tipoDeCulinaria = tipoDeCulinaria;
    }

    @Override
    public String quemLe() {
        return "Cozinheiros e entusiastas ";
    }

    @Override
    public String toString() {
		String retorno = "";
		retorno += "Nome: "     + this.getNome()     + "\n";
		retorno += "ISBN: "    + this.getISBN()    + " \n";
		retorno += "Autor: "     + this.getAutor()     + "\n";
		retorno += "Resenha: "  + this.getResenha()  + "\n";
		retorno += "Leitores: "  + quemLe()        + "\n";
        retorno += "Tipo de Culinaria: " + this.getTipoDeCulinaria()  + "\n";
		return retorno;
	}
    
}
