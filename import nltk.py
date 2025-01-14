import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssn.create_default_https_context = __create_unverified_https_context

nltk.download()