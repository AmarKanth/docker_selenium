$(document).ready(function() {
    function fetchData(query = '') {
        $.ajax({
            url: '/?query=' + encodeURIComponent(query),
            method: 'GET',
            success: function(data) {
                $('#search-table-body').html(data.html);
            },
            error: function() {
                alert('An error occurred');
            }
        });
    }

    $('#search-button').on('click', function() {
        const query = $('#search-query').val();
        fetchData(query);
    });

    setInterval(function() {
        fetchData('');
    }, 30000);
});
