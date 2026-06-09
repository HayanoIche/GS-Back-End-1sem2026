package br.com.helionhealth.model;

public class Gerenciador
{
    // Atributos
    private String nomeAplicativo = "Helion Health";

    private Cliente cliente;
    private Historico historico;
    private Calculador calculador;

    // Métodos Acessores
    public Cliente getCliente() {return cliente;}
    public Historico getHistorico() {return historico;}
    public Calculador getCalculador() {return calculador;}
    public String getNomeAplicativo() {return nomeAplicativo;}

    public void setCliente(Cliente cliente) {this.cliente = cliente;}
    public void setHistorico(Historico historico) {this.historico = historico;}
    public void setCalculador(Calculador calculador) {this.calculador = calculador;}

    // Construtores
    // Contrutor Vazio
    public Gerenciador() {}

    // Construtor Cheio
    public Gerenciador(Cliente cliente, Historico historico, Calculador calculador)
    {
        this.cliente = cliente;
        this.historico = historico;
        this.calculador = calculador;
    }
}
