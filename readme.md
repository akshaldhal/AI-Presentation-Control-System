# AI-Based Presentation Control System

This project demonstrates an AI-powered system that automatically navigates presentation slides based on live speech input. By leveraging fast embedding models and NLP techniques, the system identifies the most relevant slide based on the speaker's live speech.

## Project Overview

The AI-Based Presentation Control System automatically advances to the correct slide in a presentation based on the spoken content. The system utilizes the following technologies:

- **Transformers:** For text summarization and semantic analysis
- **SentenceTransformers:** To generate embeddings for semantic search  
- **PyTorch:** For embedding generation and similarity matching
- **HuggingFace models:** For natural language processing tasks like summarization and text generation

The main components of the system are:

1. **Text Summarization:** Each slide is summarized for easier matching with live speech
2. **Embedding Generation:** Slide summaries and live speech are converted into vector embeddings
3. **Slide Matching:** Cosine similarity is used to match live speech with the closest slide

## Installation

### Requirements

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### Dependencies

- torch
- sentence-transformers
- transformers
- numpy
- pandas
- scikit-learn
- csv
- typing

## Files

- **presentation_control_system/**: Contains the core logic and functions for summarizing slides, generating embeddings, and finding the best matching slide for live input
- **tests/presentation_tests.csv**: Generated test cases for business ideas, presentation slides, and narration
- **generate_test_cases.py**: A script for generating synthetic business presentation test data

## Usage

Run the system with the following command:

```bash
python presentation_control_system/live_slide_matching.py
```

This will process the presentation slides and perform a semantic match for an example live input text.

## How It Works

### Slide Summarization

Each presentation slide is processed using the `facebook/bart-large-cnn` model for summarization. This helps in reducing the size of the text while preserving key points.

### Embedding Generation

The summarized slides are converted into embeddings using the `all-MiniLM-L6-v2` model from SentenceTransformers. These embeddings represent the semantic content of each slide.

### Live Speech Matching

When live speech is input (e.g., a spoken sentence), it's converted into an embedding. Cosine similarity is used to compare this live speech embedding against the slide embeddings, determining which slide is most relevant.

### Example

```python
live_input = "Our proprietary EcoTech Fusion™ reduces production emissions and makes building materials cheaper."
best_slide_idx = find_closest_slide(live_input, slide_embeddings)
print(f"\nLive Input: {live_input}")
print(f"Closest Slide: Slide {best_slide_idx + 1}")
```

## Testing

Synthetic test data for business ideas, presentation slides, and narrations are generated using a GPT-based model. The test cases are saved in `presentation_tests.csv` and can be used for further evaluation.

### Example Test Case Format:

```csv
business_idea,business_name,slides,narrator,index
Innovative idea for green tech,EcoTech Solutions,Overview: ...,The following slide explains...,1
```

## Future Improvements

- Enhance slide matching accuracy by training a custom model for domain-specific presentations
- Implement real-time speech recognition to replace manual input
- Extend the system for automatic slide creation and narration generation for fully autonomous presentations
