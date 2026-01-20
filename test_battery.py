"""
Test battery command
"""

from ai_brain import AIBrain

ai = AIBrain()

commands = [
    'battery',
    'battery status',
    'check battery',
    'device info',
    'what is my battery'
]

print('Testing battery-related commands:\n')
for cmd in commands:
    intent, params = ai.understand(cmd)
    print(f'Command: "{cmd}"')
    print(f'  Intent: {intent}')
    print(f'  Params: {params}')
    print()
