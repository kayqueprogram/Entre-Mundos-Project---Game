
label akane:

    hide toya confused
    show toya interested at right

    ty "Está bem. Se você acha melhor assim..."

    s "Te vejo depois, Toya"

    "Ele não diz mais nada, apenas vira as costas e sai andando. Por algum motivo, mostrava uma expressão meio amargurada."

    "Mas deve ser só impressão, coisa da minha cabeça."

    hide toya interested with dissolve

    "Nossa mente prega peças em nós ás vezes..."

    "Certo?"

    hide akane confused with dissolve
    show akane rage with dissolve

    "Akane me chama a atenção"

    "Sua expressão interrogativa já me diz o que ela quer saber, sem que eu precise olhar o caderno que ela aponta em minha direção."

    hide akane rage 
    show akane cnvs
                    
    show book act1_3 with wipeup

    "'Ele veio me chamar para tomar o café da manhã com eles, mas eu prefiro continnossa conversa'"

    hide akane cnvs
    show akane sorr

    hide book act1_3 with dissolve

    "Espero Akane terminar de ler. Vejo um pequeno brilho de satisfação em seus olhos."

    show book act1_4 with wipeup

    "'Bela escolha a sua. Mas eu acho que você deveria ir tomar café, as aulas começam daqui a pouco'"

    hide book act1_4

    show book act1
    "Quando começam as aulas? "

    hide book act1_5

    show book act1_6

    "'Dentro de 5 minutos, te vejo na aula, Tchau! '"

    hide book act1_6 with dissolve
    hide akane cnvs with dissolve

    "Mal termino de ler, Akane toma o caderno e sai correndo em direção ao refeitório..."

    "Devo admitir que não esperava essa reação."

    menu: 
        "Ela tem um olhar diferente":
            "Aquele olhar... de alguma forma... estou hipnotizado"


        "Seu sorriso...":
            "É um sorriso tímido, alegre..., mas me sinto tão tenso..."

            "Sinto como seu eu não pudesse mover um único músculo, mesmo se tentasse"

            "Acho que vou para o meu quarto, até dar a hora..."
                    

            scene bg corredor_escola with dissolve

            play sound "audio/Alarme da escola.ogg"

            "Estou atrasado, ao que parece, todos já entraram em suas salas"

            "Preciso encontrar logo a minha..."

            show irina normal with hpunch

            play sound "audio/hard-slap-46388.mp3"

            s "Ugh!"

            s "D-desculpa! Não foi minha intenç-"

            ds "É você, Mizushima?"

            s "Ah, sim, sou eu"

            ds "Ótimo, eu estava te procurando, vamos! "

            s "Mas quem é voc-"

            hide irina normal
            show irina serious

            ds "Ah, verdade ainda não me apresentei"

            ir "Meu nome é Irina, sou a professora da classe 3-A, no caso, a {b}sua classe senhor{/b}. "

            "Sinto uma ponta de ironia em sua fala, como eu saberia que essa é minha classe? "

            hide irina serious
            show irina serious2

            s "Ah, sim, desculpe sensei. Ninguém soube me informar onde era minha sala"

            s "E ninguém da coordenação me falou nada, desde que cheguei aqui"

            hide irina serious2
            show irina normal

            irs "Esse orfanato... está cada vez pior... nesse caso, seja bem-vindo! "

            irs "Você quer se apresentar para a classe? "

            menu: 
                "Sim, Claro!":

                    s "Quer dizer... é o normal a se fazer, não?"

                    hide irina normal
                    show irina serious
                           
                    irs"Deveria ser, mas nem todo mundo gosta de estar exposto aos olhares alheios"

                    hide irina serious
                    show irina serious2

                    s "Eu sou uma dessas pessoas, mas..."


                    "Eu devo criar minha primeira impressão, e ela deve ser boa o suficiente, para que eu consiga criar novas conexões"

                    hide irina serious2
                    show irina normal

                    irs "Vamos ver então"

                    scene bg escadas_escola with dissolve

                    "Meu coração bate forte enquanto sigo a professora pelo lance de escadas."

                    scene bg corredor_escola2 with dissolve

                    "A primeira porta do corredor do terceiro andar possui uma marcação: “3-A”"

                    "Irina sensei abre a porta e entra"

                    scene bg school_room with fade

                    show irina normal with dissolve

                    irs "Bom dia a todos! Consegui encontrar a ovelhinha perdida! "

                    play sound "audio/people_laugh.ogg"

                    "Os alunos riem do trocadilho de Irina, enquanto estou parado na porta, hesitando na hora H."

                    stop sound

                    "Sinto como se fosse um grande passo. Um momento decisivo de minha vida."

                    "Se for parar para pensar, é mesmo"

                    "Se eu falhar na apresentação, provavelmente ninguém vai querer se aproximar de mim."

                    hide irina normal with dissolve

                    "Entro na sala de cabeça baixa, para não ter que dar de cara com olhares curiosos."
                           
                    "É uma sala espaçosa, mas apesar disso, as mesas são grandes e há pouco espaço entre elas."

                    "As mesas são de madeira, com um espaço abaixo, para guardar os materiais, é simples, mas eficiente."

                    "Paro em frente à turma, sentindo um leve receio, e começo a observar cada um deles."

                    "Foi um choque, quando vi que uma das meninas não possuía um dos olhos."

                    "Eu já deveria ter me acostumado, afinal, convivo com Kazuma, que já não tem uma das pernas, e Toya, que é cego desde seu nascimento."

                    "Eu não sei se “se acostumar” é a coisa certa a se fazer"

                    "O certo não seria “aprender a lidar? ”"

                    "Percebo um movimento... seus cabelos negros se movimentando... é alguém familiar para mim..."

                    show akane sorr at left, with dissolve

                    "É Akane! Que surpresa estarmos na mesma turma!"

                    hide akane sorr with dissolve

                    irs "Seu nome é Shido Mizushima"

                    s "Prazer em conhece-los pessoal! Espero me dar bem com todos vocês! "

                    "E agora? ... "

                    "Simples foi dizer que eu me apresentaria"

                    s "Tenho alguns hobbies como leitura e astronomia..."

                    "Não foi a apresentação que eu queria, devo dizer algo mais impactante não?"

                    "Termino por não dizer nada e a professora retoma a palavra."

                    "Vejo meus novos colegas cochichando entre si... bem, poderia ter sido pior."

                    show irina serious with dissolve

                    "A professora se vira para mim, um tanto desinteressada"

                    irs "Não temos muitos lugares livres, mas temos o suficiente para que possa escolher onde vai se sentar "

                    hide irina serious with dissolve

                    "Irina-sensei ri de sua fala irônica e eu me volto para os únicos lugares disponíveis na sala"
                    
                    show akane confused with dissolve

                    "Um é próximo de Akane."

                    hide akane confused with dissolve

                    show yuno normal with dissolve
                    

                    "E o outro, é próximo de uma linda menina de cabelo rosa, que parecia estar interagindo com Akane."

                    hide yuno normal

                    "Decido me sentar ao lado de Akane, afinal, eu já a conheço."

                    show akane sorr with dissolve

                    "Akane me cumprimenta com um sorriso... e que sorriso!"

                    hide akane sorr with dissolve

                    "Logo após, ela se volta para a menina ao seu lado e começam a se comunicar usando a linguagem de sinais."

                    show yuno sorr with dissolve

                    y "É um prazer te conhecer Mizu! "

                    y "Parece que você já conheceu minha amiga, Akane, ela é surda, então na maior parte do tempo, eu traduzo as coisas para ela"

                    "Mizu? ..."

                    "Que tipo de pessoa dá apelido a alguém que acabou de conhecer?"

                    s "Mizu? "

                    "Nem sei porque disse isso em voz alta, não possuo boas lembranças com este apelido."

                    y "Combina, não é? "

                    s "Se você diz"

                    y "Você tem bom gosto Akane"

                    s "Ela entendeu isso? "

                    y "Ela domina a leitura labial até certo ponto, e sim, ela conseguiu entender"

                    ak `(...)`

                    y "Queremos que se sinta bem-vindo entre nós!"

                    ak "(...)"

                    y "Não repara na personalidade da Irina-Sensei, ela pode ter um gênio difícil ás vezes"

                    "Que confusão"

                    "Não dá para saber se é Akane quem está falando ou se é Yuno"

                    "Ou se Akane completa o raciocínio de Yuno, ou vice-versa"

                    y "Akane quer que você saiba que ela é a representante de classe, e que se precisar de qualquer coisa, pode vir até ela. "

                    ak "(...)"

                    y "Podemos dar uma volta pela escola, caso não a tenha conhecido ainda. "

                    s "Bem... é meu primeiro dia.... e eu aceitaria sim."

                    hide yuno sorr with dissolve

                    "Não consigo evitar um sorriso. Parece que fiz alguns amigos."

                    "Irina-sensei passa ao meu lado e nos dirige um sorriso um tanto pretensioso"

                    show irina normal with dissolve

                    irs "Parece que você já se enturmou, não é mesmo? "

                    show yuno normal at left with dissolve 

                    y "A Akane disse que vai leva-lo para conhecer a escola, assim que a aula terminar. "

                    irs "Aproveite e mostre os clubes para ele. Não quero ver nenhum aluno meu em ociosidade"

                    irs "Agora, vamos seguir com a aula pessoal! Silêncio. "

                    hide irina normal with dissolve

                    show akane cnvs with dissolve

                    ak "(...)"

                    y "Você vai gostar daqui, embora seja um orfanato, não é um lugar ruim."

                    hide akane cnvs with dissolve
                    hide yuno normal with dissolve

                    show irina normal with dissolve

                    irs "Pessoaaal... a educação foi feita para ser usada, e não para ser guardada em suas mochilas, Silêncio! "

                    hide irina normal with dissolve

                    "Sinto que situações assim são comuns por aqui. Devo me acostumar a isso também."

                    show irina normal with dissolve

                    "Voltando ao tema, alguém poderia me dizer qual a importância de Beatrice para a obra ‘Do Inferno ao Paraíso’? "

                    "O que eu deveria fazer?"

                    menu:
                        "Levantar a Mão":
                            "Eu já li esse livro, mas não me recordo muito bem de seu conteúdo"

                            "Bem, acho que não custa nada arriscar..."

                            s "Professora... é aquele livro escrito por Davi Albuquerque??"

                            hide irina normal
                            show irina serious

                            "Irina-sensei me olha um tanto surpresa. Acho que normalmente ninguém se arriscaria a responder."

                            irs "Sim Mizushima. Esse mesmo. Você pode responder à pergunta feita? "

                            hide irina serious
                            show akane cnvs with dissolve

                            "Olho para o lado e vejo Akane me observando. Provavelmente Yuno já deve ter passado para ela o que está acontecendo."

                            hide akane cnvs with dissolve
                            show irina serious with dissolve

                            s "S-sim, eu vou tentar, sensei... "

                            s "Bem... Beatrice foi... digamos que uma figura simbólica no livro. Ela simbolizava... se eu não me engano, a graça divina e a salvação espiritual..."

                            s "A personagem Beatrice, foi fruto de um amor platônico, ou talvez, não correspondido, devido as circunstâncias da época..."

                            irs "E que circunstâncias seriam essas?"

                            s "Casamento arranjado... por exemplo? "

                            irs "“Muito bem Mizushima! Vejo que alguém aqui pode-se salvar, quando se trata de conhecimento literário... é uma obra que todos vocês já deveriam ter lido há muito tempo!"

                            hide irina serious with dissolve
                            show yuno normal with dissolve

                            y "Professora..."

                            hide yuno normal with dissolve
                            show irina serious with dissolve

                            irs "Diga, Yoshida"

                            show yuno normal at left with dissolve

                            y "Akane quer destacar um ponto sobre este livro. "

                            irs "Prossiga"

                            hide irina serious with dissolve
                            hide yuno normal with dissolve
                            show akane sorr with dissolve

                            "Akane gesticula freneticamente. Mal dando tempo para a coitada da Yuno respirar"

                            ak "(...)"

                            hide akane sorr with dissolve

                            show yuno sorr with dissolve

                            y "Akane diz que.... É interessante, como o livro destaca a ideia de punição divina... onde a alma da pessoa... vai ser punida ou recompensada por cada ação que teve em vida. "

                            hide yuno sorr with dissolve

                            show irina serious2 with dissolve

                            irs "Muito bem Tachibana! E Agraço seu auxílio Yoshida! Todos os que se pronunciaram terão mais 1 ponto em sua média final!"

                            hide irina serious2 with dissolve

                            "E assim a aula se seguiu durante toda a manhã..."

                            play sound "audio/Alarme da escola.ogg"

                            "É chegado o final da aula, os alunos se levantam ansiosos, para irem almoçar. "

                            show yuno sorr with hpunch

                            y "Ei Mizu, vamos?"

                            s "Para onde?"

                            hide yuno sorr with dissolve
                            show akane rage with hpunch

                            "Akane demonstra impaciência e me empurra para fora da sala, Yuno parece estar se divertindo com a situação. "

                            hide akane rage with dissolve


                            y "“Hahahah... não se lembra que nós íamos te mostrar a escola? Tem muita coisa para ver aqui"

                            scene bg cafeteria with fade

                            s "É que eu não achei que fosse agora"

                            show akane cnvs with dissolve

                            ak "(...)"

                            hide akane cnvs with dissolve
                            show yuno sorr with dissolve

                            y "Azar o seu!"

                            y "Veja Mizu! Este é o refeitório, provavelmente você já o viu de manhã."

                            hide yuno sorr with dissolve

                            "Curiosamente, Kibou-en possuía um interior bem moderno, em contraste com seu exterior antiquado "

                            "Principalmente o refeitório, suas janelas enormes, que dão para o pátio em direção ao portão principal "

                            s "Sim, eu vi... ele é bem espaçoso, pra falar a verdade"

                            ak "(...)"

                            y "Sim, e se você quiser, pode sair e comer na lanchonete aqui perto"

                            s "C-Como? Pode-se sair daqui?"

                            ak "[...]"

                            y "Sim, aqui não é uma prisão, diferente dos outros orfanatos. A partir de uma certa idade você já pode sair, desde que respeite os horários e não tenha nenhum problema que te atrapalhe"

                            ak "[...]"

                            y "Essa é a política do Kibou-en! "

                            "Permaneço perplexo por alguns momentos.  "

                            "Antes de vir para cá, o cenário que imaginei, foi completamente diferente..."

                            "Talvez... eu estivesse seguindo algum tipo de estereótipo proposto na sociedade? "

                            "Na qual lugares como este fossem a representação do inferno? "

                            ak "[...]"

                            y "Mizu?"

                            "Yuno e Akane me fitam, por um instante. Acho que estou viajando por tempo demais."

                            s "Para onde vamos agora?"

                            y "Deixe-me ver.. "

                            y "Você ainda não tem nenhum clube... certo? Que tal conhecer o clube de oratória? "

                            s "Clube de oratória... parece interessante... você e Akane estão nele, não é mesmo?"

                            "Yuno parece ter sido pega de surpresa. Toya e Kazuma me apresentaram alguns lugares desta escola, e o clube de oratória foi um deles. "

                            y "Então você já sabia! Hahaha"

                            s "De certa forma sim, mas você e Akane querem me arrastar para ele?"

                            ak "[...]"

                            "Akane gesticula freneticamente, mal dando tempo a Yuno, acompanhar seus movimentos "

                            "Akane é Líder do Clube de Oratória, mesmo sendo muda, e isso de certa forma é incrível."

                            "Toya, por mais que seja cego, aparentemente, nunca se deixou limitar por sua condição."

                            "Então... qual era a minha justificativa?"

                            y "Akane está dizendo que você deveria dar uma chance. Pode ser uma ótima experiência para você."

                            s "Pode até ser.... eu vou dar uma passada"

                            ak "[...]"

                            y "Ótimo! Venha, vamos apresentar você ao resto do clube."

                            "Akane me toma pelas mãos e me conduz animadamente pelos corredores "

                            s "Mas... eu nunca disse que me juntaria ao clube..."

                            "Já é tarde demais, Yuno está tão animada que já não consegue me ouvir"

                            "Continuamos a caminhar pelos corredores, passando por várias salas e grupos de estudantes, até chegarmos à porta do Clube de Oratória. "

                            "Ao entrar, sou recebido por uma sala cheia de estudantes conversando animadamente. No centro da sala, uma cadeira está vazia, indicando que o presidente do clube ainda não chegou. "

                            "Pessoal, esse é Shido, nosso novo amigo. Ele está interessado em conhecer o clube."

                            "Os membros do clube me olham com curiosidade e começam a se aproximar para se apresentarem. A energia na sala é contagiante, e não consigo evitar um sorriso. "

                            mc "Bem-vindo, Shido! Espero que goste daqui."

                            mc "Apesar de sermos um pouco brincalhões, não há nada que não possamos fazer se nos determinarmos"

                            s "Obrigado, pessoal. É um prazer conhecer todos vocês."

                            "Enquanto conversamos, percebo que Akane está ao meu lado, observando silenciosamente. "

                            "Ela me dá um sorriso encorajador, e eu sinto um calor reconfortante se espalhar por mim. Talvez, só talvez, este lugar não seja tão ruim assim."

                            scene bg months with dissolve



                            



