Wilhelm GraphDB - Visualizing Wiktionary in Graph Database
==========================================================

![Python Version Badge]
[![Neo4J DB version badge]][Neo4J Docker version]
[![Apache License Badge]][Apache License, Version 2.0]

__wilhelm-graphdb__ is a Docker image that hosts Wiktionary language data in Neo4J graph database. It is part of the
efforts that
[scales project Wilhelm](https://github.com/QubitPi/wilhelm?tab=readme-ov-file#why-do-i-decide-to-scale-project-wilhelm)

Currently, only __German__ language is loaded into the image.

Development
-----------

Although [the original Wiktionary dump](https://dumps.wikimedia.org/) is available, parsing it  from scratch involves
rather complicated process. We would probably do it in the future. At present, however, we would simply take the awesome
works by [tatuylonen](https://github.com/tatuylonen/wiktextract) which has already processed it and presented it in
[in JSON format](https://kaikki.org/dictionary/rawdata.html). wilhelm-graphdb takes the
__raw Wiktextract data (JSONL, one object per line)__ option.

### Creating Docker Image

Prerequisite:

- Docker
- Python 3.10
- [wait-on](https://www.npmjs.com/package/wait-on)

```console
git clone git@github.com:QubitPi/wilhelm-graphdb.git
cd wilhelm-graphdb
```

Creating the following environment variables:

- __DOCKERHUB_USERNAME__: The value for the `-u` argument as used in the [Docker login command]
- __DOCKERHUB_TOKEN__: The value for the `-p` argument as used in the [Docker login command]

> [!CAUTION]
>
> The script would overwrite the following environment variables with the specified values if already defined locally:
> 
> __NEO4J_URI__: `neo4j://localhost:7687`
> __NEO4J_USERNAME__: `neo4j`
> 
> The loading takes several hours, please be patient

```console
./docker.sh
```

The log can be found at `./load.log`

### Troubleshooting

#### Reinstalling `wilhelm_python_sdk`

```console
pip3 uninstall wilhelm_python_sdk
pip3 install --upgrade --force-reinstall wilhelm-python-sdk
```

License
-------

The use and distribution terms for [wilhelm-vocabulary]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0

[Docker login command]: https://docker.qubitpi.org/reference/cli/docker/login/#options

[Neo4J DB version badge]: https://img.shields.io/badge/Neo4J-5.24--enterprise-4581C3.svg?style=for-the-badge&logo=neo4j&logoColor=white
[Neo4J Docker version]: https://hub.docker.com/_/neo4j/tags?name=5.24-enterprise

[Python Version Badge]: https://img.shields.io/badge/Python-3.10-FFD845?labelColor=498ABC&style=for-the-badge&logo=python&logoColor=white
