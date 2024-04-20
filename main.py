from fastapi import FastAPI
from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,

    Doc
)
from pydantic import BaseModel
from typing import List

class PluckNamesInput(BaseModel):
    text: str

class PluckNamesBatchInput(BaseModel):
    text_batch: List[str]

app = FastAPI()

@app.post("/pluck_names")
async def pluck_names(input: PluckNamesInput):
  emb = NewsEmbedding()
  segmenter = Segmenter()
  ner_tagger = NewsNERTagger(emb)
  doc = Doc(input.text)
  doc.segment(segmenter)
  doc.tag_ner(ner_tagger)
  return extract_names(doc.spans)

@app.post("/pluck_names_batch")
async def pluck_names_batch(input: PluckNamesBatchInput):
  emb = NewsEmbedding()
  segmenter = Segmenter()
  ner_tagger = NewsNERTagger(emb)
  batch = []
  for text in input.text_batch:
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_ner(ner_tagger)
    batch.append(extract_names(doc.spans))
  return batch

def extract_names(spans):
    names = []
    for span in spans:
        if span.type == 'PER':  # Filtering condition
            names.append(span.text)
    return names
