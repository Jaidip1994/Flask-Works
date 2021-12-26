- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask Minimal App](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- [Starter Template](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [Python SQLAchemy Config Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/)

---
- How to get all the Dependencies as a Requirement.txt

```python
python -m pip freeze > requirements.txt
```

- How to create tables mentioned in app.py ( or the Data model)
As mentioned [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application)

```python
from app import db
db.create_all()
```

- How to query object, like mentioned [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application)

```python
# To Fetch all the record
Todo.query.all()

# Fetch record based on Filter Condition
Todo.query.filter_by(sno=1).first()
```

- How the Apps looks like
![image](https://user-images.githubusercontent.com/11685096/147420308-517a0308-b1cc-44bc-adcc-da09f1201e92.png)

- Currently Application Database is postgres
- Install the dependencies using the [Requirements File](https://github.com/Jaidip1994/Flask-Works/blob/main/Python%20Flask%20Web%20Development%20Tutorial-Harry/requirements.txt)
```python
pip install -r requirements.txt
```
- Start the application, using the below command
```python
python app.py
```
