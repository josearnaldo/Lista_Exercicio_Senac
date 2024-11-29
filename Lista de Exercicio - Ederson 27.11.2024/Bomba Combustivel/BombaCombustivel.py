class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Abastecido {litros_abastecidos:.2f} litros por R${valor:.2f}")
            print(f"combustível restante: {self.quantidade_combustivel:.2f} litros")
        else:
            print("combustível insuficiente na bomba.")
    def abastecerPorLitro(self, litros):
        if litros <= self.quantidade_combustivel:
            valor_a_pagar = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            print(f"Valor a ser pago por {litros} litros: R${valor_a_pagar}.")
            print(f"Combustivel Restante: {self.quantidade_combustivel} litros.")
        else:
            print("Quantidade de combustível insuficiente na bomba.")
    def alterarValor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Novo valor do litro de combustível: R${self.valor_litro}.")
    def alterarCombustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo
        print(f"Tipo de combustível alterado para: {self.tipo_combustivel}.")
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível alterada para: {self.quantidade_combustivel} litros.")