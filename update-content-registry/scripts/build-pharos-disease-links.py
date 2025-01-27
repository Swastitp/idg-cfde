#! /usr/bin/env python3
"""
Adapted from build-appyter-gene-links.py as suggested at
https://github.com/nih-cfde/update-content-registry/README.md.
"""
#############################################################################
import argparse, os.path, sys, json, urllib.parse, logging
import pandas as pd

import cfde_common

# CV for diseases are DO IDs. Map to Pharos URLs via file.
def make_markdown(cv_id):
    return f"""
## Pharos URLs

* Pharos: [https://pharos.nih.gov/diseases/{cv_id}](https://pharos.nih.gov/diseases/{cv_id}) 
* DiseaseOntology: [https://disease-ontology.org/?id={cv_id}](https://disease-ontology.org/?id={cv_id})
"""

#############################################################################
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('termtype', help="controlled vocabulary term type - gene, disease, compound, or anatomy")
    parser.add_argument('id_list', help="file containing list of IDs to build markdown for")
    parser.add_argument('--widget-name', default="widget", help="widget name, used to set the output filename(s)")
    parser.add_argument('--output-dir', '-o', help="output directory, defaults to 'output_pieces_{termtype}")
    parser.add_argument("-v", "--verbose", default=0, action="count")
    args = parser.parse_args()

    logging.basicConfig(format='%(levelname)s:%(message)s', level=(logging.DEBUG if args.verbose>1 else logging.INFO))

    # validate term
    term = args.termtype
    if term not in cfde_common.REF_FILES:
        logging.error(f"Unknown term type '{term}'")
        sys.exit(-1)

    logging.info(f"Running with term: {term}")

    # output dir default
    output_dir = args.output_dir
    if output_dir is None:
        output_dir = f"output_pieces_{term}"
    logging.info(f"Using output dir {output_dir} for pieces.")

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # validate that ID list is contained within actual IDs in database
    ref_file = cfde_common.REF_FILES.get(term)
    if ref_file is None:
        logging.error(f"No ref file for term. Dying terribly.")
        sys.exit(-1)

    # load in ref file; ID is first column
    df = pd.read_csv(ref_file, sep='\t')
    ref_id_list = set(df.iloc[:,0].tolist())
    logging.info(f"Loaded {len(ref_id_list)} reference IDs from {ref_file}")

    # load up each ID in id_list file - is it in the ref_id_list?
    # if not, complain.
    # we could also remove them here. we don't want to output markdown
    # for them!
    id_list = set()
    with open(args.id_list, 'rt') as fp:
        for line in fp:
            line = line.strip()
            if line:
                if line not in ref_id_list:
                    logging.error(f"Requested input id {line} not found in ref_id_list")
                    logging.info(f"skipping!")
                    continue
                    #sys.exit(-1)

                id_list.add(line)

    logging.info(f"Loaded {len(id_list)} IDs from {args.id_list}")

    # Iterate over and make markdown, then save JSON + md.
    # CV for diseases are DO IDs. Map to Pharos URLs via file.
    # tcrd_diseases.tsv produced by BioClients.idg.tcrd.Client listDiseases.
    tsvfile = "data/inputs/tcrd_diseases.tsv"
    df = pd.read_csv(tsvfile, sep='\t', dtype=str)
    logging.info(f"{tsvfile} rows: {df.shape[0]}")
    for cv_id in id_list:
        md = make_markdown(cv_id)
        cfde_common.write_output_pieces(output_dir, args.widget_name, cv_id, md) # JSON for upload

#############################################################################
if __name__ == '__main__':
    sys.exit(main())
