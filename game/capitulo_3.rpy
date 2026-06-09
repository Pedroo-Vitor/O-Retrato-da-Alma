# Capítulo 3: Família Campbell
label capitulo_3:

    $ influencia_campbell = 0

    scene capitulo3-transicao with fade
    pause
    scene londres-1886 with dissolve
    pause
    scene black with fade
 
    "Um mês havia se passado desde aquela noite no teatro."

    # Parte 1 - Basil e Dorian conversando antes da viagem de Basil para Paris.

    scene dorian-pensativo-em-sua-casa with fade

    dorian "\"Lorde Henry disse que a juventude deve buscar novas sensações… Que a beleza abre portas que a virtude jamais conseguiria tocar...\""
    dorian "\"Mas Basil sempre fala como se houvesse perigo nisso.\""

    scene dorian-assustado with dissolve
    pause(0.8)
    scene porta-dorian with dissolve

    dorian "\"Batidas na porta de minha casa neste horário?\""
    dorian "Quem é?"

    basil "Sou eu, Dorian. Basil."

    scene casa-dorian with fade
    show basil-neutro at right, position_left with dissolve

    basil "Boa noite, Dorian. Perdoe-me por vir tão tarde. Eu precisava vê-lo antes de partir."

    show dorian-neutro at left, position_left with dissolve

    dorian "Partir?"

    basil "Sim. Amanhã pela manhã viajarei para Paris. Ficarei fora por três meses. Há encomendas, galerias e pessoas insistentes demais para serem ignoradas."

    basil "Mas confesso que essa viagem também me servirá como descanso. Por isso vim vê-lo. Não queria partir sem antes conversar com você."

    basil "Dorian, desde que conheceu Henry, algo em você parece inquieto. Ele tem o talento terrível de fazer uma ideia ruim parecer bela, e uma escolha cruel parecer apenas coragem."

    dorian "Basil, você exagera."

    basil "Talvez. Mas prefiro exagerar por cuidado a me calar por covardia."

    basil "Tome cuidado com Henry enquanto eu estiver fora. Ele não obriga ninguém a cair, mas sabe muito bem como abrir uma janela e elogiar a vista."

    basil "Enquanto eu estiver fora, promete que não deixará Henry convencê-lo de que a beleza é a única coisa que vale a pena na vida?"

    menu:
        "Talvez ele tenha razão.":
            $ influencia_campbell += 1

            dorian "Está bem, Basil. Prometo que não deixarei Henry decidir por mim."

            basil "Ótimo. Confio em você, Dorian."

        "É melhor encerrar o assunto.":
            dorian "Prometo tentar, Basil."

            basil "Tentar já é melhor do que se entregar. Mas tome cuidado: as ideias de Henry parecem leves justamente porque são perigosas."

        "Basil está preocupado outra vez.":
            $ influencia_campbell -= 1

            dorian "Você se preocupa demais, Basil. Sei cuidar de mim mesmo."

            basil "Espero que sim. Ainda assim, amigos servem para dizer aquilo que os aduladores evitam."

    basil "Lembre-se: beleza é um dom, não uma desculpa. Se um dia começar a acreditar que sua aparência o coloca acima dos outros, então Henry terá vencido sem precisar dizer mais nada."

    basil "Amanhã meu trem parte cedo, às oito da manhã. Gostaria que fosse à estação se despedir de mim."

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

    henry "Mas me diga, Dorian, que conversa tão grave foi essa?"

    dorian "Ele pediu que eu não deixasse o senhor me convencer de que a beleza é a única coisa que vale a pena na vida."

    henry "Ah! Então Basil está mais dramático do que imaginei."

    henry "A beleza não é a única coisa que vale a pena na vida, meu caro. Seria vulgar dizer isso. Mas é, sem dúvida, uma das poucas coisas que a vida obedece sem discutir."

    henry "A bondade precisa explicar-se. A inteligência precisa provar-se. A virtude precisa ser defendida como uma causa perdida. A beleza, porém, entra em uma sala e todos compreendem imediatamente."

    menu:
        "Basil sempre vê perigo em tudo.":
            $ influencia_campbell -= 1

            dorian "Talvez Basil apenas tenha medo de tudo aquilo que não compreende."

            henry "Finalmente começa a conhecê-lo melhor."

        "Isso não parece justo.":
            dorian "Isso não parece justo."

            henry "A vida é injusta, Dorian. Alguns sofrem por isso. Outros aprendem a usar a injustiça com elegância."

        "Ele não concordaria.":
            $ influencia_campbell += 1

            dorian "Basil não concordaria com isso."

            henry "Naturalmente. Basil discorda de tudo que torna a vida menos tediosa."

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

    # Parte 3 - Jantar na casa da família Campbell.

    scene na-noite-daquele-mesmo-dia with fade
    pause

    scene dorian-defronte-casa-campbell with fade
    pause(1.4)

    scene dorian-batendo-na-porta-da-casa-campbell with dissolve

    mordomo "Quem é?"

    dorian "É Dorian Gray, o convidado mencionado por Lorde Henry Wotton."

    scene alan-dorian-cumprimentando with dissolve
    pause(0.8)

    alan "Boa noite, Dorian. Finalmente chegou. O jantar começou há algum tempo. Por favor, sente-se."

    dorian "Desculpe o atraso."

    scene henry-eliza-alan-dorian-jantando with dissolve
    pause(1.0)

    scene mesa-jantar-campbell with fade
    show alan-neutro at right, position_left with dissolve
    show dorian-neutro at left, position_left with dissolve

    alan "Então este é o famoso Dorian Gray. Lorde Henry falou muito do senhor."

    dorian "Espero que tenha falado bem."

    alan "Henry nunca fala bem de ninguém. Quando deseja elogiar, apenas ofende com mais entusiasmo."

    alan "Ainda assim, ele não exagerou completamente. O senhor possui uma aparência rara, senhor Gray. Não deveria tratá-la com falsa modéstia."

    show henry-neutro at center, position_left with dissolve

    henry "Alan é injusto comigo, Dorian. Eu ofendo todos com igual dedicação."

    alan "Essa talvez seja sua única virtude democrática."

    hide dorian-neutro with dissolve
    show elizabeth-neutra at left, position_right with dissolve

    elizabeth "Alan, por favor. Não assuste nosso convidado antes da sobremesa."

    alan "Se uma conversa pode assustá-lo, então Lorde Henry me descreveu muito mal."

    henry "Viu, Dorian? Eu disse que Alan era pior que eu."

    alan "Henry é cruel por prazer. Eu sou cruel por precisão."

    hide elizabeth-neutra with dissolve
    show dorian-neutro at left, position_left with dissolve

    alan "Diga-me, senhor Gray: já percebeu o poder que sua aparência possui?"

    menu:
        "É apenas um rosto.":
            $ influencia_campbell += 1

            dorian "É apenas um rosto, Alan. Não vejo tanto poder nisso."

            alan "Nada que move o mundo é apenas alguma coisa."

        "Talvez eu nunca tenha usado isso direito.":
            $ influencia_campbell -= 1

            dorian "Talvez eu ainda não tenha aprendido a usar essa vantagem."

            alan "Finalmente uma resposta menos inocente."

        "Basil dá importância demais a essas coisas.":
            $ influencia_campbell -= 1

            dorian "Basil trata a beleza como se fosse algo sagrado. Talvez ele exagere."

            henry "Meu caro Dorian, está começando a falar como um homem interessante."

    alan "A beleza é a primeira autoridade que o mundo reconhece. Os feios precisam argumentar. Os comuns precisam insistir. Os belos apenas entram."

    henry "Uma frase terrível, Alan. Portanto, provavelmente verdadeira."

    alan "A beleza abre portas que a bondade passa anos batendo. A juventude recebe perdões que a velhice jamais conseguiria comprar."

    show elizabeth-neutra at left, position_right with dissolve

    elizabeth "A beleza pode abrir portas, mas não ensina ninguém a atravessá-las com dignidade."

    alan "Minha querida, dignidade é apenas o nome elegante dado ao medo de aproveitar uma vantagem."

    hide elizabeth-neutra with dissolve

    henry "A juventude não foi feita para esperar permissão, Dorian. Deve buscar novas sensações, novos ambientes e novas experiências."

    alan "Exatamente. A natureza foi parcial com o senhor. Por que deveria fingir igualdade?"

    menu:
        "Talvez igualdade seja apenas cortesia.":
            $ influencia_campbell -= 2

            dorian "Talvez igualdade seja apenas uma cortesia que os favorecidos oferecem aos outros."

            alan "Excelente. Lorde Henry escolheu bem seu convidado."

        "Ainda prefiro não dever tudo à aparência.":
            $ influencia_campbell += 1

            dorian "Ainda prefiro não dever tudo aquilo que conquisto à minha aparência."

            alan "Uma preocupação admirável, embora pouco prática."

        "Os dois lados parecem exagerar.":
            dorian "Talvez vocês e Basil exagerem em direções diferentes."

            henry "Uma resposta diplomática. A diplomacia é a indecisão bem vestida."

    alan "A bondade só é admirada enquanto não atrapalha o prazer de ninguém. A beleza é admirada mesmo quando incomoda."

    alan "É por isso que ela é superior."

    henry "Aqui ninguém finge que a beleza não importa, Dorian. Apenas discordamos sobre o que fazer com ela."

    scene henry-eliza-alan-dorian-jantando-2 with dissolve
    pause(0.8)

    "A noite seguiu entre ironias e comentários afiados. Alan defendia a beleza como poder, Henry transformava suas ideias em tentação e Elizabeth evitava que a conversa perdesse toda a humanidade."

    scene dorian-se-despedindo-do-jantar with fade

    alan "Já está de saída, senhor Gray?"

    dorian "Gostei muito da noite, mas preciso ir."

    alan "Aceitarei sua desculpa desta vez."

    gladys "Papai, mamãe pediu que eu avisasse que o chá será servido na sala menor."

    alan "Gladys, este é o senhor Dorian Gray. Dorian, minha filha mais velha."

    dorian "É um prazer conhecê-la, senhorita Campbell."

    gladys "Digo o mesmo, senhor Gray."

    # Parte 4 - Gladys conversa com Dorian no jardim próximo à igreja de Saint Mark.

    scene henry-eliza-alan-dorian-jantando-2 with fade

    "Com o passar das semanas, Dorian aproximou-se cada vez mais da família Campbell. Jantavam juntos, jogavam golfe e participavam de outros encontros da alta sociedade."

    "Gladys, a filha mais velha dos Campbell, percebeu que Dorian começava a repetir as ideias de Alan e Lorde Henry. Por isso, decidiu intervir."

    scene dorian-se-despedindo-do-jantar with fade

    gladys "Senhor Gray, poderia me acompanhar amanhã em um passeio pelo jardim próximo à igreja de Saint Mark? Preciso conversar com o senhor longe de meu pai e de Lorde Henry."

    dorian "Porque precisa conversa comigo longe de Henry e de Alan?"

    gladys "Se o senhor for amanhã, saberá."

    dorian "Certo, certo. Vou ir só pela curiosidade."

    gladys "Ótimo!"

    scene jardim-basil with fade
    show gladys-neutro at left, position_right with dissolve
    show dorian-neutro at right, position_right with dissolve

    gladys "Obrigada por ter vindo. Ultimamente, o senhor tem escutado meu pai e Lorde Henry com atenção demais."

    gladys "Homens como eles sabem transformar vaidade em filosofia e perigo em liberdade."

    menu:
        "Eles ao menos são sinceros.":
            $ influencia_campbell -= 1

            dorian "Eles apenas dizem verdades que outras pessoas não têm coragem de admitir."

            gladys "Ou dizem crueldades com tanta elegância que o senhor deixou de perceber a diferença."

        "Essa conversa me lembra Basil.":
            $ influencia_campbell += 1

            dorian "A senhorita fala como Basil."

            gladys "Então Basil deve ser um amigo que vale a pena conservar."

        "Ainda estou observando.":
            dorian "Ainda não decidi se eles estão certos."

            gladys "Então desconfie principalmente das ideias que tornam seus desejos mais fáceis de justificar."

    gladys "Meu pai acredita que a beleza está acima da bondade. Lorde Henry talvez não diga isso diretamente, mas sorri quando alguém acredita."

    gladys "Eu penso diferente. A beleza abre portas, mas não ensina caráter, honestidade ou consciência."

    gladys "O senhor é belo, Dorian. Todos percebem isso antes mesmo que fale. Mas não transforme esse dom em desculpa."

    menu:
        "Não quero dever tudo a um rosto.":
            $ influencia_campbell += 1

            dorian "Não quero que minha aparência seja a única razão para as pessoas me admirarem."

            gladys "Então faça com que suas escolhas sejam tão dignas quanto o rosto que todos elogiam."

        "Talvez eu saiba usar essa vantagem.":
            $ influencia_campbell -= 2

            dorian "Talvez o erro não esteja na beleza, mas em quem não sabe usar a vantagem que possui."

            gladys "Isso não é sabedoria, senhor Gray. É arrogância procurando uma justificativa."

        "É mais difícil do que parece.":
            dorian "É mais difícil ignorar isso quando todos me tratam de maneira diferente."

            gladys "Eu sei. Mas dificuldade não transforma uma escolha errada em uma escolha correta."

    gladys "A beleza é um presente, não uma permissão. Se acreditar que ela o coloca acima dos outros, meu pai e Lorde Henry terão vencido."

    gladys "Você vai continuar visitando nossa casa?"

    menu:
        "A casa de vocês ainda me diverte.":
            $ influencia_campbell -= 2

            dorian "Sim. Seu pai e Lorde Henry tornam as noites muito menos entediantes."

            gladys "Então espero que o senhor perceba o perigo antes de começar a falar exatamente como eles."

        "Talvez eu ainda tenha algo a ouvir.":
            $ influencia_campbell += 2

            dorian "Sim. Ainda não concordo com tudo que disse, mas quero continuar ouvindo."

            gladys "Isso já é suficiente por enquanto."

        "Seria indelicado desaparecer.":
            dorian "Sim. Seria indelicado desaparecer depois de tantas visitas."

            gladys "Espero que a educação não seja o único motivo."

    "Naquela noite, Dorian deixou o jardim sem saber qual daquelas vozes seguiria."

    if influencia_campbell >= 2:
        jump final_cap3_bom
    else:
        jump final_cap3_ruim

label final_cap3_bom:

    "Durante os meses seguintes, Dorian continuou visitando os Campbell, mas passou a ouvir as ideias de Alan e Henry com mais cautela."

    scene casa-dorian with fade
    show basil-neutro at right, position_left with dissolve
    show dorian-neutro at left, position_left with dissolve

    basil "Dorian! Três meses em Paris, e ainda assim parece que fiquei longe por anos."

    dorian "Senti sua falta, Basil. Enquanto esteve fora, conheci a família Campbell."

    basil "Alan Campbell? Então Henry realmente não perdeu tempo."

    dorian "Gladys me ajudou a perceber o perigo das ideias dele."

    basil "Então há esperança naquela casa. Fico feliz que tenha escutado alguém que não elogia apenas sua beleza."

    basil "Mas já estou de saída. Ainda estou cansado da viagem."

    dorian "Amanhã irei até sua casa para conversarmos melhor."

    basil "Estarei esperando."

    basil "Antes de ir, preciso lhe dizer algo: independente do que você se transforme, continuarei sendo seu amigo."

    dorian "..."

    dorian "Digo o mesmo, Basil."

    jump capitulo_4

label final_cap3_ruim:

    $ estado_retrato += 1

    "Durante os meses seguintes, Dorian continuou visitando os Campbell. Aos poucos, passou a repetir as ideias de Alan e Lorde Henry como se fossem suas."

    scene casa-dorian with fade
    show basil-neutro at right, position_left with dissolve
    show dorian-neutro at left, position_left with dissolve

    basil "Dorian! Três meses em Paris, e ainda assim parece que fiquei longe por anos."

    basil "Confesso que tive medo de encontrar apenas a voz de Henry em você. Agora não sei se meu medo era exagero."

    dorian "Conheci Alan Campbell. Talvez ele apenas enxergue o mundo sem ilusões."

    basil "Essa é exatamente a frase que eu temia ouvir."

    dorian "Gladys tentou me advertir, mas ela pensa demais como você."

    basil "A beleza é um dom, Dorian, não uma permissão para se colocar acima dos outros."

    dorian "Talvez eu só esteja começando a entender aquilo que possuo."

    basil "Então talvez eu tenha voltado tarde demais."

    basil "Já estou de saída. Ainda estou cansado da viagem."

    dorian "Amanhã conversaremos melhor."

    basil "Espero que sim."

    basil "Antes de ir, preciso lhe dizer algo: independente do que você se transforme, continuarei sendo seu amigo."

    dorian "..."

    dorian "Digo o mesmo, Basil."

    jump capitulo_4