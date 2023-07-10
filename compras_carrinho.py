class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_valor_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
    
    def exibir_produtos(self):
        if not self.produtos:
            print("O carrinho está vazio.")
        else:
            print("Produtos no carrinho:")
            for produto in self.produtos:
                print(f"Nome: {produto.nome} | Preço: R${produto.preco:.2f}")

# Criando instância da classe CarrinhoDeCompras
carrinho = CarrinhoDeCompras()

# Criando instâncias da classe Produto
produto1 = Produto("Camiseta", 29.90)
produto2 = Produto("Calça Jeans", 99.90)
produto3 = Produto("Tênis", 199.90)

# Adicionando produtos ao carrinho
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.adicionar_produto(produto3)

# Exibindo os produtos presentes no carrinho
carrinho.exibir_produtos()

# Calculando o valor total da compra
valor_total = carrinho.calcular_valor_total()
print(f"Valor total da compra: R${valor_total:.2f}")
