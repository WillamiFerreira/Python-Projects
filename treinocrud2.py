alunos = {
	100 : ('Gabriel', [8.5, 9.0, 10.0]),
	101 : ('Pedro', [9.0, 7.5, 8.5]),
	102 : ('Maria', [10.0 ,6.5 ,8.0])
}

def criar():
    chave = max(alunos.keys()) + 1
    nome = str(input('Digite o nome do novo aluno: '))
    nota = [float(input('Digite a nota: '))]
    aluno = (nome, nota)
    alunos[chave] = aluno
    input('Aluno adicionado! Aperte enter para continuar.\n')
   
def ler(chave):
    nome, notas = alunos[chave]
    return nome, notas
    
def atualizar(chave):
    nome, notas = ler(chave)
    aux = input(f'atualizar o nome do aluno {nome} para: (vazio se não quiser mudar o nome) ')
    if aux != '':
        nome = aux
        
    aux = input(f'nova nota: (atual{notas}) ')
    if aux != '':
        nova = input('Dejesa adicionar a nova nota? (S/N): ')[0].upper() == 'S'
        if nova:
            alunos[chave][1].append(float(aux))
            input('Nova nota adicionada!. Aperte enter para continuar\n')
        else:
            print(f'notas atuais{notas}')
            i_nota = int(input('Digite o índice da nota que deseja modificar: '))
            alunos[chave][1][i_nota] = float(aux)
            print('='*30)
            input('Nota atualizada com sucesso!. Aperte enter para continuar.\n')
    else:
        print('Nome atualizado!')
    alunos[chave] = (nome, notas)
    
def apagar(chave):
    nome, _ = ler(chave)
    confirmacao = input(f'Você realemente deseja apagar o/a aluno(a) {nome}: (S/N)')[0].upper().strip() == 'S'
    if confirmacao: 
        del(alunos[chave])
        input('Aluno apagado com sucesso!. Aperte enter para continuar.\n')

def listar():
        qtd = 0
        for chave in alunos:
            nome, notas = ler(chave)
            print()
            print(f'Chave do aluno: {chave}')
            print(f'Nome do aluno: {nome}')
            print(f'Notas do aluno: {notas}')
            print('=' * 30)
            
            qtd += 1
        if qtd > 0:
            input(f'Foram listados {qtd} alunos. Aperte enter para continuar.\n')
        else:
            input('<<< Não há alunos para listar >>>', 'Aperte enter para continuar.\n')
    
def menu():
    print("1 (C) - Adicionar um novo aluno")
    print("2 (R) - Ler um Aluno.")
    print("3 (U) - Atualizar um aluno")
    print("4 (D) - Deletar um aluno")
    print("5 - Listar alunos ")
    print("0 - Sair")
    opcao = int(input("Qual sua opção: "))
    return opcao
    
 
    
def main():
    while True:
        op = menu()
        if op == 1:
            criar()
            
        elif op == 2: 
            chave = int(input('Código do aluno para ler: '))
            if chave in alunos:
                nome, notas = ler(chave)
                print('=' * 30)
                print(f'chave do aluno: {chave}')
                print(f'Nome do aluno: {nome}')
                print(f'Notas do aluno: {notas}')
                print('=' * 30,'\n')
            else:
                print('O aluno não existe!')
        elif op == 3:
           chave = int(input('Código do aluno para atualizar dados: '))
           if chave in alunos:
               atualizar(chave)
                
           else:
               print('O código informado não consta como pertencente a um aluno!')
        elif op == 4:
            chave = int(input('Digite a chave para apagar o aluno: '))
            if chave in alunos:
                apagar(chave)
            else:
                print('O código informado não consta como pertencente a um aluno!')
        elif op == 5:
            listar()
           
        elif op == 0:
            print('Fim do programa')
            break
        else:
            pass
    
if __name__ == "__main__":
    main()