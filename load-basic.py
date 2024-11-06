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
import logging
import json
from wilhelm_python_sdk.database_clients import get_database_client
from wilhelm_python_sdk.database_clients import get_node_label_attribute_key
from wilhelm_python_sdk.vocabulary_parser import GERMAN

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate JSON data')
    parser.add_argument('-i', '--input', help='Raw data file, i.e. the path to raw-wiktextract-data.jsonl', required=True)
    args = vars(parser.parse_args())

    label_key = get_node_label_attribute_key()

    with get_database_client() as database_client, open(args["input"]) as data:
        for line in data:
            vocabulary = json.loads(line)
            # logging.info(f"Loading vocabulary: {vocabulary}")
            if "lang" in vocabulary and vocabulary["lang"] == "German":
                term = vocabulary["word"]
                database_client.save_a_node_with_attributes("Term", {label_key: term, "language": GERMAN})

                definitions = [sense["glosses"][0] if "glosses" in sense else sense["raw_glosses"][0] if "raw_glosses" in sense else [] for sense in vocabulary["senses"]]
                for definition in definitions:
                    database_client.save_a_node_with_attributes("Definition", {label_key: definition})

                    database_client.save_a_link_with_attributes(
                        language=GERMAN,
                        source_label=term,
                        target_label=definition,
                        attributes={label_key: "definition"}
                    )
