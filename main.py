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

class Item(BaseModel):
    text: str

app = FastAPI()

@app.post("/pluck_names")
async def pluck_names(item: Item):
  emb = NewsEmbedding()
  segmenter = Segmenter()
  ner_tagger = NewsNERTagger(emb)
  doc = Doc(item.text)
  doc.segment(segmenter)
  doc.tag_ner(ner_tagger)
  return extract_names(doc.spans)

def extract_names(spans):
    names = []
    for span in spans:
        if span.type == 'PER':  # Filtering condition
            names.append(span.text)
    return names
