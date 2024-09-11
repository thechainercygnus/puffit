# **P**roject **F**rom **T**emplate

I've always wanted to take an example directory structure for a project structure and pipe that into an application to make it happen. So that's what this is for.

For example I would like to turn this:

```
root/
├── tasks/
│   ├── __init__.py
│   ├── task_a.py
│   └── task_b.py
├── core/
│   ├── app.py
│   ├── celery_worker.py
│   └── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

And have it turn into this:

![alt text](/docs/imgs/image.png)