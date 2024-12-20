from App.model.sala import Sala

def cadastrarSala(nome, tipo, predio, equipamento, capacidade, feedback):
    sala = Sala(nome, tipo, predio, equipamento, capacidade, feedback)
    if sala.cadastrar_sala():
        return True
    return False

def listarSala():
    todasSalas = Sala.buscar_nomeId_sala()
    listarSalas = {i[1]:i[0] for i in todasSalas}
    return(listarSalas)

def atualizarSala(nome, tipo, predio, equipamento, capacidade, observacao, idSala):
    if Sala.atualizar(nome, tipo, predio, equipamento, capacidade, observacao, idSala):
        return True
    return False
    

def deletarSala(idSala):
    if Sala.deletar(idSala):
        return True
    return False