
echo "BUILD START"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
python3 -m spacy download en_core_web_md
python3 -m spacy download en_core_web_lg
python3 -m spacy download en_core_web_trf
echo "BUILD END"