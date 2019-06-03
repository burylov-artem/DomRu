class Abstract_selectors:
    value_error_text = 'Ой! У нас возникли небольшие технические проблемы. Но мы их уже решаем.'
    logo_img = '//img[@alt="Дом.ru Movix"]'
    card_image_in_result_search = '//img[@alt="{}"]'
    section_card_film = '//section[@data-name="{}"]'
    error_result_search = '//p[@class="error__text" and text()="' + value_error_text + '"]'
    items_slider = '//img[@class="slider__item-img" and @alt="{}"]'
    section_slider = '//section[@class="slider"]'
    catalog_item = '//div[@data-name="{}"]'
