from models.event_details_model import EventDetailsModel
from models.input_details_model import InputDetailsModel
from models.event_model import EventModel
from enums.crawler_force import CrawlerForce
from repositories.crawler_repository import CrawlerRepository
from typing import List
import uvicorn
from fastapi import FastAPI
import json

app = FastAPI(version='1.0.0', title='Tenfins Crawler',
              description='To have the PlaceId of the city see https://www.bandsintown.com/cityAutocomplete?input=boston')


@app.get("/events", response_model=List[EventModel], tags=['Event'])
def getEvents(placeId: str, force: CrawlerForce = CrawlerForce.MINIMUM):
    crawler = CrawlerRepository(
        url=f'https://www.bandsintown.com/?place_id={placeId}')
    result = crawler.getEvents(force)
    events = [event.dict() for event in result]
    # list_details = []
    with open('events.json', 'w') as json_file:
        json.dump(events, json_file)
    # for event in result:
    #     details = getDetailsEvent(url=InputDetailsModel(url=event.url))
    #     list_details.append(details.dict())
    # with open('details.json', 'w') as json_file:
    #     json.dump(list_details, json_file)
    return result


@app.post("/events/details", response_model=EventDetailsModel, tags=['Details Event'])
def getDetailsEvent(url: InputDetailsModel):
    crawler = CrawlerRepository(url=url.url)
    result = crawler.getDetailsEvent()
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, debug=True)
