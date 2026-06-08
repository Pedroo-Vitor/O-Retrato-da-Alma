# Efeito de bounce para os personagens quando falarem.
transform bounce:
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    repeat 1

# Programação do bounce para os personagens.
init python:

    #PRINCIPAIS
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

    #CAPÍTULO 2
    def sibyl_bounce(event, interact=True, **kwargs):

        if event == "show":

            if renpy.showing("sibyl-neutra"):

                renpy.show(
                    "sibyl-neutra",
                    at_list=[bounce]
                )

    #CAPÍTULO 3
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

# Variável que armazena os finais ruins.
default estado_retrato = 0