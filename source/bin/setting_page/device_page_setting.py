TOP = 'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child(16) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > span'
PAGE_TWO = 'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-catalog-paginator > app-paginator > div > ul > li:nth-child(2) > a'
PAGE_THREE = 'body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-catalog-paginator > app-paginator > div > ul > li:nth-child(3) > a'


@property
def GET_PAGE_2() -> str:
    return PAGE_TWO


@property
def GET_PAGE_3() -> str:
    return PAGE_THREE


def GET_DEVICE_TITLE(x) -> str:
    DEVICE_TITLE = f"body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({x}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > a.goods-tile__heading.ng-star-inserted > span"
    return DEVICE_TITLE
