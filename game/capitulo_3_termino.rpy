# Capítulo 2 - Familia Campbell

# Efeito de bounce para os personagens quando falarem.
transform bounce:
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    # repeat 1

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
    
    def alan_bounce(event, interact=True, **kwargs):

        if event == "show":

            if renpy.showing("alan-neutro"):

                renpy.show(
                    "alan-neutro",
                    at_list=[bounce]
                )
    
    def elizabeth_bounce(event, interact=True, **kwargs):

        if event == "show":

            if renpy.showing("elizabeth-neutro"):

                renpy.show(
                    "elizabeth-neutro",
                    at_list=[bounce]
                )
    
    def gladys_bounce(event, interact=True, **kwargs):

        if event == "show":

            if renpy.showing("gladys-neutro"):

                renpy.show(
                    "gladys-neutro",
                    at_list=[bounce]
                )


# Inverte a posição horizontal para esquerda, para que o personagem olhe para o outro.
transform position_left:
    xzoom 1.0

# Inverte a posição horizontal para direita, para que o personagem olhe para o outro.
transform position_right:
    xzoom -1.0

# Definições dos personagens (caso ainda não estejam definidas)
define narrador = Character("Narrador", color="#AAAAAA")
define dorian = Character("Dorian Gray", color="#E8D845", callback=dorian_bounce)
define basil = Character("Basil Hallward", color="#C0C839", callback=basil_bounce)
define henry = Character("Henry Wotton", color="#ED6101", callback=henry_bounce)
define alan = Character("Alan Campbell", color="#6C472A", callback=alan_bounce)
define elizabeth = Character("Elizabeth Campbell", color="#FAF2DE", callback=elizabeth_bounce)
define gladys = Character("Gladys Campbell", color="#9B59B6", callback=gladys_bounce)
define mordomo = Character("Mordomo", color="#888888")

# Capítulo 3: Família Campbell
label capitulo_3_termino:

    scene capitulo3-transicao with fade
    pause
    scene black with fade
 
    "Um mês havia se passado desde aquela noite no teatro."

    # Parte 1 - Basil e Dorian conversando antes da viagem de Basil para Paris.
    scene dorian-pensativo-em-sua-casa with fade

    dorian "\"Lorde Henry disse que a juventude deve buscar novas sensações… Que não devo desperdiçar meus dias com arrependimentos... Será que... Sibyl era de fato um fracasso? ...\""

    scene dorian-assustado with dissolve
    pause(0.8)
    scene porta-dorian with dissolve

    dorian "\"Batidas na porta de minha casa neste horário?\""

    dorian "Quem é?"

    basil "Sou eu, Dorian, Basil."

    scene casa-dorian with fade
    
    show basil-neutro at right, position_left with dissolve

    basil "Boa noite, Dorian. Perdoe-me por vir tão tarde. Eu precisava vê-lo antes de partir."

    show dorian-neutro at left, position_left with dissolve

    dorian "Partir?"

    basil "Sim. Amanhã pela manhã viajarei para Paris. Ficarei fora por três meses. Há encomendas, galerias e pessoas insistentes demais para serem ignoradas. Mas confesso que essa viagem também me servirá como descanso."

    dorian "Três meses é muito tempo, Basil."

    basil "É. Por isso vim vê-lo. Não queria partir sem antes conversar com você."
    basil "Dorian, desde que conheceu Henry, algo em você parece inquieto. Não digo isso por ciúmes ou por capricho. Henry é meu amigo, mas conheço bem o perigo das palavras dele. Ele tem o talento terrível de fazer uma ideia ruim parecer bela, e uma escolha cruel parecer apenas coragem."

    dorian "Basil, você exagera."

    basil "Talvez. Mas prefiro exagerar por cuidado a me calar por covardia. Tome cuidado com Henry enquanto eu estiver fora. Ele não obriga ninguém a cair, mas sabe muito bem como abrir uma janela e elogiar a vista."

    dorian "Você fala como se ele fosse meu inimigo."

    basil "Não. Falo como se ele fosse uma influência. E você ainda é jovem demais para perceber quando uma influência começa a falar com a sua própria voz. Enquanto eu estiver fora, promete que não deixará Henry convencê-lo de que a beleza é a única coisa que vale a pena na vida?"

    dorian "Prometo, Basil. Não vou deixar Henry me convencer disso."

    basil "Ótimo. Confio em você, Dorian."

    basil "Lembre-se: beleza é um dom, não uma desculpa. Se um dia começar a acreditar que sua aparência o coloca acima dos outros, então Henry terá vencido sem precisar dizer mais nada."
    basil "Amanhã meu trem parte cedo, as 8 da manhã. Gostaria que fosse à estação se despedir de mim."

    dorian "Irei."

    basil "Obrigado. E lembre-se do que conversamos."

    dorian "Lembrarei."

    scene manha-seguinte with fade
    pause
    scene basil-dorian-henry-trem with fade

    # Parte 2 - Dorian e Henry conversando na estação de trem depois de se despedirem de Basil.

    basil "TCHAU, LORDE HENRY! TCHAU, DORIAN! TOME CUIDADO! NÃO ESQUEÇA DA NOSSA CONVERSA!"

    dorian "TCHAU, BASIL! NÃO ESQUECEREI!"

    henry "Até logo, Basil Hallward. Tente não transformar Paris em um confessionário!"

    pause(1.0)

    scene estacao-trem with dissolve
    show henry-neutro at right, position_left with dissolve

    henry "Hahaha!"

    show dorian-neutro at left, position_left with dissolve

    dorian "Qual é a graça, Senhor Henry?"

    henry "\"Tome cuidado, Dorian!\". Basil realmente te trata como uma criança de oito anos."

    henry "É curioso como Basil confunde amizade com vigilância. Ele possui uma alma boa, sem dúvida, mas almas boas costumam ser terrivelmente cansativas."

    dorian "Ele só quer o meu bem."

    henry "Sem dúvida. Esse é justamente o defeito dele. Pessoas muito boas desejam salvar o mundo inteiro e, quando não conseguem, começam a salvar os amigos por falta de opção."

    henry "Mas me diga, Dorian, que conversa tão grave foi essa? Basil falou meu nome com aquele tom de quem anuncia uma doença?"

    dorian "Ele me disse para tomar cuidado com o senhor."

    henry "Naturalmente. Basil nasceu preocupado. Se o mundo acabasse, ele choraria e pediria desculpas pelas rachaduras no céu."

    henry "Ele teme minhas palavras porque sabe que palavras são perigosas. Não por serem falsas, mas por dizerem em voz alta aquilo que as pessoas preferem esconder."

    dorian "Ele também pediu que eu não deixasse o senhor me convencer de que a beleza é a única coisa que vale a pena na vida."

    henry "Ah! Então Basil está mais dramático do que imaginei."

    henry "A beleza não é a única coisa que vale a pena na vida, meu caro. Seria vulgar dizer isso. Mas é, sem dúvida, uma das poucas coisas que a vida obedece sem discutir."

    henry "A bondade precisa explicar-se. A inteligência precisa provar-se. A virtude precisa ser defendida como uma causa perdida. A beleza, porém, entra em uma sala e todos compreendem imediatamente."

    dorian "Isso parece injusto."

    henry "A vida é injusta, Dorian. Alguns sofrem por isso. Outros aprendem a usar a injustiça com elegância."

    henry "Lembra-se do que lhe disse no jardim de Basil? Busque novas sensações. Não desperdice sua juventude tentando provar que pode ser prudente."

    henry "Você precisa conhecer pessoas que entendam isso. Pessoas que não peçam desculpas por admirar o que é belo."

    dorian "Que pessoas?"

    scene henry-entrega-papel-para-dorian with dissolve
    pause

    henry "Hoje à noite haverá um jantar na casa de Alan Campbell. Químico renomado, homem rico, membro respeitado da alta sociedade e dono de opiniões ainda piores que as minhas."

    henry "Basil o considera insuportável, o que sempre me pareceu uma excelente recomendação."

    scene estacao-trem with dissolve
    show henry-neutro at right, position_left with dissolve
    show dorian-neutro at left, position_left with dissolve

    dorian "Não sei se estou disposto a jantar com estranhos."

    henry "Ninguém está disposto a nada até estar bem vestido."

    henry "Vá, Dorian. Não por mim, nem por Alan, nem para contrariar Basil. Vá porque a vida começa quando aceitamos um convite que nos tira do lugar onde todos esperam que permaneçamos."

    henry "Te espero lá às seis em ponto. É na rua por trás da biblioteca Oscar Wilde II; uma casa enorme, cheia de luzes, com uma placa escrita: Residência da Família Campbell."

    henry "Quando chegar, basta dizer ao mordomo que é o convidado mencionado por Lorde Henry Wotton. Ele o deixará entrar."

    henry "E vista sua melhor roupa. A alta sociedade perdoa quase tudo, menos uma aparência descuidada."

    scene dorian-analisando-papel-de-henry with dissolve

    henry "Até o jantar, Dorian."

    dorian "Não prometo que irei, Henry."

    henry "Não precisa prometer. Sei que comparecerá."

    # Parte 3 - jantar na casa da família Campbell.

    scene na-noite-daquele-mesmo-dia with fade
    pause
    scene dorian-defronte-casa-campbell with fade
    pause(1.4)
    scene dorian-batendo-na-porta-da-casa-campbell with dissolve

    mordomo "Quem é?"

    dorian "É o Dorian Gray, o convidado que Lorde Henry Wotton mencionou."

    scene alan-dorian-cumprimentando with dissolve
    pause(0.8)

    alan "Boa noite, Dorian. Finalmente chegou, o jantar começou já faz um tempinho. Por favor, sente-se."
    
    dorian "Ops... Desculpe o atraso. Hehehe..."

    scene henry-eliza-alan-dorian-jantando with dissolve
    pause(1.0)
    scene mesa-jantar-campbell with fade
    show alan-neutro at right, position_left with dissolve

    alan "Então este é o famoso Dorian Gray. Lorde Henry falou muito do senhor."

    show dorian-neutro at left, position_left with dissolve

    dorian "Espero que tenha falado bem."

    alan "Henry nunca fala bem de ninguém. Quando deseja elogiar, apenas ofende com mais entusiasmo."

    alan "Ainda assim, devo admitir: desta vez ele foi econômico. O senhor possui uma aparência rara, senhor Gray. E aparência rara não deve ser tratada com falsa modéstia."

    show henry-neutro at center, position_left with dissolve

    henry "Alan é injusto comigo, Dorian. Eu ofendo todos com igual dedicação."

    alan "Essa talvez seja sua única virtude democrática."

    hide dorian-neutro with dissolve
    show elizabeth-neutra at left, position_right with dissolve

    elizabeth "Alan, por favor. Não comece a destruir nossos convidados antes da sobremesa."

    alan "Minha querida, se um convidado pode ser destruído por uma conversa, então não era um convidado; era um vaso decorativo."

    henry "Viu, Dorian? Eu disse que Alan era pior que eu."

    alan "Henry é cruel por prazer. Eu sou cruel por precisão. Há uma diferença importante."

    hide elizabeth-neutra with dissolve
    show dorian-neutro at left, position_left with dissolve

    alan "Diga-me, senhor Gray. Basil Hallward o pintou como se a beleza fosse sagrada. Henry fala do senhor como se a juventude fosse um reino. E o senhor? Já percebeu o poder que possui?"

    dorian "Não sei se penso nela dessa forma."

    alan "Então deveria começar."

    alan "A beleza é a primeira autoridade que o mundo reconhece. Antes que um homem prove inteligência, caráter ou fortuna, sua aparência já foi julgada."

    alan "Os feios precisam argumentar. Os comuns precisam insistir. Os belos apenas entram."

    henry "Uma frase terrível, Alan. Portanto, provavelmente verdadeira."

    alan "A beleza abre portas que a bondade passa anos batendo. A juventude recebe perdões que a velhice jamais conseguiria comprar."

    alan "Por isso considero humildade, em pessoas belas, quase uma ingratidão à natureza."

    hide dorian-neutro with dissolve
    show elizabeth-neutra at left, position_right with dissolve

    elizabeth "Ou talvez humildade seja apenas lembrar que beleza não é caráter, Alan."

    elizabeth "A beleza pode abrir portas, concordo. Mas não ensina ninguém a permanecer dentro de uma casa sem destruir o que encontra."

    alan "Elizabeth, minha querida, você sempre tenta devolver humanidade às minhas conclusões."

    elizabeth "E o senhor sempre tenta retirar humanidade de tudo que toca."

    hide elizabeth-neutra with dissolve
    show dorian-neutro at left, position_left with dissolve

    henry "Foi o que tentei explicar no jardim, Dorian. A juventude não foi feita para esperar permissão. Deve buscar novas sensações, novos ambientes, novas experiências."

    alan "Exatamente. O jovem belo que se comporta como todos os outros desperdiça uma vantagem rara. A natureza foi parcial com ele. Por que fingir igualdade?"

    dorian "Talvez juventude, beleza e bondade possam existir juntas."

    alan "Uma resposta bonita. Não sei se verdadeira, mas bonita."

    alan "Mas permita-me uma correção: bondade só é admirada quando não atrapalha o prazer de ninguém. A beleza é admirada mesmo quando incomoda."

    alan "É por isso que ela é superior."

    hide dorian-neutro with dissolve
    show elizabeth-neutra at center, position_left with dissolve

    elizabeth "Ou talvez seja por isso que ela seja mais perigosa."

    elizabeth "Tudo que recebe admiração demais começa a acreditar que não precisa de limites."

    elizabeth "A diferença, senhor Gray, está em descobrir se a beleza será uma ponte até os outros ou apenas um espelho onde a pessoa se ajoelha diante de si mesma."

    alan "Elizabeth, minha querida, você acabou de transformar um jantar em sermão."

    elizabeth "E o senhor tentou transformar nosso convidado em experimento. Estamos quites."

    hide alan-neutro with dissolve
    hide elizabeth-neutra with dissolve
    show henry-neutro at right, position_left with dissolve

    henry "Uma família admirável, não é mesmo, Dorian? Alan transforma virtudes em cinzas, Elizabeth tenta reconstruí-las com elegância, e todos fingem que apenas jantaram."

    dorian "É certamente divertido de assistir."

    henry "Mais que divertido, meu caro. É instrutivo. Aqui, ninguém finge que a beleza não importa. Apenas discordam sobre o que fazer com ela."

    scene henry-eliza-alan-dorian-jantando-2 with dissolve
    pause(0.8)

    "A noite seguiu entre ironias, risos e comentários afiados. Alan defendia a beleza como poder. Elizabeth lembrava que poder sem consciência era perigoso. Henry se divertia. Dorian ouvia tudo em silêncio, como se tentasse decidir qual daquelas vozes permaneceria em sua mente."

    "A noite seguiu entre ironias, risos e comentários afiados. Alan parecia sempre procurar a parte mais frágil de uma ideia para quebrá-la em público. Henry se divertia. Elizabeth corrigia os excessos com elegância. Dorian ouvia tudo com atenção e respondia com frases curtas, como se ainda tentasse decidir qual daquelas vozes permaneceria em sua mente."

    scene dorian-se-despedindo-do-jantar with fade

    alan "Já está de saida, senhor Gray? Não gostou da nossa companhia? Daqui a pouco o chá será servido, é a melhor parte da noite."

    dorian "Eu gostei muito, mas é que tenho que ir para resolver uns assuntos..."

    alan "Hmmm... Normalmente, eu associaria isso a uma desculpa enfarrapada qualquer, mas como gostei do senhor, vou considerar uma execessão. Espero que não seja nada urgente. O senhor está convidado para o campo de golfe no domingo, caso queira ir."

    dorian "Se Henry for, eu certamen..."

    gladys "Papai, mamãe pediu que eu avisasse que o chá será servido na sala menor. Ohh! Perdoem-me. Não sabia que ainda conversavam."

    alan "Sem problemas, querida. Gladys, este é o senhor Dorian Gray. Dorian, minha filha mais velha, Gladys Campbell."

    dorian "É um prazer te conhecer, senhorita Gladys."

    gladys "Digo o mesmo, senhor Gray."

    alan "Eu até gostaria que vocês se conhecessem mais, porém, Dorian, já está de saída."

    gladys "Ahhh! Então deixe-me acompanhá-lo até a saída."

    dorian "Serian uma honra."

    gladys "Obrigada por sua presença, senhor Gray. Espero que meu pai não tenha tornado a noite desagradável."

    dorian "Não. Ele apenas fala de forma… intensa."

    gladys "Essa é uma maneira gentil de dizer terrível. Papai se orgulha de ser desagradável, porque acredita que delicadeza é uma forma de mentira. Eu discordo. Às vezes, delicadeza é apenas a verdade sem desejo de ferir."

    dorian "A senhorita fala de modo muito diferente dele."

    gladys "Tento falar como eu mesma. É difícil em uma casa cheia de pessoas inteligentes. Pessoas inteligentes costumam usar palavras como espadas e depois chamam os ferimentos de conversa."

    dorian "Foi bom ouvi-la esta noite."

    gladys "Digo o mesmo. Venha para o campo de golfe no domingo. Papai convidou Lorde Henry, e imagino que Lorde Henry convidará o senhor sem pedir licença. Assim, poderemos conversar mais. O senhor parece ser um homem interessante, e eu adoraria conhecê-lo melhor."

    dorian "A senhorita também estará lá?"

    gladys "Estarei sim. Caso contrário, eu não teria mencionado."

    dorian "Então irei."

    gladys "Boa noite, senhor Gray."

    dorian "Boa noite, senhorita Campbell."

    # Parte 4 - Campo de golfe e Passeio com Gladys.
    henry "Dorian, lembre-se: no golfe, como na vida, o importante não é acertar, mas parecer superior ao erro."

    alan "Henry joga mal há anos e transformou isso em filosofia."

    henry "Exatamente. A filosofia existe para tornar nossos defeitos mais suportáveis aos outros. Hahaha!"

    gladys "Papai diz que o golfe melhora o caráter. Curiosamente, nunca melhorou o dele."

    alan "Gladys, expor verdades familiares diante de convidados é uma violência social."

    gladys "Então considere minha sinceridade uma herança sua."
    gladys "Senhor Gray, deseja caminhar um pouco? Os homens parecem ocupados demais tentando vencer uns aos outros com paus e silêncio."

    dorian "Será um prazer."

    gladys "O senhor parece menos perdido hoje do que ontem."

    dorian "Eu parecia perdido?"

    gladys "Um pouco. Como alguém que entrou em uma sala elegante procurando uma saída, não uma conversa."

    gladys "Lorde Henry oferece muitas saídas, mas quase todas levam para dentro dele mesmo. Papai é pior: ele oferece portas de ferro e chama isso de verdade."

    gladys "O senhor deveria tomar cuidado com homens que explicam demais a vida. Geralmente fazem isso para não precisar senti-la."

    dorian "A senhorita fala como o meu amigo, Basil."

    gladys "Então Basil deve ser alguém sensato. Conserve-o."

    gladys "Bons amigos são raros porque não nos deixam confortáveis o tempo todo. Eles nos lembram de quem somos quando estamos ocupados tentando parecer outra coisa."

    gladys "Meu pai e Lorde Henry são homens brilhantes, não nego. Mas há um perigo em homens brilhantes: eles fazem qualquer abismo parecer uma escada."

    dorian "Talvez eu precise ouvir mais pessoas como você e Basil."

    gladys "Talvez. Mas não me coloque ao lado de seu melhor amigo tão rápido. Ainda estou decidindo se o senhor merece bons conselhos."

    gladys "Comece não tratando tudo como um jogo. Nem toda conversa precisa ser vencida, nem toda beleza precisa ser admirada como se fosse um objeto."

    gladys "E nem toda escolha perigosa se torna menos perigosa apenas porque foi dita com elegância."

    dorian "A senhorita é sempre tão direta?"

    gladys "Apenas quando acho que vale o esforço."

    gladys "Há um jardim próximo à igreja de Saint Mark. É tranquilo à noite, e distante o bastante dos salões para que as pessoas parem de representar por alguns minutos."

    gladys "Apareça lá amanhã à noite, senhor Gray. Quero saber se o senhor consegue conversar sem Lorde Henry falando por cima de seus pensamentos."

    dorian "A senhorita está me convidando?"

    gladys "Estou oferecendo uma oportunidade. Convite é uma palavra muito confortável."
    gladys "Se for, conversaremos. Se não for, entenderei que prefere permanecer entre os homens que transformam vaidade em filosofia."

    dorian "Eu irei."

    gladys "Ótimo. Então nos veremos amanhã à noite."
    dorian "Sim, senhorita Campbell. Nos veremos lá."

    gladys "Espero que sim, senhor Gray."

    # Parte 5 - Encontro no Jardim próximo à igreja de Saint Mark.

    gladys "Obrigada por ter vindo, senhor Gray. Queria conversar longe da casa dos Campbell. Lá, toda conversa vira uma disputa entre a crueldade elegante de meu pai e as ironias de Lorde Henry."
    gladys "Ontem, percebi que o senhor escutava os dois com atenção. Isso me preocupou. Homens como eles sabem transformar vaidade em filosofia e perigo em liberdade."

    dorian "A senhorita fala como Basil."

    gladys "Então Basil deve ser uma boa influência. Guarde amigos assim. Eles nos lembram de quem somos quando estamos ocupados tentando parecer outra coisa."
    gladys "Meu pai acredita que beleza está acima da bondade. Lorde Henry talvez não diga isso tão diretamente, mas sorri quando alguém acredita. Eu penso diferente. A beleza abre portas, sim. Mas não ensina ninguém a permanecer nelas com dignidade."

    dorian "E o que ensina?"

    gladys "Caráter. Honestidade. Consciência. Coisas menos brilhantes, mas mais necessárias. O senhor é belo, Dorian. Todos percebem isso antes mesmo que fale. Mas tome cuidado para não transformar esse dom em desculpa."

    dorian "Tentarei lembrar disso."

    gladys "Tente praticar, não apenas lembrar. A beleza é um presente, não uma desculpa. Se um dia começar a acreditar que sua aparência o coloca acima dos outros, então Lorde Henry e meu pai terão vencido sem precisar dizer mais nada."
    gladys "Você vai continuar visitando nossa casa?"

    dorian "Sim. Acredito que ainda tenho algo a aprender lá."

    gladys "Então venha. Mas venha com os olhos abertos. Verá meu pai transformar sentimentos em fraqueza, Lorde Henry transformar vaidade em filosofia e minha mãe tentando manter alguma humanidade naquela mesa."
    gladys "E talvez também me veja, se quiser ouvir alguém que não pretende elogiá-lo, apenas adverti-lo."

    dorian "Eu quero ouvir."

    gladys "Ótimo. Então talvez possamos ser amigos, senhor Gray."
    
    dorian "Eu gostaria disso."
    
    gladys "Eu também. Mas não espere elogios fáceis. Já existem pessoas demais elogiando sua beleza."

    "Naquela noite, Dorian apenas caminhou ao lado de Gladys e ouviu. Pela primeira vez em muito tempo, não sentiu necessidade de transformar o silêncio em pose."
    "Depois disso, Dorian continuou frequentando a casa da família Campbell durante dois meses. Dizia a si mesmo que voltava pelos jantares e conversas, mas sabia que as palavras de Gladys permaneciam em sua mente."

    # Parte 6 - Jantar na casa dos Campbell, 2 meses depois.

    elizabeth "senhor Henry, você mal tocou no meu lindo jantar. Acredito que esteja apaixonado."

    henry "Não me apaixono desde que mandame Febe deixou a cidade."

    elizabeth "Mandame Febe? Não conheço."

    henry "É uma mulher maravilhoso, Lady. Quando seu marido morreu, seu cabelo ficou dourado de dor."

    elizabeth "Como era marido dela?"

    henry "Marido de mulheres bonitas pertece a classe dos criminosos."

    elizabeth "Não me espante que o mundo diga que é extremamente cruel."

    henry "É monstruosa a maneira como as pessoas hojes em dias sai dizendo coisas que são inteiras e absolutamente verdadeiras. As mulheres nos amam por nossos defeitos, e se tivemos muitos tudo nos perdoará."

    alan "É verdade."

    elizabeth "Ninguém jamais me convencerá de que o senhor Gray é mau, e jamais o perdoarei se continuar solteiro. Não acha que devemos arrumar uma esposa para o senhor Gray, Lorde Henry?"

    henry "Talvez sim, talvez não. Isso só depende de Dorian. Mas o meu palpite é sim, minha senhora, sou obrigado a concordar. Dorian ainda não usufruiu dessa experiência. Qualquer coisa, é só terminar o relacionamento, e ele pode voltar a ser livre. Não há problema nenhum nisso."

    alan "Cuidado, Dorian. Quando minha esposa decide casar alguém, até a ciência se retira em silêncio.Hahaha!"

    elizabeth "Farei uma lista com todas as jovens disponíveis, suas idades, famílias e virtudes."

    dorian "Eu lhe pouparei o trabalho de procurar, lady Elizabeth. Eu já escolhi, se ela me aceitar."

    henry "Ora, ora."
    
    elizabeth "Eu não acredito."

    alan "Por essa não esperava. É a maior supresa da noite. Quem é, Dorian?"

    dorian "Ninguém." 
    
    henry "Ninguém?" 
    
    dorian "Ninguém. Não desejo uma esposa escolhida como se fosse parte de uma coleção elegante. Também não quero transformar o casamento em uma nova sensação, como o senhor sugeriu, Henry. Se um dia eu amar alguém, não quero que seja por beleza, posição ou curiosidade. Quero que seja porque me tornei digno de estar ao lado dessa pessoa." 

    gladys "Estou orgulhosa, senhor Gray."

    # Parte 7 - Dorian e Basil se reencontrando depois de três meses, quando Basil retorna de Paris.
    basil "Dorian!"

    dorian "Basil!"

    basil "Três meses em Paris, e ainda assim parece que fiquei longe por anos."
    basil "Confesso que tive medo de voltar e encontrar apenas a voz de Henry em você. Mas há algo diferente no seu olhar. Parece menos perdido."

    dorian "Com é bom te ver, Basil. Senti sua falta. Enquanto estive fora, conheci a família Campbell."

    basil "Alan Campbell?"

    dorian "Sim."

    basil "Então Henry realmente não perdeu tempo. Alan é brilhante, mas perigoso. Ele transforma frieza em inteligência e chama isso de verdade."
    basil "Alan é brilhante, mas perigoso. Ele transforma frieza em inteligência e chama isso de verdade."

    dorian "Gladys me fez perceber isso."

    basil "Gladys Campbell? Então ainda há esperança naquela casa. Se ela fez você duvidar das certezas de Henry e Alan, já a considero uma boa influência."

    dorian "Ela é."

    basil "Fico feliz em ouvir isso. Mas já estou de saída, Dorian. Preciso ir para casa descansar. Ainda estou cansado do trabalho em Paris e da viagem de volta."

    dorian "Certo. Amanhã irei até sua casa para conversarmos melhor."

    basil "Fique a vontade para ir quando quiser. Mas antes de sair, Dorian, preciso lhe dizer algo. Dorian, independente do que você se transforme, continuarei sendo seu amigo."

    dorian "..."
    dorian "Digo o mesmo, Basil."

    basil "Então até amanhã, meu amigo."

    dorian "Até amanhã."

    return