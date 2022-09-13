label start:
    $ player_name = renpy.input("Введите имя персонажа", length=18).strip()

    # выбор пола
    menu:
        "Выберите пол персонажа:"

        "Женский":
            $ isWoman = True

        "Мужской":
            $ isWoman = False

    if isWoman:
        $ low = Character('Джеймс Лоу', image='lowman')  
        $ low_name = "Джеймс Лоу"
        $ low_name_name = "Джеймс"

    scene bg fox office dark
    with fade

    "Дым мой единственный друг в этом мрачном и грязном городе."
    # "Я видел лицо этого города, и это лицо уродливо."
    # "Воры, убийцы, мошенники, коррумпированные политики и мафиози..."
    # "Все они лезут как тараканы на хлеб в жажде наживы на улицы."
    # "Когда-нибудь они заполнять город и для честных людей больше не останется места."
    # "Но пока работаем мы, этот день не настанет."
    "И пока, я, детектив [player_name] Фокс, на своем посту, я буду выжигать эту мерзость каленым железом."

    if isWoman:
        show lowman at right

    else: 
        show lowwoman at right

    low "кхе-кхе"

    low "Ты опять куришь в кабинете?"

    low "Клянусь всеми святыми, когда-нибудь тебя уволят"

    # Лоу открывет окно, дым рассеивается

    low " Вот так-то лучше.\n
    Для нас есть дело."

    low "Клара просила тебя зайти в полдень - передаст все бумаги и еще..."

    # выбор характера

    menu:

        low "Она назначила нам стажеров"

        "Просто пристрели меня":
            $ character = 'pessimistic'

        "Отлично, будет пушечное мясо":
            $ character = 'sarcastic'

        "Хорошо. Чем нас больше, тем меньше преступников":
            $ character = 'optimistic'

        "Еще чего! Я не буду с ними возиться!":
            $ character = 'nigilistic'          


    if character == 'pessimistic':
        low "Ха-ха, смешно..."

    elif character == 'sarcastic':
        low "Ха-ха, смешно..."

    elif character == 'optimistic' and isWoman:
        low "Рад что ты довольна"

    elif character == 'optimistic' and isWoman == False:
        low "Рада что ты доволен"   


    elif character == 'nigilistic' and isWoman:
        low "Я ожидал, что ты так отреагируешь"
        
    elif character == 'nigilistic' and isWoman == False:
        low "Я ожидала, что ты так отреагируешь"  


    low " Как бы там ни было, нашего мнения не спрашивали.\n
    Стажеров нам передали из администрации города."

    if character == 'pessimistic':
        fox "За что мне это"

    elif character == 'sarcastic':
        fox "И мэр гнилой и администрация попахивает."

    elif character == 'optimistic':
       fox "Что ж нам пригодится любая помощь. Хотя к мэру у меня все еще есть вопросы."        

    else:
        fox "Нет уж, дудки! Сейчас я пойду к Кларе и откажусь."    
 
    


    if character == 'pessimistic' and isWoman:
        low "Hаверно, за все хорошее, что ты сделала."
        low "В любом случае..."

    elif character == 'pessimistic' and isWoman == False:
        low "Hаверно, за все хорошее, что ты сделала."  
        low "В любом случае..."  

    elif character == 'sarcastic':
        low "Наверно, поэтому их и повесили на тебя."
        low "В любом случае..."  

    elif character == 'optimistic':
       low "Может, через новичков сможем нарыть что-нибудь и на мэра."     
       low "В любом случае..."     

    else:
        low "Сожалею, но не выйдет..."

    # low "Капитан Боунс сейчас как раз беседует с мэром и велела не пускать тебя до полудня на пушечный выстрел."
    # low "Можешь пока познакомится со стажерами"
    # low "Они на самом деле выглядят как неплохие ребята"  
    # # [задумчивое лицо] 
    # low "Часть из них, во всяком случае" 
    low "Сейчас они у нас в кабинете, Капитан определила их туда, пока Чейни в отпуске" 
    if isWoman:
        low "Решай сама, что с ними делать." 
    else:
        low "Решай сам, что с ними делать."     

    hide low

    $ time = 11.30
    $ isReportDone = False
    $ wasConversationWithStagers = False

    label waitFor12: 
        menu:
            "Что делать дальше?"

            "Пойти в кабинет капитана Клары Боунс":
                if time < 12: 
                    broudi "Извини, Фокс. Шеф сказала не пускать тебя к ней, пока там мэр. Приходи после 12."
                    scene bg fox office dark
                    with fade
                    jump waitFor12
                else: 
                    "Пока не прописано"    

        
            "Выкурить еще одну сигарету":
                if time < 12:
                    "Звук зажигалки. Кабинет наполняется дымом. Время на часах меняется на +1 минуту"
                    fox "Может сигареты меня и убьют, но без них бывает тяжело."
                    $ time = time + 0.01
                    jump waitFor12
                else: 
                    "Пока не прописано"    

            "Заполнить отчет":
                if time < 12:
                    if character == "optimistic" and isReportDone:   
                        if isWoman:
                            "Я уже заполняла сегодня отчет. Больше бумажной работы нет."
                        else: 
                            "Я уже заполнял сегодня отчет. Больше бумажной работы нет."    
                    elif character == "optimistic" and isReportDone == False:   
                        "Шуршание бумаги. Время на часах меняется на +1 минуту"
                        "Очередной отчет. Необходимая щепотка бюрократии, ради важного дела."
                        $ time = time + 0.01
                    else: 
                        "Шуршание бумаги. Время на часах меняется на +5 минут"
                        $ time = time + 0.05
                        fox "На этом можно убить немного времени. Странно, что я так редко это делаю."
                    jump waitFor12
                else: 
                    "Пока не прописано"            

            "Пойти в кабинет Чейни и Лоу":      
                if wasConversationWithStagers:
                    "Сейчас там делать нечего. Надо идти к Кларе."
                else:          
                    jump meetingWithTrainees

    
########################################

    label meetingWithTrainees:
        "Кабинет Напарника и Чейни. В кабинете 3 стола: большой стол у окна, за которым сидит напарник. Стол около двери, вокруг которого расселось трое из стажеров. Третий стол стоит в углу, все на нем выглядит запыленным и давно не использовавшимся. На третий стол облокотился четвертый стажер и что-то на нем разглядывает."
        
        if character == 'optimistic':
            "Возле третьего стола стоит Мика"
            $ traineeNearTable="Mika"
        elif character == 'pessimistic':
            "Возле третьего стола стоит Борис" 
            $ traineeNearTable="Boris"
        elif character == 'sarcastic':
            "Возле третьего стола стоит Рита"    
            $ traineeNearTable="Rita"
        else:
            "Возле третьего стола стоит Август"  
            $ traineeNearTable="August"


        if character == 'optimistic':
            menu:
                "Пожалуйста, отойди от этого стола":
                    jump pleceGoAwayFromTable

                "Быстро отойди от этого стола!":
                    jump getAwayFromThisTable

                "[low_name], почему ЭТО роется в столе Рози?!":    
                    jump whoDigInTable        

        elif character == "pessimistic":
            menu:
                "Как ты смеешь там копаться?!":
                  $ rel_boris = rel_boris -1
                  boris "Я не копаюсь."
                  teller "Парень отходит от стола, складывая руки на груди"
                  boris "Просто смотрел. Не трогал."
                  jump meetWithStagers_low

                "Быстро отойди от этого стола!":
                    jump getAwayFromTable

                "[low_name], почему ЭТО роется в столе Рози?!":    
                    jump whoDigInTable      
        elif character == 'nigilistic':
            menu:
                "Бросить в стажера стул":
                    $ rel_august = rel_august - 1
                    $ rel_mika = rel_mika - 1
                    $ rel_boris = rel_boris - 1
                    $ rel_rita = rel_rita - 1  
                    teller "Парень уворачивается от стула, пригибаясь, вид у него разъяренный, но реагирует он достаточно спокойно"
                    august "Епт... Это достаточно грубо, вам не кажется? Тем более я нихрена здесь не брал и не портил, и даже не собирался"
                    low "[player_name]! Прекрати кидаться мебелью!"
                    jump meetWithStagers_low

                "Быстро отойди от этого стола!":
                    jump getAwayFromTable

                "[low_name], почему ЭТО роется в столе Рози?!":    
                    jump whoDigInTable      
        else:
            menu:
                "Быстро отойди от этого стола!":
                    jump getAwayFromTable

                "[low_name], почему ЭТО роется в столе Рози?!":    
                    jump whoDigInTable      

        return 
##########################

    label pleceGoAwayFromTable:
      mika "Простите, пожалуйста!"
      teller "Девушка выглядит действительно извиняющейся и смущенной"
      mika "Я не знала, что нельзя!.. Я не хотела ничего... украсть... или сломать. И ничего плохого не хотела"
      jump meetWithStagers_low
      return 
##########################
    
    label getAwayFromTable:
      if traineeNearTable == "Mika":
        $ rel_mika = rel_mika -1
        teller "на глазах у девушки чть ли не слезы, она выглядит очень испуганной и смущенной"
        mika "Извините!.. Простите! Я не хотела ничего украсть... или сломать... Я просто смотрела... Простите меня, пожалуйста... Извините"
        jump meetWithStagers_low

      elif traineeNearTable == "Boris":
        $ rel_boris = rel_boris -1
        boris "Не знал, что нельзя"
        teller "Парень поворачивается, скрещивая руки на груди"
        boris "Извините"
        jump meetWithStagers_low

      elif traineeNearTable == "Rita":
        $ rel_rita = rel_rita -1
        rita "Прошу меня извинить, не планировала ничего плохого."
        teller "Надменная улыбка"  
        rita "Видите? Можно разговаривать и вежливо..."
        jump meetWithStagers_low

      elif traineeNearTable == "August":
        $ rel_august = rel_august -1
        august "Чё орать-то? Уже отхожу. Больно он мне нужен, этот стол ваш"
        teller "парень с неудовольствием на лице медленно разворачивается"
        jump meetWithStagers_low 
      return 
##########################

    label whoDigInTable:
      if traineeNearTable == "Mika":
          $ rel_mika = rel_mika -1
          teller "Мика выглядит, будто сейчас расплачется"
          jump meetWithStagers_low

      elif traineeNearTable == "Boris":
        $ rel_boris = rel_boris -1
        boris "Хмм..."
        teller "Борис скрещивает руки на груди"
        jump meetWithStagers_low

      elif traineeNearTable == "Rita":
        $ rel_rita = rel_rita -1
        rita "Я вообще-то вас слышу..."
        jump meetWithStagers_low

      elif traineeNearTable == "August":
        $ rel_august = rel_august -1
        august "Э, слышь..."
        jump meetWithStagers_low 
      return  
#########################
    
    label meetWithStagers_low:
      if isWoman:
           low "Это моя вина. Я слегка погрузился в документы и забыла объяснить новичкам... Дело в том, что раньше нас в команде было четверо"
           fox "Джеймс..."
      else:
           low "Это моя вина. Я слегка погрузилаcь в документы и забыла объяснить новичкам... Дело в том, что раньше нас в команде было четверо"
           fox "Джейн..."

      low "Шеф, так будет проще. И тебе, и им и всем."
      low "Так вот. Нас было четверо: Детектив Фокс, я, Ричард Чейни и Рози Артего."
      low "Два года назад мы расследовали дело Картёжника, которое пошло совсем не туда куда надо."
      rita "Инцидент в мэрии..."
      low "В точку"
      low "В общем, Рози погибла и мы не смогли ей помочь. Картёжник нас обдурил. Потом еще были проблемы с мэром из-за всей этой ситуации. Неважно..."
      august "Ну, понятно... грусть-тоска. Я тоже терял близких. Но два года держаться за какой-то стол..."
      fox "Она была моей невестой"
      low "Да... Так что это действительно больная тема для нас."

      if isWoman: 
        low "Разумеется шеф не хотела никого из вас обидеть."
      else:   
        low "Разумеется шеф не хотел никого из вас обидеть."

      low "Просто это единственное что у нас осталось от Рози. И напоминание нам - почему мы работаем здесь"  


      menu: 
        "Спасибо [low_name_name]":
          pass
        "Не стоило это все поднимать":
          pass
        "*Промолчать*":
          pass
        "Кто еще раз полезет к столу - убью.":
          define tableKiller = True

      low "Как бы там ни было, шеф, надо что-то придумать с расположением. Ребятам неудобно будет ютиться за одним столом."  
  
      define askCapt = False
      menu my_menu: 
        "Как расположить стажеров?"

        "Попрошу у капитана выделить еще один стол" if not askCapt:
          $ askCapt = True
          low "А если не получится?"
          jump my_menu

        "Меня это не касается, пусть сидят вчетвером за одним столом или на полу":
          "Еще не готово"

        "Пусть приходят через день по двое. Вдвоем же уместятся?":
          "Еще не готово"

        "Ладно. Пусть сидят за столом Рози. Но ничего на нем не трогают." if character != "pessimistic" and character != "nigilistic" and not tableKiller:
          "Еще не готово"



    
