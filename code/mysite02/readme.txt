introducce to connect database in django

1.setup database:
  first, you should choose database type: SQLite by Default, postgresql, mysql or oracle. 
  attention: if you wish to use another database, you muse change the following key in 'default' item in site/setting.py file.setting such as user, password,and host.

  second, in order to active your app, you should change item/key 'install_apps' in site/settings.py.

  third, running command 'python manage.py migrate' to apply it, as a result, it will create the tables.

2.create models for database.
  first, edit file model.py on your app file, create your own class, they are all inherite models.Model, and use models.CharField() or models.DateTimeField() or models.ForeignKey() or models.IntegerField to define various field.
  second, add 'polls.apps.PollsConfig' which point to exact file to install_apps items. next, activating models, input this: python manage.py makemigrations apps.
  attentions:model cache files are located in app/migration/ and named by 0001* and __cache__ , once you failed to migrate models, you should try to delete that two file, then run again, but it will not affect your former data.

### using above skills, you can produce a database ###

below, i want to say something about interactive with database
1. python manage.py shell, to get into interactive mode
2. class method:
       def __str__(self):
            return self.field.
       def if_was_xx(self):
            return self.field>xx
      
    
3. field.object.all()
   field.object.save()
   field.object.get(pk)
   field.object.get(id)
   field.object.filter(field_text__startwith=xx)
   field.objects.get(field=xx)
   field.choice_set...
   
4. spacial:
   sqllite means one to mutiple, one to one, multiple to multiple.
3. field.object.all()
   field.object.save()
   field.object.get(pk)
   field.object.get(id)
   field.object.filter(field_text__startwith=xx)
   field.objects.get(field=xx)
   field.choice_set...
   
4. spacial:
   sqllite means one to mutiple, one to one, multiple to multiple.
3. field.object.all()
   field.object.save()
   field.object.get(pk)
   field.object.get(id)
   field.object.filter(field_text__startwith=xx)
   field.objects.get(field=xx)
   field.choice_set...
   
4. spacial:
   sqllite means one to mutiple, one to one, multiple to multiple. so i can get ojbect by foreignkey from otherobject in shell. that's amazing. 

### 
using amdin interface to manage app.
1.create superuser
comm: python manage.py createsuperuser

then show in web.

2.add our own app into admin interface.
edit file: app/amdin.py
    from django.contrib import admin
    from .models import Question
    
    admin.site.register(Question)

now, i can manage register_object in admin interface.

3.pay attention to different type and field.


     
###
using url and namespace to deal with multiple url mapping, such as, from app1 to app2, can produce a link like {% url 'app2:detail' %}, it accomplish overarea now.


something about generic views.
like views and models in java.
then you can use it in page.