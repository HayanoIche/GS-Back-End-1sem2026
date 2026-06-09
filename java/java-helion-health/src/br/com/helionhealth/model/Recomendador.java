package br.com.helionhealth.model;

public class Recomendador
{
    // Atributos
    private String recomendacao;
    private String informacoesGruposDeRisco;

    // Construtores
    // Construtor Cheio
    public Recomendador(String recomendacao, String informacoesGruposDeRisco) {
        this.recomendacao = recomendacao;
        this.informacoesGruposDeRisco = informacoesGruposDeRisco;
    }

    // Construtor Vazio
    public Recomendador() {};

    // toString
    @Override
    public String toString() {
        return "Recomendador: " +
                "\n  Recomendacao: " + recomendacao + '\'' +
                "\n  InformacoesGruposDeRisco: " + informacoesGruposDeRisco;
    }

    // Métodos Acessores
    public String getRecomendacao() { return recomendacao; }
    public String getInformacoesGruposDeRisco() { return informacoesGruposDeRisco; }

    public void setRecomendacao(String recomendacao) { this.recomendacao = recomendacao; }
    public void setInformacoesGruposDeRisco(String informacoesGruposDeRisco) { this.informacoesGruposDeRisco = informacoesGruposDeRisco; }


}
