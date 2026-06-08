programa {
  inclua  biblioteca Util --> u
  funcao inicio() {
    
    inteiro valor, chute, tentativas = 0
    cadeia etr
    logico jogoOn = verdadeiro

     chute = u.sorteia(1,100)

    enquanto (jogoOn == verdadeiro) {
      escreva("Tentativas restantes: ",tentativas,"/5\n")
      escreva("Digite um valor inteiro de 1 a 100: ")
      leia(valor)

      se (valor == chute) {
        escreva("Parabéns você acertou!")
        jogoOn = falso
      }
      senao se (tentativas >= 4) {
        limpa()
        escreva("você fracassou\n")
        escreva("O valor era: ",chute)
        jogoOn = falso
      }
      senao se (valor < chute) {
        escreva("O valor esta mais para direita!\n")
        tentativas++
        escreva("Aperte [Enter] para continuar")
        leia(etr)
        limpa()
      }
      senao se (valor > chute) {
        escreva("O valor esta mais para a esqueda!\n")
        tentativas++
        escreva("Aperte [Enter] para continuar")
        leia(etr)
        limpa()
      }
    }
  }
}
