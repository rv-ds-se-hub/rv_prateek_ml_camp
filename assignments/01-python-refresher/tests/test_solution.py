import pytest

from solution import Solution, TextProcessor


@pytest.fixture
def solver():
    """Provides a default Solution instance for integration tests."""
    return Solution()


# -------------------------
# TextProcessor unit tests
# -------------------------


def test_normalize_strips_and_lowercases():
    txt = "   Hello WORLD  "
    processor = TextProcessor()  # No text in constructor
    assert processor.normalize(txt) == "hello world"


def test_remove_punctuation_defaults():
    txt = "Wow! (This)—is: great?"
    processor = TextProcessor()  # No text in constructor
    # Pass text to the method instead
    cleaned = processor.remove_punctuation(txt)
    # The default punctuation set removes !, (), :, ? but not the em-dash '—'
    assert cleaned == "Wow This—is great"


def test_remove_punctuation_custom():
    txt = "a+b=c; d*e=f"
    # No text in constructor, only configuration
    proc = TextProcessor(punctuation={"+", "=", "*"})
    assert proc.remove_punctuation(txt) == "abc; def"


def test_tokenize_collapses_whitespace():
    proc = TextProcessor()
    tokens = proc.tokenize("one   two\tthree\nfour")
    assert tokens == ["one", "two", "three", "four"]


def test_remove_stop_words():
    """Tests the new stop word filtering functionality."""
    # Test with default stop words
    proc_default = TextProcessor()
    tokens = ["the", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog"]
    filtered = proc_default.remove_stop_words(tokens)
    assert filtered == ["quick", "brown", "fox", "jumps", "over", "lazy", "dog"]

    # Test with a custom stop word list
    proc_custom = TextProcessor(stop_words={"fox", "dog"})
    filtered_custom = proc_custom.remove_stop_words(tokens)
    assert filtered_custom == ["the", "quick", "brown", "jumps", "over", "a", "lazy"]


def test_count_frequencies_and_get_top_n():
    tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    proc = TextProcessor()
    counts = proc.count_frequencies(tokens)
    assert counts == {"apple": 3, "banana": 2, "cherry": 1}

    # top_n=None returns all sorted
    top_all = proc.get_top_n(counts)
    assert top_all == [("apple", 3), ("banana", 2), ("cherry", 1)]

    # top_n=2 returns only first two
    top_two = proc.get_top_n(counts, n=2)
    assert top_two == [("apple", 3), ("banana", 2)]


# -----------------------------------
# Solution.word_frequency_counter tests
# (Now reflect stop-word filtering)
# -----------------------------------


def test_simple_sentence(solver):
    text = "hello world hello"
    # No stop words, result is the same
    assert solver.word_frequency_counter(text) == [("hello", 2), ("world", 1)]


def test_case_insensitivity_and_stop_words(solver):
    text = "The Cat, the hat?"
    # "the" is a stop word and should be removed
    result = solver.word_frequency_counter(text)
    # Sorting by word alphabetically for stability when counts are equal
    assert sorted(result) == [("cat", 1), ("hat", 1)]


def test_punctuation_and_apostrophes(solver):
    text = "Isn't it amazing? Amazing, truly!"
    # "it" is a stop word. "isnt" is not (by default)
    result = solver.word_frequency_counter(text)
    assert result == [("amazing", 2), ("isnt", 1), ("truly", 1)]


def test_hyphenated_words_and_stop_words(solver):
    text = "state-of-the-art design is state of art"
    # "is" and "of" are stop words
    result = solver.word_frequency_counter(text)
    counts = dict(result)
    # "stateoftheart", "design", "state", "art" are left
    assert counts == {"stateoftheart": 1, "design": 1, "state": 1, "art": 1}


def test_numeric_tokens_and_top_n(solver):
    text = "123 456 123 test 456 456"
    # "test" is not a default stop word
    top2 = solver.word_frequency_counter(text, top_n=2)
    assert top2 == [("456", 3), ("123", 2)]


def test_whitespace_only_and_no_alphanum(solver):
    assert solver.word_frequency_counter("     ") == []
    assert solver.word_frequency_counter(".,;!?'-") == []


def test_non_string_input_raises_type_error(solver):
    with pytest.raises(TypeError):
        solver.word_frequency_counter(12345)
