#Capítulo 1 - O Retrato

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

# Personagens
define dorian = Character("Dorian Gray", color="#E8D845", callback=dorian_bounce)
define basil = Character("Basil Hallward", color="#C0C839", callback=basil_bounce)
define henry = Character("Henry Wotton", color="#ED6101", callback=henry_bounce)

# Variável que armazena a decisões ruins.
default escolhasRuins = ""

# O jogo inicia aqui.
label capitulo_1:

    #Parte 1 - Henry e Basil conversando sobre o quadro

    scene capitulo1-transicao with fade
    pause
    scene casa-basil-frente-1 with Dissolve(2.0)

    "O intenso perfume de rosas impregnava o ar. A leve brisa espalhava o aroma do lilás."

    henry "Esta é sua melhor obra, Basil. O Melhor Trabalho da sua vida."
    
    basil "Ainda faltam alguns detalhes, Hery. Assim que Dorian Gray voltar a posar, poderei terminá-lo."

    "As belas sombras dos pássaros movimentavam-se sobre as longas cortinas de seda indiana, que estavam penduradas nas imensas janelas."

    scene henry-basil-olhando-quadro with fade
    
    henry "É maravilhoso. Você deve expor a obra na galeria Grosvenor no ano que vem."

    scene casa-basil-interior with fade
    show basil-neutro at right with dissolve
    
    basil "Não desejo expor a obra, Henry. Não vou enviá-la para nenhuma galeria."
    basil "Coloquei muito de mim aí. Há parte da minha vida ilustrada neste quadro."

    show henry-neutro at left, position_right with dissolve
    
    henry "Não diga bobagem, Basil."
    
    basil "Você não entende. Quando conheci o modelo deste quadro senti que tinha diante de mim alguém que iria absorver toda a minha existência, minha arte, minha alma."
    basil "Por favor, não tire de mim aquele que dá à minha arte todo o encanto que ela possui."
    
    henry "Tem que me apresentá-lo."
    
    basil "Não precisa mais esperar, Henry, ele está logo alí, olhe pela janela!"

    #Parte 2 - Dorian entra na casa de Basil, conhece Henry e posa para o quadro.

    scene dorian-entrando-casa-basil with fade
    pause
    scene casa-basil-interior with fade
    hide henry-neutro with dissolve
    hide basil-neutro with dissolve
    show dorian-neutro at left, position_left with dissolve
    
    dorian "Bom dia, Basil. Perdoe-me, não sabia que tinha companhia. Quem é?"

    show basil-neutro at right with dissolve
    
    basil "Bom dia, Dorian. Este é o Lorde Henry Wotton, Dorian, um velho amigo."

    hide basil-neutro with dissolve
    show henry-neutro at right, position_left with dissolve
    
    dorian "Olá, Henry. Já me falaram muito sobre o senhor… E suas vítimas…"
    dorian "O senhor é de fato uma má influência, Senhor Henry?"

    show henry-neutro at right, position_left with dissolve
    
    henry "Hmm... Influenciar as pessoas é dar-lhes uma alma, senhor Gray. Seus pecados são emprestados, o medo governa as pessoas. Assim como a sociedade a moral, Deus."
    henry "Para não sermos vistos como selvagens, vivemos na auto-negação. E isso deforma nossa vida."
    henry "O senhor, no entanto, que se encontra na flor da idade, teve paixões que o assustaram, além de sonhos e desejos que o deixam cheio de vergonha."
    
    dorian "O senhor me desconcerta. Nem sei o que dizer. Preciso pensar…"

    #hide henry-neutro with dissolve
    show basil-neutro at center with dissolve
    
    basil "Desculpa interromper a conversa de vocês, acredito que o estava ótimo, mas… Dorian, já que está aqui, podes terminar de posar para a minha obra? É rapidinho, faltam só alguns detalhes, eu juro."
    
    dorian "Sim, claro, leve o tempo que quiser, Basil."

    hide basil-neutro with dissolve
    hide dorian-neutro with dissolve
    hide henry-neutro with dissolve

    scene dorian-posando with fade
    pause
    
    basil "Consegui dar-lhe uma expressão maravilhosa. Pode descansar, Dorian. Só preciso completar o fundo. Aproveite para terminar aquele papo com Henry."

    dorian "Vai ser um prazer."
    
    henry "Sim, vai ser um prazer."

    #Parte 3 - Dorian e Henry conversando sobre a juventude, a beleza e o tempo enquanto caminha pelo jardim.

    scene dorian-henry-caminhando-jardim with fade
    pause

    scene jardim-basil with fade

    show dorian-neutro at left, position_left with dissolve
    show henry-neutro at right, position_left with dissolve
    
    henry "Vamos nos sentar à sombra. Se o senhor ficar mais tempo sob o sol, perderá essa bela cor e isso seria uma pena. O senhor possui uma fantástica juventude, e a juventude é o que temos de melhor."
    
    dorian "Não sinto isso. Isso não é verdade."
    
    henry "Hmm… Quando for velho, feio e cheio de rugas, e tiver a testa cheia de dobras o senhor saberá. Agora, possui o mundo em suas mãos. A beleza é um dos grandes dons da natureza, como a luz é do sol."
    henry "Quando sua juventude acabar, a beleza vai desaparecer, e vai descobrir que já não tem nenhum triunfo. O tempo tem inveja do senhor."
    
    dorian "O senhor está me deixando nervoso e ansioso. O tempo é algo completamente normal a todo ser, não há o que temer."
    
    henry "O TEMPO NÃO É ATERRORIZANTE?! Hã… Vou dar um conselho ao senhor:"
    henry "Desfrute! Desfrute plenamente da juventude enquanto a possui. Não malgaste seus dias tentando redimir os fracassados que não têm esperança, muito menos desperdiçando sua vida com pessoas medíocres."
    henry "Viva! Viva esta vida maravilhosa que pertence ao senhor. Busque novas sensações. O mundo lhe pertence!"
    
    dorian "Eeee..."
    
    henry "Entendeu o conselho, Dorian? Entendeu?"
    
    dorian "Eeee... Sim..."
    dorian "..."

    henry "Hahaha! Não fique nervoso jovem. Olhe, siga o meu conselho, você não se arrependerá!"

    dorian "Eeee… Não estou nervoso, Senhor Henry, só um pouco… Pensativo… Hmmm..."

    basil "HEY!"

    dorian "Hã!? Olhe, é Basil chamando."

    hide henry-neutro with dissolve
    hide dorian-neutro with dissolve

    #Parte 4 - Dorian, Henry e Basil vendo o quadro terminado e Dorian fazendo um pedido.

    scene basil-chamando-henry-dorian with fade

    basil "HEY! HENRY! DORIAN! TERMINEI! VENHAM VER O RETRATO!"

    scene retrato-dorian with fade
    pause

    basil "Quando secar, enviarei para sua casa, Dorian."
    
    henry "É incrivelmente bonito."
    
    dorian "Hmm…"
    
    basil "O que houve, Dorian, não gostou?"
    
    dorian "Claro que adorei. Você fez um ótimo trabalho como sempre, Basil. É que, na verdade, o quadro é meio… Triste."

    basil "O que tem de triste? Ele é tão bonito, tão cheio de vida, tão cheio de juventude."
    
    dorian "Esse é o problema, um dia eu serei velho, feio e assustador, mas este quadro sempre me fará jovem. Nunca esquecerei este dia de primavera."
    dorian "Se fosse contrário… Se eu pudesse me manter jovem para sempre, e o retrato envelhecesse! Eu daria… Daria qualquer coisa por isso…"
    dorian "Até a minha alma!"

    #Parte 5 - Dorian guardando o retrato no sótão.

    scene dorian-retornando-casa with fade

    dorian "Ufa, finalmente em casa. Foi uma longa caminhada até aqui."

    scene dorian-olhando-retrato with fade

    dorian "Basil realmente se superou nesta pintura. Pena que não há espaço para pendurá-lo."
    dorian "..."
    dorian "Hããã! Só estou enganando a mim mesmo, tem espaço de sobra para pendurá-lo. Eu só… Eu só não quero ficar olhando para meu auto retrato e saber que um dia não serei mais assim…"
    dorian "Maldito Lorde Henry, aquela conversa que tivemos no jardim vai maturar na minha cabeça durante semanas."
    dorian "O que eu vou fazer? Hmmm… Já sei! Vou pendurá-lo no sótão, aí não preciso vê-lo todo santo dia."

    scene dorian-sotao with fade

    dorian "Cof, cof, cof. Aqui está bem empoeirado, tenho que contratar uma faxina. Enfim, isso não importa agora. Aquele é o local ideal para o quadro."

    scene retrato-sotao with fade

    dorian "Se eu deixar o quadro à mostra, ele irá estragar com o tempo com toda essa poeira. Hmmm… Preciso cobri-lo com um pano."

    scene retrato-sotao-coberto with fade

    dorian "Perfeito! Espero que Basil não fique chateado por ter feito isto com sua obra. Quando esse pensamento bobo sobre juventude sair da minha mente, penduro ele em um local de respeito. Mas até lá, ele ficará aí!"

    # Fim do capítulo 1.

    # Carrega o script do capítulo 2.
    jump capitulo_2