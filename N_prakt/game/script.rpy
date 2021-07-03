# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define mn = Character('Мис Новелти', color="#c8ffc8")
define secr = Character('секретарь', color="#c8ffc8")
define ya = Character('[name]', color="#c8ffc8")
define ink = Character('???', color="#c8ffc8") 
define rudi = Character('Pоуди', color="#c8ffc8") 
define mj = Character('Меррелин Джустилис', color="#c8ffc8")
define slowdis = Dissolve(1.0)
define water_sample = 0 #счет воды

#счетчик Роуди
define j = 0     
define camera = 1
define old_water_filter = 1
define expert_report = 1

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
#глава 1
label start:


    scene bg black
    
    with fade

    secr "Мисс Новелти готова принять вас"

    "Ну что, пора выдвигаться..."
    
    "Вы встали с мягкого дивана и направились в кабинет мисс Новелти"
    
    scene bg nkab
    
    with fade
    
    show mn normal 
    
    mn '''
    А, вот и мой новый сотрудник! Добро пожаловать в наш коллектив!

    Как вас зовут?
    '''
    
    $ name = renpy.input("как вас зовут?")
    
    mn '''
    Серьёзно,[name]? Ну ладно, будем знакомы.

    Мне много о вас рассказывали, поэтому я хочу поручить вам довольно специфичное задание.
    
    Вы должны разоблочить WaterPump Incorporated.
    
    Это задание я буду расценивать как ваш испытательный срок.
    
    Справетесь с ним - и эта работа ваша. И это не обсуждается.'''
    
    mn "Можете приступать к выполнению вашего задания прямо "
    
    show mn angry
    
    extend "Сейчас!!!"
    
    hide mn angry
    
    menu:
        "что делать?"
        
        "принять предложение":
            jump yes_job
        "отказаться и уйти":
            jump no_job
 
    return

#концовка 1
label no_job:
    
    scene bg black
    
    "Игра окончена"
    
    return
 
#глава 2
label yes_job:
    
    scene bg mykab
    
    with fade
    
    show secr 
    
    secr "Вот Ваш кабинет, в нём уже лежат все материалы по делу." 
    
    hide secr
    
    show rudi blm
    
    ink "О, привет! Ты тот самый новый сотрудник, верно? Как тебя звать?"
    
    ya "Меня зовут [name]"
    
    hide rudi blm
    
    show rudi normal
    
    rudi "Мда...Ой, подожди, я же не представился! Меня зовут Руди Роуди."
    
    ya "Приятно познакомиться. Надо начать расследование, а то не хочется проблем с Мисс Новелти"
    
    rudi "Оооо, и как прошло знакомство?"
    
    menu:
        "как прошла первая встреча с мисс Новелти?"
        
        "хорошо":
            jump good_meeting
            
            
        "нормально":
            jump norm_meeting
        
        
        "плохо":
            jump bad_meeting
    return
 
#отношение к мисс Новелти
label  good_meeting:

    scene bg mykab
    
    show rudi normal
    
    ya "хорошо. Такая женщина во главе компании принесёт только прибыль"
    
    show rudi surprise
    
    rudi "..."
    
    jump yes_job1
    
    return

#отношение к мисс Новелти
label  normal_meeting:

    scene bg mykab
    
    show rudi normal
    
    ya "Нормально. Самый обычный директор крупной компании, не больше."
    
    show rudi surprise
    
    rudi "..."
    
    jump yes_job1
    
    return

#отношение к мисс Новелти
label  bad_meeting:

    scene bg mykab
    
    show rudi normal
    
    ya "Ужасно. Как вы терпите эту стерву?"
    
    show rudi smile
    
    rudi "Хах, верно подмечено. Ладно, давай ближе к делу."
    
    ya "Руди ухмыльнулся. Видимо, Вы его заинтересовали"
    
    $ j = j+1
    
    jump yes_job1
    
    return

#продолжение главы 2
label yes_job1:

    scene bg mykab
    
    show rudi normal
    
    ya "давай. Можешь посвятить меня в курс дела?"
    
    rudi "Ага. Итак, у нас есть многомиллиардная компания, занимающаяся водоснабжением."
    
    rudi "Но в последнее время из-за очистки воды люди стали чаще попадать в больницы."
    
    rudi "Симптомы одни и те же, так что это 100 процентов проделки WaterPump."
    
    rudi "Нам нужно раздобыть как можно больше сведений и улик, чтобы доказать их вину."
    
    show rudi angry
    
    rudi'''
    
    Иначе на приближающейся \"WaterEXPA\" они покажут новое поколение фильтров...
    
    И мягко говоря сократят количесвто своих клиентов.
    
    У меня есть некоторые заметки, которые помогут нам прижучить этих гадов.'''
    
    ya "Ясно, сейчас Я изучу твои заметки и завтра мы отправимся в WaterPump."
    
    hide rudi angry
    
    scene bg black
    
    with fade
    
    "заметка 1 - Для начала надо забрать записи с камер"
    
    "заметка 2 - дальше нужно забрать отчёты эксперта по анализу воды ДО ТОГО, как он его подделает"
    
    "заметка 3 - Около дамбы находится склад водяных фильтров. Если оттуда взять старый и сравнить его с новым"
    
    "заметка 4 - И последнее, что поможет - проба воды из лаборатории. Кто знает, с чем они смешивают воду ради чистоты"
    
    scene bg mykab
    
    with fade
    
    ya "Ну что, это может сработать. Завтра выдвигаемся в офис WaterPump..."
    
    jump glava3
    
    return

#глава3    
label glava3:
    
    scene bg nebosk
    
    ya "Утреннее солнце освещает высокое здание, принадлежащее WaterPump. Где-то здесь можно найти полезные данные."
    
    show rudi normal
    
    rudi "Ахри...То есть... Вау!{w} Никогда не находился так близко к обителю зла."
    
    menu:
        "поддержать Роуди":
            jump support
            
        "не соглашаться":
            jump no_support
            
    return

#выбор в главе 3
label support:

    scene bg nebosk
        
    show rudi normal
    
    ya "Хах,надеюсь у тебя есть с собой пару бутылок святой воды."
    
    show rudi smile
    
    rudi "Аахаха. Моя тётя часто посещает церковь, возьму у нее пару бутылок"
    
    ya "Руди посмеялся. Это был верный шаг для сближения с ним."
    
    $ j = j+1
    
    jump glava3_1
    
    return
    
#выбор в главе 3
label no_support:

    scene bg nebosk
        
    show rudi normal
    
    ya "Не выдумывай, обычный небоскрёб крупной компании"
    
    show rudi surprise
    
    rudi "..."
    
    jump glava3_1
    return

#продолжение главы 3 
label glava3_1:

    scene bg nebosk
        
    show rudi normal
    
    rudi "Ладно. Перед тем, как мы войдём Ты хочешь что-то обсудить?"
    
    menu: 
        "обсудить план действий":
            jump plan
        "спросить состояние Руди":
            jump health
        "войти в здание":
            jump building
    
    return

#2-й выбор в главе 3
label plan:

    scene bg nebosk
        
    show rudi normal
    
    ya "Напомни, что мы будем искать?"
    
    rudi "Скорее всего тут можно раздобыть записи с камер и отчёт эксперта."
    
    jump glava3_1
    
    return
   
#2-й выбор в главе 3   
label health:

    scene bg nebosk
        
    show rudi normal
    
    ya "Как ты себя чувствуешь? Ты точно готов к походу?"
    
    show rudi smile
    
    rudi "А? Да, я в поряде. Спасибо за интерес."
    
    jump glava3_1
    
    return
    
#2-й выбор в главе 3
label building:
    
    scene bg nebosk
    
    show rudi normal
    
    ya "Нет, ничего. Пойдём уже."
    
    rudi "Да....Конечно.... Ну тогда в путь!"
    
    scene bg black
    
    with fade
    
    hide rudi normal
    
    "Вы вошли в здание WaterPump Incorported. По коже прошёл лёгкий ветерок. Чувство тревоги теперь сопровождает вас."
     
    jump glava_6
    
    return

label glava_6:


    scene bg sklad
    with slowdis 

    show rudi normal

    with fade

    rudi "Итак, всё, что нам нужно - это купить пончиков"
    
    ya "?????????"

    rudi "Ахахах шучу конечно же!"

    rudi "Итак, сегодня наша задача максимально простая: через пару минут приедет грузовик с водой"

    menu:
        "Продолжить":
            jump prodolzh
    return

label prodolzh:

    pause .7
    
    scene bg sklad
    with slowdis

    "Вы расположились около КПП"

    "Через пару минут подъехал грузовик с водой"

    scene bg truck
    with slowdis 

    show rudi serios 

    with fade

    rudi "Быстрее! Это наш шанс!"

    hide rudi serios 

    with fade

    menu:
        "Пойти за водой сейчас":
            jump goWater

        "Подождать":
            jump waitWater
    return

label goWater:

    "Вы решили отправиться за водой сразу же"

    "Вас заметил водитель и начал гудеть"

    pause .7

    show sec at left

    with fade 

    "На этот гул сбежались охранники и Вам пришлось убежать"

    "Вы не смогли добыть пробу воды"

    hide sec

    with fade 

if water_sample == 0:

    pause .7

    scene kpp
    with slowdis 

    show rudi serios 

    with fade
    
    rudi "Нет......"

    ya "Вот и всё на этом."

    hide rudi serios 

    with fade

    jump glava8

    return

else:

    pause .7

    rudi "Да."

    ya "Отлично, тогда пойдём к этим ребятам за отчётом."

    menu:
        "Продолжить":
            jump uchen
  
    return

    return


label waitWater:

    "Вы решили подождать немного"

    "Грузовик припарковался прямо у въезда в лабораторию"

    "Вы обошли КПП через разрушенный забор и спокойно забрали воду"

    "Вам удалось добыть пробу воды"

    $ water_sample = water_sample + 1

    pause .7

    rudi "А теперь нам надо идти в независимую экспертизу."

    ya "А у нас вода хоть есть?"

if water_sample == 0:

    pause .6
    
    rudi "Нет......"

    ya "Вот и всё на этом."

    jump glava8

    return

else:

    pause .6

    rudi "Да."

    ya "Отлично, тогда пойдём к этим ребятам за отчётом."

    menu:
        "Продолжить":
            jump uchen
  
    return

label uchen:

    pause .7

    scene bg lab
    with slowdis 

    "Вы спкойно добрались до компании ??????"

    show rudi serios at left

    with fade

    rudi "Я надеюсь, что тут кто-нибудь говорит на нормальном языке"

    show vopr at right

    with fade 

    "?" "?????! ????????" 

    rudi "Чё......?"

    ya "(голос переводчика)????????????????"

    "?" "???????!" 

    ya "(голос переводчика)?????!"

    rudi "............"

    hide vopr

    with fade

    hide rudi surprise

    with fade

    "Через несколько минут подошли несколько учёных и забрали воду"

    "Через пару часов отчёт был готов"

    "Вы смогли раздобыть отчёт от независимой экспертизы"

    jump glava8

    return

label glava8:

    pause .7

    scene bg sud
    with slowdis

    show rudi surprise

    with fade

    rudi "Сегодня суд. Готовность?"

    ya "На все 100!"

    hide rudi surprise

    with fade

    "Это был уже 7-ой судебный процесс против WaterPump" 

    "Если Вам удастся доказать их вину, то всему городу станет легче"

    "Удачного судебного заседания, [name] !" 

    show mjp

    with fade

    mj "Итак, начнём наше очередное заседание." 

    hide mjp

    with fade

    pause .7

    "Заседание суда длится уже больше 3 часов"

    pause .7

    show mjp

    with fade

    mj "Итак, Мистер Роуди, у вас есть какие-либо доказательства против WaterPump?"

    "Пора предоставить Ваши доказательства"

    hide mjp

    with fade

    show rudi angry

    with fade
    
    rudi "Да, Ваша честь.[name], Поможешь мне?"

    ya "Конечно!"

    hide rudi angry

    with fade


    $ court_for_final = camera + old_water_filter + expert_report+ water_sample

if court_for_final == 4:

    "Вы предоставили 4 доказательства"

    show mjp

    with fade

    mj "Итак, нам потребуется время на изучение. Объявляется перерыв"

    pause .7

    "После окончания перерыва Суд вынес решение в пользу \"Слова Правды\""

    pause .6

    "Вы выиграли дело!"

    hide mjp

    with fade

    jump Fin

elif court_for_final == 3:

    show mjp

    with fade

    "Вы предоставили 3 доказательства"

    mj "Итак, нам потребуется время на изучение. Объявляется перерыв"

    pause .7

    "После окончания перерыва Суд вынес решение в пользу \"Слова Правды\""

    pause .6

    "Вы выиграли дело!" 

    hide mjp

    with fade

    jump Fin
     
elif court_for_final == 2:

    show mjp

    with fade

    "Вы предоставили 2 доказательства"

    mj "Итак, нам потребуется время на изучение. Объявляется перерыв"

    pause .7

    mj "Итак, предъявленных вами доказательств оказалось недостаточно"

    "После окончания перерыва Суд вынес решение в пользу WaterPump"

    pause .6

    "Вы проиграли дело!"

    hide mjp

    with fade

    jump Fin

elif court_for_final == 1:

    show mjp

    with fade

    "Вы предоставили 1 доказательство"

    mj "Итак, нам потребуется время на изучение. Объявляется перерыв"

    pause .7

    mj "Итак, предъявленных вами доказательств оказалось недостаточно"

    "После окончания перерыва Суд вынес решение в пользу WaterPump"

    pause .6

    "Вы проиграли дело!"

    hide mjp

    with fade

    jump Fin

elif court_for_final == 0:

    show mjp

    with fade

    "Вы не предоставили никаких доказательств"

    mj "Итак, для принятия решения нам нужно время. Объявляется перерыв"

    pause .7

    mj "Итак, издательство \"Слово Правды\" не предоставило никаких доказательств, поэтому WaterPump может продолжить свою деятельность в городе"

    "После окончания перерыва Суд вынес решение в пользу WaterPump"

    pause .6

    "Вы проиграли дело!" 

    hide mjp

    with fade

    jump Fin

label Fin:

    pause .7

    scene bg final
    with slowdis
    
    "КОНЕЦ"

    "Данная визуальная новелла была сделана как проект для учебной практики"

    "Подготовили новеллу: Фещенко Игорь (ИСТ-102), Мирошин Илья (ИСТ-102), Рыков Дмитрий (ИСТ-102)"

    "Для создания использовались: язык программирования Python и движок для новелл Ren'Py"

    "Спасибо за прохождение!"
  