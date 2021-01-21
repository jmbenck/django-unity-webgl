# Unity WebGL integration with Python Django REST API
## This project consists in a Rest API made with Django and Rest framework that communicate with an Unity WebGL application (in this example, a game).
### Unity:
#### Lets start by understanding the Unity WebGL structure.

#### This is what a WebGL build, straight from Unity should look like:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/UnityWebGLExport.png)
> WebGL project builded from Unity.

- The source files of the exported game from the Unity is in the **Build** folder.
- The layout of the game container is in the **TemplateData** folder.
- The **index.html** file is a simple HTML page calling the WebGL container from Unity, calling:
    - Build/UnityLoader.js
    - Build/build.json
    - TemplateData stuff.

#### Opening the index.html will load Unity WebGL Player and then the game:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/GameDemonstration.png)
> WebGL game exported from Unity loaded and running in full screen.

#### Now we'll prepare this WebGL application to have user access control, to receive and send data from an external source, through an API.

### Django:

#### The main point in Django is to control users access, identify them, to get access to their score and persist this data in a database.

#### First of all, a Django Project was created and the Unity WebGL content imported in the static folder of the Django project. The source files of the game exported from the Unity is in the static folder but the index page that call the Unity WebGL container is in the templates django folder, since we want to access that page dynamically.

#### To control user access to the game there is an user authentication page and the url to the game is blocked until the user is logged in:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/TelaLogin.png)
> Authentication page.

#### New Users can sign up within a form. This way the data will persist in a database and the user will now can be identified.
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/TelaCadastro.png)
> Authentication page.

#### Once an user is logged in, they will be redirected to the game url. The game will load with an identification of the user in the center top of the container.
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/TelaJogoInicial.png)
> User authenticated and game loaded.

#### To get the user data we can use the API builded with Django-Rest-Framework. The API configuration is in the app called "api" in the Django project.

#### Since we don't want the page to refresh when sending a data, to be able to send user score even during the game lets use Jquery. There is a function called 'salvaPontuacao' that recives as argument the score of the user.
#### Note: This function needs to be inside the object **window.Unity** from index.html to be used later from Unity.
````javascript
    SalvaPontucao(pontos) {
      console.log('Pagina says: salvando pontuacao ' + pontos);
      var pontuacao = '{"pontuacao":' + pontos + "}";
      var url = 'http://localhost:8000/api/usuario/'+ {{user.id}} + '/';
      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
      });
      $.ajax({
        url: '/api/usuario/' + {{user.id}} + '/',
        contentType: 'application/json',
        cache: false,
        method: 'PATCH',
        dataType: 'json',
        data: pontuacao,
        headers: {
          'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content'),
        },
        success: function(data) {
          console.log(data);
        },
        error: function(data){
          console.log(data);
        }
      });

    }
  }
````
----------Part of the Unity code acessing the jquery----------

#### See the communication running in action. The Unity calls the function "salvaPontuacao" and the jQuery code uses the Rest API to modify the score of the user. See the console output:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/ApiComunication.png)
> Demonstration of the communication between Unity and a Django.

#### Once data is persisted in a database we can access that from other pages. Just like a Ranking page listing all the users and their score:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/TelaRanking.png)
> Ranking page.

#### Of course, we can manipulate all that stored data. That is where Django Admin comes on. It is a powerful part of Django to manage data and make operations like Create, Read, Update and Delete in such a easy way:

#### Once you created an admin user, just access "/admin" url:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/AdmHome.png)
> Admin Login page.

#### After authentication we are now able to manage the data:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/AdmCidades.png)
> Admin Interfcae - Managing the Cidades(Cities) records that are used in the user form registration.

![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/AdmEscolas.png)
> Admin Interfcae - Managing the Escolas(Schools) records that are used in the user form registration.

![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/AdmJogadoresExport.png)
> Admin Interfcae - Managing the Jogador(User) records. Note: you can export selected data do CSV.

#### That's all. Feel free to use this code or collaborate to this repo. Thank you.
