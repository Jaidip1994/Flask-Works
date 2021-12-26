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
