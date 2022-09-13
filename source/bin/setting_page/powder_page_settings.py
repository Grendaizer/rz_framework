SECOND_PAGE = 'li.pagination__item:nth-child(2) > a:nth-child(1)'
THIRD_PAGE = 'li.pagination__item:nth-child(3) > a:nth-child(1)'
FOUR_PAGE = 'li.pagination__item:nth-child(4) > a:nth-child(1)'
FIVE_PAGE = 'li.pagination__item:nth-child(5) > a:nth-child(1)'


def GET_POWDER_NAME(x) -> str:
    POWDER_NAME = f'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({x}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > a.goods-tile__heading.ng-star-inserted > span'
    return POWDER_NAME


def GET_POWDER_PRICE(x) -> str:
    POWDER_PRICE = f'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({x}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > div.goods-tile__prices > div.goods-tile__price.price--red.ng-star-inserted > p > span.goods-tile__price-value'
    return POWDER_PRICE


def GET_POWDER_OLD_PRICE(x) -> str:
    OLD_PRICE = f'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({x}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > div.goods-tile__prices > div.goods-tile__price.ng-star-inserted > p > span.goods-tile__price-value'
    return OLD_PRICE


def GET_WASHING_POWDER_PAGE_TWO() -> str:
    return SECOND_PAGE


def GET_WASHING_POWDER_PAGE_THREE() -> str:
    return THIRD_PAGE


def GET_WASHING_POWDER_PAGE_FOUR() -> str:
    return FOUR_PAGE


def GET_WASHING_POWDER_PAGE_FIVE() -> str:
    return FIVE_PAGE
