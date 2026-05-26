# Efeito de bounce para os personagens quando falarem.
transform bounce:
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    repeat 1

# Programação do bounce para os personagens.
init python:

    def dorian_bounce(event, interact=True, **kwargs):

        if event == "show":

            if renpy.showing("dorian-neutro"):

                renpy.show(
                    "dorian-neutro",
                    at_list=[bounce]
                )


    def basil_bounce(event, interact=True, **kwargs):

        if event == "show":

            if renpy.showing("basil-neutro"):

                renpy.show(
                    "basil-neutro",
                    at_list=[bounce]
                )


    def henry_bounce(event, interact=True, **kwargs):

        if event == "show":

            if renpy.showing("henry-neutro"):

                renpy.show(
                    "henry-neutro",
                    at_list=[bounce]
                )

# Inverte a posição horizontal para esquerda, para que o personagem olhe para o outro.
transform position_left:
    xzoom 1.0

# Inverte a posição horizontal para direita, para que o personagem olhe para o outro.
transform position_right:
    xzoom -1.0

define dorian = Character("Dorian Gray", color="#E8D845", callback=dorian_bounce)
define basil = Character("Basil Hallward", color="#C0C839", callback=basil_bounce)
define henry = Character("Henry Wotton", color="#ED6101", callback=henry_bounce)
define ator = Character("Ator(a)", color="#AAAAAA")
define desconhecido = Character("Desconhecido", color="#888888")
define sibyl = Character("Sibyl Vane", color="#FF69B4")

# O jogo inicia aqui.
label capitulo_2:

    dorian "\"... Sinto que estou em perigo... Mas essa simples sensação me enche de deleite, o senhor Henry disse que a busca pela beleza é o verdadeiro segredo da vida.\""
    dorian "\"Talvez eu a encontre em algumas dessas vidas... Ao menos isso me enche de curiosidade.\""

    dorian "\"Um teatro! Faz tanto tempo que não vou a um. O show vai começar daqui 30 minutos.\""
    dorian "\"Bem... Já que estou com bastante tempo livre...\""
    dorian "Um ingresso de camarote para a apresentação de agora!"

    dorian "\"Ora, ora... Vão apresentar Romeu e Julieta.\""
    dorian "\"Hã... O cenário é ainda mais pobre que a orquestra...\""
    dorian "\"O show já vai começar, finalmente!\""

    ator "Ama, e minha filha? Peça que venha."
    ator "Oh, mas eu já não pedi que viesse. Ei, Pombinha! Rainha! Santo Deus, onde está essa menina… Julieta!"

    dorian "\"Hã, que show deprimente! acho melhor ir embora...\""

    sibyl "Quem está me chamando? Estou aqui. O que deseja, senhora?"

    dorian "\"Santo Deus! Que... Perfeição!\""

    sibyl "Ama-me? Sei que dirá que sim, e eu Acreditarei. Ah, gentil Romeu, se de fato me ama, apenas diga."

    dorian "\"E desde então, eu fui todos os dias.\""

    sibyl "Onde está a sua cabeça? Onde? Ohh! Onde está?..."

    dorian "\"Às vezes, ela resplandece como Imogênia em 'Cymbeline'... \""

    sibyl "Otelo, não me mate!"

    dorian "\"Outro dia, o cruel Otelo apertou seu pescoço!\""

    desconhecido "Com licença, senhor… Por acaso, é um jornalista? O senhor vem com bastante frequência."

    dorian "Não, não so... QUER DIZER! SOU SIM! SOU SIM!"
    dorian "Ahhh... Estou entrevistando os atores do para... Ehh... Escrever e publicar um artigo sobre o teatro local. Já contactei todos, só falta aquela bela moça alí."

    desconhecido "Ahhh, você está falando da Sibyl Vane! Nesse caso, levarei o senhor para conhecer a atriz mais extraordinária de todos os tempos!"

    dorian "vai ser um prazer!"
    dorian "\"Sibyl Vane, que nome lindo.\""

    desconhecido "Ei, Sibyl, este jornalista quer entrevista-a, é para um artigo."

    dorian "Ehhh... Olá!"

    sibyl "Ohh, um jornalista!? Querendo me entrevistar!? Uau, que inesperado. Vai ser um prazer. Por favor, entre!"

    sibyl "Obrigada por assistir à minha atuação, milorde."

    dorian "Não sou milorde, senhorita. Não me chame assim!"

    sibyl "Então o chamarei de 'príncipe encantado'. É assim que o senhor me parece."

    henry "Caramba, Dorian, você não para de falar sobre essa tal garota. Você fala como se estivesse apaixonada por ela!"

    dorian "E estou! Henry, Sibyl Vane é sagrada."

    henry "Hmm... Que lugar estranho para se encontrar uma deusa."

    dorian "É verdade, encontrei-a aqui, e ela é a encarnação da divindade. Essas pessoas medíocres, de rostos primitivos e gestos brutais, transformam-se quando Sibyl entra em cena."
    dorian "Elas ficam caladas e escutam, choram e riem, exatamente como Sibyl quer que o façam. Eles sentem que foram feitos da mesma carne de nós."

    basil "Shhh!!! Façam silêncio, a peça vai começar."

    dorian "Daqui a pouco Sibyl entra em cena, senhores."

    basil "Estou ansioso para vê-la."

    henry "Eu também. Quero ver se essa tal de Sibyl é tudo o que Dorian diz."

    dorian "É AGORA! É ELA! É AGORA! SIBYL!"

    sibyl "bondoso peregrino fazeis injustiça à vossa mão…"

    basil "Mas..."

    henry "É uma voz maravilhosa, mas não há emoção. Não expressa nada. Parece uma aluna em uma peça escolar."

    dorian "Não diga isso, Henry!"
    dorian "\"Eu não entendo, não entendo.... O que há com ela? Será que adoeceu e não me falou? Deve haver alguma explicação...\""
    dorian "Vamos esperar a cena da varanda. Não vamos julgá-la ainda."

    sibyl "se não fosse a noite a ocultar-me com seu véu minhas bochechas ficariam ruborizadas pelo que disse antes como eu gostaria de seguir as regras e negar o que foi dito ama-me sei que dirás que sim, e eu vou acreditar romeu"

    basil "... Patético..."

    henry "Basil está certo, simplesmente patético. Vamos embora!"

    dorian "NÃO! ESPEREM!"

    henry "Ela é de fato formosa, Dorian, mas incapaz de interpretar. Vamos!"

    basil "Até mais, Dorian."

    dorian "Peço-lhes desculpa... Senhores..."
    dorian "..."
    dorian "\"Por quê? ... Por quê? ... O que será que houve? Exijo explicações!\""

    sibyl "Oh, meu Príncipe Encantado! Hahaha, como atuei mal esta noite! Hahaha!"

    dorian "O que há de engraçado? Foi terrivelmente mal! Foi de espantar! Está doente? Não imagina como sofri."

    dorian "Você não deveria representar quando está doente. Meus amigos ficaram aborrecidos."

    sibyl "O porquê de eu ter atuado tão mal; Porque nunca mais voltarei a atuar bem. Você deveria ter compreendido. Mas entendeu agora, certo?"

    dorian "Entender o quê, Sibyl?"

    sibyl "Príncipe Encantado, antes de você atuar era minha única realidade. Acreditava que tudo o que acontecia no teatro era verdade… Tudo! Mas você, Meu Grande Amor, libertou minha alma. Você me ensinou o que é a realidade."
    sibyl "Esta noite, pela primeira vez, eu vi o vazio, a mentira: que Romeu não passa de um velho maquiado, que a lua está pintada, e que as palavras não eram minhas. A arte nada mais é do que um reflexo do amor. O amor! Meu amor!"

    dorian "VOCÊ MATOU O MEU AMOR!"

    sibyl "O quê? Não está falando sério, não é, Príncipe Encantado? Está apenas atuando…"

    dorian "Você matou o meu amor! Eu amava você porque era maravilhosa... Porque era um gênio e inteligente, pois tornava real os sonhos de grandes poetas e dava forma e sentido às sombras da arte."
    dorian "Mas você é superficial e estúpida. Santo Deus! Como fui louco por amá-la. Que idiota eu fui. Nunca mais voltarei a vê-la. NUNCA!"

    sibyl "Não! Não me deixe! Farei o que quiser! Eu o amo mais que tudo no mundo! E…"

    sibyl "Não! Não! Não me deixe!"

    return