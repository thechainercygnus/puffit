# PuffIt

![Python 3.9](./docs/badges/python39.svg) ![Python 3.10](./docs/badges/python310.svg) ![Python 3.11](./docs/badges/python311.svg) ![Python 3.12](./docs/badges/python312.svg) ![Coverage](./docs/badges/coverage.svg)



I've always wanted to take an example directory structure for a project structure and pipe that into an application to make it happen. So that's what this is for.

For example I would like to take this:

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

## Features

Supports a variety of layout syntaxes.

## Installation

pipx install puffit

## Usage

Create your `template.pft` file containing the textual layout for the project. Then just run `puffit template.pft` where you'd like to create your new project directory. Check out `templates/` for example `.pft` files.

## Contributing

Coming Soon

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Roadmap

* Integreate CI/CD release automation
* Improve error handling
* Improve documentation
* Implement logging


Tests Updated: 1/1/1970


Coverage Updated: 1/1/1970