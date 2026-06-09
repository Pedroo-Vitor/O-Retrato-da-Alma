# Efeito de bounce para os personagens quando falarem
transform bounce:
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    #repeat 1

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

# Personagens

# PRINCIPAIS
define dorian = Character("Dorian Gray", color="#E8D845", callback=dorian_bounce)
define basil = Character("Basil Hallward", color="#C0C839", callback=basil_bounce)
define henry = Character("Henry Wotton", color="#ED6101", callback=henry_bounce)

# CAPÍTULO 1
define naoRevelado = Character("???", color="#FFFFFF")

#CAPÍTULO 2
define ator = Character("Ator(a)", color="#AAAAAA")
define desconhecido = Character("James vane", color="#888888")
define sibyl = Character("Sibyl Vane", color="#3A5A93", callback=sibyl_bounce)

# CAPÍTULO 3
define alan = Character("Alan Campbell", color="#6C472A", callback=alan_bounce)
define elizabeth = Character("Elizabeth Campbell", color="#FAF2DE", callback=elizabeth_bounce)
define gladys = Character("Gladys Campbell", color="#9B59B6", callback=gladys_bounce)
define mordomo = Character("Mordomo", color="#888888")
