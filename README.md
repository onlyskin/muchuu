# muchuu - 夢中

A webapp for realising your mid term goals. Add steps which will get you towards your dreams. Each step should be small enough that you would be prepared to do it right now and it would take no more than five minutes.

Use the app to get a random step whenever you feel like working towards your dreams. If you aren't prepared to do the step, you should follow the app's flow and change the step into something smaller which you would be prepared to do now.

`muchuu` is hosted on heroku with a postgres database. Only a single user is currently supported, with password set in the heroku environment variables.

### build
```./build.sh```

### test
```./test.sh```

### deploy

```git push heroku master```

Required environment variables are `SECRET_KEY`, `MUCHUU_DATABASE_URL`, and `MUCHUU_PASSWORD`.
