document.addEventListener('DOMContentLoaded', function () {
  let getProjects = () => {

    let projectsURL = 'http://127.0.0.1:8000/api/projects/'

    fetch(projectsURL)
      .then(response => response.json())
        .then(data => {
          console.log(data)
        })
  }

  getProjects()
});