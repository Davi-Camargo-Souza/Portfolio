package Biblioteca;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import javax.swing.JOptionPane;


public class Biblioteca {
	private ArrayList<Livro> livros;

	public Biblioteca() {
		this.livros = new ArrayList<Livro>();
	}
	public String[] leValores (String [] dadosIn){
		String [] dadosOut = new String [dadosIn.length];

		for (int i = 0; i < dadosIn.length; i++)
			dadosOut[i] = JOptionPane.showInputDialog  ("Entre com " + dadosIn[i]+ ": ");

		return dadosOut;
	}

	public LivrosInfantis leLivrosInfantis (){

		String [] valores = new String [4];
		String [] nomeVal = {"Nome", "ISBN", "Autor","Resenha","Brinde"};
		valores = leValores (nomeVal);

		long isbn = this.retornaLong(valores[1]);

		LivrosInfantis livroInfantil = new LivrosInfantis (valores[0],isbn,valores[2],valores[3],valores[4]);
		return livroInfantil;
	}

	public LivrosDeCulinaria leLivrosDeCulinaria (){

		String [] valores = new String [4];
		String [] nomeVal = {"Nome", "ISBN", "Autor","Resenha","Tipo de culinária"};
		valores = leValores (nomeVal);

		long isbn = this.retornaLong(valores[1]);

		LivrosDeCulinaria livroDeCulinaria = new LivrosDeCulinaria (valores[0],isbn,valores[2],valores[3],valores[4]);
		return livroDeCulinaria;
	}

	public GuiasDeViagem leGuiasDeViagem (){

		String [] valores = new String [4];
		String [] nomeVal = {"Nome", "ISBN", "Autor","Resenha","Local"};
		valores = leValores (nomeVal);

		long isbn = this.retornaLong(valores[1]);

		GuiasDeViagem guiaDeViagem = new GuiasDeViagem (valores[0],isbn,valores[2],valores[3],valores[4]);
		return guiaDeViagem;
	}

	public long retornaLong (String entrada){
		while (!this.longValido(entrada)) {
			entrada = JOptionPane.showInputDialog(null, "Valor incorreto!\n\nDigite um número inteiro.");
		}
		return Long.parseLong(entrada);
	}

	private boolean longValido(String s){
		try {
			Long.parseLong(s); // Método estático, que tenta tranformar uma string em long
			return true;
		} catch (NumberFormatException e) { // Não conseguiu tranformar em long e gera erro
			return false;
		}
	}

	private boolean intValido(String s) {
		try {
			Integer.parseInt(s); // Método estático, que tenta tranformar uma string em inteiro
			return true;
		} catch (NumberFormatException e) { // Não conseguiu tranformar em inteiro e gera erro
			return false;
		}
	}

	public int retornaInteiro(String entrada) { // retorna um valor inteiro
		int numInt;

		//Enquanto não for possível converter o valor de entrada para inteiro, permanece no loop
		while (!this.intValido(entrada)) {
			entrada = JOptionPane.showInputDialog(null, "Valor incorreto!\n\nDigite um número inteiro.");
		}
		return Integer.parseInt(entrada);
	}

	public void salvaLivros (ArrayList<Livro> livros){
		ObjectOutputStream outputStream = null;
		try {
			outputStream = new ObjectOutputStream 
					(new FileOutputStream("biblioteca.dados"));
			for (int i=0; i < livros.size(); i++)
				outputStream.writeObject(livros.get(i));
		} catch (FileNotFoundException ex) {
			JOptionPane.showMessageDialog(null,"Impossível criar arquivo!");
			ex.printStackTrace();
		} catch (IOException ex) {
			ex.printStackTrace();
		} finally {  //Close the ObjectOutputStream
			try {
				if (outputStream != null) {
					outputStream.flush();
					outputStream.close();
				}
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}

	@SuppressWarnings("finally")
	public ArrayList<Livro> recuperaLivros (){
		ArrayList<Livro> livrosTemp = new ArrayList<Livro>();

		ObjectInputStream inputStream = null;

		try {	
			inputStream = new ObjectInputStream
					(new FileInputStream("biblioteca.dados"));
			Object obj = null;
			while ((obj = inputStream.readObject()) != null) {
				if (obj instanceof Livro) {
					livrosTemp.add((Livro) obj);
				}   
			}          
		} catch (EOFException ex) { // when EOF is reached
			System.out.println("Fim de arquivo.");
		} catch (ClassNotFoundException ex) {
			ex.printStackTrace();
		} catch (FileNotFoundException ex) {
			JOptionPane.showMessageDialog(null,"Arquivo com livros não existe!");
			ex.printStackTrace();
		} catch (IOException ex) {
			ex.printStackTrace();
		} finally {  //Close the ObjectInputStream
			try {
				if (inputStream != null) {
					inputStream.close();
				}
			} catch (final IOException ex) {
				ex.printStackTrace();
			}
			return livrosTemp;
		}
	}

	public void menuBiblioteca (){

		String menu = "";
		String entrada;
		int    opc1, opc2;

		do {
			menu = "Controle Biblioteca\n" +
					"Opções:\n" + 
					"1. Entrar Livros\n" +
					"2. Exibir Livros\n" +
					"3. Limpar Livros\n" +
					"4. Gravar Livros\n" +
					"5. Recuperar Livros\n" +
					"9. Sair";
			entrada = JOptionPane.showInputDialog (menu + "\n\n");
			opc1 = this.retornaInteiro(entrada);

			switch (opc1) {
			case 1:// Entrar dados
				menu = "Entrada de Livros\n" +
						"Opções:\n" + 
						"1. Livro Infantil\n" +
						"2. Livro de culinária\n" +
						"3. Guia de Viagem";

				entrada = JOptionPane.showInputDialog (menu + "\n\n");
				opc2 = this.retornaInteiro(entrada);

				switch (opc2){
				case 1: livros.add((Livro)leLivrosInfantis());
				break;
				case 2: livros.add((Livro)leLivrosDeCulinaria());
				break;
				case 3: livros.add((Livro)leGuiasDeViagem());
				break;
				default: 
					JOptionPane.showMessageDialog(null,"Livro para entrada não escolhido!");
				}

				break;
			case 2: // Exibir dados
				if (livros.size() == 0) {
					JOptionPane.showMessageDialog(null,"Entre com livros primeiramente");
					break;
				}
				String dados = "";
				for (int i=0; i < livros.size(); i++)	{
					dados += livros.get(i).toString() + "---------------\n";
				}
				JOptionPane.showMessageDialog(null,dados);
				break;
			case 3: // Limpar Dados
				if (livros.size() == 0) {
					JOptionPane.showMessageDialog(null,"Entre com livros primeiramente");
					break;
				}
				livros.clear();
				JOptionPane.showMessageDialog(null,"Dados LIMPOS com sucesso!");
				break;
			case 4: // Grava Dados
				if (livros.size() == 0) {
					JOptionPane.showMessageDialog(null,"Entre livros primeiramente");
					break;
				}
				salvaLivros(livros);
				JOptionPane.showMessageDialog(null,"Dados SALVOS com sucesso!");
				break;
			case 5: // Recupera Dados
				livros = recuperaLivros();
				if (livros.size() == 0) {
					JOptionPane.showMessageDialog(null,"Sem dados para apresentar.");
					break;
				}
				JOptionPane.showMessageDialog(null,"Dados RECUPERADOS com sucesso!");
				break;
			case 9:
				JOptionPane.showMessageDialog(null,"Fim do aplicativo BIBLIOTECA");
				break;
			}
		} while (opc1 != 9);
	}


	public static void main (String [] args){

		Biblioteca livro = new Biblioteca ();
		livro.menuBiblioteca();

	}

}
