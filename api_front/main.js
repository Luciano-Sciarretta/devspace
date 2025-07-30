document.addEventListener('DOMContentLoaded', function () {

  // Login y Logout

  const loginBtn = document.getElementById('login-btn')
  const logoutBtn = document.getElementById('logout-btn')
  let token = localStorage.getItem('token')

  if (token) {
    loginBtn.remove()
  } else {
    logoutBtn.remove()
  }
  
  loginBtn.addEventListener('click', (e) => {
   
    window.location = 'http://127.0.0.1:5500/api_front/login.html'
  })


  logoutBtn.addEventListener('click', (e) => {
    localStorage.removeItem('token')
    window.alert("Cerraste sesión correctamente")
    window.location.reload()
  })

////////////////////////////////////////////////////////////////////


  const baseDir = 'http://127.0.0.1:8000/'
  const projectsWrapper = document.getElementById('projects-wrapper');

  const template = document.createElement('template');
  template.innerHTML = `
    <div class="project__card">
      <div class='img__container'>
        <img src="project__img" alt="">
      </div>
      <div class='project__header'>
        <h3></h3>
        <i></i>
        <p class='project__description'></p>
        <div class= 'vote__container'>
        <h6>Place your vote</h6>
          <a href="#"   class="vote__option" data-vote = 'up'>&#43</a>
          <a href="#"   class="vote__option" data-vote = 'down'>&#8722</a>
        </div>
      </div>
    </div>
  `;

  const getProjects = () => {
    let projectsURL = `${baseDir}/api/projects/`

    fetch(projectsURL)
      .then(response => response.json())
      .then(data => {

        showProjects(data)
        addVoteEvent()
      })
      .catch(error => {
        console.error('Error al obtener proyectos:', error);
      });
  }

  //Insertar proyectos en el DOM

  const showProjects = (projects) => {
    //

    for (let i = 0; projects.length > i; i++) {
      let project = projects[i]
      const projectCard = template.content.cloneNode(true);

      const img = projectCard.querySelector('img');
      img.src = project.featured_image ? `${baseDir}${project.featured_image}` : `${baseDir}media/projects/default.jpg`;


      projectCard.querySelector('h3').textContent = project.title || 'Proyecto sin título';

      const voteButtons = projectCard.querySelectorAll('.vote__option')

      for (let i = 0; voteButtons.length > i; i++) {
        voteButtons[i].dataset.project = project.id
      }


      projectCard.querySelector('i').textContent = project.vote_ratio + "% Positive Feedback"

      projectsWrapper.appendChild(projectCard);
    }
  }

  // Eventos de botones para votar

  const addVoteEvent = () => {
    let voteButtons = document.getElementsByClassName('vote__option')
    for (let i = 0; voteButtons.length > i; i++) {

      voteButtons[i].addEventListener('click', (e) => {

        let vote = e.target.dataset.vote
        let projectId = e.target.dataset.project
        fetch(`${baseDir}api/projects/${projectId}/vote/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({'value': vote, })

        })
        .then(response => response.json()
      ) 
        .then(data => {
          console.log("Success:", data)
        })
      })
    }
  }
  getProjects()
});