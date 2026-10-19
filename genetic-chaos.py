# (4^3,200,000)
exponente_base_10 = 1926591

def gerar():
    arquivo = "genetic_possibilities.txt"
    
    print(f"Escrevendo 1 seguido por {exponente_base_10} zeros para o arquivo {arquivo}...")
    
    with open(arquivo, "w") as f:
        f.write("1")
        # escrevendo em blocos pra não matar a RAM
        bloco = 100000
        zeros = 0
        
        while zeros < exponente_base_10:
            restante = exponente_base_10 - zeros
            faltam = min(bloco, restante)
            f.write("0" * faltam)
            zeros += faltam
            
    print("Concluído! O arquivo tem por volta de 1.9 MB. Não abra sem o VS Code ou similares!!")

if __name__ == "__main__":
    gerar()
