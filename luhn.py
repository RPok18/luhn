import re
from collections import Counter

def luhn_summarization(text, num_sentences=3):
    # Step 1: Preprocess text
    sentences = re.split(r'(?<=[.!?]) +', text)
    words = re.findall(r'\w+', text.lower())
    
    # Step 2: Word frequency analysis
    word_freq = Counter(words)
    
    # Step 3: Calculate sentence significance
    sentence_scores = {}
    for sentence in sentences:
        score = sum(word_freq[word] for word in re.findall(r'\w+', sentence.lower()))
        sentence_scores[sentence] = score
    
    # Step 4: Select key sentences
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    # Step 5: Compile summary
    summary = ' '.join(summarized_sentences)
    return summary

# Load content from the provided file (assuming it's saved as 'test_text.txt')
with open('test_text.txt', 'r') as file:
    blog_post_content = file.read()

# Generate summary
summary_output = luhn_summarization(blog_post_content)

# Display summary
print("Summary Output:")
print(summary_output)