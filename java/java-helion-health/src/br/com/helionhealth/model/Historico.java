package br.com.helionhealth.model;

import java.util.ArrayList;

public class Historico
{
    // Atributos
    private ArrayList<Localizacao> pedidosPassados = new ArrayList<>();
    private ArrayList<Integer> uvPassadas = new ArrayList<>();

    // Construtor Vazio
    public Historico() {}

    // toString
    @Override
    public String toString() {
        return "Historico:" +
                "\n  pedidosPassados: " + pedidosPassados +
                "\n  uvsPassadas: " + uvPassadas;
    }

    // Métodos Workers
    public void adicionarPedido(int uv, Localizacao l)
    {
        pedidosPassados.add(l);
        uvPassadas.add(uv);
    }

    public void verPedidosAnteriores()
    {
        for(int i = 0; i < pedidosPassados.size(); i += 1)
        {
            System.out.println(pedidosPassados.get(i) + " | " + uvPassadas.get(i) + "UV");
        }
    }
}
