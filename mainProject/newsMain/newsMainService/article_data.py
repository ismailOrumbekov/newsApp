
SELECTORS = {
    "Tengri Life": {
        "title": ("h1", "post-title"),
        "date": ("span", "date"),
        "description": ("div", "post-content"),
        "image": ("div", "post-content"),
        "tags": ["Туризм", "Позновательно"]
    },
    "Tengri Travel": {
        "title": ("h1", "entry-title"),
        "date": ("span", "entry-date"),
        "description": ("div", "post-content"),
        "image": ("div", "post-formats-wrapper"),
        "tags": ["Повседневное", "Интересное", "Популярное"]
    },
    "Tengri Auto": {
        "title": ("h1", "head-single"),
        "date": ("div", "date-time"),
        "description": ("div", "content_main_text"),
        "image": ("picture", "content_main_thumb_img"),
        "tags": ["Автомобили", "Интересное", "Популярное"]
    },
    "Tengri Sport": {
        "title": ("h1", "head-single"),
        "date": ("div", "date-time"),
        "description": ("div", "content_main_text"),
        "image": ("picture", "content_main_thumb_img"),
        "tags": ["Спорт", "Интересное", "Полезное", "Оздоровительное"]
    },
    "Tengri Education": {
        "title": ("h1", "head-single"),
        "date": ("div", "date-time"),
        "description": ("div", "content_main_text"),
        "image": ("picture", "content_main_thumb_img"),
        "tags": ["Интересное", "Полезное", "Образовательное"]
    },
    None: {
        "title": ("h1", "head-single"),
        "date": ("div", "date-time"),
        "description": ("div", "content_main_text"),
        "image": ("picture", "content_main_thumb_img"),
        "tags": ["Интересное", "Полезное", "Образовательное"]
    }
}


