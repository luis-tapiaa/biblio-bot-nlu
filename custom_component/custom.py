import re
from rasa.nlu.components import Component
import typing
from typing import Any, Optional, Text, Dict


if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


class GeneralSearch(Component):
    # This component serves to override previous processing
    # and trigger general search in case the message satisfies a regex
    # which would qualify it for a search query.
    provides = ["entities"]
    requires = ["entities"]
    defaults = {}
    language_list = None # this matches all languages

    def __init__(self, component_config=None):
        super().__init__(component_config)
        self.pattern = r"\s*(?P<search_key>(buscar)|(buscando)|(encontrar)|(encuentro)|(requiero)|(necesito))*\s*(?P<search_trigger>(sobre)|(de la)|(del)|(de los)|(de))\s*(?P<search_phrase>.+)"
        # This matches only those messages which start with the phrase "wyszukaj" or "szukaj"
        # (whitespace is ignored). You can add additional keywords for triggering search here
        # but this is not reccomended, as we want to avoid collisions between NLP intent recognition
        # and keyword based recognition. And the users should ideally understand this distinction,
        # And use the bot with this distinction in mind (i.e. recognize "wyszukaj" as special)
        # The regex then recognizes whatever follows as the search phrase and so marks it accordingly
        # it is case insensitive
        self.compiled = re.compile(self.pattern, flags = re.IGNORECASE)


    def train(self, training_data, cfg, **kwargs):
        pass

    def process(self, message, **kwargs):
        text = message.text
        result = self.compiled.search(text)
        if not result:
          return
        else:
          s_phrase = result.group("search_phrase")
          start, end = result.span(2)        
          sphr_entity = {
            "start": start,
            "end": end,
            "value": s_phrase,
            "entity": "search_phrase",
            "extractor": "GeneralSearch",
            "confidence": 1.0,
            "processors": []
            }
          message.set("entities", message.get("entities", []) + [sphr_entity], add_to_output=True)
        

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
