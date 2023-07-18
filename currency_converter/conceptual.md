### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  JavaScript - used for front and backend , mainly frontend
  Python - used for backend
  Javacsript - runs in most browsers
  Python - does not run in browser interpreter needed

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.
  for (k,v) in obj.items():
  print (k,v)
  for key in obj.keys():
  print (key)
- What is a unit test?
  testing individual components of code

- What is an integration test?
  testing how components work together

- What is the role of web application framework, like Flask?
  frameworks impose rules / structure about hoe the application should look like/behave like

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  use a Url param when its the subject of the page
  Use when sorting/filtering or providing extra info about the subject

- How do you collect data from a URL placeholder parameter using Flask?
  @app.route('/user/<int:user_id>')
  def user_page(user_id):

- How do you collect data from the query string using Flask?
  request.args["]

- How do you collect data from the body of the request using Flask?
  request.data

- What is a cookie and what kinds of things are they commonly used for?
  cookies are a key-value pair stored by the client when ask by the server. The client sends the cookies to the server automatically with each request. This is so specified info can be saved even after the browser is closed.

- What is the session object in Flask?
  When we use sessions the data is stored in the browser as a cookie. The cookie used to store session data is known session cookie. However, unlike an ordinary cookie, Flask signs the session cookie making it unreadable and unmodifiable without the sectret key.

- What does Flask's `jsonify()` do?
  allows an api to respond with JSON instead of html
