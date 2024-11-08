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

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

EMPTY_DEFINITION = ""

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate Hugging Face Dataset')
    parser.add_argument('-i', '--input', help='Raw data file, i.e. the path to raw-wiktextract-data.jsonl', required=True)
    args = vars(parser.parse_args())

    with open(args["input"]) as data, open("german-wiktextract-data.jsonl", "w") as german, open("latin-wiktextract-data.jsonl", "w") as latin, open("ancient-greek-wiktextract-data.jsonl", "w") as ancient_greek:
        for line in data:
            vocabulary = json.loads(line)
            if "lang" in vocabulary:
                term = vocabulary["word"]
                definitions = [sense["glosses"][0] if "glosses" in sense else sense["raw_glosses"][0] if "raw_glosses" in sense else EMPTY_DEFINITION for sense in vocabulary["senses"]]
                for definition in definitions:
                    if definitions is not EMPTY_DEFINITION:
                        if vocabulary["lang"] == "German":
                            german.write(json.dumps({"term": term, "definition": definition}))
                            german.write("\n")
                        if vocabulary["lang"] == "Latin":
                            latin.write(json.dumps({"term": term, "definition": definition}))
                            latin.write("\n")
                        if vocabulary["lang"] == "Ancient Greek":
                            ancient_greek.write(json.dumps({"term": term, "definition": definition}))
                            ancient_greek.write("\n")
