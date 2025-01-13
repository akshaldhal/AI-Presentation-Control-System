from transformers import pipeline

def __summarize(text: str, max_length: int = 150) -> str:
  summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
  summarized_text = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
  return summarized_text[0]["summary_text"]

def __summarize_slides(slides: List[str]) -> List[str]:
  return [__summarize(slide) for slide in slides]
