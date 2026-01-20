"""
AI Brain - Natural Language Understanding and Intent Recognition
"""

import re

class AIBrain:
    def __init__(self):
        """Initialize AI brain with intent patterns"""
        self.intents = self._define_intents()
    
    def _define_intents(self):
        """Define intent patterns for command recognition"""
        return {
            "send_message": {
                "patterns": [
                    r"send.*message.*to\s+(\w+).*(.+)",
                    r"message\s+(\w+).*(.+)",
                    r"whatsapp\s+(\w+).*(.+)",
                    r"text\s+(\w+).*(.+)",
                ],
                "keywords": ["send", "message", "text", "whatsapp", "sms"]
            },
            "make_call": {
                "patterns": [
                    r"call\s+(\w+)",
                    r"phone\s+(\w+)",
                    r"dial\s+(\w+)",
                ],
                "keywords": ["call", "phone", "dial"]
            },
            "open_app": {
                "patterns": [
                    r"open\s+(\w+)",
                    r"launch\s+(\w+)",
                    r"start\s+(\w+)",
                ],
                "keywords": ["open", "launch", "start"]
            },
            "get_tasks": {
                "patterns": [
                    r"show.*task",
                    r"what.*task",
                    r"list.*task",
                ],
                "keywords": ["task", "tasks", "reminder"]
            },
            "add_task": {
                "patterns": [
                    r"add.*task.*(.+)",
                    r"remind.*me.*(.+)",
                    r"note.*(.+)",
                ],
                "keywords": ["add", "task", "remind", "note"]
            },
            "screenshot": {
                "patterns": [
                    r"screenshot",
                    r"take.*screenshot",
                    r"capture.*screen",
                ],
                "keywords": ["screenshot", "capture"]
            },
            "get_contacts": {
                "patterns": [
                    r"show.*contacts",
                    r"list.*contacts",
                    r"find\s+(\w+)",
                ],
                "keywords": ["contacts", "contact", "find"]
            },
            "get_messages": {
                "patterns": [
                    r"show.*messages",
                    r"read.*messages",
                    r"list.*sms",
                ],
                "keywords": ["messages", "sms", "texts"]
            },
            "get_device_info": {
                "patterns": [
                    r"device.*info",
                    r"phone.*info",
                    r"battery",
                ],
                "keywords": ["device", "phone", "info", "battery"]
            },
            "get_call_logs": {
                "patterns": [
                    r"call.*history",
                    r"recent.*calls",
                    r"who.*called",
                ],
                "keywords": ["call", "history", "calls"]
            },
        }
    
    def understand(self, command):
        """Understand voice command and return intent and parameters"""
        command = command.lower()
        
        # Try to match intent patterns
        for intent_name, intent_data in self.intents.items():
            for pattern in intent_data["patterns"]:
                match = re.search(pattern, command)
                if match:
                    return self._extract_action(intent_name, match, command)
        
        # If no pattern matches, try keyword matching
        for intent_name, intent_data in self.intents.items():
            if any(keyword in command for keyword in intent_data["keywords"]):
                return self._extract_action(intent_name, None, command)
        
        return "unknown", {}
    
    def _extract_action(self, intent, match, command):
        """Extract action parameters from command"""
        params = {}
        
        if intent == "send_message" and match:
            groups = match.groups()
            if len(groups) >= 2:
                params['contact'] = groups[0]
                params['message'] = groups[1]
            else:
                params['contact'] = groups[0] if groups else "unknown"
                params['message'] = command
        
        elif intent == "make_call" and match:
            params['contact'] = match.group(1)
        
        elif intent == "open_app" and match:
            params['app_name'] = match.group(1)
        
        elif intent == "add_task" and match:
            params['task'] = match.group(1)
        
        elif intent == "screenshot":
            params = {}
        
        return intent, params
