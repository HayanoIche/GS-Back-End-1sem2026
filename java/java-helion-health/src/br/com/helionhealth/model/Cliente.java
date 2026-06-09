package br.com.helionhealth.model;

import java.time.LocalDate;

public class Cliente
{
    // Atributos
    private String nome;
    private LocalDate dataNascimento;
    private String condicao;
    private String cor;

    private Localizacao localizacao;

    // Construtores
    // Construtor Vazio
    public Cliente() {}

    // Construtor Cheio
    public Cliente(String nome, LocalDate dataNascimento, String condicao, String cor) {
        this.nome = nome;
        this.dataNascimento = dataNascimento;
        this.condicao = condicao;
        this.cor = cor;
    }

    // ToString
    @Override
    public String toString() {
        return "Cliente" +
                "\n  nome: " + nome +
                "\n  dataNascimento: " + dataNascimento +
                "\n  condicao: " + condicao +
                "\n  cor: " + cor;
    }

    // Métodos Acessores
    public String getNome() { return nome; }
    public LocalDate getDataNascimento() { return dataNascimento; }
    public String getCondicao() { return condicao; }
    public String getCor() { return cor; }
    public Localizacao getLocalizacao() { return localizacao; }

    public void setNome(String nome) { this.nome = nome; }
    public void setDataNascimento(LocalDate dataNascimento) { this.dataNascimento = dataNascimento; }
    public void setCondicao(String condicao) { this.condicao = condicao; }
    public void setCor(String cor) { this.cor = cor; }
    public void setLocalizacao(Localizacao localizacao) { this.localizacao = localizacao; }

    // Métodos Workers
    public int calcularIdade()
    {
        if (this.dataNascimento == null) return 0;
        LocalDate hoje = LocalDate.now();
        return java.time.Period.between(this.dataNascimento, hoje).getYears();
    }

    public String pegarGrupoGeracional()
    {
        int idade = calcularIdade();

        if (idade <= 12) {
            return "criança";
        }  else if (idade >= 13 && idade <= 17) {
            return "adolescente";
        } else if (idade >= 18 && idade <= 59) {
            return "adulto";
        } else if (idade >= 60) {
            return "idoso";
        }

        return "n/i"; // Não indentificado
    }
}
