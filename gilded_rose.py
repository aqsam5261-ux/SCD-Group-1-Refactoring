AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
MAX_QUALITY = 50
MIN_QUALITY = 0
BACKSTAGE_DOUBLE_RATE_BELOW = 11
BACKSTAGE_TRIPLE_RATE_BELOW = 6


class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            handler = self._get_item_handler(item)
            handler(item)

    def _get_item_handler(self, item):
        if item.name == SULFURAS:
            return self._update_sulfuras
        if item.name == AGED_BRIE:
            return self._update_aged_brie
        if item.name == BACKSTAGE_PASSES:
            return self._update_backstage_pass
        return self._update_normal_item

    def _update_sulfuras(self, item):
        pass

    def _update_aged_brie(self, item):
        self._increase_quality(item)
        self._decrement_sell_in(item)
        if self._is_expired(item):
            self._increase_quality(item)

    def _update_backstage_pass(self, item):
        self._increase_quality(item)
        if item.sell_in < BACKSTAGE_DOUBLE_RATE_BELOW:
            self._increase_quality(item)
        if item.sell_in < BACKSTAGE_TRIPLE_RATE_BELOW:
            self._increase_quality(item)

        self._decrement_sell_in(item)
        if self._is_expired(item):
            item.quality = MIN_QUALITY

    def _update_normal_item(self, item):
        self._decrease_quality(item)
        self._decrement_sell_in(item)
        if self._is_expired(item):
            self._decrease_quality(item)

    def _decrement_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def _is_expired(self, item):
        return item.sell_in < 0

    def _increase_quality(self, item):
        if item.quality < MAX_QUALITY:
            item.quality = item.quality + 1

    def _decrease_quality(self, item):
        if item.quality > MIN_QUALITY:
            item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)