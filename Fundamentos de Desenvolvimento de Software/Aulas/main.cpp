#include <stdio.h>
/*
Program aque calcula a média aritmética
Obter as 2 notas de provas
Calcular a média aritmética
Se a média for igual ou maior que 7, o aluno foi aprovado
senão ele foi reprovado
*/
int main(void)
{
    // declaração de variável
    float nota1, nota2, media;

    // Obter as 2 notas de provas
    printf("Digite a primeira nota:  ");
    scanf_s("%f", &nota1);

    printf("Digite a segunda  nota:  ");
    scanf_s("%f", &nota2);

    // Calcular a média aritmética
    media = (nota1 + nota2) / 2;

    // mostro o resultado
    if (media >= 7)
        printf("Aprovado! \n");
    else
        printf("Reprovado! \n");

    return 0;
}