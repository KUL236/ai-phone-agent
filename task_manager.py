"""
Task Manager - Manages daily tasks and reminders
"""

import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, task_file="tasks.json"):
        """Initialize task manager"""
        self.task_file = task_file
        self.tasks = self._load_tasks()
    
    def _load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.task_file):
            try:
                with open(self.task_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _save_tasks(self):
        """Save tasks to file"""
        with open(self.task_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, task_text, due_time=None):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "text": task_text,
            "created": datetime.now().isoformat(),
            "due_time": due_time,
            "completed": False
        }
        self.tasks.append(task)
        self._save_tasks()
        print(f"✅ Task added: {task_text}")
        return task
    
    def get_today_tasks(self):
        """Get all tasks for today"""
        today = datetime.now().date()
        today_tasks = []
        
        for task in self.tasks:
            if not task['completed']:
                created_date = datetime.fromisoformat(task['created']).date()
                if created_date == today:
                    today_tasks.append(task)
        
        return today_tasks
    
    def complete_task(self, task_id):
        """Mark task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self._save_tasks()
                print(f"✅ Task completed: {task['text']}")
                return True
        return False
    
    def get_pending_tasks(self):
        """Get all pending tasks"""
        return [task for task in self.tasks if not task['completed']]
    
    def delete_task(self, task_id):
        """Delete a task"""
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self._save_tasks()
