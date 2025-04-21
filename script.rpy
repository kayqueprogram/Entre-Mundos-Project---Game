# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg pesadelo with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    play music "audio/trilhas/to_dive.wav"

    

    voice "audio/narration/aud001.ogg"

    "Eu estou de volta àquela casa, a opressão familiar  está me envolvendo como uma nuvem densa. "
   
    voice "audio/narration/aud002.ogg"

    "As paredes parecem se fechar sobre mim, o ar é pesado e está difícil de respirar. "
    
    voice "audio/narration/aud003.ogg"
    
    "Meu coração acelera, eu sei muito bem o que vai acontecer."

    voice "audio/narration/aud004.ogg"

    s "I-isso não pode estar acontecendo..."

    voice "audio/narration/aud005.ogg"  

    "I-isso não pode estar acontecendo..."

    show pai with hpunch

    play sound "audio/hard-slap-46388.mp3"

   
    voice "audio/narration/aud006.ogg"

    "Antes que eu pudesse reagir, senti o impacto de um tapa no rosto, o som ressoou pela sala. "

    scene bg pesadelo with hpunch
    
    voice "audio/narration/aud007.ogg"   

    "Caio no chão, a dor irradia pela minha face, e lágrimas surgem em meus olhos sem que eu queira."
    
    voice "audio/narration/aud008.ogg"

    "A voz fria e desdenhosa da minha mãe ecoou da cozinha."

    show mae with dissolve

  
    voice "audio/narration/aud009.ogg"

    m "Deixe-o. Ele não vale nosso tempo."

    voice "audio/narration/aud010.ogg"

    "Tento me levantar, mas uma dor lancinante percorre pelo meu corpo. "
    hide mae with dissolve

    voice "audio/narration/aud011.ogg"

    "Olhei ao redor, desesperado, buscando uma saída...\nmas a casa parecia um labirinto sem fim, cada porta me levando de volta ao mesmo lugar."

    voice "audio/narration/aud012.ogg"

    s "Eu... preciso sair daqui... Preciso fugir..."

    
 
    "De repente, ouvi uma risada distante, suave e reconfortante. Era a voz de Toshiro, meu antigo amigo."

    

    t "Shido, você pode superar isso. Isso não é real!!"

    show pai with hpunch

   

    "A presença de Toshiro trouxe uma leve esperança, mas o som se dissipou rapidamente, substituído pelo grito furioso de meu pai."

   

    p "Você nunca vai escapar de nós!"


    scene bg espc with hpunch

    

    "Tento correr, mas meus pés parecem presos ao chão. Grito, clamando por ajuda, mas minha voz não faz som. "
    
    

    "O desespero tomou conta, e senti uma escuridão sufocante me envolver."

    stop music

    scene bg acr with fade

    play sound "audio/despert.mp3"



    "No momento em que parecia que eu não conseguiria mais lutar, acordo sobressaltado, suando e ofegante. "

 

    "Estou de volta ao meu quarto no orfanato Kibou-en. A familiaridade do ambiente ao redor me trouxe um alívio imediato."

    stop sound

    

    s "Foi apenas um sonho... Apenas um sonho..."

    voice "audio/narração/aud022.ogg"

    "Os fantasmas do meu passado ainda me assombram..."

    scene bg dormshido with fade

    voice "audio/narração/aud023.ogg"

    "Com o coração ainda acelerado, me levanto devagar da cama, tentando não fazer barulho para não acordar Toya e Kazuma. "

    scene bg dorshido_blurred
    show relogio at truecenter with wipeup

    voice "audio/narração/aud024.ogg"

    "Olho para o relógio no criado-mudo: 6:12 da manhã. "

    voice "audio/narração/aud025.ogg"

    "Eu não vou conseguir dormir "

    voice "audio/narração/aud026.ogg"

    "Vou dar uma volta pelo orfanato"

    voice "audio/narração/aud027.ogg"

    "Preciso respirar um pouco"

    scene bg dorm_corr_msc with fade

    voice "audio/narração/aud028.ogg"

    "Caminho silenciosamente pelo corredor, observando os quartos ainda escuros e silenciosos. "

    voice "audio/narração/aud029.ogg"

    "A luz fraca da madrugada começa a infiltrar-se pelas janelas, lançando sombras compridas nas paredes. "

    play audio "audio/porta.mp3"

    scene bg jardim_orfanato with fade

    play audio "audio/brisa.mp3"

    voice "audio/narração/aud030.ogg"

    "Sinto uma brisa suave ao abrir a porta para o jardim e deixo o ar fresco aliviar a tensão que ainda estava em meu peito."

    voice "audio/narração/aud031.ogg"

    "Sento-me em um banco próximo a uma árvore, observando o orfanato despertar lentamente."

    voice "audio/narração/aud032.ogg"

    "Alguns funcionários começavam a preparar o café da manhã na cozinha e os primeiros pássaros começavam a cantar. "

    play sound "audio/passos.mp3"

    voice "audio/narração/aud033.ogg"

    "Enquanto respiro fundo, sentindo o aroma das flores no jardim, ouço passos leves se aproximando."

    stop sound

    show akane cnvs with dissolve

    show book act1 with wipeup

    voice "audio/narração/aud034.ogg"
    
    "Akane não consegue se comunicar usando a fala. Então quando encontra alguém que não sabe a língua de sinais, ela usa  este caderno"


    menu:
        "Estou bem":
            hide book act1
            show book act1_2
            "'Bom dia, Akane. Estou... bem. Apenas acordei cedo demais.'" 
            hide book act1_2 with dissolve
            hide akane cnvs
            show akane sorr

            "Ela lê minha resposta e sorri de forma compreensiva, sentando-se ao meu lado no banco. "

            "Por um momento, ficamos em silêncio, apenas apreciando a tranquilidade do amanhecer."

            "De repente, uma voz familiar interrompe nosso momento. "

            show toya confused at right with dissolve

            

            "Toya aparece"

            "Por que ele tinha que aparecer justo agora?"

            ty "Olá? Alguém aí?"

            hide akane sorr
            show akane confused at Position(xpos=0.3, ypos=0.99) with dissolve

            "Akane recua, desconcertada. Me parece que eles não se dão muito bem"
            
            s "Aqui vemos um homem visionário, bom dia Toya!"

            "Toya recua por um instante, e logo, percebo a gafe que cometi"

            s "“D-desculpa Toya, eu juro que não foi minha intenção..."

            hide toya confused

            show toya confused2 at right 

            ty "Hahahaha"

            ty "Você está meio engraçadinho hoje não?"

            s "Não foi por querer, sério"

            "Akane se mostra visivelmente incomodada por não fazer ideia do que está acontecendo."

            "Eu meio que entendo isso, estar perdido em meio aos outros..."

            ty "Tem mais alguém aqui?"

            s "Sim... a Akane"

            hide toya confused2

            show toya confused at right

            ty "Oh... entendo. Vim te chamar para tomar o café da manhã, Kazuma também está te esperando, vamos?"
            
            menu: 
                "Ficar com Akane":

                    jump akane



                "Ir com Toya":
                    "Eu realmente querto ir com Toya, mas acho que não terei outra oportunidade de conhecer Akane melhor"
                    jump akane

        
        "Poderia estar melhor":
            hide book act1
            show book act1_2_2
            "'Poderia estar melhor, eu acho'"

            "Ela lê minha resposta e sorri de forma compreensiva, sentando-se ao meu lado no banco. "

            "Por um momento, ficamos em silêncio, apenas apreciando a tranquilidade do amanhecer."

            "De repente, uma voz familiar interrompe nosso momento. "

            show toya confused at right with dissolve

            

            "Toya aparece"

            "Por que ele tinha que aparecer justo agora?"

            ty "Olá? Alguém aí?"

            hide akane sorr
            show akane confused at Position(xpos=0.3, ypos=0.99) with dissolve

            "Akane recua, desconcertada. Me parece que eles não se dão muito bem"
            
            s "Aqui vemos um homem visionário, bom dia Toya!"

            "Toya recua por um instante, e logo, percebo a gafe que cometi"

            s "“D-desculpa Toya, eu juro que não foi minha intenção..."

            hide toya confused

            show toya confused2 at right 

            ty "Hahahaha"

            ty "Você está meio engraçadinho hoje não?"

            s "Não foi por querer, sério"

            "Akane se mostra visivelmente incomodada por não fazer ideia do que está acontecendo."

            "Eu meio que entendo isso, estar perdido em meio aos outros..."

            ty "Tem mais alguém aqui?"

            s "Sim... a Akane"

            hide toya confused2

            show toya confused at right

            ty "Oh... entendo. Vim te chamar para tomar o café da manhã, Kazuma também está te esperando, vamos?"

            menu: 
                "Ficar com Akane":

                    jump akane



                "Ir com Toya":
                    "Eu realmente querto ir com Toya, mas acho que não terei outra oportunidade de conhecer Akane melhor"
                    jump akane

            



    return
