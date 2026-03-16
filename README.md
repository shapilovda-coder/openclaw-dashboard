# 🎛️ OpenClaw Mission Control Dashboard

Веб-дашборд для управления проектами, скиллами и задачами OpenClaw.

## 🚀 Быстрый старт (Vercel)

### 1. Создай репозиторий на GitHub
```bash
cd /root/.openclaw/workspace/dashboard
git init
git add .
git commit -m "Initial dashboard"
# Создай репозиторий на GitHub и запушь
```

### 2. Импортируй в Vercel
1. Зайди на [vercel.com](https://vercel.com)
2. "Add New Project"
3. Импортируй свой GitHub репозиторий
4. Framework Preset: **Other**
5. Root Directory: `./`
6. Deploy

### 3. Готово!
Сайт будет доступен по `https://your-project.vercel.app`

---

## 🚀 Альтернатива: Render

### 1. Создай Static Site на Render
1. Зайди на [render.com](https://render.com)
2. "New" → "Static Site"
3. Подключи GitHub репозиторий
4. Build Command: `echo "No build needed"`
5. Publish Directory: `./`
6. Deploy

---

## 📊 Функционал

### Проекты
- 8 активных проектов с прогресс-барами
- Фильтрация по статусу (активные/на паузе)
- Быстрый доступ к деталям

### Task Board (Kanban)
- **To Do**: Задачи в очереди
- **In Progress**: В работе
- **Done**: Выполненные
- Drag-and-drop (можно добавить)

### Skills Arsenal
- Все 32 скилла с иконками
- Поиск по названию
- Фильтрация по категориям
- Статус (активен/требует доработки)

### Activity Log
- Лента последних действий
- Временные метки
- Типы событий (цветовые индикаторы)

### Real-time
- Текущее время MSK
- Статус агента (Online)
- Кнопка ручного обновления

---

## 🔧 Настройка обновления данных

### Вариант 1: При заходе на сайт (рекомендуется)
Данные обновляются автоматически при каждой загрузке страницы.

В `script.js` (уже реализовано):
```javascript
window.addEventListener('load', refreshData);
```

### Вариант 2: Cron job (раз в день в 12:00 MSK)

#### Через GitHub Actions (для Vercel)
Создай файл `.github/workflows/update.yml`:
```yaml
name: Daily Update
on:
  schedule:
    - cron: '0 9 * * *'  # 12:00 MSK = 09:00 UTC
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Update Data
        run: |
          # Скрипт обновления данных
          node update-data.js
      - name: Commit and Push
        run: |
          git config --global user.name 'Bot'
          git config --global user.email 'bot@example.com'
          git add .
          git commit -m "Daily update $(date)" || exit 0
          git push
```

#### Через Cron на VPS (для Render)
Добавь в crontab на своём VPS:
```bash
# Обновление данных dashboard каждый день в 12:00 MSK
0 12 * * * cd /root/.openclaw/workspace/dashboard && ./update-data.sh
```

---

## 🔒 Безопасность (ВАЖНО!)

### ❌ НЕ включай в репозиторий:
- API ключи (Apify, OpenAI, Telegram)
- Пароли и токены
- Файлы `.env`

### ✅ Что включено (безопасно):
- Только `index.html` со статическими данными
- Структура проектов (названия, прогресс)
- Список скиллов (без API ключей)
- Общая статистика

### 🔑 Если нужны API-запросы:
Используй Serverless Functions (Vercel Functions или Render Functions) и храни ключи в Environment Variables.

---

## 🎨 Кастомизация

### Добавить новый проект
В `index.html` найди `<!-- Projects Grid -->` и добавь:
```html
<div class="glass rounded-xl p-6 project-card" data-status="active">
    <div class="flex justify-between items-start mb-4">
        <div class="text-3xl">🆕</div>
        <span class="px-3 py-1 bg-green-500/20 text-green-400 rounded-full text-xs">Активен</span>
    </div>
    <h3 class="text-xl font-bold mb-2">Название проекта</h3>
    <p class="text-gray-400 text-sm mb-4">Описание проекта</p>
    <div class="mb-4">
        <div class="flex justify-between text-sm mb-1">
            <span>Прогресс</span>
            <span class="text-blue-400">0%</span>
        </div>
        <div class="w-full bg-gray-700 rounded-full h-2">
            <div class="bg-blue-500 h-2 rounded-full progress-bar" style="width: 0%"></div>
        </div>
    </div>
</div>
```

### Обновить прогресс проекта
Найди проект и измени:
```html
<span class="text-blue-400">75%</span>  <!-- Новый процент -->
...
<div class="bg-blue-500 h-2 rounded-full progress-bar" style="width: 75%"></div>
```

### Добавить задачу
В нужную колонку (`todo-column`, `progress-column`, `done-column`) добавь:
```html
<div class="task-card bg-gray-800 p-4 rounded-lg border-l-4 border-blue-500">
    <h4 class="font-semibold mb-1">Название задачи</h4>
    <p class="text-sm text-gray-400">Описание</p>
    <div class="flex justify-between items-center mt-2">
        <span class="text-xs text-gray-500">Проект</span>
        <span class="text-xs bg-blue-500/20 text-blue-400 px-2 py-1 rounded">Priority</span>
    </div>
</div>
```

---

## 📝 Локальная разработка

```bash
cd /root/.openclaw/workspace/dashboard

# Простой HTTP сервер
python3 -m http.server 8080

# Или Node.js
npx serve .

# Открыть в браузере
http://localhost:8080
```

---

## 🔄 Обновление данных

### Ручное обновление
1. Отредактируй `index.html`
2. Закоммить и запушь
3. Vercel/Render автоматически перезадеплоит

### Автоматическое обновление
Для полной автоматизации нужно:
1. Скрипт, который читает `memory/`, `tasks/`, `skills/`
2. Генерирует обновлённый `index.html`
3. Коммитит и пушит в GitHub
4. Vercel/Render перезадеплоит

Пример скрипта обновления:
```bash
#!/bin/bash
# update-dashboard.sh

cd /root/.openclaw/workspace

# Сгенерировать JSON с данными
python3 scripts/generate-dashboard-data.py > dashboard/data.json

# Перейти в dashboard
cd dashboard

# Коммит
 git add .
git commit -m "Auto-update: $(date '+%Y-%m-%d %H:%M')"
git push origin main
```

---

## 📱 Доступ

После деплоя дашборд будет доступен:
- **Vercel**: `https://your-project.vercel.app`
- **Render**: `https://your-project.onrender.com`

Можно открывать с телефона, планшета, компьютера.

---

## 🎯 TODO

- [ ] Добавить drag-and-drop для задач
- [ ] Интеграция с реальными API (через прокси)
- [ ] Тёмная/светлая тема
- [ ] Уведомления в браузере
- [ ] Экспорт данных в PDF

---

**Готов к деплою!** 🚀
