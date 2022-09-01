LOGIN_BUTTON = '/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[1]'
DEVICE_TV_SELECTOR = 'body > app-root > div > div > rz-main-page > div > aside > rz-main-page-sidebar > div.fat-wrap > rz-sidebar-fat-menu > div > ul > li:nth-child(2)'
DEVICE_PAGE_SELECTOR = 'body > app-root > div > div > rz-super-portal > div > main > section > div:nth-child(3) > rz-dynamic-widgets > rz-widget-list:nth-child(3) > section > ul > li:nth-child(1) > rz-list-tile > div > a.tile-cats__heading.tile-cats__heading_type_center.ng-star-inserted'


def GET_DEVICE_TV_SELECTOR()-> str:
    return DEVICE_TV_SELECTOR


def GET_DEVICE_PAGE_SELECTOR()->str:
    return DEVICE_PAGE_SELECTOR

