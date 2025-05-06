public class Pessoa{
    private String nome;
    private int CPF;
    private String Email;
    private String telefone;
    
    public void setNome(String n){
        this.nome = n;
    }
    
    public void setCPF( int cpf){
        this.CPF=cpf;
    }
    
    public void setEmail(String email){
        this.Email = email;
    }
    
    public void setTelefone(String telefone){
        this.telefone = telefone;
    }
    
    public String getNome(){
        return nome;
    }
    public int getCPF(){
        return CPF;
    }
    public String getEmail(){
        return Email;
    }
    public String getTelefone(){
        return telefone;
    }
}