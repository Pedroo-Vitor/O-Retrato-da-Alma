# Capítulo 2 - O Amor Ideal
label capitulo_2:

    # Parte 1 (Intro) - Dorian vai ao teatro e conhece Sibyl Vane.

    scene capitulo2-transicao with dissolve
    pause
    scene londres-1886 with dissolve
    pause
    scene dorian-caminhando-cidade with Dissolve(2.0)

    dorian "\"... Sinto que estou em perigo... Mas essa simples sensação me enche de deleite, o senhor Henry disse que a busca pela beleza é o verdadeiro segredo da vida.\""
    dorian "\"Talvez eu a encontre em algumas dessas vidas... Ao menos isso me enche de curiosidade.\""

    scene dorian-olhando-placa-teatro with dissolve
    pause(1.5)
    scene placa-teatro with dissolve

    dorian "\"Um teatro! Faz tanto tempo que não vou a um. O show vai começar daqui 30 minutos.\""
    dorian "\"Bem... Já que estou com bastante tempo livre...\""
    dorian "Um ingresso para a apresentação de agora!"

    scene dorian-assistindo-peca with dissolve

    dorian "\"Ora, ora... Vão apresentar Romeu e Julieta.\""
    dorian "\"Hã... O cenário é ainda mais pobre que a orquestra...\""
    dorian "\"O show já vai começar, finalmente!\""

    scene peca-teatro with dissolve

    ator "Ama, e minha filha? Peça que venha."
    ator "Oh, mas eu já não pedi que viesse. Ei, Pombinha! Rainha! Santo Deus, onde está essa menina… Julieta!"

    scene dorian-assistindo-peca with dissolve

    dorian "\"Hã, que peça deprimente! acho melhor ir embora...\""

    scene sibyl-interpretando-julieta-1 with dissolve
    pause(1.5)

    sibyl "Quem está me chamando? Estou aqui. O que deseja, senhora?"

    scene dorian-assistindo-peca with dissolve
    scene dorian-encantado-com-sibyl with Dissolve(1.0)

    dorian "\"Santo Deus! Que... Perfeição!\""

    scene sibyl-interpretando-julieta-2 with dissolve

    dorian "\"Sua beleza me comoveu às lágrimas… E a sua voz, ora uma doce flauta, ora um áspero oboé…\""

    sibyl "Ama-me? Sei que dirá que sim, e eu Acreditarei. Ah, gentil Romeu, se de fato me ama, apenas diga."

    dorian "\"E desde então, eu fui todos os dias.\""

    scene sibyl-interpretando-imogenia with dissolve

    dorian "\"Às vezes, ela resplandece como Imogênia em 'Cymbeline'... \""

    sibyl "Onde está a sua cabeça? Onde? Ohh! Onde está?..."

    scene sibyl-interpretando-desdemona with dissolve

    dorian "\"Outro dia, o cruel Otelo apertou seu pescoço!\""

    sibyl "Otelo, não me mate!"

    scene dorian-encantado-com-sibyl with dissolve
    pause(0.8)
    
    dorian "Não posso ficar apenas sentando na cadeira assistindo ela, como qualquer um da plateia. Preciso conhecê-la!"

    # Parte 2 - Dorian vai ao camarim de Sibyl Vane.

    scene sibyl-camarim with fade
    pause(0.8)
    scene dorian-e-desconhecido-entra-camarim with fade

    sibyl "Pai! Não esperava o senhor aqui neste horário." 
    
    sibyl "Hmmm... Quem é ele?"

    desconhecido "Oi, filha. Este é o lorde Dorian Gray. Ele insistiu em te conhecer."

    dorian "Ehhh... Olá. Não sabia que ela era sua filha, senhor..."

    scene sibyl-chocada with dissolve
    pause(0.8)
    scene sibyl-feliz with dissolve
    pause(0.8)

    sibyl "Que inesperado! Vai ser um prazer. Por favor, entre!"

    scene cenario-camarim with dissolve
    show sibyl-neutra at right, position_right with dissolve

    sibyl "Obrigada por assistir à minha atuação, milorde."

    show dorian-neutro at left, position_left with dissolve

    menu:
        "Não sou milorde.":
            dorian "Não sou milorde, senhorita. Não me chame assim!"

            sibyl "Oh! Então cometi um erro terrível logo em nossa primeira conversa."
            sibyl "Mas o senhor tem um ar tão nobre que quase me pareceu natural."

        "Apenas Dorian.":
            dorian "Pode me chamar apenas de Dorian."

            sibyl "Dorian..."
            sibyl "É um nome bonito. Mas ainda acho simples demais para alguém que apareceu diante de mim como se tivesse saído de uma história."

        "Não precisa ser tão formal.":
            dorian "Não precisa ser tão formal comigo."

            sibyl "Então também não precisa ser formal comigo."
            sibyl "No teatro, todos usam nomes, títulos e personagens. É bom falar com alguém sem fingir tanto."

    sibyl "Então o chamarei de Príncipe Encantado. É assim que o senhor me parece."

    menu:
        "Príncipe Encantado?":
            dorian "Príncipe Encantado?"

            sibyl "Sim! Não ria de mim. Quando o vi observando do camarote, pensei que talvez fosse alguém importante."
            sibyl "Depois pensei que talvez fosse apenas alguém gentil. E isso é ainda mais raro."

        "Esse nome é estranho.":
            dorian "Esse nome é estranho."

            sibyl "Talvez. Mas nomes estranhos combinam com encontros estranhos."
            sibyl "O senhor apareceu de repente, disse que queria me entrevistar, e agora está aqui no meu camarim. Parece início de peça."

        "E você, quem seria?":
            dorian "E você, quem seria?"

            sibyl "Eu? Depende da noite."
            sibyl "Às vezes sou Julieta. Às vezes Imogênia. Às vezes Desdêmona. Mas agora... acho que sou apenas Sibyl."

    sibyl "Gosto quando posso ser apenas Sibyl. No palco, todos esperam que eu seja outra pessoa. Esperam que eu chore na hora certa, ame na hora certa, sofra na hora certa."

    sibyl "Mas quando a cortina fecha, eu volto para este camarim pequeno, para este espelho gasto, para os vestidos que precisam ser costurados outra vez."

    menu:
        "Você parece amar o palco.":
            dorian "Você parece amar o palco."

            sibyl "Amo. Mesmo quando ele é pobre, mesmo quando a luz falha, mesmo quando a plateia mal presta atenção."
            sibyl "Quando estou em cena, tudo parece maior do que a vida comum."

        "É difícil viver assim?":
            dorian "É difícil viver assim?"

            sibyl "Às vezes. O teatro pertence à minha família, então todos trabalham muito."
            sibyl "Mas eu não reclamo. Quando atuo bem, sinto que todo o esforço vale alguma coisa."

        "Você muda completamente em cena.":
            dorian "Você muda completamente em cena."

            sibyl "É o maior elogio que poderia me dar."
            sibyl "Eu tento desaparecer dentro das personagens. Se a plateia esquece que sou Sibyl, então fiz meu trabalho bem."

    sibyl "Hoje, quando entrei no palco, percebi que o senhor estava prestes a ir embora. Vi seu rosto de tédio antes de eu falar."

    sibyl "Então pensei: preciso fazê-lo ficar."

    menu:
        "Você conseguiu.":
            dorian "Você conseguiu."

            sibyl "Fico feliz."
            sibyl "Não sei por quê, mas queria muito que o senhor continuasse assistindo."

        "Eu não esperava nada.":
            dorian "Eu não esperava nada daquela peça."

            sibyl "Então foi melhor ainda."
            sibyl "É bom surpreender alguém que já estava pronto para se decepcionar."

        "Sua voz me fez ficar.":
            dorian "Sua voz me fez ficar."

            sibyl "Minha voz?"
            sibyl "Que coisa bonita de ouvir. Sempre achei que minha voz pertencesse mais às personagens do que a mim."

    sibyl "Espero que volte outras vezes, Príncipe Encantado."

    menu:
        "Voltarei.":
            dorian "Voltarei."

            sibyl "Então atuarei melhor ainda."

        "Talvez eu volte amanhã.":
            dorian "Talvez eu volte amanhã."

            sibyl "Talvez?"
            sibyl "Então farei de tudo para transformar esse talvez em certeza."

        "Não perderia sua próxima apresentação.":
            dorian "Não perderia sua próxima apresentação."

            sibyl "Agora o senhor está sendo gentil demais."
            sibyl "Mas confesso que gostei."

    sibyl "Então está combinado. O senhor volta para assistir, e eu finjo não ficar esperando sua presença no camarote."

    dorian "Combinado."

    "Depois daquela noite, Dorian Gray e Sibyl Vane continuaram se encontrando. Ele não faltava a uma única apresentação, e cada nova noite no teatro parecia tornar Sibyl ainda mais extraordinária aos seus olhos."

    # Parte 3 - Dorian fala sobre Sibyl Vane para Henry e Basil e convida eles para assisti-la atuando.

    scene casa-basil-interior with fade
    show henry-neutro at left, position_right with dissolve

    henry "Caramba, Dorian, você não para de falar sobre essa tal garota. Você fala como se estivesse apaixonado por ela!"

    show dorian-neutro at right, position_right with dissolve

    menu:
        "Talvez eu esteja.":
            dorian "Talvez eu esteja."

            henry "Talvez? Meu caro Dorian, quando um jovem bonito diz talvez, geralmente já está perdido."
            henry "O amor adora entrar disfarçado de dúvida."

        "Ela é diferente.":
            dorian "Ela é diferente."

            henry "Todos os apaixonados dizem isso. É uma frase muito comum para um sentimento que se imagina extraordinário."
            henry "Mas continue. Quero saber o que torna essa moça tão incomparável."

        "Você precisa vê-la.":
            dorian "Você precisa vê-la para entender."

            henry "Ah, então chegamos ao estágio da exibição. Excelente."
            henry "Quando um homem apaixonado não consegue explicar sua paixão, ele tenta levá-la ao teatro."

    dorian "Sibyl Vane é sagrada."

    henry "Sagrada? Que palavra perigosa para usar sobre uma atriz."
    henry "Atrizes são criaturas encantadoras justamente porque pertencem a muitas vidas ao mesmo tempo. Hoje amam Romeu, amanhã choram por Otelo, depois morrem em alguma tragédia antiga e retornam para jantar como se nada tivesse acontecido."
    henry "Mas sagrada? Não sei. A santidade costuma estragar as pessoas. Torna-as muito difíceis de convidar para jantar."

    show basil-neutro at center, position_left with dissolve

    basil "Henry, por favor. Deixe Dorian falar sem transformar cada palavra em veneno."

    show basil-neutro at center, position_right with dissolve

    basil "Dorian, estou feliz por vê-lo entusiasmado, mas também preocupado. Você fala dessa jovem como se ela fosse mais sonho do que pessoa."

    basil "A arte pode nos elevar, sim. Mas quando confundimos uma pessoa com a arte que ela cria, corremos o risco de amar apenas aquilo que inventamos sobre ela."

    menu:
        "Ela é uma grande artista.":
            dorian "Ela é uma grande artista."

            basil "Então admire sua arte, Dorian. Apenas não esqueça que, fora do palco, ela também deve ter medos, cansaços e uma vida comum."
            basil "Ninguém consegue permanecer extraordinário o tempo todo."

        "Ela transforma tudo ao redor.":
            dorian "Ela transforma tudo ao redor."

            basil "Isso é belo de ouvir."
            basil "Mas tome cuidado. Às vezes, quando alguém ilumina muito uma sala, esquecemos de olhar para a pessoa segurando a vela."

        "Não é invenção minha.":
            dorian "Não é invenção minha, Basil. Ela realmente é maravilhosa."

            basil "Acredito em você. Só peço que a veja com olhos humanos também, não apenas com olhos encantados."
            basil "O encanto é belo, mas pode ser injusto."

    henry "Basil, você consegue transformar até uma paixão juvenil em sermão de domingo."

    show basil-neutro at center, position_left with dissolve

    basil "E você consegue transformar qualquer sermão em piada."

    henry "Naturalmente. É minha forma de caridade."

    henry "Mas confesso que estou curioso, Dorian. Uma jovem capaz de fazê-lo falar como poeta merece ao menos ser observada."

    show basil-neutro at center, position_right with dissolve

    basil "Eu também gostaria de vê-la. Não por curiosidade cruel, como Henry, mas porque quero entender o que tocou tanto o seu espírito."

    menu:
        "Venham comigo hoje.":
            dorian "Venham comigo hoje."

            henry "Hoje? Que entusiasmo admirável."
            henry "Muito bem, aceitarei. Seria uma crueldade deixar Basil sozinho com a própria prudência."

            basil "Eu irei, Dorian. Se ela é importante para você, quero conhecê-la pelo menos através de sua arte."

        "Quero que vejam o que eu vejo.":
            dorian "Quero que vejam o que eu vejo."

            basil "Então iremos."
            basil "Mas lembre-se: talvez vejamos algo diferente. Cada pessoa assiste à beleza com os próprios olhos."

            henry "E eu, felizmente, tenho olhos excelentes para esse tipo de desastre encantador."

        "Ela se apresentará esta noite.":
            dorian "Ela se apresentará esta noite."

            henry "Então está decidido. Iremos ao teatro."
            henry "Espero que sua deusa saiba sobreviver à nossa plateia particular."

            basil "Henry..."

            henry "Estou sendo gentil, Basil. Para meus padrões, quase angelical."

    dorian "Então está combinado."

    basil "Sim. Iremos com você."

    henry "E espero, Dorian, que essa Sibyl Vane seja metade do que você promete. Caso contrário, sua paixão será melhor que a peça."

    scene dorian-henry-basil-caminhando-pelo-teatro with fade

    # Parte 4 - Henry e Basil, junto de Dorian vão ver Sibyl Vane atuando como Julieta, mas acabam se decepcionando.

    henry "Hmm... Que lugar estranho para se encontrar uma deusa."

    dorian "É verdade, encontrei-a aqui, e ela é a encarnação da divindade."

    scene dorian-henry-basil-sentando-teatro with fade

    basil "Shhh!!! Façam silêncio, a peça vai começar."

    scene peca-teatro with fade

    dorian "Daqui a pouco Sibyl entra em cena, senhores."

    basil "Estou ansioso para vê-la."

    henry "Eu também. Quero ver se essa tal de Sibyl é tudo o que Dorian diz."

    scene sibyl-interpretando-julieta-3 with fade

    dorian "É AGORA! É ELA! É AGORA! SIBYL!"

    sibyl "bondoso peregrino fazeis injustiça à vossa mão..."

    "Diferente do que Dorian dizia, Sibyl Vane interpretava Julieta sem emoção nenhuma..."

    scene henry-dorian-basil-assistindo-sibyl with fade

    basil "Mas..."

    henry "É uma voz maravilhosa, mas não há emoção. Não expressa nada. Parece uma aluna em uma peça escolar."

    dorian "Não diga isso, Henry!"
    dorian "\"Eu não entendo, não entendo... O que há com ela? Será que adoeceu e não me falou? Deve haver alguma explicação...\""
    dorian "Vamos esperar a cena da varanda. Não vamos julgá-la ainda."

    scene sibyl-interpretando-julieta-4 with fade

    sibyl "se não fosse a noite a ocultar-me com seu véu minhas bochechas ficariam ruborizadas pelo que disse antes como eu gostaria de seguir as regras e negar o que foi dito ama-me sei que dirás que sim e eu vou acreditar romeu"

    scene henry-dorian-basil-assistindo-sibyl with fade

    basil "Paté... Não sei se devo dizer isso..."
    
    henry "Eu falo por você, Basil: Pa-té-ti-co. Vamos embora!"

    scene henry-basil-saindo-do-teatro with fade

    dorian "NÃO! ESPEREM!"

    henry "Ela é de fato formosa, Dorian, mas é incapaz de interpretar. Vamos!"

    basil "Até mais, Dorian."

    scene dorian-sentado-triste-teatro with fade

    dorian "Peço-lhes desculpa... Senhores..."
    dorian "..."
    dorian "\"Por quê? ... Por quê? ... O que será que houve? Exijo explicações!\""

    scene sibyl-camarim with fade
    pause(0.8)
    scene dorian-entrando-camarim with fade

    # Parte 5 (Final) - Dorian vai atrás de Sibyl pedindo explicações.

    # Variável de que contabiliza o quanto dorian está copreendendo Sibyl. 

    # Ela é responsável por alterar o final!
    $ compreensao_sibyl = 0

    scene cenario-camarim with dissolve
    show dorian-neutro at right, position_right with dissolve
    show sibyl-neutra at left with dissolve

    sibyl "Oh, meu Príncipe Encantado! Hahaha, como atuei na minha última apresentação. Hahaha!"

    menu:
        "*Expressar sua decepção*":
            $ compreensao_sibyl -= 1
            dorian "O que há de engraçado? Foi terrivelmente mal! Foi de espantar! Não imagina como sofri."

            sibyl "Eu sei que foi ruim. Eu mesma percebi enquanto falava."
            sibyl "Mas, pela primeira vez, aquilo não me feriu. Parecia que eu finalmente enxergava a mentira do palco."

        "*Cobrar explicações*":
            $ compreensao_sibyl += 1
            dorian "Sibyl, explique com calma. Quero entender o que aconteceu."

            sibyl "Obrigada por perguntar assim."
            sibyl "Eu temia que viesse apenas para me condenar, sem querer ouvir nada."

    sibyl "Antes, o palco era minha única realidade. Eu acreditava em tudo: no luar pintado, nos reis de papelão, nas lágrimas falsas e no amor dito por homens maquiados."
    sibyl "Mas depois que conheci você, tudo aquilo pareceu vazio. Eu vi o teatro como ele era: pobre, cansado, sustentado por aplausos que mal pagavam as contas da minha família."

    menu:
        "Então você estavam apenas por dinheiro?!":
            $ compreensao_sibyl -= 1
            dorian "Então era isso? Você continuava naquele palco apenas pelo dinheiro?!"

            sibyl "Não diga isso. O teatro é pobre, sim, e minha família precisa dele. Mas isso não significa que tudo em mim era interesse."
            sibyl "Eu amava atuar porque acreditava no que fazia. O problema é que, esta noite, deixei de acreditar."

        "Sua família depende de você e do teatro?":
            $ compreensao_sibyl += 1
            dorian "Então sua família depende de você e do teatro?"

            sibyl "Sim. Mais do que eu gostaria."
            sibyl "Por isso minha falha desta noite também me assusta. Não decepcionei apenas você. Talvez tenha abalado tudo que sustenta minha casa."

    sibyl "Cresci ali dentro. Aprendi a sorrir quando a plateia sorria e a chorar quando esperavam lágrimas."
    sibyl "Mas esta noite eu não consegui. Não porque quisesse feri-lo. Apenas não consegui transformar mentira em verdade depois de ter conhecido algo real, como você, Pequeno Príncipe."

    menu:
        "Nunca mais voltará a atuar como antes?":
            dorian "Então nunca mais voltará a atuar como antes?"

            sibyl "Não sei. Talvez eu volte. Talvez descubra outra forma de atuar."
            sibyl "Mas não posso prometer que serei a mesma Sibyl que o senhor viu no palco pela primeira vez."

        "Então você realmente mudou.":
            $ compreensao_sibyl += 1
            dorian "Talvez eu não tenha entendido que você mudou."

            sibyl "Sim. Eu mudei."
            sibyl "E talvez eu tenha sido ingênua por pensar que o senhor ficaria feliz com isso."

        "Você abandonou arte por conta de algo passageiro.":
            $ compreensao_sibyl -= 1
            dorian "Você abandonou sua arte por causa de um sentimento passageiro."

            sibyl "Não chame assim. Para o senhor pode parecer passageiro, mas para mim foi como acordar de uma vida inteira." 
            sibyl "Talvez eu esteja errada, mas não consigo fingir que nada mudou."

    sibyl "Antes de você, eu era Julieta, Imogênia, Desdêmona... Todas pareciam mais vivas que eu."
    sibyl "Agora eu sou Sibyl. Apenas Sibyl. E por isso atuei mal. Porque, pela primeira vez, as palavras dos poetas pareciam pequenas diante do que eu sentia fora do palco."

    menu:
        "Você fez eu passar vergonha na frente meus amigos.":
            $ compreensao_sibyl -= 1
            dorian "Meus amigos estavam lá. Você me fez parecer um tolo diante deles."

            sibyl "Sinto muito por tê-lo envergonhado. Mas eu não estava atuando para Lorde Henry, nem para Basil. Eu esperava que o senhor me visse, mesmo quando todos os outros me julgassem."

        "Amava aquela atriz que transformava sonhos em realidade.":
            $ compreensao_sibyl -= 1
            dorian "Eu amava a atriz que transformava sonhos em realidade. Não sei quem está diante de mim agora."

            sibyl "Então talvez o senhor amasse uma personagem."
            sibyl "Eu não posso ser Julieta para sempre apenas para continuar sendo amada."

        "Talvez eu devesse amar a pessoa por trás da atriz.":
            $ compreensao_sibyl += 1
            dorian "Talvez eu tenha amado mais a imagem que criei de você do que você mesma."

            sibyl "Essa é uma coisa triste de ouvir."
            sibyl "Mas talvez seja a primeira coisa verdadeira dita nesta noite."

    sibyl "Eu continuo sendo eu. Só não consigo mais viver como se o palco fosse minha única verdade."
    sibyl "Se isso decepciona você, talvez nunca tenha amado Sibyl Vane. Talvez tenha amado apenas as mulheres que eu fingia ser."

    menu:

        "Talvez eu tenha sido injusto.":
            $ compreensao_sibyl += 1
            dorian "Talvez eu tenha sido injusto com você."

            sibyl "Talvez nós dois tenhamos sido ingênuos."
            sibyl "Eu por achar que o amor resolveria tudo. O senhor por achar que eu continuaria sendo uma visão perfeita para sempre."
            
        "Você fala como se a culpa fosse minha.":
            $ compreensao_sibyl -= 1
            dorian "Você fala como se a culpa fosse minha."

            sibyl "Não quero colocar toda a culpa no senhor."
            sibyl "Mas também não quero fingir que fui a única a transformar amor em ilusão."

    if compreensao_sibyl >= 2:
        jump final_sibyl_juntos
    else:
        jump final_sibyl_termino


label final_sibyl_termino:

    $ estado_retrato += 1

    menu:
        "VOCÊ MATOU O MEU AMOR!":
            scene dorian-gritando-com-sibyl with dissolve
            dorian "VOCÊ MATOU O MEU AMOR!"

    sibyl "O quê? Não está falando sério, não é, Príncipe Encantado? Está apenas atuando..."

    dorian "Eu amava você porque era maravilhosa. Porque dava forma e sentido às sombras da arte."
    dorian "Mas agora vejo apenas uma garota comum, presa a um teatro pobre, rindo da própria ruína."

    scene dorian-terminando-relacionamento-sibyl with dissolve

    dorian "Como fui louco por amá-la. Nunca mais voltarei a vê-la. NUNCA!"

    sibyl "Não! Não me deixe! Farei o que quiser! Eu o amo mais que tudo no mundo!"

    scene sibyl-ajoelhada-chorando with dissolve
    pause(1.1)

    scene sibyl-deitada-chorando with dissolve
    pause

    sibyl "Não! Não! Não me deixe!"

    # Carrega o script do capítulo 3
    jump capitulo_3

label final_sibyl_juntos:

    menu:
        "Talvez eu tenha amado a atriz e não a mulher diante de mim.":
            scene dorian-e-sibyl-conversando-tranquilamente with dissolve
            dorian "Talvez eu tenha amado demais a atriz no palco e escutado pouco a mulher diante de mim."

    sibyl "Eu não quero deixar de ser amada por ter sido sincera. Podemos continuar a nos encontrar?"

    dorian "Sim, continuaremos. Amanhã conversaremos com calma. Sobre você, sobre o teatro, sobre sua família... Sem plateia. Sem Meus Amigos. Sem orgulho."

    sibyl "Ótimo. E muito reconfortante ouvir isso!"

    scene dorian-se-despedindo-de-sibyl with dissolve

    dorian "Até amanhã, Sibyl!"

    sibyl "Pequeno Príncipe! Antes de ir, preciso de contar uma coisa..."

    dorian "Hmm... Diga sem medo!"

    sibyl "Eu te amo!"

    menu:
        "Eu também te amo, Sibyl Vane!":
            dorian "Eu também te amo, Sibyl Vane!"
    
    scene dorian-e-sibyl-se-abracando with dissolve
    pause
    scene black with fade
    pause

    # Carrega o script do capítulo 3
    jump capitulo_3