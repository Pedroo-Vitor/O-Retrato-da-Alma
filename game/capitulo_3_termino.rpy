# Capítulo 3: Família Campbell
label capitulo_3_termino:

    $ influencia_campbell = 0

    scene capitulo3-transicao with fade
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
        "Prometer com firmeza.":
            $ influencia_campbell += 1
            dorian "Prometo, Basil. Não vou deixar Henry me convencer disso."

            basil "Ótimo. Confio em você, Dorian."

        "Responder com dúvida.":
            dorian "Prometo tentar, Basil."

            basil "Tentar já é melhor do que se entregar. Mas tome cuidado: as ideias de Henry parecem leves justamente porque são perigosas."

        "Acalmar Basil.":
            $ influencia_campbell -= 1
            dorian "Não se preocupe tanto comigo, Basil."

            basil "Preocupo-me porque sou seu amigo. E amigos servem para dizer aquilo que os aduladores evitam."

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
        "Isso parece injusto.":
            dorian "Isso parece injusto."

            henry "A vida é injusta, Dorian. Alguns sofrem por isso. Outros aprendem a usar a injustiça com elegância."

        "Basil discordaria disso.":
            $ influencia_campbell += 1
            dorian "Basil discordaria disso."

            henry "Naturalmente. Basil discorda de tudo que torna a vida menos tediosa."

        "Talvez haja verdade nisso.":
            $ influencia_campbell -= 1
            dorian "Talvez haja alguma verdade nisso."

            henry "Há mais verdade nisso do que a sociedade teria coragem de confessar."

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

    dorian "É Dorian Gray, o convidado que Lorde Henry Wotton mencionou."

    scene alan-dorian-cumprimentando with dissolve
    pause(0.8)

    alan "Boa noite, Dorian. Finalmente chegou. O jantar começou já faz um tempinho. Por favor, sente-se."
    
    dorian "Desculpe o atraso."

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

    menu:
        "Ainda não pensei nisso.":
            dorian "Não sei se penso nela dessa forma."

            alan "Então deveria começar."

        "Talvez seja apenas aparência.":
            $ influencia_campbell += 1
            dorian "Talvez seja apenas aparência."

            alan "Nada que move o mundo é apenas alguma coisa."

        "Basil diria que é um dom.":
            $ influencia_campbell += 1
            dorian "Basil diria que é um dom, não um poder."

            alan "Basil é artista. Artistas adoram tornar perigos inofensivos dando a eles nomes bonitos."

    alan "A beleza é a primeira autoridade que o mundo reconhece. Os feios precisam argumentar. Os comuns precisam insistir. Os belos apenas entram."

    henry "Uma frase terrível, Alan. Portanto, provavelmente verdadeira."

    alan "A beleza abre portas que a bondade passa anos batendo. A juventude recebe perdões que a velhice jamais conseguiria comprar."

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

    menu:
        "Juventude e bondade podem existir juntas.":
            $ influencia_campbell += 1
            dorian "Talvez juventude, beleza e bondade possam existir juntas."

            alan "Uma resposta bonita. Não sei se verdadeira, mas bonita."

        "Talvez Basil tenha razão.":
            $ influencia_campbell += 1
            dorian "Talvez Basil tenha razão em temer esse tipo de pensamento."

            henry "Pobre Basil. Sempre ausente e ainda assim sempre interrompendo."

        "Talvez a beleza seja mesmo superior.":
            $ influencia_campbell -= 2
            dorian "Talvez a beleza seja mesmo superior."

            alan "Finalmente uma frase menos tímida."

    alan "Bondade só é admirada quando não atrapalha o prazer de ninguém. A beleza é admirada mesmo quando incomoda. É por isso que ela é superior."

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

    "A noite seguiu entre ironias, risos e comentários afiados. Alan defendia a beleza como poder. Elizabeth lembrava que poder sem consciência era perigoso. Henry se divertia. Dorian ouvia tudo em silêncio."

    scene dorian-se-despedindo-do-jantar with fade

    alan "Já está de saída, senhor Gray? Não gostou da nossa companhia? Daqui a pouco o chá será servido."

    dorian "Gostei muito, mas preciso ir."

    alan "Normalmente, eu associaria isso a uma desculpa qualquer. Mas, como gostei do senhor, aceitarei como exceção."

    gladys "Papai, mamãe pediu que eu avisasse que o chá será servido na sala menor. Oh! Perdoem-me. Não sabia que ainda conversavam."

    alan "Sem problemas, querida. Gladys, este é o senhor Dorian Gray. Dorian, minha filha mais velha, Gladys Campbell."

    dorian "É um prazer conhecê-la, senhorita Gladys."

    gladys "Digo o mesmo, senhor Gray."

    alan "Eu até gostaria que conversassem mais, porém Dorian já está de saída."

    gladys "Então deixe-me acompanhá-lo até a porta."

    # Parte 4 - Gladys conversa com Dorian no jardim próximo à igreja de Saint Mark.

    scene casa-dorian with fade

    "Nas semanas seguintes, Dorian continuou frequentando a casa da família Campbell. Entre jantares, conversas e provocações de Lorde Henry, começou a notar que Gladys observava tudo com uma sinceridade rara."

    scene jardim-basil with fade
    show gladys-neutro at left, position_right with dissolve
    show dorian-neutro at right, position_right with dissolve

    gladys "Obrigada por ter vindo, senhor Gray. Queria conversar longe da casa dos Campbell."

    gladys "Lá, toda conversa vira uma disputa entre a crueldade elegante de meu pai e as ironias de Lorde Henry."

    gladys "Ontem percebi que o senhor escutava os dois com atenção. Isso me preocupou. Homens como eles sabem transformar vaidade em filosofia e perigo em liberdade."

    menu:
        "A senhorita fala como Basil.":
            $ influencia_campbell += 1
            dorian "A senhorita fala como Basil."

            gladys "Então Basil deve ser uma boa influência."

        "Eles apenas dizem o que pensam.":
            $ influencia_campbell -= 1
            dorian "Eles apenas dizem o que pensam."

            gladys "Talvez. Mas algumas pessoas pensam com tanta elegância que esquecemos de perguntar se estão certas."

        "Não sei em quem acreditar.":
            dorian "Não sei em quem acreditar."

            gladys "Então comece desconfiando de quem elogia demais aquilo que o senhor já deseja ouvir."

    gladys "Guarde amigos que o deixam desconfortável de vez em quando. Eles nos lembram de quem somos quando estamos ocupados tentando parecer outra coisa."

    gladys "Meu pai acredita que beleza está acima da bondade. Lorde Henry talvez não diga isso tão diretamente, mas sorri quando alguém acredita."

    gladys "Eu penso diferente. A beleza abre portas, sim. Mas não ensina ninguém a permanecer nelas com dignidade."

    dorian "E o que ensina?"

    gladys "Caráter. Honestidade. Consciência. Coisas menos brilhantes, mas mais necessárias."

    gladys "O senhor é belo, Dorian. Todos percebem isso antes mesmo que fale. Mas tome cuidado para não transformar esse dom em desculpa."

    menu:
        "Tentarei lembrar disso.":
            $ influencia_campbell += 1
            dorian "Tentarei lembrar disso."

            gladys "Tente praticar, não apenas lembrar."

        "Isso parece difícil.":
            dorian "Isso parece difícil."

            gladys "É difícil. Por isso tantos preferem discursos bonitos a escolhas corretas."

        "Talvez beleza seja uma desculpa inevitável.":
            $ influencia_campbell -= 2
            dorian "Talvez beleza seja uma desculpa inevitável."

            gladys "Não, senhor Gray. Essa é justamente a mentira que homens como meu pai e Lorde Henry esperam que o senhor aceite."

    gladys "A beleza é um presente, não uma desculpa. Se um dia começar a acreditar que sua aparência o coloca acima dos outros, então Lorde Henry e meu pai terão vencido sem precisar dizer mais nada."

    gladys "Você vai continuar visitando nossa casa?"

    menu:
        "Sim, ainda quero aprender com você.":
            $ influencia_campbell += 1
            dorian "Sim. Ainda quero aprender com você."

            gladys "Então venha com os olhos abertos."

        "Sim, Alan e Henry são fascinantes.":
            $ influencia_campbell -= 2
            dorian "Sim. Alan e Lorde Henry são fascinantes."

            gladys "Fascinantes, sim. Mas também perigosos. O brilho deles pode cegar mais do que iluminar."

        "Sim, ainda tenho algo a compreender.":
            dorian "Sim. Acredito que ainda tenho algo a aprender lá."

            gladys "Então venha com os olhos abertos."

    gladys "Verá meu pai transformar sentimentos em fraqueza, Lorde Henry transformar vaidade em filosofia e minha mãe tentando manter alguma humanidade naquela mesa."

    gladys "E talvez também me veja, se quiser ouvir alguém que não pretende elogiá-lo, apenas adverti-lo."

    dorian "Eu quero ouvir."

    gladys "Ótimo. Então talvez possamos ser amigos, senhor Gray."

    dorian "Eu gostaria disso."

    gladys "Eu também. Mas não espere elogios fáceis. Já existem pessoas demais elogiando sua beleza."

    "Naquela noite, Dorian apenas caminhou ao lado de Gladys e ouviu."

    if influencia_campbell >= 2:
        jump final_cap3_bom
    else:
        jump final_cap3_ruim


label final_cap3_bom:

    "Depois disso, Dorian continuou frequentando a casa da família Campbell durante dois meses. Dizia a si mesmo que voltava pelos jantares e conversas, mas sabia que as palavras de Gladys permaneciam em sua mente."

    # Parte 5 - Dorian e Basil se reencontrando depois de três meses, quando Basil retorna de Paris.

    scene casa-dorian with fade
    show basil-neutro at right, position_left with dissolve
    show dorian-neutro at left, position_left with dissolve

    basil "Dorian!"

    dorian "Basil!"

    basil "Três meses em Paris, e ainda assim parece que fiquei longe por anos."

    basil "Confesso que tive medo de voltar e encontrar apenas a voz de Henry em você. Mas há algo diferente no seu olhar. Parece menos perdido."

    dorian "Como é bom te ver, Basil. Senti sua falta. Enquanto esteve fora, conheci a família Campbell."

    basil "Alan Campbell?"

    dorian "Sim."

    basil "Então Henry realmente não perdeu tempo."

    basil "Alan é brilhante, mas perigoso. Ele transforma frieza em inteligência e chama isso de verdade."

    dorian "Gladys me fez perceber isso."

    basil "Gladys Campbell? Então ainda há esperança naquela casa."

    basil "Se ela fez você duvidar das certezas de Henry e Alan, já a considero uma boa influência."

    dorian "Ela é."

    basil "Fico feliz em ouvir isso. Mas já estou de saída, Dorian. Preciso ir para casa descansar. Ainda estou cansado do trabalho em Paris e da viagem de volta."

    dorian "Certo. Amanhã irei até sua casa para conversarmos melhor."

    basil "Fique à vontade para ir quando quiser."

    basil "Mas antes de sair, Dorian, preciso lhe dizer algo."

    basil "Independente do que você se transforme, continuarei sendo seu amigo."

    dorian "..."

    dorian "Digo o mesmo, Basil."

    basil "Então até amanhã, meu amigo."

    dorian "Até amanhã."

    return


label final_cap3_ruim:

    $ estado_retrato += 1

    "Depois disso, Dorian continuou frequentando a casa da família Campbell durante dois meses. Dizia a si mesmo que voltava para compreender melhor aquele mundo, mas pouco a pouco passou a admirar justamente aquilo que Gladys tentava advertir."

    "As palavras de Alan e Lorde Henry permaneceram em sua mente com mais força do que as de Gladys. A beleza começava a parecer menos um dom e mais uma permissão."

    scene casa-dorian with fade
    show basil-neutro at right, position_left with dissolve
    show dorian-neutro at left, position_left with dissolve

    basil "Dorian!"

    dorian "Basil!"

    basil "Três meses em Paris, e ainda assim parece que fiquei longe por anos."

    basil "Confesso que tive medo de voltar e encontrar apenas a voz de Henry em você."

    basil "E agora... não sei se esse medo era exagero."

    dorian "Como é bom te ver, Basil. Enquanto esteve fora, conheci a família Campbell."

    basil "Alan Campbell?"

    dorian "Sim."

    basil "Então Henry realmente não perdeu tempo."

    basil "Alan é brilhante, mas perigoso. Ele transforma frieza em inteligência e chama isso de verdade."

    dorian "Talvez ele apenas enxergue o mundo sem ilusões."

    basil "Essa é exatamente a frase que eu temia ouvir."

    dorian "Gladys também tentou me advertir."

    basil "Tentou?"

    dorian "Sim. Mas talvez ela seja parecida demais com você."

    basil "E isso se tornou um defeito?"

    dorian "Não um defeito. Apenas... uma forma de ver o mundo que talvez não seja a minha."

    basil "Dorian..."

    basil "A beleza é um dom, mas também é uma armadilha. Se começar a acreditar que sua aparência o coloca acima dos outros, então já terá começado a se perder."

    dorian "Talvez eu só esteja começando a entender o que possuo."

    basil "Então talvez eu tenha voltado tarde demais."

    dorian "Não diga isso."

    basil "Já estou de saída, Dorian. Preciso ir para casa descansar. Ainda estou cansado do trabalho em Paris e da viagem de volta."

    dorian "Certo. Amanhã irei até sua casa para conversarmos melhor."

    basil "Vá quando quiser."

    basil "Mas antes de sair, preciso lhe dizer algo."

    basil "Independente do que você se transforme, continuarei sendo seu amigo."

    dorian "..."

    dorian "Digo o mesmo, Basil."

    basil "Então até amanhã, meu amigo."

    dorian "Até amanhã."

    return