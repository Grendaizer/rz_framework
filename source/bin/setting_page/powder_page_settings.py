HOUSEHOLD_PRODUCTS = 'body > app-root > div > div > rz-main-page > div > aside > rz-main-page-sidebar > div.fat-wrap > rz-sidebar-fat-menu > div > ul > li:nth-child(5) > a'
WASHING_POWDER = 'body > app-root > div > div > rz-super-portal > div > main > section > div:nth-child(3) > rz-dynamic-widgets > rz-widget-list:nth-child(3) > section > ul > li:nth-child(5) > rz-list-tile > div > ul > li:nth-child(2) > a'
SECOND_PAGE = 'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-catalog-paginator > app-paginator > div > ul > li:nth-child(2) > a'
THIRD_PAGE = 'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-catalog-paginator > app-paginator > div > ul > li:nth-child(3) > a'
FOUR_PAGE = 'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-catalog-paginator > app-paginator > div > ul > li:nth-child(4) > a'
FIVE_PAGE = 'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-catalog-paginator > app-paginator > div > ul > li:nth-child(5) > a'


def GET_HOUSEHOLD_PRODUCTS_PAGE() -> str:
    return HOUSEHOLD_PRODUCTS


def GET_POWDER_NAME(x) -> str:
    POWDER_NAME = f'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({x}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > a.goods-tile__heading.ng-star-inserted > span'
    return POWDER_NAME


def GET_POWDER_PRICE(x) -> str:
    POWDER_PRICE = f'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({x}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > div.goods-tile__prices > div.goods-tile__price.price--red.ng-star-inserted > p > span.goods-tile__price-value'
    return POWDER_PRICE


def GET_POWDER_OLD_PRICE(x) -> str:
    OLD_PRICE = f'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({i}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > div.goods-tile__prices > div.goods-tile__price.ng-star-inserted > p > span.goods-tile__price-value'
    return OLD_PRICE


@property
def GET_WASHING_POWDER_PAGE() -> str:
    return WASHING_POWDER


@property
def GET_WASHING_POWDER_PAGE_TWO() -> str:
    return SECOND_PAGE


@property
def GET_WASHING_POWDER_PAGE_THREE() -> str:
    return THIRD_PAGE


@property
def GET_WASHING_POWDER_PAGE_FOUR() -> str:
    return FOUR_PAGE


@property
def GET_WASHING_POWDER_PAGE_FIVE() -> str:
    return FIVE_PAGE
