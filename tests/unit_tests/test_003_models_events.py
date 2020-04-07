from sshportal_api.models.events import EventsModel


def test_events_by_id():
    """
    GIVEN a Event model
    WHEN test the first event
    THEN check the id, action, comment, weight
    """
    event = EventsModel.by_id(1)
    assert event.id == 1
    assert event.domain == "system"
    assert event.author_id == 0
    assert event.action == "migrated"
    assert event.entity == ""
    assert event.args is None


def test_events_to_json():
    """
    GIVEN a Events model
    WHEN test the to_json method
    THEN check the domain, author_id, action, entity, and more
    """
    event = EventsModel.by_id(1)
    event_json = EventsModel.to_json(event)
    assert event.id == event_json['id']
    assert event.domain == event_json['domain']
    assert event.author_id == event_json['author_id']
    assert event.action == event_json['action']
    assert event.entity == event_json['entity']