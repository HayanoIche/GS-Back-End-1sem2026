package br.com.helionhealth.model;

import java.util.Random;

public class Calculador
{
    // Atributos
    private int nivelUv;

    // toString
    @Override
    public String toString() {
        return "CalculadorUV:" +
                "\n  nivelUv" + nivelUv;
    }

    // Construtor Vazio
    public Calculador() {}

    // Metodo Worker
    public void calcularUv(Localizacao l)
    {
        // Aqui iria o código que chama a API pra pegar o nível de UV
        // passando a cidade, o estado e o pais.
        // Porém por agora vamos só deixar o UV um valor aleatório

        Random rng = new Random();
        nivelUv = rng.nextInt(16);
    }

    // Metodo acessor
    public int getUV()
    {
        return nivelUv;
    }
}
