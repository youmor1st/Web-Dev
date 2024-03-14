function addTask() {
    const newTaskInput = document.getElementById('new-task');
    const taskText = newTaskInput.value.trim();

    if (taskText !== '') {
        const tasksList = document.getElementById('tasks-list');

        const taskElement = document.createElement('div');
        taskElement.className = 'task';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.addEventListener('change', function () {
            if (checkbox.checked) {
                taskTextElement.style.textDecoration = 'line-through';
            } else {
                taskTextElement.style.textDecoration = 'none';
            }
            sortTasks();
        });

        const taskTextElement = document.createElement('span');
        taskTextElement.textContent = taskText;

        const editButton = document.createElement('button');
        editButton.className = 'edit-button';
        editButton.textContent = 'Edit';
        editButton.addEventListener('click', function () {
            editTask(taskTextElement);
        });

        const deleteButton = document.createElement('button');
        deleteButton.className = 'delete-button';
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', function () {
            tasksList.removeChild(taskElement);
            sortTasks();
        });

        taskElement.appendChild(checkbox);
        taskElement.appendChild(taskTextElement);
        taskElement.appendChild(editButton);
        taskElement.appendChild(deleteButton);

        tasksList.appendChild(taskElement);

        newTaskInput.value = '';

        sortTasks();
    }
}

function editTask(taskTextElement) {
    const newText = prompt('Edit task:', taskTextElement.textContent);
    if (newText !== null) {
        taskTextElement.textContent = newText.trim();
        sortTasks();
    }
}




function sortTasks() {
    const tasksList = document.getElementById('tasks-list');
    const tasks = Array.from(tasksList.children);

    tasks.sort((a, b) => {
        const aChecked = a.querySelector('input[type="checkbox"]').checked;
        const bChecked = b.querySelector('input[type="checkbox"]').checked;

        if (aChecked && !bChecked) {
            return 1;
        } else if (!aChecked && bChecked) {
            return -1;
        } else {
            return 0;
        }
    });

    tasks.forEach(task => tasksList.appendChild(task));
}
function editTask(taskTextElement) {
    const newText = prompt('Edit task:', taskTextElement.textContent);
    if (newText !== null) {
        taskTextElement.textContent = newText.trim();
        sortTasks();
    }
}

function clearCompletedTasks() {
    const tasksList = document.getElementById('tasks-list');
    const completedTasks = Array.from(tasksList.querySelectorAll('.task input:checked'));
    completedTasks.forEach(task => tasksList.removeChild(task.parentNode));
    sortTasks();
}

function filterTasks(filterType) {
    const tasksList = document.getElementById('tasks-list');
    tasksList.querySelectorAll('.task').forEach(task => {
        const checkbox = task.querySelector('input[type="checkbox"]');
        const isCompleted = checkbox.checked;

        switch (filterType) {
            case 'all':
                task.style.display = 'flex';
                break;
            case 'completed':
                task.style.display = isCompleted ? 'flex' : 'none';
                break;
            case 'active':
                task.style.display = isCompleted ? 'none' : 'flex';
                break;
        }
    });
}