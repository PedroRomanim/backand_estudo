class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
    
    def inscrever(self, quantidade):
        self.inscritos += quantidade

    def postar_video(self, video):
        if video in self.videos:
            print(f"O vídeo '{video.titulo}' já foi postado no canal '{self.nome}'.")
            return
        self.videos.append(video)

class CanalEmpresarial(Canal):#Heranca de classe
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []

    @property #encapsulamento
    def equipe(self):
        return self._equipe
    
    def adicionar_membro(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f"{membro} já faz parte da equipe.")
    
    def remover_membro(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f"{membro} não faz parte da equipe.")
    
class Video:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        
        self.visualizacoes = 0
        self.curtidas = 0
        self.deslikes = 0
        self.comentarios = []
    
    def assistir(self):
        self.visualizacoes += 1
    
    def gostei(self):
        self.curtidas += 1
    
    def nao_gostei(self):
        self.deslikes += 1

    def comentar(self, comentario):
        self.comentarios.append(comentario)

    def info(self):
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Visualizações: {self.visualizacoes}")
        print(f"Curtidas: {self.curtidas}")
        print(f"Deslikes: {self.deslikes}")
        print("Comentários:")
        for comentario in self.comentarios:
            print(f"- {comentario}")

    def __repr__(self):
        return f"<{self.titulo}>"

canal_Fallzi = Canal('Fallzi', 'Canal de programação e tecnologia', 10000)
canal_Lancode = Canal('Lancode', 'Codigos e gatos', 34000)
canal_Duolingo = CanalEmpresarial('DuoLIngo', 'Ingreis', 50000)

video1 = Video('Python para iniciantes', 'Aprenda Python do zero!')
canal_Fallzi.postar_video(video1)

