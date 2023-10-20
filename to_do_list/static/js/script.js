


function showAddTaskModal() {
    $('#addTaskModal').modal('show');
}


function showEditTaskModal(taskId) {
    $(`#editTaskModal${taskId}`).modal('show');
}

function showConfirmationPopup(event) {
    return confirm('Are you sure you want to delete this task?');
}


$(function () {
    $('.btn-outline-primary').on('click', function () {
    var targetModalId = $(this).data('bs-target');
    $(targetModalId).modal('show');
    });
});
