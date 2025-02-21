import spacy
# from job_description import job_description
from job_description2 import job_description2
from cv import cv

nlp = spacy.load('en_core_web_md')

doc = nlp(job_description2)

# print(doc.text)
# print([token for token in doc if not token.is_stop and not token.is_punct])
#
# for entity in doc.ents:
#     print(entity.text, entity.label_)

doc1 = nlp(cv)
print([token for token in doc1 if not token.is_stop and not token.is_punct])
for entity in doc1.ents:
    print(entity.text, entity.label_)
