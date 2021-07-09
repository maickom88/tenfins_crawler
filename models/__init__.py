class Event:
    title: str
    local: str
    hours: str
    day: str
    image: str
    url: str
    month: str

    def __init__(self, title: str,
                 local: str,
                 hours: str,
                 day: str,
                 image: str,
                 url: str,
                 month: str):
        self.title = title
        self.local = local
        self.hours = hours
        self.day = day
        self.image = image
        self.url = url
        self.moth = month
