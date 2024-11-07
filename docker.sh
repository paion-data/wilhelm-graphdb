#!/bin/bash
set -x
set -e

# Copyright Jiaqi Liu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

export NEO4J_URI=neo4j://localhost:7687
export NEO4J_USERNAME=neo4j

wget https://kaikki.org/dictionary/raw-wiktextract-data.jsonl

docker run \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --env=NEO4J_AUTH=none \
    --env=NEO4J_ACCEPT_LICENSE_AGREEMENT=yes \
    --name neo4j-loader \
    neo4j:5.24-enterprise &

python3 -m virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

wait-on http://localhost:7474

python3 load-basic.py -i ./raw-wiktextract-data.jsonl > load.log

docker cp neo4j-loader:/data .
docker build -t jack20191124/wilhelm-graphdb:neo4j .

docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD
docker push jack20191124/wilhelm-graphdb:neo4j
