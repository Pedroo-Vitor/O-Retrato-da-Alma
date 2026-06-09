label capitulo_4:

    scene capitulo4-transicao with fade
    pause

    if estado_retrato == 0:
        jump capitulo4_dorian_envelhecido
    else:
        jump capitulo4_dorian_jovem

# Final 1 - Dorian envelheceu normalmente.
label capitulo4_dorian_envelhecido:

    scene londres-1896 with dissolve

    "Dez anos se passaram desde que Dorian conheceu Sibyl Vane e a família Campbell."

    "Dorian e Sibyl se casaram, Gladys permaneceu uma grande amiga e, com o passar dos anos, Dorian envelheceu como qualquer ser humano."

    scene dorian-caminhando-rua-nevoa with fade

    dorian "Amanhã faço trinta anos... Devo preparar um festa!"

    scene basil-abordando-dorian-na-rua with dissolve

    basil "Dorian, que sorte encontrá-lo!"

    dorian "Basil Hallward?"

    basil "Não está me reconhecendo?"

    dorian "Com essa névoa toda? Mal consigo reconhecer minha própria casa."

    basil "Já estamos na frente da sua casa. Deixe-me entrar por um momento. Tenho algo para lhe dizer"

    scene dorian-basil-conversando-casa-dorian with dissolve

    dorian "Do que se trata? espero que não tenha nada a ver comigo."

    basil "E não se trata. Só vim me despedir, viajarei amanhã para a França por uma semana, pegarei o trem da meia-noite."

    dorian "Ahh. Era só isso. Por um momento fiquei preocupado. Ainda não me acostumei com você vindo tarde da noite apenas para se despedir."

    basil "Desculpe, não era a minha intenção. Hahaha!"

    "O que era para ser uma despedida simples se tornou em uma longa conversa..."

    scene basil-se-despedindo-dorian with dissolve

    dorian "Até amanhã, Basil. Estarei com Henry na estação."

    basil "Obrigado, Dorian, por ser tão gen..."

    scene basil-pergunta-sobre-o-quadro with dissolve

    basil "Espere! Quase ia esquecendo. Antes de partir, preciso perguntar algo. Onde está o retrato que pintei?"

    dorian "Qual?"

    basil "O retrato que pintei de você. A minha melhor obra, não vejo ela em lugar nenhum."

    dorian "Ahhh... Então... Ela está no sótão. Coloquei-o lá há muitos anos e acabei esquecendo."

    scene basil-indignado-com-dorian with dissolve

    basil "Esqueceu minha melhor obra?"

    dorian "Hahaha! Foi mal..." 
    dorian "Eu te levo ao sótão. Vamos vê-la."

    scene retrato-sotao-coberto with dissolve
    pause

    dorian "O retrato está ali, debaixo daquele pano."

    basil "Então retire o pano, Dorian. Já faz uma década que não vejo o meu melhor trabalho."

    jump fim_cap4_final1


# Finais 2 e 3 - Dorian continua jovem.
label capitulo4_dorian_jovem:

    scene londres-1896 with dissolve

    if estado_retrato == 1:

        "Dez anos se passaram desde que Dorian conheceu Sibyl Vane e a família Campbell."

        "Durante esse período, Dorian alternou entre boas e más escolhas. Às vezes, sentia culpa; em outras, preferia ignorá-la."

        "Sua aparência, porém, não mudou. Em Londres, diziam que Dorian Gray havia descoberto o elixir da juventude."

    else:

        "Dez anos se passaram desde que Dorian conheceu Sibyl Vane e a família Campbell."

        "Dorian passou a viver apenas pelo prazer, sem se preocupar com as consequências. Pouco a pouco, começou a pensar e agir como Lorde Henry."

        "Sua aparência permaneceu intocada. Alguns acreditavam que Dorian Gray havia descoberto o segredo da imortalidade."

    scene dorian-caminhando-rua-nevoa with fade

    dorian "Amanhã faço trinta anos... Devo preparar uma festa."

    scene basil-abordando-dorian-na-rua with dissolve

    basil "Dorian, que sorte encontrá-lo!"

    dorian "Basil Hallward?"

    basil "Não está me reconhecendo?"

    dorian "Com essa névoa toda? Mal consigo reconhecer minha própria casa."

    basil "Já estamos na frente da sua casa. Deixe-me entrar por um momento. Tenho algo para lhe dizer"

    scene dorian-basil-conversando-casa-dorian with dissolve

    dorian "Do que se trata? espero que não tenha nada a ver comigo."

    basil "E não se trata. Só vim me despedir, viajarei amanhã para a França por uma semana, pegarei o trem da meia-noite."

    dorian "Ahh. Era só isso. Por um momento fiquei preocupado. Ainda não me acostumei com você vindo tarde da noite apenas para se despedir."

    basil "Desculpe, não era a minha intenção. Hahaha!"

    "O que era para ser uma despedida simples se tornou em uma longa conversa..."

    scene basil-se-despedindo-dorian with dissolve

    dorian "Até amanhã, Basil. Estarei com Henry na estação."

    basil "Obrigado, Dorian, por ser tão gen..."

    scene basil-pergunta-sobre-o-quadro with dissolve

    basil "Espere! Quase ia esquecendo. Antes de partir, preciso perguntar algo. Onde está o retrato que pintei?"

    dorian "Qual?"

    basil "O retrato que pintei de você. A minha melhor obra, não vejo ela em lugar nenhum."

    dorian "Ahhh... Então... Ela está no sótão. Coloquei-o lá há muitos anos e acabei esquecendo."

    scene basil-indignado-com-dorian with dissolve

    basil "Esqueceu minha melhor obra?"

    dorian "Hahaha! Foi mal..." 
    dorian "Eu te levo ao sótão. Vamos vê-la."

    scene retrato-sotao-coberto with dissolve

    dorian "O retrato está ali, debaixo daquele pano."

    basil "Então retire o pano, Dorian. Já faz uma década que não vejo o meu melhor trabalho."

    if estado_retrato == 1:
        jump fim_cap4_final2
    else:
        jump fim_cap4_final3