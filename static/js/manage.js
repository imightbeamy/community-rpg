function append_token(token_data) {
    // TODO: render token_row.mustache
    $('.tokens').append($('<tr>').text(token_data.title));
}

function append_question(question_data) {
    // TODO: render questions_row.mustache
    $('.questions').append(
        $('<li>').addClass('list-group-item').text(question_data.text));
}

// Manage tokens
$('.add-new-token').submit(function(e) {
    e.preventDefault();
    $.post('/api/token', $(this).serialize()).success(append_token);
});

$('.tokens')
    .on('click', '.delete', function(e) {
        var token_row = $(this).parents('tr');
        $.ajax({
            url: '/api/token/' + token_row.attr("data-token-id"),
            type: 'DELETE',
            success: function() {
                token_row.remove();
            }
        });
    });

// Manage questions
$('.add-new-question').submit(function(e) {
    e.preventDefault();
    $.post('/api/question', $(this).serialize()).success(append_question)
});

$('.questions')
    .on('click', '.add-weight', function(e) {
        e.preventDefault();
        var question_row = $(this).parents('li'),
            question_id = question_row.attr("data-question-id"),
            token_id = question_row.find('.token-id').val(),
            yes_weight = question_row.find('.yes-weight').val(),
            no_weight = question_row.find('.no-weight').val();

        $.post('/api/question/' + question_id + '/token/' + token_id, {
            yes_weight: yes_weight,
            no_weight: no_weight
        });
    })
    .on('click', '.delete-weight', function(e) {
        e.preventDefault();
        var question_row = $(this).parents('li'),
            token_row = $(this).parents('tr'),
            question_id = question_row.attr("data-question-id"),
            token_id = token_row.attr("data-token-id");

        $.ajax({
            url: '/api/question/' + question_id + '/token/' + token_id,
            type: 'DELETE',
            success: function() {
                token_row.remove();
            }
        });
    });