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

app = FastAPI()

@app.get("/my-first-api")
def hello(text: str):
  print(text)
  emb = NewsEmbedding()
  ner_tagger = NewsNERTagger(emb)
  doc = Doc(text)
  doc.tag_ner(ner_tagger)
  print(doc.ner.print())
  return {"success"}
