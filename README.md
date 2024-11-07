---
license: apache-2.0
pretty_name: Wiktionary in JSON
language:
  - en
configs:
  - config_name: languages
    data_files:
      - split: German
        path: wiktextract-data.jsonl
---

Wilhelm GraphDB - Visualizing Wiktionary in Graph Database
==========================================================

![Python Version Badge]
[![Neo4J DB version badge]][Neo4J Docker version]
[![GitHub workflow status badge][GitHub workflow status badge]][GitHub workflow status URL]
[![Hugging Face sync status badge]][Hugging Face sync status URL]
[![Hugging Face dataset badge]][Hugging Face dataset URL]
[![Apache License Badge]][Apache License, Version 2.0]

__wilhelm-graphdb__ is a Docker image that hosts Wiktionary language data in Neo4J graph database. It is part of the
efforts that
[scales project Wilhelm](https://github.com/QubitPi/wilhelm?tab=readme-ov-file#why-do-i-decide-to-scale-project-wilhelm)

Currently, only __German__ language is loaded into the image.

🤗 Hugging Face Datasets
------------------------

If a graph database is not exactly what one need the data to be stored, the Wiktionary language data is also available
on 🤗 [Hugging Face Datasets][Hugging Face dataset URL].

```python
from datasets import load_dataset
dataset = load_dataset("QubitPi/wilhelm-graphdb", split="German")
```

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
> - __NEO4J_URI__: `neo4j://localhost:7687`
> - __NEO4J_USERNAME__: `neo4j`
>
> The loading takes several hours, please be patient

```console
./docker.sh
```

- The loading log can be found at `./load.log`
- The database UI can now be accessed at http://localhost:7474 which shows how much data has been loaded

### Troubleshooting

#### Reinstalling `wilhelm_python_sdk`

```console
pip3 uninstall wilhelm_python_sdk
pip3 install --upgrade --force-reinstall wilhelm-python-sdk
```

License
-------

The use and distribution terms for [wilhelm-graphdb]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0

[Docker login command]: https://docs.docker.com/reference/cli/docker/login/#options

[GitHub workflow status badge]: https://img.shields.io/github/actions/workflow/status/QubitPi/wilhelm-graphdb/ci-cd.yaml?branch=master&style=for-the-badge&logo=github&logoColor=white&label=Database%20Loading
[GitHub workflow status URL]: https://github.com/QubitPi/wilhelm-graphdb/actions/workflows/ci-cd.yaml

[Hugging Face dataset badge]: https://img.shields.io/badge/Hugging%20Face%20Dataset-wilhelm--graphdb-FFD21E?style=for-the-badge&logo=huggingface&logoColor=white
[Hugging Face dataset URL]: https://huggingface.co/datasets/QubitPi/wilhelm-graphdb

[Hugging Face sync status badge]: https://img.shields.io/github/actions/workflow/status/QubitPi/wilhelm-graphdb/ci-cd.yaml?branch=master&style=for-the-badge&logo=github&logoColor=white&label=Hugging%20Face%20Sync%20Up
[Hugging Face sync status URL]: https://github.com/QubitPi/wilhelm-graphdb/actions/workflows/ci-cd.yaml

[Neo4J DB version badge]: https://img.shields.io/badge/Neo4J-5.24--enterprise-4581C3.svg?style=for-the-badge&logo=neo4j&logoColor=white
[Neo4J Docker version]: https://hub.docker.com/_/neo4j/tags?name=5.24-enterprise

[Python Version Badge]: https://img.shields.io/badge/Python-3.10-FFD845?labelColor=498ABC&style=for-the-badge&logo=python&logoColor=white
