const ctx = document.getElementById('categoryChart');

new Chart(ctx, {
    type: 'pie',

    data: {
        labels: Object.keys(categoryData),

        datasets: [{
            data: Object.values(categoryData)
        }]
    }
});
if (flashMessages.length > 0) {
    flashMessages.forEach(([category, message]) => {
        Swal.fire({
            icon: category,
            title: message,
            confirmButtonText: 'OK'
        });
    });
}
