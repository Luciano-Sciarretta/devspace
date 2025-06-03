
let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
    alertClose.addEventListener('click', () => {
        alertWrapper.style.display = 'none'
    })
}

// Paginación en la barra de búsqueda

const searchForm = document.getElementById('searchForm')
const pageLinks = document.getElementsByClassName('page-link')
if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (event) {
            event.preventDefault()
            let page = this.dataset.page
            searchForm.innerHTML += `<input value = ${page} name="page" hidden/>`;
            searchForm.submit()
        });
    }
}





