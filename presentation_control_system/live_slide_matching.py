from typing import List
import torch
from sentence_transformers import util
from .embedding import generate_embeddings

def find_closest_slide(live_text: str, slide_embeddings: torch.Tensor) -> int:
  live_embedding = embedding_model.encode(live_text, convert_to_tensor=True)
  cosine_scores = util.cos_sim(live_embedding, slide_embeddings)
  best_match_idx = torch.argmax(cosine_scores).item()
  return best_match_idx

if __name__ == "__main__":
  presentation_slides = [ ... ]  # Add slides here
  slide_embeddings = generate_embeddings(presentation_slides)

  live_input = "Our proprietary EcoTech Fusion™ reduces production emissions and makes building materials cheaper."
  best_slide_idx = find_closest_slide(live_input, slide_embeddings)

  print(f"\nLive Input: {live_input}")
  print(f"Closest Slide: Slide {best_slide_idx + 1}")
