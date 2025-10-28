# Project Chitti - Code Review & Improvement Recommendations

**Review Date:** October 17, 2025  
**Reviewer:** AI Code Review Assistant

---

## 🔴 **Critical Issues**

### 1. **State Management Bug in `app.py`**
**Location:** Lines 95-98  
**Issue:** The chunking and embedding happen **inside** the file upload loop but **outside** any session state, so they get overwritten on each file. If multiple files are uploaded, only the last file's data is retained.

**Current Code:**
```python
# Chunking and embedding text from pdf
chunks = chunk_text(text=text)
pdf_embeddings = get_embeddings(chunks=chunks)
```

**Recommended Fix:**
```python
if "file_data" not in st.session_state:
    st.session_state.file_data = {}

st.session_state.file_data[uploaded_file.name] = {
    "chunks": chunks,
    "embeddings": pdf_embeddings,
    "text": text
}
```

---

### 2. **Variable Scope Error in `app.py`**
**Location:** Lines 121-128  
**Issue:** `prompt_embeddings`, `chunks`, and `pdf_embeddings` may not exist if no file has been uploaded, causing a runtime crash.

**Recommended Fix:**
```python
if prompt := st.chat_input("Ask Chitti"):
    # Check if files have been uploaded
    if "file_data" not in st.session_state or not st.session_state.file_data:
        st.error("Please upload a PDF file first!")
        st.stop()
    
    # Continue with embedding logic...
```

---

### 3. **Memory Leak in Chat History**
**Location:** Line 131  
**Issue:** `formatted_chunks_str += ...` keeps appending without reset, so each new query contains ALL previous chunks, growing exponentially.

**Current Code:**
```python
formatted_chunks_str = ""  # At top of file
# ...
for idx, chunk in enumerate(relevant_chunks):
    formatted_chunks_str += f"CHUNK #{idx+1}: \n{chunk} \n\n"
```

**Recommended Fix:**
```python
# Inside the prompt block:
if prompt := st.chat_input("Ask Chitti"):
    formatted_chunks_str = ""  # Reset for each new query
    # ... rest of code
```

---

### 4. **Duplicate Session State Initialization**
**Location:** Lines 103-108  
**Issue:** `st.session_state.messages` is initialized twice, which is redundant.

**Current Code:**
```python
if "messages" not in st.session_state:
    st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []
```

**Recommended Fix:** Remove the duplicate initialization.

---

## 🟡 **Significant Issues**

### 5. **Inefficient Cosine Similarity Implementation**
**Location:** Lines 159-182 in `chunking_embedding.py`  
**Issue:** Manual implementation of cosine similarity is slow and inefficient, especially when working with PyTorch tensors.

**Current Code:**
```python
def cosine_sim(a, b):
    # Manual calculation with loops
    dot_value = 0
    magnitude_a = 0
    magnitude_b = 0
    for i, j in zip(a, b):
        dot_value += i * j
        magnitude_a += i**2
        magnitude_b += j**2
    return dot_value / (magnitude_a**0.5 * magnitude_b**0.5)
```

**Recommended Fix:**
```python
import torch.nn.functional as F

def cosine_sim(a, b):
    return F.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0)).item()

# Or even better for batch operations:
def batch_cosine_sim(query_embedding, doc_embeddings):
    return F.cosine_similarity(query_embedding.unsqueeze(0), doc_embeddings)
```

---

### 6. **Missing Error Handling**
**Issues:**
- No handling for when Ollama isn't running (lines 11-18 in `llm_utils.py`)
- No validation for empty PDF uploads
- No handling for PDFs with no extractable text
- No timeout configuration for LLM requests

**Recommended Fix for `llm_utils.py`:**
```python
import requests
from requests.exceptions import RequestException, Timeout

def llm_convo(messages, model: str = "gemma3:1b", timeout: int = 30):
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": False
            },
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    except Timeout:
        raise Exception("Request timed out. Please check if Ollama is running.")
    except RequestException as e:
        raise Exception(f"Failed to connect to Ollama: {str(e)}")
    except KeyError:
        raise Exception("Unexpected response format from Ollama")
```

---

### 7. **Hard-coded Ollama Model**
**Location:** Line 3 in `llm_utils.py`  
**Issue:** Model is hardcoded as `"gemma3:1b"`. Should be configurable via environment variable or UI.

**Recommended Fix:**
```python
import os

def llm_convo(messages, model: str = None):
    if model is None:
        model = os.getenv("OLLAMA_MODEL", "gemma3:1b")
    # ... rest of code
```

---

### 8. **Page Slider Hard-coded Maximum**
**Location:** Line 76 in `app.py`  
**Issue:** `max_value=10` assumes all PDFs have at most 10 pages, which will break for longer documents.

**Current Code:**
```python
page_idx = st.slider("Choose page", min_value=1, max_value=10, value=1)
```

**Recommended Fix:**
```python
doc = pymupdf.open(stream=pdf_bytes, filetype='pdf')
page_count = len(doc)
page_idx = st.slider("Choose page", min_value=1, max_value=page_count, value=1)
```

---

### 9. **Unused Imports and Functions**
**Issues:**
- `pdf_utils.py` has multiple unused extraction functions (pdfminer functions)
- `metrics.py` is defined but never used in the app
- Unused imports like `tiktoken`, `numpy` in `chunking_embedding.py`
- `base64` imported but never used in `app.py`

**Recommendation:** Remove unused code or document why it's kept (e.g., for future features or analysis).

---