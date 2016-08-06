__author__ = 'Prathmesh'

from pytagcloud import create_tag_image, create_html_data, make_tags, LAYOUT_HORIZONTAL, LAYOUTS, LAYOUT_MIX, LAYOUT_VERTICAL, LAYOUT_MOST_HORIZONTAL, LAYOUT_MOST_VERTICAL
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

class TagCloud:

    def __init__(self,docSet):
        self.docSet = docSet

    def tagCloud(self):
        texts =""
        for item in self.docSet:
            texts = texts +" " +item

        tags = make_tags(get_tag_counts(texts), maxsize=120)
        create_tag_image(tags,'filename.png', size=(2000,1000), background=(0, 0, 0, 255), layout=LAYOUT_MIX, fontname='Lobster', rectangular=True)
        # create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')

        # print(tags)
        # print(texts)
