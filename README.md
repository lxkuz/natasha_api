# Setup

1. docker build -t natasha-api .
2. docker run -it --rm -p 3000:80 natasha-api


# Usage

## pluck_names
Request:
```
POST /pluck_names

Body (JSON):
{"text": "Some text here..."}
```
Response JSON:
```
["Name 1", "Name 2"]
```

## pluck_names_batch
Request:
```
POST /pluck_names_batch

Body (JSON):
{"text_batch": ['"Some text here...", ...]}
```
Response JSON:
```
[
  ["Name 1", "Name 2"],
  ...
]
```