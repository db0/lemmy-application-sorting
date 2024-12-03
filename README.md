# lemmy-application-sorting
Sorts lemmy.dbzer0.com application answers into categories 

# DB extraction

```sql
\COPY (SELECT json_build_object('answer', answer)::text FROM registration_application) TO '/tmp/registration_answers.json';
```

with username

```sql
\COPY (
    SELECT json_build_object(
        'answer', registration_application.answer,
        'username', person.name
    )::text
    FROM registration_application
    JOIN local_user ON registration_application.local_user_id = local_user.id
    JOIN person ON local_user.person_id = person.id
    WHERE local_user.accepted_application = true
    ORDER BY registration_application.published ASC
) TO '/tmp/registration_answers.json';
```


early birds

```sql
\COPY (
    SELECT DISTINCT json_build_object(
        'username', person.name
    )::text
    FROM person
    JOIN local_user ON person.id = local_user.person_id
    LEFT JOIN registration_application ON local_user.id = registration_application.local_user_id
    WHERE registration_application.id IS NULL
) TO '/tmp/registration_answers_early_birds.json';
```

