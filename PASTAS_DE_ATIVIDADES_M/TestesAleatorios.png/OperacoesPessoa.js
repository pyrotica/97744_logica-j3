import java.util.Scanner;
import java.util.ArrayList; 
public class OperacoesPessoa{
ArrayList<Pessoa> listaDePessoas = new ArrayList<Pessoa>();
Scanner ler = new Scanner(System.in);

public void cadastrarPessoa(){
    Pessoa p = new Pessoa();
    System.out.println("Digite o nome da pessoa");
    p.setNome(ler.nextLine());
    System.out.println("Digite o E-mail da pessoa");
    p.setEmail(ler.nextLine());
    System.out.println("Digite o Telefone da pessoa");
    p.setTelefone(ler.nextLine());
    System.out.println("Digite o CPF da pessoa");
    p.setCPF(Integer.parseInt(ler.nextLine()));
    listaDePessoas.add(p);

}
public void listarPessoas(){
    
    for(int i = 0; i < listaDePessoas.size(); i++ ){
        System.out.println(listaDePessoas.get(i).getNome());
        System.out.println(listaDePessoas.get(i).getEmail());
        System.out.println(listaDePessoas.get(i).getTelefone());
        System.out.println(listaDePessoas.get(i).getCPF());
    }
}
public void buscarPessoa(int cpf){
    
    for(int i = 0; i < listaDePessoas.size(); i++ ){
        if(listaDePessoas.get(i).getCPF() == cpf){
        System.out.println(listaDePessoas.get(i).getNome());
        System.out.println(listaDePessoas.get(i).getEmail());
        System.out.println(listaDePessoas.get(i).getTelefone());
        System.out.println(listaDePessoas.get(i).getCPF());
        }else{
            System.out.println("Pessoa não encontrada");
        
        }
    }
}
public void excluirPessoa(int cpf){
     for(int i = 0; i < listaDePessoas.size(); i++ ){
        if(listaDePessoas.get(i).getCPF() == cpf){
        listaDePessoas.remove(listaDePessoas.get(i));
        }else{
            System.out.println("Pessoa não encontrada");
        
        }
    }
}
}