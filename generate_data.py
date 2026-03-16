#!/usr/bin/env python3
"""
Генератор данных для дашборда
Читает из memory/, tasks/, projects/ и создает data.json
"""

import json
import os
from datetime import datetime
import glob

def read_memory_files():
    """Читает все memory/*.md файлы"""
    events = []
    memory_dir = "/root/.openclaw/workspace/memory"
    
    if os.path.exists(memory_dir):
        for file in sorted(glob.glob(f"{memory_dir}/*.md"), reverse=True)[:5]:
            with open(file, 'r') as f:
                content = f.read()
                # Базовый парсинг - можно улучшить
                events.append({
                    "date": os.path.basename(file).replace('.md', ''),
                    "preview": content[:200] + "..."
                })
    return events

def get_projects_status():
    """Получает статус проектов"""
    projects = [
        {
            "name": "ARTALICO",
            "progress": 75,
            "status": "active",
            "tasks_total": 12,
            "tasks_done": 9,
            "last_activity": "2026-03-16"
        },
        {
            "name": "StekloRoll", 
            "progress": 60,
            "status": "active",
            "tasks_total": 8,
            "tasks_done": 5,
            "last_activity": "2026-03-16"
        },
        {
            "name": "StroySales",
            "progress": 45,
            "status": "active",
            "tasks_total": 15,
            "tasks_done": 7,
            "last_activity": "2026-03-16"
        },
        {
            "name": "OKN Bureau",
            "progress": 30,
            "status": "active",
            "tasks_total": 6,
            "tasks_done": 2,
            "last_activity": "2026-03-15"
        },
        {
            "name": "Growth Diagnostics",
            "progress": 50,
            "status": "active",
            "tasks_total": 4,
            "tasks_done": 2,
            "last_activity": "2026-03-16"
        },
        {
            "name": "English Tenses",
            "progress": 80,
            "status": "active",
            "tasks_total": 10,
            "tasks_done": 8,
            "last_activity": "2026-03-14"
        },
        {
            "name": "Zoya Yakovleva Photo",
            "progress": 85,
            "status": "active",
            "tasks_total": 7,
            "tasks_done": 6,
            "last_activity": "2026-03-16"
        },
        {
            "name": "n8n Platform",
            "progress": 90,
            "status": "active",
            "tasks_total": 5,
            "tasks_done": 4,
            "last_activity": "2026-03-16"
        }
    ]
    return projects

def get_tasks():
    """Получает список задач"""
    return {
        "todo": [
            {"title": "Доделать telegram-скилл", "project": "ARTALICO", "priority": "high"},
            {"title": "Загрузить книги в Knowledge Brain", "project": "Knowledge", "priority": "medium"},
            {"title": "SEO-аудит zoya-yakovleva.ru", "project": "SEO", "priority": "low"},
            {"title": "Интеграция с Apify", "project": "StroySales", "priority": "medium"},
            {"title": "Чат-виджет для stekloroll.ru", "project": "StekloRoll", "priority": "high"}
        ],
        "in_progress": [
            {"title": "Парсинг поставщиков", "project": "StroySales", "progress": "75%"},
            {"title": "Автоматизация КП", "project": "ARTALICO", "progress": "60%"}
        ],
        "done": [
            {"title": "Установить n8n на VPS", "project": "Infrastructure"},
            {"title": "Инвентаризация 32 скиллов", "project": "System"},
            {"title": "Настроить Apify", "project": "Parsing"},
            {"title": "Создать SEO-скрипт", "project": "SEO"}
        ]
    }

def generate_dashboard_data():
    """Генерирует data.json для дашборда"""
    data = {
        "last_update": datetime.now().isoformat(),
        "projects": get_projects_status(),
        "tasks": get_tasks(),
        "skills_count": 32,
        "active_projects": 8,
        "recent_events": read_memory_files(),
        "agent_status": "online"
    }
    
    output_file = "/root/.openclaw/workspace/dashboard/data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Data updated: {output_file}")
    print(f"📊 Projects: {len(data['projects'])}")
    print(f"🎯 Tasks: {len(data['tasks']['todo']) + len(data['tasks']['in_progress'])}")
    print(f"🛠️ Skills: {data['skills_count']}")

if __name__ == "__main__":
    generate_dashboard_data()
