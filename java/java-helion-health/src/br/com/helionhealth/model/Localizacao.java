package br.com.helionhealth.model;

public class Localizacao
{
    // Atributos
    private String cidade;
    private String estado;
    private String pais;

    // Construtores
    // Construtor Vazio
    public Localizacao() {}

    // Construtor Cheio
    public Localizacao(String cidade, String estado, String pais) {
        this.cidade = cidade;
        this.estado = estado;
        this.pais = pais;
    }

    // toString
    @Override
    public String toString() {
        return "Localizacao:" +
                "\n  cidade: " + cidade +
                "\n  estado: " + estado +
                "\n  pais: " + pais;
    }

    // Métodos Acessores
    public String getCidade() { return cidade; }
    public String getEstado() { return estado; }
    public String getPais() { return pais; }

    public void setCidade(String cidade) { this.cidade = cidade; }
    public void setEstado(String estado) { this.estado = estado; }
    public void setPais(String pais) { this.pais = pais; }
}
