function colorize() {
    // Get the 4 rows in the tbody
    const rows = document.querySelectorAll('table tbody tr:nth-child(even)');
    // Change the color of the even rows to teal color
    rows.forEach(el => el.style.backgroundColor = 'teal')
}