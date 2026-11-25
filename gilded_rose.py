
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
            if item.name == SULFURAS:
                continue

            self._update_item_quality(item)
            self._decrement_sell_in(item)

            if self._is_expired(item):
                self._handle_expired_item(item)

    def _update_item_quality(self, item):
        if item.name == AGED_BRIE:
            self._increase_quality(item)
        elif item.name == BACKSTAGE_PASSES:
            self._update_backstage_pass_quality(item)
        else:
            self._decrease_quality(item)

    def _update_backstage_pass_quality(self, item):
        self._increase_quality(item)
        if item.sell_in < BACKSTAGE_DOUBLE_RATE_BELOW:
            self._increase_quality(item)
        if item.sell_in < BACKSTAGE_TRIPLE_RATE_BELOW:
            self._increase_quality(item)

    def _handle_expired_item(self, item):
        if item.name == AGED_BRIE:
            self._increase_quality(item)
        elif item.name == BACKSTAGE_PASSES:
            item.quality = MIN_QUALITY
        else:
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