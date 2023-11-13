# Language Trainer

Simple service with help you learn another language.

## Futures

- Words (add words for learning)
- Irregular Verbs
- Passive voice
- Conditions
- Idioms
- Read text (read random text)

## Configuration
create .env file in enlearn directory
```
SECRET_KEY=<generate_secret_key>
DB_NAME=<db_name>
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_HOST=<db_host>
DB_PORT=<db_port>
```

## Deployment
### Build
```
docker build -t 10.0.0.200:5000/enlearn:0.0.1 .
```
### Push
```
docker push 10.0.0.200:5000/enlearn:0.0.1
```
### Deploy
```
kubectl -n dev apply -f .
```