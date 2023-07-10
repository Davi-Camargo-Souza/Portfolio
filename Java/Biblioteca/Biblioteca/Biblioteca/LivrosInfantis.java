package Biblioteca;

public class LivrosInfantis extends Livro{

    private static final long serialVersionUID = 1L;
    private String brinde;

    public String getBrinde(){
        return brinde;
    }

    public LivrosInfantis(String nome, long ISBN, String autor, String resenha, String brinde){
        super(nome, ISBN, autor, resenha);
        this.brinde = brinde;
    }

    public String quemLe(){
        return "Crianças e Famílias";
    }

    @Override
    public String toString() {
		String retorno = "";
		retorno += "Nome: "     + this.getNome()     + "\n";
		retorno += "ISBN: "    + this.getISBN()    + " \n";
		retorno += "Autor: "     + this.getAutor()     + "\n";
		retorno += "Resenha: "  + this.getResenha()  + "\n";
        retorno += "Brinde: " + this.getBrinde() + "\n";
		retorno += "Leitores: "  + quemLe()        + "\n";
		return retorno;
	}
    
}
