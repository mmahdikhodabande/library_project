function Danger() {
    $.get('/register').then(res => {
        if (res.status === 'ERROR_len4') {
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'اوکی',
            })
        }
        if (res.status === 'ERROR_len12') {
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'اوکی',
            })
        }
    });
}