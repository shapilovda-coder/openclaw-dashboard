# 🚀 Деплой Dashboard (Пошаговая инструкция)

## ⚡ Быстрый старт (Vercel) - 5 минут

### Шаг 1: Подготовка (1 минута)
```bash
# Заходи на свой VPS
cd /root/.openclaw/workspace/dashboard

# Инициализируй git (если еще не сделано)
git init
git add .
git commit -m "Initial dashboard commit"
```

### Шаг 2: Создай репозиторий на GitHub (2 минуты)
1. Зайди на github.com
2. Нажми "New Repository"
3. Название: `openclaw-dashboard`
4. **ВАЖНО**: Выбери "Public" (если нет приватного аккаунта)
5. Не добавляй README (уже есть)
6. Создай репозиторий

### Шаг 3: Запушь код (1 минута)
```bash
# В терминале на VPS (в папке dashboard)
git remote add origin https://github.com/ТВОЙ_НИК/openclaw-dashboard.git
git branch -M main
git push -u origin main
```

### Шаг 4: Деплой на Vercel (2 минуты)
1. Зайди на vercel.com (регистрация через GitHub)
2. Нажми "Add New Project"
3. Выбери свой репозиторий `openclaw-dashboard`
4. **Настройки:**
   - Framework Preset: `Other`
   - Root Directory: `./`
   - Build Command: оставь пустым
   - Output Directory: `./`
5. Нажми "Deploy"

✅ Готово! Сайт доступен по ссылке вида `https://openclaw-dashboard.vercel.app`

---

## 🔒 Безопасность (проверь!)

### ❌ Что НЕ попало в репозиторий (проверено):
- API ключи Apify
- Токены Telegram
- Пароли Supabase
- Любые .env файлы

### ✅ Что в репозитории (безопасно):
- Только HTML/CSS/JS
- Названия проектов
- Список скиллов
- Общая статистика

---

## 🔄 Автообновление данных

### Вариант 1: При заходе на сайт (уже работает)
Данные обновляются каждый раз, когда ты заходишь на страницу.

### Вариант 2: Раз в день в 12:00 MSK (Cron)

#### Добавь cron job на VPS:
```bash
# Открой crontab
 crontab -e

# Добавь строку:
0 12 * * * cd /root/.openclaw/workspace/dashboard && ./update.sh

# Сохрани (Ctrl+O, Enter, Ctrl+X)
```

Это будет:
- Обновлять data.json
- Коммитить в GitHub
- Vercel автоматически перезадеплоит

---

## 📊 Что увидишь на дашборде

### Главная страница:
- 🤖 Статус агента (Online/Offline)
- 📊 8 проектов с прогресс-барами
- 🎯 Task Board (To Do / In Progress / Done)
- 🛠️ 32 скилла с фильтрами
- 📝 Activity Log (последние действия)

### Проекты:
1. **ARTALICO** - 75% (CRM, КП, счета)
2. **StekloRoll** - 60% (сайт, чат-виджет)
3. **StroySales** - 45% (парсер, каталог)
4. **OKN Bureau** - 30% (архитектура)
5. **Growth Diagnostics** - 50% (консалтинг)
6. **English Tenses** - 80% (edtech)
7. **Zoya Yakovleva Photo** - 85% (фото)
8. **n8n Platform** - 90% (инфраструктура)

---

## 🛠️ Обновление дашборда

### Ручное обновление (через GitHub):
1. Редактируй `index.html` на GitHub
2. Нажми "Commit changes"
3. Vercel автоматически обновит сайт (~30 сек)

### Обновление через VPS:
```bash
cd /root/.openclaw/workspace/dashboard

# Отредактируй index.html
nano index.html

# Сохрани и запушь
git add .
git commit -m "Update: новые данные"
git push origin main
```

---

## 🆘 Если что-то пошло не так

### Ошибка "git push rejected":
```bash
git pull origin main --rebase
git push origin main
```

### Ошибка "Permission denied":
```bash
# Проверь SSH ключ или используй HTTPS
git remote set-url origin https://github.com/ТВОЙ_НИК/openclaw-dashboard.git
```

### Vercel не деплоит:
1. Зайди в dashboard проекта на vercel.com
2. Нажми "Redeploy"
3. Проверь логи в разделе "Deployments"

---

## 🎯 Дальнейшие улучшения

Что можно добавить:
- [ ] Drag-and-drop для задач
- [ ] Тёмная/светлая тема
- [ ] Уведомления в браузере
- [ ] Интеграция с Telegram (bot webhook)
- [ ] График активности (Chart.js)
- [ ] Экспорт в PDF

---

## 📱 Доступ

После деплоя:
- **Desktop**: просто открой ссылку
- **Mobile**: открой ссылку в Safari/Chrome
- **Tablet**: работает адаптивно

---

**Готов к запуску?** Выполни Шаги 1-4 выше ⬆️

Если что-то не получится — пиши, помогу!
