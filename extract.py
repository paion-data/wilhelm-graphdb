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

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate Hugging Face Dataset')
    parser.add_argument('-i', '--input', help='Raw data file, i.e. the path to raw-wiktextract-data.jsonl', required=True)
    parser.add_argument('-o', '--output', help='Path to the output JSON. Default to "wiktextract-data.json" in current directory', required=False)
    args = vars(parser.parse_args())

    with open(args["input"]) as data, open(args["output"] if args["output"] else "wiktextract-data.json", "w") as output:
        output.write("[\n")

        for line in data:
            vocabulary = json.loads(line)
            if "lang" in vocabulary and vocabulary["lang"] == "German":
                term = vocabulary["word"]
                definitions = [sense["glosses"][0] if "glosses" in sense else sense["raw_glosses"][0] if "raw_glosses" in sense else [] for sense in vocabulary["senses"]]
                for definition in definitions:
                    output.write(json.dumps({"term": term, "definition": definition}))
                    output.write(",\n")
        output.write("]\n")