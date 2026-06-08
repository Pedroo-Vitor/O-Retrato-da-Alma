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
define naoRevelado = Character("???", color="#FFFFFF")

# Variável que armazena a decisões ruins.
default escolhasRuins = ""

# O jogo inicia aqui.
label capitulo_1:

    #Parte 1 (Introdução) - Henry e Basil conversando sobre o quadro

    scene capitulo1-transicao with fade
    pause
    scene casa-basil-frente-1 with Dissolve(2.0)

    "O intenso perfume de rosas impregnava o ar. A leve brisa espalhava o aroma do lilás."

    henry "Esta é sua melhor obra, Basil. O Melhor Trabalho da sua vida."
    
    basil "Ainda faltam alguns detalhes, Henry. Assim que o modelo voltar a posar, poderei terminá-lo."

    "As belas sombras dos pássaros movimentavam-se sobre as longas cortinas de seda indiana, que estavam penduradas nas imensas janelas."

    scene henry-basil-olhando-quadro with dissolve
    
    henry "É maravilhoso. Você deve expor a obra na galeria Grosvenor no ano que vem."

    scene casa-basil-interior with fade
    show basil-neutro at right with dissolve
    
    basil "Não desejo expor a obra, Henry. Não vou enviá-la para nenhuma galeria. oloquei muito de mim aí. Há parte da minha vida ilustrada neste quadro."

    show henry-neutro at left, position_right with dissolve
    
    henry "Hahaha!"
    
    basil "Sabia que ia rir, mas da mesma forma é verdade. Por favor, não tire de mim aquele que dá à minha arte todo o encanto que ela possui."
    
    henry "Sem dúvida não há qualquer semelhança entre você e o jovem Adônis.Você tem uma expressão intelectual, e o intelecto destroi a beleza de qualquer rosto. Não fique lisonjeado, Basil, mas você não é nada igual a ele."
    
    basil "É lógico que não sou igual a ele, e fico satisfeito."

    henry "Sempre teve uma paixão por virtude, Basil. Por que sua alegria de não ser como ele?"

    basil "Sofremos pelo o que os deuses nos dão. E creio que, Dorian Gray, pagará por sua beleza."

    henry "Dorian Gray. Então esse é o nome do modelo de sua obra."

    basil "..."
    basil "É… Não tinha a intenção de te contar."

    henry "Porque não pretendia me dizer o nome dele?"

    basil "Eu não vou explicar. Quanto mais velho fico, mais gosto de mistérios. Deve parecer tolice para você."

    henry "Não me parece tolice nenhuma. Esquece que eu sou casado e que o encanto do casamento é o que torna uma vida de decepção absolutamente necessária para ambas as partes."

    basil " Eu acredito que seja realmente um bom marido, Henry, mas é totalmente envergonhado de suas próprias virtudes. Seu cinismo é simplesmente podre."

    henry "Ser natural é só afetação e a posse mais irritante que conheço. Mas ainda não respondeu a minha pergunta, quero saber o motivo de não exibir o retrato de Dorian Gray."

    basil "Há realmente muito pouco a contar, Henry. Além do mais, dificilmente acreditará."

    henry "Acredito em qualquer coisa, portanto que seja bem incrível."

    basil "Eu acho que é o que parece. Há alguma coisa em que… Que não consigo entender… Qualquer coisa de místico…"

    henry "Místico?"

    basil "Eu não sei como explicar, mas…Toda vez que Dorian posa para mim, é como se uma força fora de mim mesmo estivesse guiando a minha própria mão. É como se o quadro tivesse vida própria, independente de mim. É por isso que não vou expô-lo. Pertence por direito a Dorian Gray, e eu devo dar a ele."
    henry "Quero conhecer esse jovem extraordinário. Creio que seremos amigos. Sempre escolho os amigos pela boa aparência e os inimigos pelo bom intelecto. Um homem não pode ser zeloso demais na escolha de inimigos"

    basil "Henry, desprezo seus princípios, mas me agrada a maneira como os expressas. Além disso, não quero que conheça Dorian Gray e eu vou fazer o possível para isso se tornar realidade. Prometo a mim mesmo."

    henry "E porque?"

    basil "Você sabe muito bem, Henry. Você sabe muito bem..."

    scene henry-basil-ouvindo-batidas-na-porta with dissolve
    pause(0.8)

    naoRevelado "Basil, abre a porta."

    henry "Hahaha! Parece que essa promessa não durou muito tempo."

    basil "Droga."

    scene dorian-batendo-na-porta-de-basil with dissolve
    pause(0.8)

    dorian "Basil, vem abrir a porta, sou eu, Dorian!"

    basil "Já vai! Já vai!"

    # Parte 2 - Dorian entra na casa de Basil, conhece Henry e posa para o quadro.

    scene casa-basil-interior with fade
    hide henry-neutro with dissolve
    hide basil-neutro with dissolve
    show dorian-neutro at left, position_left with dissolve
    
    dorian "Bom dia, Basil. Perdoe-me, não sabia que tinha companhia. Quem é?"

    show basil-neutro at right with dissolve
    
    basil "Bom dia, Dorian. Este é o Lorde Henry Wotton, Dorian, um velho amigo."

    hide basil-neutro with dissolve
    show henry-neutro at right, position_left with dissolve
    
    menu:
        "*Cumprimentar com educação*":
            dorian "Olá, Lorde Henry."

            henry "Um prazer, senhor Gray. Basil realmente foi modesto ao descrevê-lo."

        "Espero não estar interrompendo.":
            dorian "Olá, Lorde Henry. Espero não estar interrompendo."

            henry "Pelo contrário. Interrupções belas quase sempre melhoram uma manhã."

    henry "Vejo que Basil realmente transmitiu a beleza de sua aparência naquele quadro de forma precisa. Pena que não será assim para sempre, não é mesmo, senhor Dorian Gray."

    menu:
        "*Estranhar o comentário.*":
            dorian "Nossa… Humm… Que coisa estranha para se dizer a alguém que acabou de conhecer…"

            henry "As coisas estranhas costumam ser as únicas que merecem ser ditas."

        "Responder sem saber o que dizer.":
            dorian "Eu… Não sei como responder a isso."

            henry "Excelente. As melhores conversas começam quando alguém perde a resposta."

        "*Tentar não parecer afetado*":
            dorian "O senhor fala de um modo curioso."

            henry "Curioso é apenas o nome educado que damos ao perigoso quando ele nos diverte."

    show basil-neutro at center, position_right with dissolve

    basil "Henry, eu quero terminar esse quadro hoje. Será que seria grosseria minha pedir para ir embora?"

    henry "Devo ir, Senhor Gray?"

    menu:
        "*Pedir que Henry fique.*":
            dorian "Fique, não vejo problema nenhum."

            henry "Muito gentil de sua parte."

        "*Deixar Basil decidir.*":
            dorian "Não quero atrapalhar o trabalho de Basil."

            show basil-neutro at center, position_left with dissolve
            basil "Você não atrapalha, Dorian. Henry é quem costuma fazer isso."

            henry "E sempre com grande elegância."

    henry "Não vai se incomodar. Vai, Basil? Gosta que seus modelos conversem com alguém."

    show basil-neutro at center, position_right with dissolve
    basil "Então fique a vontade."
    show basil-neutro at center, position_left with dissolve 
    basil "Dorian, vá ao seu lugar e não dê nenhuma atenção que o Lorde Henry diz. Ele exerce má influência sobre seus amigos, sendo eu a única exceção."

    hide basil-neutro with dissolve
    hide dorian-neutro with dissolve
    hide henry-neutro with dissolve

    scene dorian-posando with fade
    pause
    
    basil "Consegui dar-lhe uma expressão maravilhosa. Pode descansar, Dorian. Só preciso completar o fundo."

    henry "Enquanto Basil termina o seu retrato, vamos dar um passeio pelo jardim para nos conhecer melhor. Que tal, Senhor Gray?"

    menu:
        "*Aceitar com educação*":
            dorian "Sim. Gostaria de conversar melhor com o senhor."

        "*Aceitar ainda inseguro*":
            dorian "Bem… Se Basil não se importar, eu aceito."

    basil "Quando eu terminar eu chamo vocês. Ah… E lembre-se, Dorian: Henry é má influência, não siga os seus conselhos!"

    #Parte 3 - Dorian e Henry conversando sobre a juventude, a beleza e o tempo enquanto caminha pelo jardim.

    scene dorian-henry-caminhando-jardim with fade
    pause

    scene jardim-basil with dissolve

    show dorian-neutro at left, position_left with dissolve

    menu:
        "O senhor realmente exerce má influência?":
            dorian "O senhor realmente exerce má influência, Lorde Henry?"

        "Basil fala como se o senhor fosse perigoso":
            dorian "Basil fala como se o senhor fosse perigoso. Pensei que vocês fossem amigos."

            henry "E nos somos amigos, mas, basil, sabe que eu tenho um incrível poder de persuasão. Meus conselhos são influentes."

    show henry-neutro at right, position_left with dissolve

    henry "Uma coisa que não existe é uma boa influência, Senhor Gray. Toda influência é imoral."

    dorian "Por quê?"

    henry "Porque o objetivo da vida é autodesenvolvimento, perceber perfeitamente sua natureza. É por isso que estamos aqui. Um homem deve viver sua vida total e completamente, dar forma a cada sentimento, expressão a cada pensamento, realidade a cada sonho."
    henry "Cada impulso que reprimimos remoi na mente e nos envenena. Só há uma maneira de se livrar de uma tentação é cedendo a ela. Resistir? A alma fica doente. Não há algo que possa curar a alma se não os sentidos, como nada há que possa curar os sentidos se não a alma."

    menu:

        "*Discordar*":
            dorian "Discordo, mas suas palavras me deixam inquieto."

            henry "A inquietação é um excelente começo, Senhor Gray."

        "*Concordar*":
            dorian "É estranho, mas... De certa forma é verdade..."

            henry "Naturalmente. As ideias perigosas costumam ser as únicas realmente interessantes e verdadeiras."

        "*Refletir*":
            dorian "O senhor me desconcerta. Nem sei o que dizer. Preciso pensar…"

    henry "Vamos nos sentar à sombra. Se o senhor ficar mais tempo sob o sol, perderá essa bela cor e isso seria uma pena. O senhor possui uma fantástica juventude, e a juventude é o que temos de melhor."

    menu:
        "*Negar a importância da juventude*":
            dorian "Não sinto isso. Isso não é verdade."

        "*Concordar a importância da juventude*":
            dorian "Talvez o senhor tenha razão. Nunca pensei na juventude como algo tão precioso."
            henry "É natural. Os jovens raramente percebem o valor da juventude enquanto a possuem. É como respirar: só se entende sua importância quando começa a faltar."

        "*Perguntar sobre a juventude*":
            dorian "O senhor fala da juventude como se fosse uma espécie de poder."

            henry "E é, meu caro Dorian. O poder mais delicado e mais breve de todos."

    henry "Quando for velho, feio e cheio de rugas, e tiver a testa cheia de dobras o senhor saberá. Agora, possui o mundo em suas mãos. A beleza é um dos grandes dons da natureza, como a luz é do sol."
    henry "Quando sua juventude acabar, a beleza vai desaparecer, e vai descobrir que já não tem nenhum triunfo. O tempo tem inveja do senhor."

    menu:
        "O tempo é algo completamente normal.":
            dorian "O tempo é algo completamente normal a todo ser. Todos envelhecem. Talvez não haja razão para ter medo disso."

            henry "Essa é uma frase muito confortável. Infelizmente, conforto raramente é verdade."

        "Um dia tudo isso pode desaparecer.":
            dorian "É estranho imaginar que um dia tudo isso pode desaparecer."

            henry "Não é estranho, Dorian. É trágico."

    henry "Vou dar um conselho ao senhor: Desfrute! Desfrute plenamente da juventude enquanto a possui. Não malgaste seus dias tentando redimir os fracassados que não têm esperança, muito menos desperdiçando sua vida com pessoas medíocres."
    henry "Viva! Viva esta vida maravilhosa que pertence ao senhor. Busque novas sensações. O mundo lhe pertence!"
    henry "Entendeu o conselho, Dorian?"

    menu:
        "Sim, mas discordo":
            dorian "Sim, entendi. Mas não sei se concordo. Uma vida guiada apenas por prazeres me parece perigosa."

            henry "Perigosa? Sem dúvida. Mas as coisas seguras raramente transformam alguém."
            henry "Ainda assim, gosto da sua resistência. Ela tornará sua queda, caso aconteça, muito mais interessante."


        "Sim, e concordo":
            dorian "Sim. Talvez o senhor tenha razão. Talvez eu deva aproveitar mais a vida enquanto ainda posso."

            henry "Excelente, Dorian. Essa é a primeira resposta verdadeiramente jovem que ouvi de você."
            henry "A juventude só se torna trágica quando é desperdiçada tentando parecer prudente."


        "Preciso refletir mais":
            dorian "Entendi o que o senhor quis dizer, mas preciso refletir mais. Suas palavras me deixaram inquieto."

            henry "A inquietação é um ótimo começo."

    basil "HEY!"

    dorian "Hã!? Olhe, é Basil chamando."

    hide henry-neutro with dissolve
    hide dorian-neutro with dissolve

    #Parte 4 - Dorian, Henry e Basil vendo o quadro terminado e Dorian fazendo um pedido.

    scene basil-chamando-henry-dorian with fade

    basil "HEY! HENRY! DORIAN! TERMINEI! VENHAM VER O RETRATO!"

    scene retrato-dorian with fade
    pause

    basil "Quando secar, pode levar para sua casa, Dorian."
    
    henry "É incrivelmente bonito. Ainda acho que deve expô-lo, Basil."
    
    dorian "Hmm…"
    
    basil "O que houve, Dorian, não gostou?"
    
    dorian "Claro que adorei. Você fez um ótimo trabalho como sempre, Basil. É que, na verdade, o quadro é meio… Triste."

    basil "O que tem de triste? Ele é tão bonito, tão cheio de vida, tão cheio de juventude."
    
    dorian "Esse é o problema, um dia eu serei velho, feio e assustador, mas este quadro sempre me fará jovem. Nunca esquecerei este dia de primavera."
    dorian "Se fosse contrário… Se eu pudesse me manter jovem para sempre, e o retrato envelhecesse! Eu daria… Daria qualquer coisa por isso…"
    dorian "Até a minha alma!"

    basil "Agora você entende porque não queria que Dorian conhecesse você, Henry. Olha o que você fez com a cabeça dele em apenas 3 horas."
    basil "Talvez uma xícara de chá o faça recuperar-se, Dorian. Irá tomar também, não é, Henry? Ou se opõe a esses prazeres simples?"

    henry "Adoro prazeres simples, são os últimos refúgios do complexo."

    #Parte 5 (Final) - Dorian guardando o retrato no sótão de sua casa.

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