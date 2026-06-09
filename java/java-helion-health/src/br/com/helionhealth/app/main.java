package br.com.helionhealth.app;

import br.com.helionhealth.model.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class main
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("~~~~~~~~~~ BEM-VINDO AO SISTEMA HELION HEALTH ~~~~~~~~~~");

        // Instanciando a localização
        System.out.println("\n--- Cadastro de Localização Atual ---");
        System.out.print("Digite a Cidade: ");
        String cidade = scanner.nextLine();
        System.out.print("Digite o Estado (UF): ");
        String estado = scanner.nextLine();
        System.out.print("Digite o País: ");
        String pais = scanner.nextLine();
        Localizacao localizacao = new Localizacao(cidade, estado, pais);

        // Instanciando o cliente
        System.out.println("\n--- Cadastro do Cliente ---");
        System.out.print("Digite o Nome do Cliente: ");
        String nome = scanner.nextLine();
        System.out.print("Digite a Data de Nascimento (dd/mm/aaaa): ");
        String dataStr = scanner.nextLine();
        LocalDate dataNascimento = LocalDate.parse(dataStr, formatter);
        System.out.print("Digite a Condição Médica (ex: Nenhuma, Dermatite): ");
        String condicao = scanner.nextLine();
        System.out.print("Digite o Tom/Cor de Pele (Escala Fitzpatrick ou descrição): ");
        String cor = scanner.nextLine();

        Cliente cliente = new Cliente(nome, dataNascimento, condicao, cor);
        cliente.setLocalizacao(localizacao); // Associando a localização ao cliente

        // Instanciando o processamento e o histórico
        Calculador calculador = new Calculador();
        Historico historico = new Historico();
        Recomendador recomendador = new Recomendador();

        // Instanciando o gerenciador
        Gerenciador gerenciador = new Gerenciador(cliente, historico, calculador);

        System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("  DADOS INICIAIS REGISTRADOS (Teste toString)  ");
        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println(gerenciador.getCliente().toString());
        System.out.println(gerenciador.getCliente().getLocalizacao().toString());
        System.out.println(gerenciador.getCalculador().toString());
        System.out.println(gerenciador.getHistorico().toString());

        System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("      PROCESSAMENTO DOS MÉTODOS FUNCIONAIS     ");
        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

        int idadeCalculada = gerenciador.getCliente().calcularIdade();
        System.out.println("[Método Cliente.calcularIdade()] Idade processada: " + idadeCalculada + " anos.");

        String grupoGeracional = gerenciador.getCliente().pegarGrupoGeracional();
        System.out.println("[Método Cliente.pegarGrupoGeracional()] Grupo: " + grupoGeracional);

        System.out.println("\nEfetuando medição meteorológica para " + localizacao.getCidade() + "...");
        gerenciador.getCalculador().calcularUv(localizacao);
        gerenciador.getCalculador().calcularKp(localizacao);

        System.out.println("\n[Estado pós-cálculo] " + gerenciador.getCalculador().toString());

        recomendador.setRecomendacao("Para o nível de UV " + gerenciador.getCalculador().getUV() + ", use Protetor FPS 50.");
        recomendador.setInformacoesGruposDeRisco("Risco aumentado para o grupo: " + grupoGeracional + " com pele " + cliente.getCor());

        gerenciador.getHistorico().adicionarPedido(gerenciador.getCalculador().getUV(), localizacao);
        System.out.println("\n[Método Historico.adicionarPedido()] Dados salvos no histórico com sucesso.");

        System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("        SAÍDAS E ESTADOS FINAIS DO PROGRAMA   ");
        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("Nome do App: " + gerenciador.getNomeAplicativo());
        System.out.println("\n--- Dados do Recomendador ---");
        System.out.println(recomendador.toString());

        System.out.println("\n--- Listando Histórico de Consultas Realizadas ---");

        gerenciador.getHistorico().verPedidosAnteriores();

        scanner.close();
    }
}