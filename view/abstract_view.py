 
class AbstractView:
 
    def le_num_inteiro(self,mensagem,inteiros_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: \
Digite um valor numerico inteiro valido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)
    
    def le_num_flutuante(self,mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                flutuante = float(valor_lido)
                if not (isinstance(flutuante,float)):
                    raise ValueError
                return flutuante
            except ValueError:
                print("Valor incorreto: \
Digite um valor numerico flutuante valido")