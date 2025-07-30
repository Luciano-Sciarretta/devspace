document.addEventListener('DOMContentLoaded', () => {

  const form = document.querySelector('.login__form')

  form.addEventListener('submit', (e) => {
    e.preventDefault()
    const formData = {
      'username': form.username.value,
      'password': form.password.value,

    }
    fetch('http://127.0.0.1:8000/api/users/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',

      },
      body: JSON.stringify(formData)
    })
      .then(response => response.json())
      .then(data => {
        console.log("DATA:", data.access)
        if (data.access) {
          localStorage.setItem('token', data.access)
          window.alert("Sesión iniciada correctamente")
          window.location = 'http://127.0.0.1:5500/api_front/index.html#'
        }
        else {
          alert("Username or password incorrect")
        }
      })
  })

})