label akane:

    hide toya confused
    show toya interested at right

    voice "audio/narration/aud053.ogg"

    ty "Está bem. Se você acha melhor assim..."

    voice "audio/narration/aud054.ogg"

    s "Te vejo depois, Toya"

    voice "audio/narration/aud055.ogg"

    "Ele não diz mais nada, apenas vira as costas e sai andando. Por algum motivo, mostrava uma expressão meio amargurada."

    voice "audio/narration/aud056.ogg"

    "Mas deve ser só impressão, coisa da minha cabeça."

    hide toya interested with dissolve

    voice "audio/narration/aud057.ogg"

    "Nossa mente prega peças em nós ás vezes... Certo?"


    hide akane confused with dissolve
    show akane rage with dissolve

    voice "audio/narration/aud058.ogg"

    "Akane me chama a atenção"

    voice "audio/narration/aud059.ogg"

    "Sua expressão interrogativa já me diz o que ela quer saber, sem que eu precise olhar o caderno que ela aponta em minha direção."

    hide akane rage 
    show akane cnvs
                    
    show book act1_3 with wipeup

    voice "audio/narration/aud060.ogg"

    "'Ele veio me chamar para tomar o café da manhã com eles, mas eu prefiro continuar nossa conversa'"

    hide akane cnvs
    show akane sorr

    hide book act1_3 with dissolve

    voice "audio/narration/aud061.ogg"

    "Espero Akane terminar de ler. Vejo um pequeno brilho de satisfação em seus olhos."

    show book act1_4 with wipeup

    voice "audio/narration/aud062.ogg"

    "'Bela escolha a sua. Mas eu acho que você deveria ir tomar café, as aulas começam daqui a pouco'"

    hide book act1_4

    show book act1

    voice "audio/narration/aud063.ogg"
    "Quando começam as aulas? "

    hide book act1_5

    show book act1_6

    voice "audio/narration/aud064.ogg"

    "'Dentro de 5 minutos, te vejo na aula, Tchau! '"

    hide book act1_6 with dissolve
    hide akane cnvs with dissolve

    voice "audio/narration/aud065.ogg"

    "Mal termino de ler, Akane toma o caderno e sai correndo em direção ao refeitório..."

    voice "audio/narration/aud066.ogg"

    "Devo admitir que não esperava essa reação."

    menu: 

        "Seu sorriso...":
            voice "audio/narration/aud068.ogg"
            "É um sorriso tímido, alegre..., mas me sinto tão tenso..."

            voice "audio/narration/aud069.ogg"
            "Acho que vou para o meu quarto, até dar a hora..."
                    

            scene bg corredor_escola with dissolve

            play sound "audio/Alarme da escola.ogg"

            voice "audio/narration/aud070.ogg"

            "Estou atrasado, ao que parece, todos já entraram em suas salas"

            voice "audio/narration/aud071.ogg"

            "Preciso encontrar logo a minha..."

            show irina normal with hpunch

            play sound "audio/hard-slap-46388.mp3"

            s "Ugh!"

            voice "audio/narration/aud072.ogg"

            s "D-desculpa! Não foi minha intenç-"

            voice "audio/narration/aud073.ogg"

            ds "É você, Mizushima?"

            voice "audio/narration/aud074.ogg"

            s "Ah, sim, sou eu"

            voice "audio/narration/aud075.ogg"

            ds "Ótimo, eu estava te procurando, vamos! "

            voice "audio/narration/aud076.ogg"

            s "Mas quem é voc-"

            hide irina normal
            show irina serious


            voice "audio/narration/aud077.ogg"

            ds "Ah, verdade ainda não me apresentei"

            voice "audio/narration/aud078.ogg"

            ir "Meu nome é Irina, sou a professora da classe 3-A, no caso, a {b}sua classe senhor{/b}. "

            voice "audio/narration/aud079.ogg"

            "Sinto uma ponta de ironia em sua fala, como eu saberia que essa é minha classe? "

            hide irina serious
            show irina serious2

            voice "audio/narration/aud080.ogg"

            s "Ah, sim, desculpe sensei. Ninguém soube me informar onde era minha sala"

            voice "audio/narration/aud081.ogg"

            s "E ninguém da coordenação me falou nada, desde que cheguei aqui"

            hide irina serious2
            show irina normal

            voice "audio/narration/aud082.ogg"

            irs "Esse orfanato... está cada vez pior... nesse caso, seja bem-vindo! "

            voice "audio/narration/aud083.ogg"

            irs "Você quer se apresentar para a classe? "

            menu: 
                "Sim, Claro!":

                    voice "audio/narration/aud084.ogg"

                    s "Quer dizer... é o normal a se fazer, não?"

                    hide irina normal
                    show irina serious

                    voice "audio/narration/aud085.ogg"
                           
                    irs"Deveria ser, mas nem todo mundo gosta de estar exposto aos olhares alheios"

                    hide irina serious
                    show irina serious2

                    voice "audio/narration/aud086.ogg"

                    s "Eu sou uma dessas pessoas, mas..."

                    voice "audio/narration/aud087.ogg"
                    "Eu devo criar minha primeira impressão, e ela deve ser boa o suficiente, para que eu consiga criar novas conexões"

                    hide irina serious2
                    show irina normal

                    voice "audio/narration/aud088.ogg"

                    irs "Vamos ver então"

                    scene bg escadas_escola with dissolve

                    voice "audio/narration/aud089.ogg"

                    "Meu coração bate forte enquanto sigo a professora pelo lance de escadas."

                    scene bg corredor_escola2 with dissolve

                    voice "audio/narration/aud090.ogg"

                    "A primeira porta do corredor do terceiro andar possui uma marcação: “3-A”"

                    voice "audio/narration/aud091.ogg"

                    "Irina sensei abre a porta e entra"

                    scene bg school_room with fade

                    show irina normal with dissolve

                    voice "audio/narration/aud092.ogg"

                    irs "Bom dia a todos! Consegui encontrar a ovelhinha perdida! "

                    play sound "audio/people_laugh.ogg"

                    voice "audio/narration/aud093.ogg"

                    "Os alunos riem do trocadilho de Irina, enquanto estou parado na porta, hesitando na hora H."

                    stop sound

                    voice "audio/narration/aud094.ogg"

                    "Sinto como se fosse um grande passo. Um momento decisivo de minha vida."

                    voice "audio/narration/aud095.ogg"

                    "Se for parar para pensar, é mesmo"

                    voice "audio/narration/aud096.ogg"

                    "Se eu falhar na apresentação, provavelmente ninguém vai querer se aproximar de mim."

                    hide irina normal with dissolve

                    voice "audio/narration/aud097.ogg"

                    "Entro na sala de cabeça baixa, para não ter que dar de cara com olhares curiosos."

                    voice "audio/narration/aud098.ogg"
                           
                    "É uma sala espaçosa, mas apesar disso, as mesas são grandes e há pouco espaço entre elas."

                    voice "audio/narration/aud099.ogg"

                    "As mesas são de madeira, com um espaço abaixo, para guardar os materiais, é simples, mas eficiente."

                    voice "audio/narration/aud100.ogg"

                    "Paro em frente à turma, sentindo um leve receio, e começo a observar cada um deles."

                    voice "audio/narration/aud101.ogg"

                    "Foi um choque, quando vi que uma das meninas não possuía um dos olhos."

                    voice "audio/narration/aud102.ogg"

                    "Eu já deveria ter me acostumado, afinal, convivo com Kazuma, que já não tem uma das pernas, e Toya, que é cego desde seu nascimento."
                    
                    voice "audio/narration/aud103.ogg"

                    "Eu não sei se “se acostumar” é a coisa certa a se fazer"

                    voice "audio/narration/aud104.ogg"

                    "O certo não seria “aprender a lidar? ”"

                    voice "audio/narration/aud105.ogg"

                    "Percebo um movimento... seus cabelos negros se movimentando... é alguém familiar para mim..."

                    show akane sorr at left, with dissolve

                    voice "audio/narration/aud106.ogg"

                    "É Akane! Que surpresa estarmos na mesma turma!"

                    hide akane sorr with dissolve

                    voice "audio/narration/aud107.ogg"

                    irs "Seu nome é Shido Mizushima"

                    voice "audio/narration/aud108.ogg"


                    s "Prazer em conhece-los pessoal! Espero me dar bem com todos vocês! "

                    voice "audio/narration/aud109.ogg"

                    "E agora? ... "

                    voice "audio/narration/aud110.ogg"

                    "Simples foi dizer que eu me apresentaria"

                    voice "audio/narration/aud111.ogg"

                    s "Tenho alguns hobbies como leitura e astronomia..."

                    voice "audio/narration/aud112.ogg"

                    "Não foi a apresentação que eu queria, devo dizer algo mais impactante não?"

                    voice "audio/narration/aud113.ogg"

                    "Termino por não dizer nada e a professora retoma a palavra."

                    voice "audio/narration/aud114.ogg"

                    "Vejo meus novos colegas cochichando entre si... bem, poderia ter sido pior."

                    show irina serious with dissolve

                    voice "audio/narration/aud115.ogg"

                    "A professora se vira para mim, um tanto desinteressada"

                    voice "audio/narration/aud116.ogg"

                    irs "Não temos muitos lugares livres, mas temos o suficiente para que possa escolher onde vai se sentar "

                    hide irina serious with dissolve

                    voice "audio/narration/aud117.ogg"

                    "Irina-sensei ri de sua fala irônica e eu me volto para os únicos lugares disponíveis na sala"
                    
                    show akane confused with dissolve

                    voice "audio/narration/aud118.ogg"

                    "Um é próximo de Akane."

                    hide akane confused with dissolve

                    show yuno normal with dissolve

                    voice "audio/narration/aud119.ogg"
                    

                    "E o outro, é próximo de uma linda menina de cabelo rosa, que parecia estar interagindo com Akane."

                    hide yuno normal

                    voice "audio/narration/aud120.ogg"

                    "Decido me sentar ao lado de Akane, afinal, eu já a conheço."

                    show akane sorr with dissolve

                    voice "audio/narration/aud121.ogg"

                    "Akane me cumprimenta com um sorriso... e que sorriso!"

                    hide akane sorr with dissolve

                    voice "audio/narration/aud122.ogg"

                    "Logo após, ela se volta para a menina ao seu lado e começam a se comunicar usando a linguagem de sinais."

                    show yuno sorr with dissolve

                    voice "audio/narration/aud123.ogg"

                    y "É um prazer te conhecer Mizu! "

                    voice "audio/narration/aud124.ogg"

                    y "Parece que você já conheceu minha amiga, Akane, ela é surda, então na maior parte do tempo, eu traduzo as coisas para ela"

                    voice "audio/narration/aud125.ogg"
                    
                    "Mizu? ..."

                    voice "audio/narration/aud126.ogg"

                    "Que tipo de pessoa dá apelido a alguém que acabou de conhecer?"
                    voice "audio/narration/aud125.ogg"
                    

                    s "Mizu? "

                    voice "audio/narration/aud127.ogg"

                    "Nem sei porque disse isso em voz alta, não possuo boas lembranças com este apelido."

                    voice "audio/narration/aud128.ogg"

                    y "Combina, não é? "

                    voice "audio/narration/aud129.ogg"

                    s "Se você diz"

                    voice "audio/narration/aud130.ogg"

                    y "Você tem bom gosto Akane"

                    voice "audio/narration/aud131.ogg"

                    s "Ela entendeu isso? "

                    voice "audio/narration/aud132.ogg"

                    y "Ela domina a leitura labial até certo ponto, e sim, ela conseguiu entender"

                    ak `(...)`

                    voice "audio/narration/aud133.ogg"

                    y "Queremos que se sinta bem-vindo entre nós!"

                    ak "(...)"

                    voice "audio/narration/aud134.ogg"

                    y "Não repara na personalidade da Irina-Sensei, ela pode ter um gênio difícil ás vezes"

                    voice "audio/narration/aud135.ogg"

                    "Que confusão"

                    voice "audio/narration/aud136.ogg"

                    "Não dá para saber se é Akane quem está falando ou se é Yuno"

                    voice "audio/narration/aud137.ogg"

                    "Ou se Akane completa o raciocínio de Yuno, ou vice-versa"

                    voice "audio/narration/aud138.ogg"

                    y "Akane quer que você saiba que ela é a representante de classe, e que se precisar de qualquer coisa, pode vir até ela. "

                    ak "(...)"

                    voice "audio/narration/aud139.ogg"

                    y "Podemos dar uma volta pela escola, caso não a tenha conhecido ainda. "

                    voice "audio/narration/aud140.ogg"

                    s "Bem... é meu primeiro dia.... e eu aceitaria sim."

                    hide yuno sorr with dissolve

                    voice "audio/narration/aud141.ogg"

                    "Não consigo evitar um sorriso. Parece que fiz alguns amigos."

                    voice "audio/narration/aud142.ogg"

                    "Irina-sensei passa ao meu lado e nos dirige um sorriso um tanto pretensioso"

                    show irina normal with dissolve

                    voice "audio/narration/aud143.ogg"

                    irs "Parece que você já se enturmou, não é mesmo? "

                    show yuno normal at left with dissolve 

                    voice "audio/narration/aud144.ogg"

                    y "A Akane disse que vai leva-lo para conhecer a escola, assim que a aula terminar. "

                    voice "audio/narration/aud145.ogg"

                    irs "Aproveite e mostre os clubes para ele. Não quero ver nenhum aluno meu em ociosidade"

                    voice "audio/narration/aud146.ogg"

                    irs "Agora, vamos seguir com a aula pessoal! Silêncio. "

                    hide irina normal with dissolve

                    show akane cnvs with dissolve

                    ak "(...)"

                    voice "audio/narration/aud147.ogg"

                    y "Você vai gostar daqui, embora seja um orfanato, não é um lugar ruim."

                    hide akane cnvs with dissolve
                    hide yuno normal with dissolve

                    show irina normal with dissolve

                    voice "audio/narration/aud148.ogg"

                    irs "Pessoaaal... a educação foi feita para ser usada, e não para ser guardada em suas mochilas, Silêncio! "

                    hide irina normal with dissolve

                    voice "audio/narration/aud149.ogg"

                    "Sinto que situações assim são comuns por aqui. Devo me acostumar a isso também."

                    show irina normal with dissolve

                    voice "audio/narration/aud150.ogg"

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

                            show akane cnvs with dissolve

                            ak "(...)"

                            hide akane cnvs with dissolve
                            show yuno normal with dissolve

                            y "Sim, e se você quiser, pode sair e comer na lanchonete aqui perto"

                            hide yuno normal with dissolve

                            s "C-Como? Pode-se sair daqui?"

                            show akane cnvs at left with dissolve 

                            ak "(...)"

                            show yuno sorr with dissolve

                            y "Sim, aqui não é uma prisão, diferente dos outros orfanatos. A partir de uma certa idade você já pode sair, desde que respeite os horários e não tenha nenhum problema que te atrapalhe"

                            ak "(...)"

                            y "Essa é a política do Kibou-en! "

                            hide akane cnvs with dissolve
                            hide yuno sorr with dissolve

                            "Permaneço perplexo por alguns momentos.  "

                            "Antes de vir para cá, o cenário que imaginei, foi completamente diferente..."

                            "Talvez... eu estivesse seguindo algum tipo de estereótipo proposto na sociedade? "

                            "Na qual lugares como este fossem a representação do inferno? "

                            show akane confused with dissolve

                            ak "(...)"

                            hide akane confused with dissolve
                            show yuno normal with dissolve

                            y "Mizu?"
                            show akane confused at left with dissolve

                            "Yuno e Akane me fitam, por um instante. Acho que estou viajando por tempo demais."

                            s "Para onde vamos agora?"

                            hide akane confused with dissolve

                            

                            y "Deixe-me ver.. "

                            y "Você ainda não tem nenhum clube... certo? Que tal conhecer o clube de oratória? "

                            s "Clube de oratória... parece interessante... você e Akane estão nele, não é mesmo?"

                            "Yuno parece ter sido pega de surpresa. Toya e Kazuma me apresentaram alguns lugares desta escola, e o clube de oratória foi um deles. "

                            hide yuno normal
                            show yuno sorr

                            y "Então você já sabia! Hahaha"

                            s "De certa forma sim, mas você e Akane querem me arrastar para ele?"

                            show akane cnvs at left with dissolve

                            ak "(...)"

                            "Akane gesticula freneticamente, mal dando tempo a Yuno, acompanhar seus movimentos "

                            "Akane é Líder do Clube de Oratória, mesmo sendo muda, e isso de certa forma é incrível."

                            "Toya, por mais que seja cego, aparentemente, nunca se deixou limitar por sua condição."

                            "Então... qual era a minha justificativa?"

                            hide akane cnvs with dissolve
                            hide yuno sorr
                            show yuno normal

                            y "Akane está dizendo que você deveria dar uma chance. Pode ser uma ótima experiência para você."

                            s "Pode até ser.... eu vou dar uma passada"

                            y "Ótimo! Venha, vamos apresentar você ao resto do clube."

                            hide yuno normal with dissolve

                            "Akane me toma pelas mãos e me conduz animadamente pelos corredores "

                            s "Mas... eu nunca disse que me juntaria ao clube..."

                            "Já é tarde demais, Yuno está tão animada que já não consegue me ouvir"

                            scene bg corredor with fade

                            "Continuamos a caminhar pelos corredores, passando por várias salas e grupos de estudantes, até chegarmos à porta do Clube de Oratória. "

                            scene bg clube with dissolve

                            "Ao entrar, sou recebido por uma sala cheia de estudantes conversando animadamente. No centro da sala, uma cadeira está vazia, indicando que o presidente do clube ainda não chegou. "

                            show yuno sorr with dissolve

                            y "Pessoal, esse é Shido, nosso novo amigo. Ele está interessado em conhecer o clube."
                            hide yuno sorr with dissolve

                            "Os membros do clube me olham com curiosidade e começam a se aproximar para se apresentarem. A energia na sala é contagiante, e não consigo evitar um sorriso. "

                            show aluno normal at left with dissolve

                            mc "Bem-vindo, Shido! Espero que goste daqui."

                            mc "Apesar de sermos um pouco brincalhões, não há nada que não possamos fazer se nos determinarmos"
                            hide aluno normal with dissolve

                            s "Obrigado, pessoal. É um prazer conhecer todos vocês."

                            show akane sorr at left with dissolve

                            "Enquanto conversamos, percebo que Akane está ao meu lado, observando silenciosamente. "

                            "Ela me dá um sorriso encorajador, e eu sinto um calor reconfortante se espalhar por mim. Talvez, só talvez, este lugar não seja tão ruim assim."

                            scene bg months with dissolve

                            scene bg school_room with dissolve

                            show irina normal with dissolve


                            s "Irina-sensei, é verdade o que dizem no Clube de Oratória? O orfanato oferece aulas de linguagem de sinais?"

                            irs "Sim, é verdade Mizushima. Porquê? Você tem interesse?"

                            s "Meio que sim"

                            irs "Meio que sim? Isso não existe. Desembucha logo menino, qual o motivo desse interesse?"

                            s "É que assim..."

                            irs "Hum..."

                            s "Eu, Akane e Yuno estamos sempre juntos. Akane e eu conversamos bastante quando Yuno está por perto para traduzir"

                            s "Quando ela não está, precisamos usar um caderno para nos comunicar, e isso pode ser um pouco frustrante às vezes. Entende?"

                            irs "Entendo... e ás vezes você deseja se aprofundar nas conversas com Akane, mas se sente retraído por precisar de Yuno?"

                            "Sinto meu rosto queimar de vergonha. Coloco minhas mãos sobre ele, esperando que esse simples gesto disfarce meu constrangimento"

                            "É claro que não irá"

                            "Irina-sensei possui a habilidade de saber exatamente o que seus alunos estão pensando, apenas por olhar para eles"

                            irs "Você é mais emocional do que eu pensei"

                            irs "Vai me dizer que está tendo uma queda por ela?"

                            s "N-não tem nada a ver com isso, sensei!"

                            "Irina-sensei dá uma leve gargalhada, aparentemente ela está se divertindo com a situação"

                            irs "Quer conversar sobre?"

                            s "Eu..."
                            
                            irs "Não há mal nenhum em desabafar de vez em quando... e você não me parece bem... venha, sente-se aqui. Vamos conversar."

                            
                            "Sento-me em frente a ela, perplexo. Como ela sabia que eu estava mal? Quer dizer, eu não contei a ninguém e ainda assim..."

                            
                            irs "O que tem acontecido, Shido?"
                            
                            s "Eu..."
                            
                            s "Respiro fundo e desvio meu olhar... Será que ela vai levar isso a sério?"

                            
                            s "Não é nada demais sensei, é besteira."

                            hide irina normal
                            show irina serious

                            
                            irs "Por mais que não seja nada em sua perspectiva, eu sei que algo está acontecendo, e diferente do que pensa, eu me importo com você."

                            
                            "Nunca imaginei que palavras tão simples seriam capazes de fazer minha garganta se fechar..."

                            
                            irs "Isso... não é somente sobre Akane, não é?"

                            
                            "Curiosamente reparo que Irina-sensei age mais informalmente quando se trata de um assunto mais pessoal. De certa forma, me sinto agradecido por isso."

                            
                            s "Não..."
                            
                            s "Eu estou aflito por algo, mas não é nada demais."
                            
                            s "Eu sinto que... de certa forma, não consigo lidar muito bem com as 'deficiências' de meus colegas."

                            
                            s "A-alguns dias atrás... vi Kazuma chorando escondido... ele tinha se envolvido em uma discussão e disseram a ele que os pais dele o abandonaram porque ele era um inútil."

                           
                            
                            s "Disseram a ele que ele não tinha sequer a capacidade de orgulha-los."

                            
                            s "Na mesma semana... ouvi Toya conversando sozinho... ele provavelmente não notou minha presença... mas ele falava sobre... tudo o que ele queria fazer... todo o tipo de coisa que ele sonhava em fazer mas não podia por sua limitação..."

                            
                            s  "Ouvi uma menina no pátio falando sobre como foi abusada por seu pai..."
                            
                            s  "Por que sensei? Porque pessoas que deveriam nos dar amor, carinho e exemplo nos dão rejeição, ódio e mágoa?"


                            hide irina serious
                            show irina serious2

                            
                            irs "A vida é complexa, Shido. Nem sempre as pessoas que deveriam nos proteger conseguem fazê-lo."
                            
                            irs "Muitas vezes, elas próprias carregam suas próprias dores e acabam descontando isso nos outros. Não estou dizendo que é justo ou certo, mas é uma realidade que muitos enfrentam."
                            
                            irs "Cada um lida com suas experiências de maneiras diferentes. O importante é encontrar maneiras saudáveis de enfrentar essas dificuldades e buscar apoio quando necessário."

                            hide irina serious2
                            show irina serious

                            
                            s "Eu só... quero poder ajudar. Fazer alguma coisa por eles. Mas não sei por onde começar."

                            hide irina serious

                            show irina serious2

                            
                            irs "Seu desejo de ajudar já é um bom começo. Muitas vezes, apenas estar presente e ouvir pode fazer uma grande diferença. Ofereça seu apoio, e mais importante: mostre que eles não estão sozinhos."
                            
                            irs "E não se esqueça de cuidar de si mesmo também, Shido. Para ajudar os outros, você também precisa estar bem."

                            hide irina serious2
                            show irina serious

                            s  "Talvez, ao compartilhar um pouco do meu próprio fardo, eu possa aprender a aliviar o dos outros."

                            
                            s "Sensei..."
                            
                            irs "Sim?.."

                            
                            s "Você está certa... eu amo aquela garota."

                            
                            "Irina-sensei parece um pouco surpresa em relação à minha coragem, mas logo após ri. Deve estar pensando em quão bobo estou sendo falando sobre amor... uma palavra tão simples mas ao mesmo tempo, com significado tão complexo."


                            irs "Sabe Shido..."
                            
                            s "Sim?.."
                            
                            hide irina serious
                            show irina serious2
                            
                            irs "Gostei da sua resposta... mas eu gostaria de acrescentar uma pitada de minha experiência..."
                            
                            irs "O amor... é um sentimento complexo demais para que seja explicado em uma pequena fala."
                            
                            irs "O amor é benigno e não sente ciúmes; o amor não é orgulhoso e não recente do mal: o amor perdoa, seja qual for o erro. O verdadeiro amor está além da distância, do toque, do cheiro."
                            
                            irs "Não se busca razão para amar, não se ama porque alguém tem qualidades interessantes ao se ver ou porque é bonito. O verdadeiro amor é simplesmente amar, coisa que nós seres humanos demonstramos uma imensa dificuldade, pois o amor é algo que não pode ser explicado com palavras, apenas com gestos, e isso não basta para responder nossos questionamentos em relação a ele."
                            
                            irs "O amor é muito mais do que você pode imaginar, então se prepare pequeno Shido..."

                            hide irina serious2
                            show irina serious

                            "Suas palavras ecoam na minha mente, fazendo-me refletir sobre o que realmente sinto. Será que estou pronto para entender algo tão complexo como o amor?"

                            
                            s "Eu... acho que entendo o que está dizendo, sensei. Talvez ainda esteja aprendendo a amar de verdade."

                            
                            irs "E esse é o primeiro passo, Shido. Aprender. Nunca paramos de aprender, mesmo quando pensamos que já sabemos o suficiente."

                            
                            "Essas palavras me confortam, pois percebo que não preciso ter todas as respostas agora. O que importa é estar disposto a descobrir."

                            
                            s "Obrigado, sensei. Vou tentar lembrar disso."

                            hide irina serious
                            show irina serious2
                            
                            irs "Não precisa agradecer. Apenas viva suas experiências e aprenda com elas. O amor pode ser a jornada de uma vida inteira."

                            scene bg jardim_orfanato with dissolve

                            show akane confused with dissolve
             
                            s "Olho para Akane, e me dou conta do quanto ela significa para mim. Talvez eu ainda não compreenda completamente o amor, mas sei que ela é uma parte importante da minha vida."
                            
                            ak "..."

                            hide akane confused with dissolve
                            show yuno normal with dissolve
                            
                            y "Shido! Akane estava perguntando se você quer ir à biblioteca com a gente. Tem uma exposição de arte que parece interessante."
                            
                            s "Claro, eu adoraria!"
                            
                            "À medida que nos dirigimos à biblioteca, sinto que cada momento que passo com elas é uma oportunidade de aprender mais sobre mim mesmo e sobre o que significa amar."

                            
                            scene bg biblioteca with dissolve
                            
                            "À biblioteca está silenciosa, exceto pelo som suave das páginas virando. A exposição de arte é uma coleção de obras de artistas locais, cheias de cor e emoção."

                            
                            s "Enquanto caminhamos pela exposição, noto a expressão de encantamento no rosto de Akane. Sua paixão pela arte é contagiante, e eu me pego admirando não apenas as obras, mas também a maneira como ela as observa."
                            show yuno normal with dissolve
                            y "Akane diz que esta pintura é a favorita dela. Ela gosta da forma como as cores se misturam e criam uma sensação de movimento."
                            
                            s "É realmente incrível. Acho que entendo por que ela gosta tanto."
                            
                            s "Observar Akane é como ver a arte em movimento. Ela me inspira a ver o mundo de maneiras que nunca imaginei."
                            
                            ak "..."
                            
                            y "Akane está perguntando se você já pensou em se expressar através da arte, Shido."
                            
                            s "Eu nunca fui muito bom com pincéis, mas acho que, de certa forma, estou aprendendo a expressar meus sentimentos de outras maneiras."
                            
                            s "Talvez essa seja a beleza do amor. Não importa como você o expressa, contanto que seja genuíno."

                            
                            scene bg jardim_orfanato
                            
                            "O sol está se pondo, pintando o céu com tons de laranja e rosa. Shido, Akane e Yuno estão sentados em um banco, admirando a vista."

                            
                            s "O amor é mais do que palavras ou gestos; é a presença silenciosa daqueles que importam. Enquanto estivermos                          
                            juntos, sei que vou descobrir mais sobre o que isso realmente significa."
                            
                            s "Obrigado, Akane, Yuno. Por tudo. Eu sou realmente grato por ter vocês na minha vida."

                            show yuno normal with dissolve
                            
                            y "Estamos sempre aqui, Shido. Somos amigos, afinal de contas."

                            show akane sorr at left with dissolve
                            
                            ak "..."
                            
                            y "Akane diz que também é grata por ter você por perto."
                            
                            "E assim, enquanto o sol se põe, percebo que este é apenas o começo de uma jornada que estou ansioso para continuar."

                            
                            scene colegio with dissolve


                            $ renpy.movie_cutscene("video/pt1.webm")

                            $ renpy.movie_cutscene("video/pt2.webm")


                            
                            






                            



                            



