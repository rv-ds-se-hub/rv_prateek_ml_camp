from typing import Iterable


class TextProcessor:
    """A configurable processor for cleaning and analyzing text."""

    def __init__(
        self,
        punctuation: Iterable[str] | None = None,
        stop_words: Iterable[str] | None = None,
    ):
        """
        Initializes the processor with specific configurations.

        Args:
            punctuation: An iterable of punctuation characters to remove. Defaults to a standard set if None.
            stop_words: An iterable of stop words to remove. Defaults to few English words  .
        """
        # Default punctuation set if none provided
        default_punct = ".,?!;:\"'()[]-"
        self.punctuation = (
            set(punctuation) if punctuation is not None else set(default_punct)
        )

        # Default stop words if none provide
        default_sw = {"a", "an", "the", "and", "but", "if", "or"}
        self.stop_words = set(stop_words) if stop_words is not None else default_sw

    def normalize(self, text: str) -> str:
        """Converts text to lowercase and strips leading/trailing whitespace."""
        # TODO: implement normalization
        raise NotImplementedError

    def remove_punctuation(self, text: str) -> str:
        """Strip all characters in self.punctuation from the text."""
        # TODO: implement punctuation removal
        raise NotImplementedError

    def tokenize(self, text: str) -> list[str]:
        """Split text into tokens on whitespace, collapsing multiple spaces."""
        # TODO: implement tokenization
        # Hint, there could be not-so-evident edge cases here
        raise NotImplementedError

    def remove_stop_words(self, tokens: list[str]) -> list[str]:
        """Removes all tokens that are in self.stop_words."""
        # TODO: implement tokenization
        raise NotImplementedError

    def count_frequencies(self, tokens: list[str]) -> dict[str, int]:
        """Count how often each token appears."""
        # TODO: implement frequency counting
        raise NotImplementedError

    def get_top_n(
        self, counts: dict[str, int], n: int | None = None
    ) -> list[tuple[str, int]]:
        """
        Return a list of (word, count) sorted by count descending.
        If n is provided, return only the top n items.
        """
        # TODO: implement top-n extraction
        raise NotImplementedError


class Solution:
    def word_frequency_counter(
        self, text: str, top_n: int | None = None
    ) -> list[tuple[str, int]]:
        """
        Main entry point.
        This method chains together the steps:
            1. Normalization
            2. Punctuation Removal
            3. Tokenization
            4. Stop-Word Filtering
            5. Frequency Counting
            6. Top N Extraction
        """
        # 1. Instantiate the configurable processor
        processor = TextProcessor()

        # 2. Chain the methods in a clear pipeline
        normalized = processor.normalize(text)
        no_punctuation = processor.remove_punctuation(normalized)
        tokens = processor.tokenize(no_punctuation)
        filtered_tokens = processor.remove_stop_words(tokens)
        counts = processor.count_frequencies(filtered_tokens)

        return processor.get_top_n(counts, top_n)
