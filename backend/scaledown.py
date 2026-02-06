def compress_docs(text: str):
    words = text.split()
    compressed = int(len(words) * 0.15)

    return {
        "original_words": len(words),
        "compressed_words": compressed,
        "summary": " ".join(words[:compressed])
    }
