Wilhelm Graph Database
======================

[![Neo4J DB version badge]][Neo4J Docker version]
[![Apache License Badge]][Apache License, Version 2.0]

__wilhelm-graphdb__ is a Docker image that hosts Wiktionary languge data in Neo4J graph database. It is part of the
efforts that
[scales project Wilhelm](https://github.com/QubitPi/wilhelm?tab=readme-ov-file#why-do-i-decide-to-scale-project-wilhelm)

> [!NOTE]
>
> wilhelm-graphdb is under active development and will start serving alone with
> [paion-data/aristotle](https://aristotle-ws.com/)

Development
-----------

### Updating the Datasource

We use Wiktionary (English) as the vocabulary source. Thanks to the awesome works by
[tatuylonen](https://github.com/tatuylonen/wiktextract), the source data is already
[in JSON format](https://kaikki.org/dictionary/rawdata.html). The source data is going to be updated regularly so to get
the latest data, simply download the __raw Wiktextract data (JSONL, one object per line)__

### Start a Local Neo4J Database

```console
docker run \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --env=NEO4J_AUTH=none \
    --env=NEO4J_ACCEPT_LICENSE_AGREEMENT=yes neo4j:5.24-enterprise
```

To manually

```console
python3 -m virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

```console
pip3 uninstall wilhelm_python_sdk
pip3 install --upgrade --force-reinstall wilhelm-python-sdk
```

### Load Basic Data

```console
python3 load-basic.py -i path/to/raw-wiktextract-data.jsonl
```

> [!WARNING]
>
> The loading takes several hours, please be patient


### Infer More Links

```console
python3 extract.py -i path/to/raw-wiktextract-data.jsonl -o path/to/output.json
```

...more TBA

License
-------

The use and distribution terms for [wilhelm-vocabulary]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0

[Neo4J DB version badge]: https://img.shields.io/badge/Neo4J-5.24--enterprise-4581C3.svg?style=for-the-badge&logo=neo4j&logoColor=white
[Neo4J Docker version]: https://hub.docker.com/_/neo4j/tags?name=5.24-enterprise
