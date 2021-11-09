Continuation from the last update

*STEPS TO BUILDING A RESTAPI*

  * Setup Django
  * Create a model into the DB that Django ORM will manage
  * Setup the Django REST Framework
  * Serialize the Model
  * Create the URI endpoints to view the serialized data
  

Some we created a Django project and named it cfeapi, then an app called updates. Both folders are in `/src`

Next, we created a class Update in our models and declared several instances, also created a func that will be called whenever we want to update our image instance.

We also pip install pillow since we are using an ImageField.
