var addTaskBtn = document.getElementById('add-task-btn');
var addTaskModal = document.getElementById('add-task-modal');
var closeBtn = document.getElementsByClassName('close')[0];
var cancelBtn = document.getElementsByClassName('cancel-btn')[0];
var body = document.getElementsByTagName('body')[0];
var toggleBtn = document.getElementById('toggle-btn');


addTaskBtn.onclick = function() {
    addTaskModal.style.display = 'block';
}

closeBtn.onclick = function() {
    addTaskModal.style.display = 'none';
}

cancelBtn.onclick = function() {
    addTaskModal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == addTaskModal) {
        addTaskModal.style.display = 'none';
    }
}

toggleBtn.onclick = function() {
    body.classList.toggle('dark-mode');
}

