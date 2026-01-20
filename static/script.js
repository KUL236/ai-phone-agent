// AI Phone Agent Web UI JavaScript

// API Base URL
const API_URL = '/api';

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    checkStatus();
    loadExamples();
    loadTasks();
    setInterval(checkStatus, 5000); // Check status every 5 seconds
});

// Connect to phone
async function connectPhone() {
    const btn = document.getElementById('connectBtn');
    const msg = document.getElementById('connectionMsg');
    
    btn.disabled = true;
    btn.textContent = 'Connecting...';
    
    try {
        const response = await fetch(`${API_URL}/connect`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            showMessage(msg, 'Connected to device!', 'success');
            updateStatus(true, data.device_id);
        } else {
            showMessage(msg, data.message, 'error');
        }
    } catch (error) {
        showMessage(msg, 'Connection error: ' + error.message, 'error');
    } finally {
        btn.disabled = false;
        btn.textContent = 'Connect Phone';
    }
}

// Send command
async function sendCommand() {
    const input = document.getElementById('commandInput');
    const command = input.value.trim();
    const msg = document.getElementById('commandMsg');
    const responseSection = document.getElementById('responseSection');
    const responseContent = document.getElementById('responseContent');
    
    if (!command) {
        showMessage(msg, 'Please enter a command', 'error');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/command`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command })
        });
        
        const data = await response.json();
        
        if (data.status === 'success' || data.status === 'unknown') {
            showMessage(msg, data.message, 'success');
            
            // Show response
            responseSection.style.display = 'block';
            responseContent.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
            
            // Clear input
            input.value = '';
            input.focus();
        } else {
            showMessage(msg, data.message, 'error');
        }
    } catch (error) {
        showMessage(msg, 'Error: ' + error.message, 'error');
    }
}

// Add task
async function addTask() {
    const input = document.getElementById('taskInput');
    const task = input.value.trim();
    
    if (!task) return;
    
    try {
        const response = await fetch(`${API_URL}/command`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command: `add task ${task}` })
        });
        
        const data = await response.json();
        input.value = '';
        loadTasks();
    } catch (error) {
        console.error('Error adding task:', error);
    }
}

// Load tasks
async function loadTasks() {
    try {
        const response = await fetch(`${API_URL}/tasks`);
        const data = await response.json();
        
        const tasksList = document.getElementById('tasksList');
        
        if (data.tasks && data.tasks.length > 0) {
            tasksList.innerHTML = data.tasks.map(task => `
                <div class="task-item">
                    <div class="task-text">${task.text}</div>
                    <button class="btn btn-danger" onclick="deleteTask(${task.id})">Done</button>
                </div>
            `).join('');
        } else {
            tasksList.innerHTML = '<p style="text-align: center; color: #999;">No tasks yet</p>';
        }
    } catch (error) {
        console.error('Error loading tasks:', error);
    }
}

// Delete task
async function deleteTask(taskId) {
    try {
        await fetch(`${API_URL}/tasks/${taskId}`, {
            method: 'DELETE'
        });
        loadTasks();
    } catch (error) {
        console.error('Error deleting task:', error);
    }
}

// Load examples
async function loadExamples() {
    try {
        const response = await fetch(`${API_URL}/examples`);
        const examples = await response.json();
        
        const examplesDiv = document.getElementById('examples');
        
        let html = '';
        for (const [category, commands] of Object.entries(examples)) {
            html += `
                <div class="example-category">
                    <h3>${category.charAt(0).toUpperCase() + category.slice(1)}</h3>
                    <ul>
                        ${commands.map(cmd => `
                            <li onclick="setCommand('${cmd}')" title="Click to use">${cmd}</li>
                        `).join('')}
                    </ul>
                </div>
            `;
        }
        
        examplesDiv.innerHTML = html;
    } catch (error) {
        console.error('Error loading examples:', error);
    }
}

// Set command
function setCommand(command) {
    document.getElementById('commandInput').value = command;
    document.getElementById('commandInput').focus();
}

// Check status
async function checkStatus() {
    try {
        const response = await fetch(`${API_URL}/status`);
        const data = await response.json();
        updateStatus(data.connected, data.device_id);
    } catch (error) {
        updateStatus(false);
    }
}

// Update status UI
function updateStatus(connected, deviceId = null) {
    const indicator = document.querySelector('.indicator');
    const statusText = document.getElementById('statusText');
    const connectBtn = document.getElementById('connectBtn');
    
    if (connected) {
        indicator.classList.add('connected');
        statusText.textContent = `Connected (${deviceId || 'Device'})`;
        connectBtn.textContent = '✓ Connected';
        connectBtn.disabled = true;
    } else {
        indicator.classList.remove('connected');
        statusText.textContent = 'Disconnected';
        connectBtn.textContent = 'Connect Phone';
        connectBtn.disabled = false;
    }
}

// Show message
function showMessage(element, text, type) {
    element.textContent = text;
    element.className = `message show ${type}`;
    
    setTimeout(() => {
        element.classList.remove('show');
    }, 5000);
}

// Allow Enter key to send command
document.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && document.activeElement.id === 'commandInput') {
        sendCommand();
    }
    if (e.key === 'Enter' && document.activeElement.id === 'taskInput') {
        addTask();
    }
});
