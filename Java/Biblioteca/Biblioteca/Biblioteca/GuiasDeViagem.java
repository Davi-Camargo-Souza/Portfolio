package Biblioteca;

public class GuiasDeViagem extends Livro{

    private static final long serialVersionUID = 1L;
    private String local;

    public String getLocal() {
        return local;
    }


    public GuiasDeViagem(String nome, Long ISBN, String autor, String resenha, String local) {
        super(nome, ISBN, autor, resenha);
        this.local = local;
    }

    @Override
    public String quemLe() {
        return "Turistas";
    }

    @Override
    public String toString() {
		String retorno = "";
		retorno += "Nome: "     + this.getNome()     + "\n";
		retorno += "ISBN: "    + this.getISBN()    + " \n";
		retorno += "Autor: "     + this.getAutor()     + "\n";
		retorno += "Resenha: "  + this.getResenha()  + "\n";
		retorno += "Leitores: "  + quemLe()        + "\n";
        retorno += "Local: " + this.getLocal()          + "\n";
		return retorno;
	}
    
}
