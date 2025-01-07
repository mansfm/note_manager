username = input("Введите имя пользователя: ")
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки, в формате ДД.ММ.ГГГГ: ")
issue_date = input("Введите дату истечения заметки (дедлайн), в формате ДД.ММ.ГГГГ: ")

title = [title1, title2, title3]
note = [username, title, content, status, created_date, issue_date]

print(note)