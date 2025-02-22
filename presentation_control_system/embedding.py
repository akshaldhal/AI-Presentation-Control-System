from sentence_transformers import SentenceTransformer
import .summarize

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(slides: List[str]) -> torch.Tensor:
  slide_summaries = __summarize_slides(slides)
  return embedding_model.encode(slide_summaries, convert_to_tensor=True)
