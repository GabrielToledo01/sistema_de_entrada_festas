#exercício  de um sistema para controle de entrada em um espaço de festas. O cliente precisa que o sistema possua os seguintes requisitos:
#• É necessário que o programa fique em execução enquanto houver pessoas para entrar;
#• Deve ser informado o sexo da pessoa e a idade;
#• Somente pessoas maiores de idade podem acessar o espaço;
#• Para acesso às pessoas do sexo masculino, a entrada está 
#condicionada a presença do dobro de pessoas do sexo feminino em relação ao masculino;
#• Ao final da execução do sistema, deverá ser emitido um relatório com o número total de pessoas, o número do sexo masculino e do sexo feminino que entraram no espaço

total_de_mulheres=0
total_de_homens=0
while True:
    idade = int(input('Digite sua idade'))
    if idade < 18:
        print('Acesso Negado')
    else:
        sexo = str(input('Sexo:[M/F]')).strip().upper()[0]
        print('Seja bem-vindo(a)! Aproveite o evento!')
        if sexo in 'M':
            if total_de_mulheres/2>total_de_homens:
                print('Homens podem passar')
                total_de_homens+=1
        else:
            total_de_mulheres += 1
    print('Tem mais alguem na fila?')
    if not(int(input('1 para sim ou 0 para não[1/0]'))):
        break

print(f'Homens:{total_de_homens}, Mulheres:{total_de_mulheres}')
