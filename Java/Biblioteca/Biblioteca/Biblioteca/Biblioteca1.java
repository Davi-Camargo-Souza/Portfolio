package Biblioteca;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

public class Biblioteca1 {

	private ArrayList<Livro> livros;


	public Biblioteca1() {
		this.livros = new ArrayList<Livro>();
	}

	public void adicionaLivro(Livro livr) {
		this.livros.add(livr);
	}

	public void listarLivros() {
		for(Livro livr:livros) {
			System.out.println(livr.toString());
		}
		System.out.println("Total = " + this.livros.size() + " livros listados com sucesso!\n");
	}
	
	public void excluirLivro(Livro livr) {
		if (this.livros.contains(livr)) {
			this.livros.remove(livr);
			System.out.println("[Livro " + livr.toString() + "excluido com sucesso!]\n");
		}
		else
			System.out.println("Livro inexistente!\n");
	}

	public void excluirLivros() {
		livros.clear();
		System.out.println("Livros excluidos com sucesso!\n");
	}
	public void gravarLivros()  {
		ObjectOutputStream outputStream = null;
		try {
			outputStream = new ObjectOutputStream (new FileOutputStream("livros.dat"));
			for(Livro livr:livros) {
				outputStream.writeObject(livr);
			}
		}catch (FileNotFoundException ex) {
			ex.printStackTrace();
		}catch (IOException ex) {
			ex.printStackTrace();
		}finally{
			try {
				if (outputStream != null ) {
					outputStream.flush();
					outputStream.close();
				}
			}catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
	public void recuperarLivros() {
		ObjectInputStream inputStream = null;
		try {
			inputStream	= new ObjectInputStream (new FileInputStream ("livros.dat"));
			Object obj = null;
			while((obj = inputStream.readObject ()) != null) {
				if (obj instanceof LivrosInfantis)  
					this.livros.add((LivrosInfantis)obj);
				else if (obj instanceof LivrosDeCulinaria)  
					this.livros.add((LivrosDeCulinaria)obj);
				else if (obj instanceof GuiasDeViagem)
					this.livros.add((GuiasDeViagem) obj);
			}
		}catch (EOFException ex) {     // when EOF is reached
			System.out.println ("End of file reached");
		}catch (ClassNotFoundException ex) {
			ex.printStackTrace();
		}catch (FileNotFoundException ex) {
			ex.printStackTrace();
		}catch (IOException ex) {
			ex.printStackTrace();
		}finally{
			try {
				if (inputStream != null ) {
					inputStream.close();
					System.out.println("Livros recuperados com sucesso!\n");
				}
			}catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}


	public static void main(String[] args) {
		Biblioteca1 livro  = new Biblioteca1();

		LivrosInfantis livroInfant1 = new LivrosInfantis("O Pequeno Príncipe", 9788567097107L, "Antoine de Saint-Exupéry",
		"Uma história maravilhosa e profunda, contada pelo Pequeno Príncipe", "Marca páginas");

		LivrosInfantis livroInfant2 = new LivrosInfantis("O Meu Pé de Laranja Lima", 9788506086896L, "José Mauro de Vasconcelos", 
		"Acompanhe as aventuras e travessuras do menino Zezé", "Desenho para colorir");

		LivrosDeCulinaria livroCulin1 = new LivrosDeCulinaria("Chef Profissional", 8539607492L, "Senac Editoras", 
		"Aprimore seus conhecimentos na culinária", "Receitas no geral");

		LivrosDeCulinaria livroCulin2 = new LivrosDeCulinaria("Enciclopédia dos bolos: intermediário", 8506084105L, "Otávia Sommavilla", 
		"Mais de 80 receitas e técnicas de bolos com recheios e coberturas", "Bolos");

		GuiasDeViagem livroViagem1 = new GuiasDeViagem("Guia de Veneza - Segredos de um viajante", 8575265156L, "Ruy Araujo", 
		"Uma cidade linda que merece ser conhecida", "Veneza");

		GuiasDeViagem livroViagem2 = new GuiasDeViagem("Roma Com A Familia", 8579145295L, "Vários Autores", 
		"Um guia divertido e com muita informação", "Roma");

		livro.adicionaLivro(livroInfant1);
		livro.adicionaLivro(livroInfant2);
		livro.adicionaLivro(livroCulin1);
		livro.adicionaLivro(livroCulin2);
		livro.adicionaLivro(livroViagem2);
		livro.adicionaLivro(livroViagem1);
		livro.listarLivros();
		livro.gravarLivros();
		livro.excluirLivro(livroViagem1);
		livro.excluirLivro(livroInfant1);
		livro.listarLivros();
		livro.excluirLivros();
		livro.listarLivros();
		livro.recuperarLivros();
		livro.listarLivros();
	}

}
