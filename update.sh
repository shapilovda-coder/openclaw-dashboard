#!/bin/bash
# update-dashboard.sh - Cron job для обновления дашборда

echo "🔄 Updating dashboard data..."
cd /root/.openclaw/workspace/dashboard

# Генерируем новые данные
python3 generate_data.py

# Если есть git-репозиторий - коммитим и пушим
if [ -d ".git" ]; then
    git add data.json
    git commit -m "Auto-update: $(date '+%Y-%m-%d %H:%M MSK')" || echo "No changes to commit"
    git push origin main || echo "Push failed or no remote"
fi

echo "✅ Done!"
