# Getting start

## step1: clone project

#### - using git

```base
git clone https://github.com/PhirunOem/manufacture.git
```

And then cd manufacture

## step2 : set up project enviroment

#### - using python

```base
python -m venv myenv
```

#### - activate enviroment for macOS and Linux

```base
source myenv/bin/activate
```

#### - for window

```base
myenv\Scripts\activate
```

## step3: install requirements

```base
pip install -r ./requirements.txt
```

## step4: run project:

#### - using python

```base
python .\manage.py runserver
```

#### - using py

```base
py .\manage.py runserver
```

when success go to => http://127.0.0.1:8000/ <br/>
<b>Note : </b> if you have problem with installation , try to run =>

```base
 python -m pip install --upgrade pip
```

# Documents:

<b>Official document : </b>https://www.djangoproject.com/start/ <br/>
-> Generic class in django : https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/ <br/>
-> User authentication and user permission in django: https://docs.djangoproject.com/en/5.0/topics/auth/default/#user-objects <br/>
-> Create django enviroment : https://www.freecodecamp.org/news/how-to-set-up-a-django-development-environment/
