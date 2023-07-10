package Biblioteca;

import java.io.Serializable;

public abstract class Livro implements Serializable {

	private static final long serialVersionUID = 1L;
	private String nome;
	private long ISBN;
	private String autor;
	protected String resenha;
	
	public Livro(String nome, long ISBN, String autor, String resenha) {
		this.nome = nome;
		this.ISBN = ISBN;
		this.autor = autor;
		this.resenha = resenha;
	}

	public String toString() {
		String retorno = "";
		retorno += "Nome: "     + this.nome     + "\n";
		retorno += "ISBN: "    + this.ISBN    + "\n";
		retorno += "Autor: "     + this.autor     + "\n";
		retorno += "Resenha: "  + this.resenha  + "\n";
		retorno += "Leitores "  + quemLe()        + "\n";
		return retorno;
	}

	public abstract String quemLe();

	public String getNome() {
		return nome;
	}

	public long getISBN() {
		return ISBN;
	}

	public String getAutor() {
		return autor;
	}

	public String getResenha() {
		return resenha;
	}

	

}
