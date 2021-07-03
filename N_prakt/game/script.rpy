# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define mn = Character('Мис Новелти', color="#c8ffc8")
define secr = Character('секретарь', color="#c8ffc8")
define ya = Character('[name]', color="#c8ffc8")
define ink = Character('???', color="#c8ffc8") 
define rudi = Character('Roudi', color="#c8ffc8") 
define j = 0     #счетчик Роуди

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
    
    "Меня зовут [name]"
    
    hide rudi blm
    
    show rudi normal
    
    rudi "Мда...Ой, подожди, я же не представился! Меня зовут Руди Роуди."
    
    "Приятно познакомиться. Надо начать расследование, а то не хочется проблем с Мисс Новелти"
    
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
    
    "хорошо. Такая женщина во главе компании принесёт только прибыль"
    
    show rudi surprise
    
    rudi "..."
    
    jump yes_job1
    
    return

#отношение к мисс Новелти
label  normal_meeting:

    scene bg mykab
    
    show rudi normal
    
    "Нормально. Самый обычный директор крупной компании, не больше."
    
    show rudi surprise
    
    rudi "..."
    
    jump yes_job1
    
    return

#отношение к мисс Новелти
label  bad_meeting:

    scene bg mykab
    
    show rudi normal
    
    "Ужасно. Как вы терпите эту стерву?"
    
    show rudi smile
    
    rudi "Хах, верно подмечено. Ладно, давай ближе к делу."
    
    "Руди ухмыльнулся. Видимо, Вы его заинтересовали"
    
    $ j = j+1
    
    jump yes_job1
    
    return

#продолжение главы 2
label yes_job1:

    scene bg mykab
    
    show rudi normal
    
    "давай. Можешь посвятить меня в курс дела?"
    
    rudi "Ага. Итак, у нас есть многомиллиардная компания, занимающаяся водоснабжением."
    
    rudi "Но в последнее время из-за очистки воды люди стали чаще попадать в больницы."
    
    rudi "Симптомы одни и те же, так что это 100 процентов проделки WaterPump."
    
    rudi "Нам нужно раздобыть как можно больше сведений и улик, чтобы доказать их вину."
    
    show rudi angry
    
    rudi'''
    
    Иначе на приближающейся \"WaterEXPA\" они покажут новое поколение фильтров...
    
    И мягко говоря сократят количесвто своих клиентов.
    
    У меня есть некоторые заметки, которые помогут нам прижучить этих гадов.'''
    
    "Ясно, сейчас Я изучу твои заметки и завтра мы отправимся в WaterPump."
    
    hide rudi angry
    
    scene bg black
    
    with fade
    
    "заметка 1 - Для начала надо забрать записи с камер"
    
    "заметка 2 - дальше нужно забрать отчёты эксперта по анализу воды ДО ТОГО, как он его подделает"
    
    "заметка 3 - Около дамбы находится склад водяных фильтров. Если оттуда взять старый и сравнить его с новым"
    
    "заметка 4 - И последнее, что поможет - проба воды из лаборатории. Кто знает, с чем они смешивают воду ради чистоты"
    
    scene bg mykab
    
    with fade
    
    "Ну что, это может сработать. Завтра выдвигаемся в офис WaterPump..."
    
    jump glava3
    
    return

#глава3    
label glava3:
    
    scene bg nebosk
    
    "Утреннее солнце освещает высокое здание, принадлежащее WaterPump. Где-то здесь можно найти полезные данные."
    
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
    
    "Хах,надеюсь у тебя есть с собой пару бутылок святой воды."
    
    show rudi smile
    
    rudi "Аахаха. Моя тётя часто посещает церковь, возьму у нее пару бутылок"
    
    "Руди посмеялся. Это был верный шаг для сближения с ним."
    
    $ j = j+1
    
    jump glava3_1
    
    return
    
#выбор в главе 3
label no_support:

    scene bg nebosk
        
    show rudi normal
    
    "Не выдумывай, обычный небоскрёб крупной компании"
    
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
    
    "Напомни, что мы будем искать?"
    
    rudi "Скорее всего тут можно раздобыть записи с камер и отчёт эксперта."
    
    jump glava3_1
    
    return
   
#2-й выбор в главе 3   
label health:

    scene bg nebosk
        
    show rudi normal
    
    "Как ты себя чувствуешь? Ты точно готов к походу?"
    
    show rudi smile
    
    rudi "А? Да, я в поряде. Спасибо за интерес."
    
    jump glava3_1
    
    return
    
#2-й выбор в главе 3
label building:

    scene bg nebosk
        
    show rudi normal
    
    "Нет, ничего. Пойдём уже."
    
    rudi "Да....Конечно.... Ну тогда в путь!"
    
    scene bg black
    
    with fade
    
    hide rudi normal
    
    "Вы вошли в здание WaterPump Incorported. По коже прошёл лёгкий ветерок. Чувство тревоги теперь сопровождает вас."
    
    return
  