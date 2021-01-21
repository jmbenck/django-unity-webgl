# Unity WebGL integration with Python Django REST API
## This project consist in a Unity game (WebGL) that uses a Rest API made with Django and Restframework.

### Unity:
#### This is what Unity WebGL build should look like:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/UnityWebGLExport.png)
> WebGL project builded from Unity.

- The source files of the exported game from the Unity is in **Build** folder.
- The layout of the game container is in the **TemplateData** folder.
- The **index.html** file is a simple HTML page calling the WebGL containter from Unity, calling Build/UnityLoader.js, Build/build.json and some TemplateData stuff.

#### Accessing the index.html will load Unity WebGL Player and execute the game:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/GameDemonstration.png)
> WebGL game exported from Unity loaded and running in full screen.

#### Now I want this WebGL application to have a user access control, receive and send data an from external source, through an API.

### Django:

#### They in main point in Django is to control users access, indentify them, get access to their score and persist this data in a database.

#### First of all, I created a Django Project and imported the Unity WebGL content in the static folder of the Django project. The source files of the game exported from the Unity is in the static folder but the index page that call the Unity WebGL container is in the templates django folder, since we want to access that page dynamically.

#### To control user access to the game I made an user authentication page and blocked the url to the game until the user is logged in:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/TelaLogin.png)
> Authentication page.

#### New Users can sign up within a form. This way the data will persist in a database and the user will now can be identified.
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/TelaCadastro.png)
> Authentication page.

#### Once user is logged in, they will be redirected to the game url. The game will load with an identification of the user in the center top of the container.
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/TelaJogoInicial.png)
> User authenticated and game loaded.

#### To get the user data I used an API builded with Django-Rest-Framework. The api configuration is in the app called "api" in the Django project.

#### Since we don't want the page to refresh when sending a data, to be able to send user score even during the game I used Jquery. I made an function called 'salvaPontuacao' that recives as argument the score of the User.
#### This function will be used later from Unity.
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

#### Once data is persisted in a database we can access and manipulate that data.So I build a Ranking page, listing all the users and their score:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/TelaRanking.png)
> Ranking page.

#### Of course, we can manipulate all that stored data. That's where Django Admin comes on. It's a powerful part of Django to manage data and make operations like Create, Read, Update and Delete in such a easy way:

#### Once you created and admin user, just access /admin url:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/AdmHome.png)
> Admin Login page.

#### After authentication you are now able to manage the data:
![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/AdmCidades.png)
> Admin Interfcae - Managing the Cidades(Cities) records that are used in the user form registration.

![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/AdmEscolas.png)
> Admin Interfcae - Managing the Escolas(Schools) records that are used in the user form registration.

![](https://github.com/jmbenck/Django-UnityWebGL/blob/master/demonstration/AdmJogadoresExport.png)
> Admin Interfcae - Managing the Jogador(User) records. Note: you can export selected data do CSV.

#### That's all. Feel free to use this code or collaborate to this repo. Thank you.
