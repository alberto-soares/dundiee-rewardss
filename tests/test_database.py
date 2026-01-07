"""Module"""

import pytest

from dundie.database import EMPTY_DB, add_movement, add_person, commit, connect


@pytest.mark.unit
def test_database_schema():
    """Module"""
    db_ = connect()
    assert db_.keys() == EMPTY_DB.keys()


@pytest.mark.unit
def test_commit_to_database():
    """Module"""
    db_ = connect()
    data = {"name": "Joe Doe", "role": "Saleman", "dept": "Sales"}
    db_["people"]["joe@doe.com"] = data
    commit(db_)

    db_ = connect()
    assert db_["people"]["joe@doe.com"] == data


@pytest.mark.unit
def test_add_person_for_the_first_time():
    """Module"""
    pk = "joe@doe.com"
    data = {"name": "Joe Doe", "role": "Saleman", "dept": "Sales"}
    db_ = connect()
    _, created = add_person(db_, pk, data)
    assert created is True
    commit(db_)

    db_ = connect()
    assert db_["people"][pk] == data
    assert db_["balance"][pk] == 500
    assert len(db_["movement"][pk]) > 0
    assert db_["movement"][pk][0]["value"] == 500


@pytest.mark.unit
def test_negative_add_person_invalid_email():
    """Module"""
    with pytest.raises(ValueError):
        add_person({}, ".@bla", {})


@pytest.mark.unit
def test_add_or_remove_points_for_person():
    """Module"""
    pk = "joe@doe.com"
    data = {"name": "Joe Doe", "role": "Saleman", "dept": "Sales"}
    db_ = connect()
    _, created = add_person(db_, pk, data)
    assert created is True
    commit(db_)

    db_ = connect()
    before = db_["balance"][pk]

    add_movement(db_, pk, -100, "manager")
    commit(db_)

    db_ = connect()
    after = db_["balance"][pk]

    assert after == before - 100
    assert after == 400
    assert before == 500
