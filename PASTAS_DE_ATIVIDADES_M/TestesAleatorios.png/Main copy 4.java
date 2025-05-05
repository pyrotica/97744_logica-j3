/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		int opcao; 
		OperacoesPessoa operacoesPessoa = new OperacoesPessoa();
		Scanner ler = new Scanner(System.in);
		do{
		System.out.println(" Escolha \n 1 - para cadastrar pessoa  \n 2 - para buscar pessoa \n 3 - para listar pessoas \n 4 - para excluir uma pessoa \n DIGITE A OPÇÃO DE DESEJA");
		opcao = Integer.parseInt(ler.nextLine());
		switch(opcao){
		    case 1:
		        operacoesPessoa.cadastrarPessoa();
		        break;
		    case 2:
		        operacoesPessoa.buscarPessoa(12);
		        break;
		    case 3:
		        operacoesPessoa.listarPessoas();
		        break;
		    case 4:
		        operacoesPessoa.excluirPessoa(2);
		        break;
		    default:
		        System.out.println(" opção invalida");
		}
		}while(opcao !=5);
	}
}