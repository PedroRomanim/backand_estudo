class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
        self.playlists:list[Playlist] = []
    
    def inscrever(self, quantidade):
        self.inscritos += quantidade

    def postar_video(self, video):
        if video in self.videos:
            print(f"O vídeo '{video.titulo}' já foi postado no canal '{self.nome}'.")
            return
        self.videos.append(video)

    def info_playlists(self):
        print(f"Playlists do canal '{self.nome}':")
        for playlist in self.playlists:
            print(f"- {playlist.nome}")
            playlist.info_videos()

    def adicionar_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)
        else:
            print(f"A playlist '{playlist.nome}' já está no canal '{self.nome}'.")
    
    def remover_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)
        else:
            print(f"A playlist '{playlist.nome}' não está no canal '{self.nome}'.")

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
    def __init__(self, titulo, descricao, data_publicacao):
        self.titulo = titulo
        self.descricao = descricao
        self.data_publicacao = data_publicacao
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
    
class Playlist:
    def __init__(self, nome):
        self.nome = nome

        self.videos:list[Video] = []

    def adicionar_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print(f"O vídeo '{video.titulo}' já está na playlist '{self.nome}'.")
        
    def remover_video(self, video):
        if video in self.videos:
            self.videos.remove(video)
        else:
            print(f"O vídeo '{video.titulo}' não está na playlist '{self.nome}'.")
    
    def info_videos (self):
        for video in self.videos:
            video.info()


canal_blackcats = Canal("Black Cats", "Canal de gatos pretos", 100000)
canal_cats = Canal("Cats", "Canal de gatos", 50000) 
canal_pedrinhogamer = Canal("Pedrinho Gamer", "Canal de games", 200000)

video_gato = Video('Gato Preto', 'Um vídeo de um gato preto', '2024-06-01')
video_gato2 = Video('Gato Branco', 'Um vídeo de um gato branco', '2024-06-02')  

playlist_gatos = Playlist('Gatos')
playlist_gatos.adicionar_video(video_gato)
playlist_gatos.adicionar_video(video_gato2)

canal_blackcats.adicionar_playlist(playlist_gatos)

canal_blackcats.info_playlists()