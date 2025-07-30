
document.addEventListener('DOMContentLoaded', () => {

  // Obtengo el csrf_token 
  function getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie != "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim()
        if (cookie.startsWith(name + "=")) {
          cookieValue = cookie.substring(name.length + 1).trim();
          break;
        }
      }
    }
    return cookieValue
  }
  const csrfToken = getCookie('csrftoken')






  let tags = document.getElementsByClassName('remove-tag')
  const endpoint = `http://127.0.0.1:8000/projects/remove_tag/`

  for (let i = 0; i < tags.length; i++) {
    tags[i].addEventListener('click', (event) => {
      const clickedElement = event.currentTarget;
      let tagId = clickedElement.dataset.tag
      let projectId = clickedElement.dataset.project


      // console.log("Ejecutando fetch con tagId:", tagId, "projectId:", projectId);
      fetch(endpoint, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
          tag_id: tagId,
          project_id: projectId,
        })
      })
        .then(response => {
          console.log("Estado de la respuesta:", response.status);
          return response.json()
        })
        .then(data => {
          // console.log("Data:", data)
          if (data.message == "Tag removed successfully") {

            const parentTag = clickedElement.closest('.tag')
            if (parentTag) {
              parentTag.remove()

            } else {
              console.warn(`No se encontró el elemento del tag ${data.tag_id} para el proyecto ${data.project_id}`);
            }
          }
        })
        .catch(error => {
          console.log("Ocurrió un error:", error)
        })
    })
  }
})

