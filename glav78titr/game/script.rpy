# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define mj = Character('Меррелин Джустилис', color="#c8ffc8")
define slowdis = Dissolve(1.0)
define water_sample = 0 #счет воды

#ЭТО ПОТОМ УБРАТЬ
define camera = 1
define old_water_filter = 1
define expert_report = 1




# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label glava6:


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

